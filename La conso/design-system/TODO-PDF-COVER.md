# TODO — Intégrer la cover V8-4 dans le PDF design-system

> À faire quand le serveur Bleen est accessible (localhost:3400).
> Objectif : aligner le design-system Conso sur le pattern LGD / Vélotaf.

---

## Pourquoi

Les PDF de **La Grande Démission** et **Vélotaf** ont une première page avec :
1. Gradient coloré en haut + zone sombre en bas
2. **Titre rasterisé en PNG** (le mot du podcast en Knewave)
3. **Cover complète en PNG** dans un cadre avec ombre portée
4. Sous-titre "Cover Art — Design System" + version/date/signature

Le PDF Conso actuel n'a que du texte — pas d'aperçu visuel de la cover retenue.

**Références :**
- `La Grande Démission/design-system/design-system-lgd.pdf` (pages 1-2)
- `Velotaf/design-system/design-system-velotaf.pdf` (pages 1-2)

---

## Ce qui manque

| Fichier attendu | Rôle | Dimensions |
|-----------------|------|------------|
| `covers/cover-v8-4.png` | Cover complète (fond + illustration + titre + logo) | 3000×3000 px (ou 1080 min) |
| `covers/layers/cover-v8-4-text.png` | Titre "Deconsommation" seul, transparent | ~1800×400 px |

---

## Étape 1 — Démarrer le serveur Bleen

### Option A — Dashboard (le plus simple)
1. Ouvrir le dashboard : `http://localhost:3000`
2. Sur la carte Bleen → cliquer **Start**
3. Vérifier que `http://localhost:3400` répond

### Option B — Manuel
```bash
cd /Users/denishenin/Documents/Bleen
node server.js
```

Le serveur expose :
- `GET /api/export-png/:project/:file` → PNG via Puppeteer
- `GET /api/export-png/:project/:file?w=1080&h=1080&scale=2` → PNG 2x retina

---

## Étape 2 — Créer les pages HTML d'export

Il faut **2 fichiers HTML standalone** (car l'API exporte un fichier HTML entier) :

### 2.1 — `covers/v8-4-cover.html` (cover complète)

À créer dans `La conso/covers/v8-4-cover.html`. Structure :

```html
<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <link href="https://fonts.googleapis.com/css2?family=Knewave&display=swap" rel="stylesheet">
  <style>
    html, body { margin: 0; padding: 0; }
    body {
      width: 1080px; height: 1080px;
      background: linear-gradient(170deg, #221C46 0%, #3D1A3E 55%, #C75B7A 100%);
      position: relative; overflow: hidden;
    }
    .illustration {
      position: absolute; top: 0; left: -2%;
      width: 140%; height: 140%;
      object-fit: cover;
      filter: drop-shadow(0 5px 18px rgba(0,0,0,0.35));
    }
    .gradient-overlay {
      position: absolute; top: 0; left: 0; right: 0;
      height: 36%;
      background: linear-gradient(to bottom, rgba(34,28,70,0.94) 38%, transparent 100%);
    }
    .title {
      position: absolute; top: 6%; left: 2.5%; right: 2.5%;
      text-align: center;
      font-family: 'Knewave', cursive;
      font-size: 135px;  /* = clamp 36px * 3.75 pour 1080px */
      color: #FFF5E1;
      letter-spacing: -0.015em;
      -webkit-text-stroke: 6px rgba(232,57,107,0.5);
      paint-order: stroke fill;
      line-height: 0.9;
      white-space: nowrap;
    }
    .bleen-logo {
      position: absolute; bottom: 6%; right: 6%;
      color: rgba(255,255,255,0.85);
    }
    .bleen-logo svg { height: 115px; width: auto; }
  </style>
</head>
<body>
  <img class="illustration" src="images/used/v6/v6-souriante-hoodie-rose.png" alt="">
  <div class="gradient-overlay"></div>
  <div class="title">Deconsommation</div>
  <div class="bleen-logo">
    <!-- Copier le SVG Bleen de l'index.html (symbol id="bleen-logo") -->
  </div>
</body>
</html>
```

**Note** : copier le SVG Bleen complet depuis `La conso/index.html` lignes 361-381 (bloc `<defs><symbol id="bleen-logo">...`).

### 2.2 — `covers/v8-4-title.html` (juste le titre transparent)

```html
<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <link href="https://fonts.googleapis.com/css2?family=Knewave&display=swap" rel="stylesheet">
  <style>
    html, body { margin: 0; padding: 0; background: transparent; }
    body {
      width: 1800px; height: 400px;
      display: flex; align-items: center; justify-content: center;
    }
    .title {
      font-family: 'Knewave', cursive;
      font-size: 240px;
      color: #FFF5E1;
      letter-spacing: -0.015em;
      -webkit-text-stroke: 8px rgba(232,57,107,0.6);
      paint-order: stroke fill;
      line-height: 0.9;
      white-space: nowrap;
    }
  </style>
</head>
<body>
  <div class="title">Deconsommation</div>
</body>
</html>
```

---

## Étape 3 — Exporter en PNG

Une fois les 2 HTML créés et le serveur tournant :

```bash
# Cover complète (1080x1080)
curl "http://localhost:3400/api/export-png/La%20conso/v8-4-cover?w=1080&h=1080&scale=2" \
  -o "/Users/denishenin/Documents/Bleen/projects/podcast_design/La conso/covers/cover-v8-4.png"

# Titre seul (1800x400, transparent — à vérifier si le fond transparent passe)
curl "http://localhost:3400/api/export-png/La%20conso/v8-4-title?w=1800&h=400&scale=2" \
  -o "/Users/denishenin/Documents/Bleen/projects/podcast_design/La conso/covers/layers/cover-v8-4-text.png"
```

**Vérifier** que `covers/layers/` existe, sinon :
```bash
mkdir -p "/Users/denishenin/Documents/Bleen/projects/podcast_design/La conso/covers/layers"
```

---

## Étape 4 — Mettre à jour le .tex

### 4.1 — Ajouter `\IfFontExistsTF` pour Knewave (pattern LGD)

Dans `design-system-conso.tex`, remplacer :

```tex
\newcommand{\knewave}{\fontspec{Marker Felt}}
```

par :

```tex
% Knewave is the actual cover font (Google Fonts). Install it for accurate rendering.
% Fallback: Marker Felt (pre-installed macOS).
% To install: download from https://fonts.google.com/specimen/Knewave
% then double-click the .ttf to add it to Font Book.
\IfFontExistsTF{Knewave}{%
  \newcommand{\knewave}{\fontspec{Knewave}}%
}{%
  \newcommand{\knewave}{\fontspec{Marker Felt}\bfseries}%
}
```

### 4.2 — Remplacer la page de titre

Trouver le bloc `% TITLE PAGE` (autour de la ligne 128) et remplacer par :

```tex
\thispagestyle{empty}

\begin{tikzpicture}[remember picture, overlay]
  % Gradient V8-4 : navy -> prune -> vieux rose
  \shade[top color=consoNavy, middle color=consoPrune, bottom color=consoVieuxRose]
    (current page.north west) rectangle ([yshift=-11cm]current page.north east);
  % Dark bottom (navy)
  \fill[consoNavy]
    ([yshift=-11cm]current page.north west) rectangle (current page.south east);
\end{tikzpicture}

\vspace*{0.8cm}

\begin{center}
  \includegraphics[width=11cm]{../covers/layers/cover-v8-4-text.png}\\[6pt]
  {\Large\color{consoCreme}\bfseries Cover Art — Design System}\\[4pt]
  {\small\color{consoCreme!70}Version 2.1 — Avril 2026}\\[2pt]
  {\small\color{consoCreme!50}Denis Henin — Graphiste Designer @ bleen}
\end{center}

\vspace{0.6cm}

\begin{center}
  \begin{tikzpicture}
    \node[drop shadow={shadow xshift=1pt, shadow yshift=-2pt, opacity=0.3, fill=black}, inner sep=0pt] {%
      \includegraphics[width=8cm]{../covers/cover-v8-4.png}%
    };
  \end{tikzpicture}
\end{center}

\vfill

\begin{center}
  {\footnotesize\color{consoCreme!50}Cover V8-4 « Navy dominant, rose accent » · 3000×3000px}
\end{center}

\newpage
```

### 4.3 — Supprimer le bloc intermédiaire actuel

Le placeholder actuel (badge "PISTE RETENUE — V8-4" en tcolorbox) devient redondant avec le PNG de cover. Le retirer.

---

## Étape 5 — Recompiler

```bash
cd "/Users/denishenin/Documents/Bleen/projects/podcast_design/La conso/design-system"
xelatex -interaction=nonstopmode design-system-conso.tex
xelatex -interaction=nonstopmode design-system-conso.tex  # 2e passe pour TOC
```

Ouvrir `design-system-conso.pdf` → la page 1 doit maintenant ressembler à LGD/Vélotaf avec la cover V8-4 au centre.

---

## Checklist finale

- [ ] Serveur Bleen démarré sur `localhost:3400`
- [ ] `covers/v8-4-cover.html` créé (avec SVG Bleen inline)
- [ ] `covers/v8-4-title.html` créé
- [ ] `covers/layers/` dossier créé si absent
- [ ] `cover-v8-4.png` exporté (1080×1080 ou 2160×2160)
- [ ] `cover-v8-4-text.png` exporté (transparent, ~1800×400)
- [ ] `.tex` : `\IfFontExistsTF{Knewave}` ajouté
- [ ] `.tex` : page de titre remplacée
- [ ] PDF recompilé 2× (TOC)
- [ ] Page 1 vérifiée visuellement — comparable à LGD/Vélotaf

---

## Notes

- **Knewave** : si pas installé, le PDF tombera en fallback Marker Felt. Pour un rendu 100% fidèle, l'installer depuis https://fonts.google.com/specimen/Knewave
- **Taille du PNG de cover** : LGD utilise un fichier ~3 MB, Vélotaf ~1.5 MB. Viser qualité sans exploser le PDF.
- **Fond transparent du titre** : Puppeteer peut avoir besoin de `?transparent=1` selon l'implémentation de l'API (à tester). Fallback : exporter sur fond navy puis détourer.
