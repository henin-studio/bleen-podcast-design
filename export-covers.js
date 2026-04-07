#!/usr/bin/env node
/**
 * Export podcast covers from the actual index.html pages.
 * Uses deviceScaleFactor to upscale the real card rendering to 3000x3000.
 *
 * Usage: node export-covers.js
 * Requires: puppeteer (Bleen root)
 */

const puppeteer = require('puppeteer');
const path = require('path');
const fs = require('fs');

const TARGET = 3000;

const jobs = [
  {
    label: 'Velotaf',
    indexPath: 'Velotaf/index.html',
    coverId: 'v3-1',
    coverOut: 'Velotaf/covers/cover-1-pure.png',
    logoOut: 'Velotaf/covers/layers/cover-1-logo.png',
  },
  {
    label: 'La Grande Démission',
    indexPath: 'La Grande Démission/index.html',
    coverId: 'v3-13',
    coverOut: 'La Grande Démission/covers/cover-v3-13.png',
    logoOut: 'La Grande Démission/covers/layers/cover-v3-13-logo.png',
  },
];

(async () => {
  const baseDir = __dirname;
  console.log(`\nExporting covers at ${TARGET}x${TARGET}...\n`);

  const browser = await puppeteer.launch({
    headless: 'new',
    executablePath: '/Applications/Brave Browser.app/Contents/MacOS/Brave Browser',
  });

  for (const job of jobs) {
    console.log(`${job.label}:`);
    const filePath = path.resolve(baseDir, job.indexPath);

    // ── 1. Full cover ──
    const page = await browser.newPage();
    // Load at normal viewport first to let everything render
    await page.setViewport({ width: 1200, height: 2000, deviceScaleFactor: 1 });
    await page.goto(`file://${filePath}`, { waitUntil: 'networkidle0' });
    await new Promise(r => setTimeout(r, 2000));

    // Get the bounding box of the .cover-inner inside the right card
    const cardSelector = `.design-card[onclick*="'${job.coverId}'"]`;
    const box = await page.evaluate((sel) => {
      const card = document.querySelector(sel);
      if (!card) return null;
      // Try .cover-inner first (Velotaf), then the div inside aspect-ratio container (LGD)
      let inner = card.querySelector('.cover-inner');
      if (!inner) {
        const aspectDiv = card.querySelector('[style*="aspect-ratio"]');
        if (aspectDiv) inner = aspectDiv.querySelector('div[style*="position:relative"]') || aspectDiv.firstElementChild;
      }
      if (!inner) return null;
      // Kill border-radius, borders, and box-shadow for export
      inner.style.borderRadius = '0';
      let el = inner.parentElement;
      while (el && el !== document.body) {
        el.style.borderRadius = '0';
        el.style.overflow = 'hidden';
        el.style.border = 'none';
        el.style.boxShadow = 'none';
        el = el.parentElement;
      }
      // Kill ::after pseudo-elements that add inset box-shadow with border-radius
      const style = document.createElement('style');
      style.textContent = '.design-preview::after, .design-card::after, .design-card::before { display: none !important; } .design-card { border: none !important; box-shadow: none !important; border-radius: 0 !important; } .design-preview { border-radius: 0 !important; }';
      document.head.appendChild(style);
      const rect = inner.getBoundingClientRect();
      return { x: rect.x, y: rect.y, width: rect.width, height: rect.height };
    }, cardSelector);

    if (!box) {
      console.log(`  ✗ Card ${job.coverId} not found, skipping`);
      await page.close();
      continue;
    }

    // Calculate deviceScaleFactor to get TARGET px output from the card's natural size
    const scale = TARGET / Math.min(box.width, box.height);

    // Re-set viewport with the high scale factor
    await page.setViewport({
      width: 1200,
      height: 2000,
      deviceScaleFactor: scale,
    });
    await new Promise(r => setTimeout(r, 2000)); // re-render at new scale

    // Re-read box (positions might shift slightly at new scale)
    const box2 = await page.evaluate((sel) => {
      const card = document.querySelector(sel);
      let inner = card.querySelector('.cover-inner');
      if (!inner) {
        const aspectDiv = card.querySelector('[style*="aspect-ratio"]');
        if (aspectDiv) inner = aspectDiv.querySelector('div[style*="position:relative"]') || aspectDiv.firstElementChild;
      }
      const rect = inner.getBoundingClientRect();
      return { x: rect.x, y: rect.y, width: rect.width, height: rect.height };
    }, cardSelector);

    const coverOutPath = path.resolve(baseDir, job.coverOut);
    fs.mkdirSync(path.dirname(coverOutPath), { recursive: true });

    // Clip is in CSS pixels — Puppeteer multiplies by deviceScaleFactor for the actual PNG
    await page.screenshot({
      path: coverOutPath,
      type: 'png',
      clip: {
        x: box2.x,
        y: box2.y,
        width: Math.min(box2.width, box2.height), // force square
        height: Math.min(box2.width, box2.height),
      },
    });

    const coverSize = fs.statSync(coverOutPath).size;
    console.log(`  ✓ ${job.coverOut}: ${(coverSize / 1024 / 1024).toFixed(1)} MB`);
    await page.close();

    // ── 2. Logo-only layer (transparent) ──
    const logoPage = await browser.newPage();
    await logoPage.setViewport({ width: 1200, height: 2000, deviceScaleFactor: 1 });
    await logoPage.goto(`file://${filePath}`, { waitUntil: 'networkidle0' });
    await new Promise(r => setTimeout(r, 2000));

    // Get the cover-inner box and logo position relative to it
    const logoInfo = await logoPage.evaluate((sel) => {
      const card = document.querySelector(sel);
      let inner = card.querySelector('.cover-inner');
      if (!inner) {
        const aspectDiv = card.querySelector('[style*="aspect-ratio"]');
        if (aspectDiv) inner = aspectDiv.querySelector('div[style*="position:relative"]') || aspectDiv.firstElementChild;
      }
      const innerRect = inner.getBoundingClientRect();

      // Find the logo SVG div
      const logoDiv = card.querySelector('div[style*="bottom:6%"][style*="right:6%"]');
      if (!logoDiv) return null;
      const logoRect = logoDiv.getBoundingClientRect();

      return {
        innerBox: { x: innerRect.x, y: innerRect.y, width: innerRect.width, height: innerRect.height },
        logoBox: { x: logoRect.x, y: logoRect.y, width: logoRect.width, height: logoRect.height },
      };
    }, cardSelector);

    if (!logoInfo) {
      console.log(`  ✗ Logo not found for ${job.coverId}`);
      await logoPage.close();
      continue;
    }

    const logoScale = TARGET / Math.min(logoInfo.innerBox.width, logoInfo.innerBox.height);
    await logoPage.setViewport({ width: 1200, height: 2000, deviceScaleFactor: logoScale });
    await new Promise(r => setTimeout(r, 1000));

    // Hide everything except the logo div
    await logoPage.evaluate((sel) => {
      const card = document.querySelector(sel);
      let inner = card.querySelector('.cover-inner');
      if (!inner) {
        const aspectDiv = card.querySelector('[style*="aspect-ratio"]');
        if (aspectDiv) inner = aspectDiv.querySelector('div[style*="position:relative"]') || aspectDiv.firstElementChild;
      }
      // Hide all children except the logo div
      for (const child of inner.children) {
        if (!child.matches('div[style*="bottom:6%"][style*="right:6%"]')) {
          child.style.visibility = 'hidden';
        }
      }
      // Make background transparent
      inner.style.background = 'transparent';
      // Also clear any overlay divs that might have been the parent bg
      const parent = inner.parentElement;
      if (parent) parent.style.background = 'transparent';
    }, cardSelector);

    const box3 = await logoPage.evaluate((sel) => {
      const card = document.querySelector(sel);
      let inner = card.querySelector('.cover-inner');
      if (!inner) {
        const aspectDiv = card.querySelector('[style*="aspect-ratio"]');
        if (aspectDiv) inner = aspectDiv.querySelector('div[style*="position:relative"]') || aspectDiv.firstElementChild;
      }
      const rect = inner.getBoundingClientRect();
      return { x: rect.x, y: rect.y, width: rect.width, height: rect.height };
    }, cardSelector);

    const logoOutPath = path.resolve(baseDir, job.logoOut);
    fs.mkdirSync(path.dirname(logoOutPath), { recursive: true });

    await logoPage.screenshot({
      path: logoOutPath,
      type: 'png',
      clip: {
        x: box3.x,
        y: box3.y,
        width: Math.min(box3.width, box3.height),
        height: Math.min(box3.width, box3.height),
      },
      omitBackground: true,
    });

    const logoSize = fs.statSync(logoOutPath).size;
    console.log(`  ✓ ${job.logoOut}: ${(logoSize / 1024).toFixed(0)} KB (transparent)`);
    await logoPage.close();
  }

  await browser.close();
  console.log('\nDone.');
})();
