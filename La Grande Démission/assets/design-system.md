# Bleen Consulting -- Design System

Extracted from `https://bleenconsulting.webflow.io/`
Source CSS: `https://cdn.prod.website-files.com/695a6f93f9706c2977bf7fa1/css/bleenconsulting.shared.79c901a72.min.css`

---

## 1. Typography

### Font Families

| Role | Font | Fallbacks | Source |
|------|------|-----------|--------|
| **Primary** | Satoshi Variable | Arial, sans-serif | Self-hosted WOFF2 (`Satoshi-Variable.woff2`) |
| **Secondary** (headings) | Chillax | Arial, sans-serif | Self-hosted WOFF2 (`Chillax-Medium.woff2`) |

```css
--_typography---font--primary-family: "Satoshi Variable", Arial, sans-serif;
--_typography---font--secondary-family: Chillax, Arial, sans-serif;
```

### Font Weights

| Token | Value | Usage |
|-------|-------|-------|
| `--_typography---font--primary-regular` | 400 | Body text |
| `--_typography---font--primary-medium` | 500 | Default body, buttons, UI |
| `--_typography---font--primary-bold` | 700 | Bold emphasis |
| `--_typography---font--secondary-medium` | 500 | All headings (Chillax) |

Satoshi Variable supports weight range 300--900.

### Font Sizes (fluid clamp values)

All sizes use fluid typography via `clamp()` between viewport-min (20rem / 320px) and viewport-max (90rem / 1440px).

| Token | Min | Max | CSS Variable |
|-------|-----|-----|--------------|
| **Display** | 4rem (64px) | 7rem (112px) | `--_typography---font-size--display` |
| **H1** | 3rem (48px) | 5rem (80px) | `--_typography---font-size--h1` |
| **H2** | 2.5rem (40px) | 4rem (64px) | `--_typography---font-size--h2` |
| **H3** | 2.25rem (36px) | 3rem (48px) | `--_typography---font-size--h3` |
| **H4** | 1.75rem (28px) | 2rem (32px) | `--_typography---font-size--h4` |
| **H5** | 1.1rem (17.6px) | 1.5rem (24px) | `--_typography---font-size--h5` |
| **H6** | 1rem (16px) | 1.125rem (18px) | `--_typography---font-size--h6` |
| **Text Large** | 1.125rem (18px) | 1.25rem (20px) | `--_typography---font-size--text-large` |
| **Text Main** | 1rem (16px) | 1.125rem (18px) | `--_typography---font-size--text-main` |
| **Text Small** | 0.875rem (14px) | 1rem (16px) | `--_typography---font-size--text-small` |

### Line Heights

| Token | Value | Usage |
|-------|-------|-------|
| `--_typography---line-height--small` | 1 | Display, H1, H2, H3 |
| `--_typography---line-height--medium` | 1.1 | H4, H5, H6 |
| `--_typography---line-height--large` | 1.3 | Rich text, accordion content |
| `--_typography---line-height--huge` | 1.5 | Body text (main, large, small) |

### Letter Spacing

| Token | Value | Usage |
|-------|-------|-------|
| `--_typography---letter-spacing--tight` | -0.05em | Display, H1, H2, H3 |
| `--_typography---letter-spacing--normal` | -0.02em | H4, H5, H6, body text |
| `--_typography---letter-spacing--wide` | 0.2em | Uppercase labels |

### Text Style Summary

| Style | Font Family | Size | Line Height | Letter Spacing | Weight |
|-------|------------|------|-------------|----------------|--------|
| Display | Satoshi (primary) | display | small (1) | tight (-0.05em) | 500 |
| H1 | Chillax (secondary) | h1 | small (1) | tight (-0.05em) | 500 |
| H2 | Chillax (secondary) | h2 | small (1) | tight (-0.05em) | 500 |
| H3 | Chillax (secondary) | h3 | small (1) | tight (-0.05em) | 500 |
| H4 | Satoshi (primary) | h4 | medium (1.1) | normal (-0.02em) | 500 |
| H5 | Satoshi (primary) | h5 | medium (1.1) | normal (-0.02em) | 500 |
| H6 | Satoshi (primary) | h6 | medium (1.1) | normal (-0.02em) | 500 |
| Large | Satoshi (primary) | text-large | huge (1.5) | normal (-0.02em) | 500 |
| Main (body) | Satoshi (primary) | text-main | huge (1.5) | normal (-0.02em) | 500 |
| Small | Satoshi (primary) | text-small | huge (1.5) | normal (-0.02em) | 500 |

### Text Trim (line-height compensation)

```css
--_typography---font--primary-trim-top: .34em;
--_typography---font--primary-trim-bottom: .38em;
--_typography---font--secondary-trim-top: .34em;
--_typography---font--secondary-trim-bottom: .33em;
```

### Text Transform Tokens

```css
--_typography---text-transform--none: var(--text-transform, none);
--_typography---text-transform--uppercase: uppercase;
--_typography---text-transform--capitalize: capitalize;
--_typography---text-transform--lowercase: lowercase;
```

---

## 2. Colors

### Core Swatches

| Token | Value | Usage |
|-------|-------|-------|
| `--swatch--brand-500` | `#2ed5a3` | **Primary brand green** |
| `--swatch--dark-900` | `#0f1f1d` | Dark background, text on light |
| `--swatch--dark-800` | `#07352f` | Dark section alt background |
| `--swatch--light-100` | `white` | White background |
| `--swatch--light-200` | `#dae9e7` | Light sage/mint background |
| `--swatch--transparent` | `transparent` | Transparent |

### Brand Color Scale (auto-generated via color-mix)

| Token | Formula | Approximate Hex |
|-------|---------|-----------------|
| `--swatch--brand-100` | brand-500 + 80% white | ~#c9f3e7 |
| `--swatch--brand-200` | brand-500 + 60% white | ~#a5ebd4 |
| `--swatch--brand-300` | brand-500 + 40% white | ~#80e2c1 |
| `--swatch--brand-400` | brand-500 + 20% white | ~#58dab2 |
| `--swatch--brand-500` | `#2ed5a3` | #2ed5a3 |
| `--swatch--brand-600` | brand-500 + 20% black | ~#25aa82 |
| `--swatch--brand-700` | brand-500 + 40% black | ~#1c8062 |
| `--swatch--brand-800` | brand-500 + 60% black | ~#125541 |
| `--swatch--brand-900` | brand-500 + 80% black | ~#092b21 |

### Accent Colors

| Token | Value | Usage |
|-------|-------|-------|
| `--swatch--brand-pastel-red` | `#ff6b6b` | Accent red |
| `--swatch--brand-sky-blue` | `#66d9ff` | Accent blue |
| `--swatch--brand-sunglow` | `#ffd23f` | Accent yellow |
| `--swatch--brand-tangerine` | `#ff9f6b` | Accent orange |
| `--swatch--brand-violet` | `#b38fff` | Accent violet |

### Opacity Variants

```css
--swatch--dark-900-o20: color-mix(in srgb, #0f1f1d 20%, transparent);
--swatch--light-100-o20: color-mix(in srgb, white 20%, transparent);
--swatch--brand-text-o20: color-mix(in srgb, var(--swatch--brand-text) 20%, transparent);
```

### Theme System

Three theme contexts: **Light** (default), **Dark**, **Brand**.

| Theme Variable | Light | Dark | Brand |
|---------------|-------|------|-------|
| `--_theme---background` | `--swatch--light-200` (#dae9e7) | `--swatch--dark-900` (#0f1f1d) | `--swatch--brand-500` (#2ed5a3) |
| `--_theme---background-2` | `--swatch--light-100` (white) | `--swatch--dark-800` (#07352f) | `--swatch--brand-600` |
| `--_theme---text` | `--swatch--dark-900` (#0f1f1d) | `--swatch--light-100` (white) | `--swatch--brand-text` (#0f1f1d) |
| `--_theme---heading-accent` | `--swatch--brand-600` | `--swatch--brand-500` | color-mix text+20% white |
| `--_theme---border` | dark-900 at 20% | light-100 at 20% | brand-text at 20% |
| `--_theme---selection--background` | `--swatch--brand-300` | `--swatch--brand-300` | `--swatch--brand-300` |
| `--_theme---selection--text` | `--swatch--brand-text` | `--swatch--brand-text` | `--swatch--brand-text` |

### Button Theme Colors

**Primary button:**
| State | Light theme | Dark theme | Brand theme |
|-------|------------|------------|-------------|
| Background | `--swatch--brand-500` | `--swatch--brand-text` | `--swatch--brand-text` |
| Background hover | color-mix +10% white | `--_theme---text` | `--_theme---text` |
| Text | `--swatch--brand-500` | `--swatch--brand-text` | `--swatch--brand-500` |
| Text hover | `--_theme---background` | `--_theme---background` | `--_theme---button-primary--text` |
| Border | same as background | same as background | same as background |

**Secondary button:**
| State | Value |
|-------|-------|
| Background | transparent |
| Background hover | `--_theme---text` |
| Text | `--_theme---text` |
| Text hover | `--_theme---background` |
| Border | `--_theme---border` |
| Border hover | same as bg hover |

### Link Colors

```css
--_theme---text-link--text: var(--_theme---text);
--_theme---text-link--text-hover: var(--_theme---text-link--text);
--_theme---text-link--border: var(--_theme---border);
--_theme---text-link--border-hover: var(--_theme---text);  /* or brand-500 in dark */
```

### Gradients

```css
/* Dark overlay on images */
linear-gradient(#0000, #0000009e 84%)

/* Top fade from dark */
linear-gradient(#0f1f1dcc, #fff0 15%)

/* Horizontal mask for marquee/slider */
linear-gradient(90deg, #0000, #000 10% 90%, #0000)
linear-gradient(90deg, #0000, #000 3% 97%, #0000)
```

### Hero Scroll Color

```css
--color: #2ED5A3;  /* Used in hero scroll animation clip-path */
```

---

## 3. Spacing

### Spacing Scale (fluid clamp values)

All spacing uses `clamp()` between viewport-min (20rem) and viewport-max (90rem).

| Token | Min | Max | ~Desktop |
|-------|-----|-----|----------|
| `--_spacing---space--1` | 0.375rem (6px) | 0.5rem (8px) | 8px |
| `--_spacing---space--2` | 0.625rem (10px) | 0.75rem (12px) | 12px |
| `--_spacing---space--3` | 0.875rem (14px) | 1rem (16px) | 16px |
| `--_spacing---space--4` | 1.25rem (20px) | 1.5rem (24px) | 24px |
| `--_spacing---space--5` | 1.75rem (28px) | 2rem (32px) | 32px |
| `--_spacing---space--6` | 2rem (32px) | 2.5rem (40px) | 40px |
| `--_spacing---space--7` | 2.25rem (36px) | 3rem (48px) | 48px |
| `--_spacing---space--8` | 2.5rem (40px) | 4rem (64px) | 64px |

### Section Spacing

| Token | Min | Max |
|-------|-----|-----|
| `--_spacing---section-space--none` | 0px | 0px |
| `--_spacing---section-space--small` | 3rem (48px) | 5rem (80px) |
| `--_spacing---section-space--main` | 4rem (64px) | 7rem (112px) |
| `--_spacing---section-space--large` | 5.5rem (88px) | 10rem (160px) |
| `--_spacing---section-space--page-top` | 10rem (160px) | 14rem (224px) |

### Gutter & Margin

```css
--site--gutter: clamp(1rem, fluid, 2rem);   /* Column gap */
--site--margin: clamp(1rem, fluid, 3rem);    /* Page margin */
```

### Component-Specific Spacing

**Button padding:** `0.9rem 1.5rem` (14.4px 24px)
**Card padding (large/medium screens):** space--7 (36-48px)
**Card padding (small screens):** space--5 top/bottom, space--4 left/right
**Accordion padding:** space--2 horizontal (space--5), space--4 vertical
**Tag/pill padding:** `0.5rem 0.75rem` (8px 12px)
**Footer section:** section-space--main top and bottom
**Footer bottom:** `2.5rem` (40px) top and bottom padding

---

## 4. Layout

### Viewport & Container

```css
--site--viewport-min: 20;   /* 20rem = 320px */
--site--viewport-max: 90;   /* 90rem = 1440px */
--max-width--main: calc(var(--site--viewport-max) * 1rem);  /* 90rem = 1440px */
--max-width--small: 50rem;   /* 800px */
--max-width--full: 100%;
--site--column-count: 12;
```

### Column System

```css
--site--column-width: calc(
  (min(var(--max-width--main), 100% - var(--site--margin) * 2)
  - (var(--site--gutter) * (var(--site--column-count) - 1)))
  / var(--site--column-count)
);
```

12-column grid with fluid gutter. Column widths use `data-large-columns`, `data-medium-columns`, `data-small-columns` attributes (values 1--12).

### Breakpoints (Container Queries)

| Name | Container Width | CSS Variable |
|------|----------------|--------------|
| Large | >= 50em (800px) | `--_responsive---large: 1` |
| Medium | < 50em (800px) | `--_responsive---medium: 1` |
| Small | < 35em (560px) | `--_responsive---small: 1` |
| X-Small | < 20em (320px) | `--_responsive---xsmall: 1` |

Uses `@container` queries, not `@media` queries.

### Grid Gap Utilities

```css
.u-gap-row-0    { grid-row-gap: 0 }
.u-gap-row-1    { grid-row-gap: var(--_spacing---space--1) }
.u-gap-row-2    { grid-row-gap: var(--_spacing---space--2) }
.u-gap-row-gutter { grid-row-gap: var(--site--gutter) }
.u-gap-row-3..8 { grid-row-gap: var(--_spacing---space--N) }
```

Default grid gap: `var(--_gap---size)` = `var(--site--gutter)`.

---

## 5. Components

### Buttons

**Button Main (Primary)**

```css
.button_main_wrap {
  border-radius: var(--radius--small);  /* 0.5rem = 8px */
  display: inline-block;
}

.button_main_element {
  padding: 0.9rem 1.5rem;
  border: var(--border-width--main) solid;  /* 0.2rem = 3.2px */
  border-radius: inherit;
  gap: 0.5rem;
  line-height: 1;
  transition: all 0.2s ease;
  /* Colors driven by theme variables */
}
```

**Button Main underline animation:**
```css
.button_main_line {
  height: var(--border-width--main);  /* 0.2rem */
  position: absolute;
  bottom: 0;
  /* Scales from 0 to full width on hover */
  transform: translateY(100%) scaleX(calc(100% * var(--_trigger---off)));
  transition: transform 0.3s cubic-bezier(.25, .46, .45, .94);
}
```

**Button Arrow / Toggle / Close (Icon Buttons)**
```css
width: var(--button-size--medium);  /* 3rem = 48px */
/* or */
width: var(--button-size--large);   /* 5rem = 80px */
aspect-ratio: 1;
border-radius: var(--radius--round);  /* 100vw = pill */
/* Same border and transition as main button */
```

**Button Sizes:**
| Token | Value |
|-------|-------|
| `--button-size--medium` | 3rem (48px) |
| `--button-size--large` | 5rem (80px) |

**Button Hover System:** Uses `color-mix()` with CSS `--_trigger---on/off` variables. On hover, `--_trigger---on: 0` and `--_trigger---off: 1`, which swaps the mixed color to the hover variant. No class toggling needed.

### Cards

**Primary Card:**
```css
.card_primary_element {
  gap: var(--_spacing---space--4);  /* 20-24px */
  border: var(--border-width--main) solid;  /* 0.2rem */
  background-color: var(--_theme---background-2);
  border-radius: inherit;
  /* Responsive padding: space--7 on large, space--5/space--4 on small */
  transition: border-color 0.2s ease;
}

.card_primary_image {
  /* Scale animation on hover */
  transform: scale(calc(1 + 0.1 * var(--_trigger---off)));
  transition: transform 0.3s ease;
  position: absolute;
  inset: 0;
}

.card_primary_group {
  border-radius: var(--radius--small);  /* 0.5rem */
  overflow: clip;
}
```

### Tags / Pills

```css
.tag_wrap {
  border-radius: var(--radius--small);  /* 0.5rem = 8px */
  background-color: var(--_theme---text);
  color: var(--_theme---background);
  line-height: 1;
  text-align: center;
  min-width: 4rem;
  padding: 0.5rem 0.75rem;
  display: inline-block;
}
```

H6 tag variant (used for service subtitles):
```css
.u-text-style-h6 {
  padding: var(--_spacing---space--2) var(--_spacing---space--1);
  border-radius: var(--radius--tiny);  /* 0.2rem */
  background-color: var(--swatch--brand-500);  /* #2ed5a3 */
}
```

### Navigation

```css
.nav_component {
  z-index: 1000;
  position: sticky;
  top: 0;
  pointer-events: none;
  container-type: inline-size;
}

.nav_desktop_layout {
  height: var(--nav--height);  /* 4rem = 64px */
  max-width: var(--nav--max-width-inner);  /* 90rem */
  gap: var(--_spacing---space--3);
  justify-content: space-between;
}

/* Nav bar background */
--nav--radius: var(--radius--small);  /* 0.5rem */
--_theme---nav--background: var(--_theme---background-2);

/* Spacing */
--nav--spacing-outer-horizontal: var(--site--margin);  /* 1-3rem */
--nav--spacing-outer-vertical: var(--site--margin);
--nav--spacing-inner-horizontal: var(--_spacing---space--5);  /* 28-32px */
--nav--height-total: calc(var(--nav--height) + var(--nav--spacing-outer-vertical));

/* Hamburger */
--nav--hamburger-thickness: var(--border-width--main);  /* 0.2rem */
--nav--hamburger-gap: var(--_spacing---space--2);  /* 10-12px */
```

**Mobile menu:** Full-screen overlay with `padding-top: var(--nav--height)` (4rem), same border-radius as nav bar.

### Accordion / FAQ

```css
.accordion_component {
  padding: var(--_spacing---space--2) var(--_spacing---space--5);
  border-radius: var(--radius--small);  /* 0.5rem */
  background-color: var(--swatch--light-100);  /* white */
}

.accordion_component:hover {
  background-color: var(--swatch--brand-200);  /* light green */
}

.accordion_toggle_button {
  padding: var(--_spacing---space--4) 0;
  gap: var(--_spacing---space--3);
  justify-content: space-between;
}

.accordion_toggle_icon {
  width: 1.4rem;
  color: var(--swatch--brand-500);  /* #2ed5a3 */
  transition: transform 0.2s ease;
  /* Rotates 180deg when open */
}

.accordion_content_text.u-rich-text {
  line-height: var(--_typography---line-height--large);  /* 1.3 */
}

.accordion_list {
  margin-top: calc(var(--_spacing---space--4) * -1);
}
```

Config: `data-close-previous="true"`, `data-close-on-second-click="true"`.

### Slider / Carousel

```css
.slider_wrap {
  gap: 0 (col), var(--_spacing---space--4) (row);
  flex-flow: column;
}

.slider_bullet_item {
  width: 1rem;
  aspect-ratio: 1;
  border: 0.09rem solid var(--_theme---border);
  border-radius: 100vw;  /* pill */
}

.slider_controls {
  gap: var(--_spacing---space--3);
  justify-content: space-between;
}
```

Responsive slide count: `--lg: 3; --md: var(--lg); --sm: var(--md); --xs: var(--sm)`.

### Footer

```css
.footer_contain {
  padding: var(--_spacing---section-space--main) 0;  /* 64-112px */
}

.footer_content {
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 18rem), 1fr));
  gap: var(--site--gutter);
}

.footer_logo_wrap {
  width: 25rem;  /* 400px */
}

.footer_social_link {
  width: 3rem;  /* 48px */
  padding: 0.5rem;
}

.footer_bottom_layout {
  border-top: var(--border-width--main) solid var(--swatch--brand-500);
  padding: 2.5rem 0;
  gap: var(--_spacing---space--4);
}

.footer_link_wrap {
  padding: var(--_spacing---space--2) 0;
  opacity: calc(1 - 0.5 * var(--_trigger---off));  /* 50% opacity, full on hover */
  transition: opacity 0.1s ease;
}
```

### Hero

```css
.hero_main_title {
  color: var(--swatch--brand-300);
  font-size: var(--_typography---font-size--h5);
  line-height: var(--_typography---line-height--medium);  /* 1.1 */
  font-weight: var(--_typography---font--primary-medium);  /* 500 */
}

.hero_main_scroll_component {
  font-family: var(--_typography---font--secondary-family);  /* Chillax */
  font-size: var(--_typography---font-size--h2);
  line-height: var(--_typography---line-height--medium);  /* 1.1 */
  letter-spacing: var(--_typography---letter-spacing--tight);  /* -0.05em */
}

.hero_main_divider {
  color: var(--swatch--light-200);
  width: 100%;
  height: 2rem;
  position: absolute;
  bottom: -1px;
  transform: rotate(180deg);  /* Wave/divider shape */
}
```

### Testimonials

```css
.testimonials_slide { margin-right: 5rem; }
.testimonials_logo-wrapper { max-width: 10rem; }
.testimonials_logo { max-height: 4rem; }
.testimonials_slide-nav { height: 1.75rem; }
```

### Service Cards

```css
.service_list_card {
  padding: var(--_spacing---space--6) var(--_spacing---space--5);
  /* 32-40px vertical, 28-32px horizontal */
}

.service_list_card_icon_wrap {
  width: 6rem;  /* 96px */
}

.service_kpi_card {
  padding: var(--_spacing---space--6) var(--_spacing---space--5);
}
```

### Case Studies

```css
.case_cms_item.u-grid-autofit {
  transition: all 0.3s;
}

.case_cms_item.u-grid-autofit:hover {
  background-color: var(--swatch--brand-100);
}

.case_tag {
  padding: var(--_spacing---space--1) var(--_spacing---space--2);
}
```

---

## 6. Effects

### Border Radius

| Token | Value | Usage |
|-------|-------|-------|
| `--radius--tiny` | 0.2rem (3.2px) | Tags (H6 badge), inline highlights |
| `--radius--small` | 0.5rem (8px) | Buttons, cards, accordion, nav |
| `--radius--main` | 1rem (16px) | Images, larger containers |
| `--radius--round` | 100vw | Pills, icon buttons, bullet dots |

### Border Width

```css
--border-width--main: 0.2rem;  /* 3.2px -- used for all borders */
```

### Box Shadows

```css
/* Subtle card shadow */
box-shadow: 0 0 0 1px #0000001a, 0 1px 3px #0000001a;

/* Focus ring */
box-shadow: 0 0 0 2px #fff;

/* Webflow system */
box-shadow: 0 0 3px #3336;
box-shadow: 0 0 3px 1px #3898ec;
```

### Transitions

| Property | Duration | Easing | Usage |
|----------|----------|--------|-------|
| `all` | 0.2s | ease | Buttons, general hover |
| `all` | 0.3s | ease | Cards, case items |
| `transform` | 0.3s | ease | Card image zoom |
| `transform` | 0.3s | cubic-bezier(.25,.46,.45,.94) | Button underline |
| `transform` | 0.2s | ease | Accordion icon rotation |
| `border-color` | 0.2s | ease | Card border on hover |
| `opacity` | 0.1s | ease | Footer links, nav text |
| `background-color, color` | 0.1s | - | Slider bullets |

### Focus States

```css
--focus--width: 0.125rem;  /* 2px */
--focus--offset-outer: /* default offset */

:focus-visible {
  outline-color: var(--_theme---text);
  outline-width: var(--focus--width);
  outline-style: solid;
}
```

### GSAP Animations

Libraries loaded:
- GSAP 3.13.0 + 3.14.2
- ScrollTrigger
- SplitText
- ScrambleTextPlugin

Animation types used:

| Animation | Trigger | Details |
|-----------|---------|---------|
| Scramble text | `data-scramble="load"` | Text scrambles on page load |
| Scramble text | `data-scramble="scroll"` | Text scrambles when scrolled into view |
| Scramble text | `data-scramble-hover="link"` | Text scrambles on hover |
| Hero clip-path | scroll progress | Clip-path reveal animation with `--clip-progress` |
| SVG path stroke | `svg="animated"` | Stroke animation with configurable `svg-animation-time` |
| Logo wall cycle | `data-logo-wall-cycle-init` | Scale 0.5->1, blur 8px->0, duration 0.9s, shuffle |
| Tab autoplay | `data-autoplay-duration` | GSAP timeline with `data-duration="0.3"` |
| Background/CTA | `data-animate="background"` / `data-animate="cta"` | Hidden initially, revealed via Webflow IX3 |

### Logo Marquee Animation

```css
@keyframes references-timeline {
  /* Infinite horizontal scroll, translateX at 50% */
}
```

---

## 7. Images & Media

### Aspect Ratios Used

| Ratio | Value | Typical Usage |
|-------|-------|---------------|
| Square | 1:1 | Icon buttons, bullets |
| Landscape | 16:9 | Video, hero backgrounds |
| Portrait | 2:3, 4:5 | Team photos, case studies |
| Wide | 3:2, 5:4, 2:1, 3:1.5 | Cards, feature images |

### Image Treatment

- Border radius: `var(--radius--main)` (1rem = 16px) or `var(--radius--small)` (0.5rem = 8px)
- Card images use `overflow: clip` on container with `position: absolute; inset: 0` for cover behavior
- Hover zoom: `transform: scale(1.1)` with 0.3s ease transition
- Formats served: AVIF, WebP, SVG, PNG, JPG (responsive srcsets via Webflow CDN)

### Icon Style

- SVG format, inline
- Accordion toggle icon: 1.4rem, colored `var(--swatch--brand-500)` (#2ed5a3)
- Button arrow/close icon: 36% of button width
- Nav hamburger: lines using `var(--nav--hamburger-thickness)` (0.2rem)
- Social icons: 3rem container with 0.5rem padding
- Client logos: SVG with light/dark variants, max-height 4rem

### Logo Wall

- Client logos displayed in infinite marquee
- Horizontal mask gradient: `linear-gradient(90deg, transparent, black 10% 90%, transparent)`
- Shuffle enabled via `data-logo-wall-shuffle="true"`
- Color fade transition: scale 0.5->1, blur 8px->0, duration 0.9s

---

## 8. CSS Custom Properties Reference

### Site-Level

```css
--site--viewport-min: 20;
--site--viewport-max: 90;
--site--column-count: 12;
--site--gutter: clamp(1rem, fluid, 2rem);
--site--margin: clamp(1rem, fluid, 3rem);
--max-width--main: 90rem;    /* 1440px */
--max-width--small: 50rem;   /* 800px */
--max-width--full: 100%;
--border-width--main: 0.2rem;
--button-size--medium: 3rem;
--button-size--large: 5rem;
```

### Nav-Level

```css
--nav--height: 4rem;
--nav--radius: var(--radius--small);
--nav--max-width-outer: var(--max-width--main);
--nav--max-width-inner: var(--max-width--main);
--nav--spacing-outer-horizontal: var(--site--margin);
--nav--spacing-outer-vertical: var(--site--margin);
--nav--spacing-inner-horizontal: var(--_spacing---space--5);
--nav--hamburger-thickness: var(--border-width--main);
--nav--hamburger-gap: var(--_spacing---space--2);
```

### State/Trigger System

```css
/* Default state */
--_trigger---on: 1;
--_trigger---off: 0;

/* On hover (inverted) */
--_trigger---on: 0;
--_trigger---off: 1;

/* State toggle */
--_state---true: 1;
--_state---false: 0;
```

Used for CSS-only hover/active transitions via `color-mix()` and `calc()`.

---

## 9. Page Structure Summary

```
nav_component (sticky, z-1000)
  nav_desktop_layout (4rem height, 90rem max-width)
    Logo
    nav_links (Home, ESG, Capability, Academy, About, Cases, Podcasts, News, FAQ)
    CTA: "Let's talk impact" -> /contact

hero_main (dark background #0f1f1d)
  "Sustainability Consulting in Brussels"
  "World's gone nuts. Time to rethink our economy."
  Scroll-animated text (Chillax, H2 size, clip-path)

section: "The new economy" (light-200 #dae9e7)
section: "What we fight for" -- 4 tabs (Decarbonized, Regenerative, Distributive, Resilient)
section: "Our services" -- 3 cards (ESG, CaaS, Academy)
section: "Our certifications" -- logo grid (21 certifications)
section: "Common questions" -- 6 FAQ accordions
section: "Client stories" -- testimonial slider
section: "Trusted by 100+ partners" -- logo marquee (30+ logos)
section: "Work with us" CTA (brand-500 background)

footer (dark-900 #0f1f1d)
  Logo + address (Brussels)
  4 link columns (ESG, Capability, Academy, Bleen)
  Social (LinkedIn, Facebook)
  Bottom: copyright + privacy + "Website by fabergast.studio"
```
