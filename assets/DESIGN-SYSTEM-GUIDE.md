# Guide — Design System PDF pour podcasts Bleen

> Process reproductible pour produire un design system PDF de qualité professionnelle.
> Template de reference : Velotaf (`Velotaf/design-system/design-system-velotaf.tex`)

---

## Structure attendue par podcast

```
podcast_design/
  [Podcast Name]/
    index.html                  <- SOURCE DE VERITE (couleurs, fonts, CSS)
    DESIGN-SYSTEM.md            <- peut etre obsolete, cross-checker avec HTML
    covers/
      cover-xxx.png             <- composite final (3000x3000)
      layers/
        cover-xxx-bg.png        <- fond gradient
        cover-xxx-character.png <- personnage, fond transparent
        cover-xxx-text.png      <- titre, fond transparent    <-- UTILISE SUR LA COVER PAGE
        cover-xxx-logo.png      <- bb + bleen, fond transparent
    design-system/
      design-system-xxx.tex     <- source LaTeX
      design-system-xxx.pdf     <- output final
```

---

## Pipeline en 6 phases

### Phase 1 — Rassembler les sources

Lire TOUS les fichiers avant de toucher au LaTeX :

| Source | Priorite | Contient |
|--------|----------|----------|
| `index.html` | **1 (verite)** | Hex couleurs, fonts, gradients CSS, dimensions |
| `covers/layers/` | **1** | PNGs pour la cover page et la section Typographie |
| `DESIGN-SYSTEM.md` | 2 | Structure du contenu (peut etre obsolete) |
| `covers/cover-xxx.png` | 2 | Composite pour preview dans le PDF |

**Regle :** HTML > .md quand ils se contredisent. Toujours verifier les hex, noms de fonts et directions de gradient contre le HTML.

### Phase 2 — Scaffolder le .tex depuis Velotaf

Copier le preamble de `design-system-velotaf.tex` et adapter uniquement les couleurs. Les elements suivants sont non-negociables :

#### Preamble

```latex
\usetikzlibrary{shadows,shadings}     % shadings OBLIGATOIRE pour les gradients
\usepackage{pifont}                    % AVANT titlesec
\usepackage{titlesec}
```

#### Tables

```latex
% Definir AVANT \begin{document}
\definecolor{tableHeader}{HTML}{F0F0F0}
\definecolor{tableRowAlt}{HTML}{F9FAFB}
\newcommand{\tableheader}{\rowcolor{tableHeader}\bfseries}
```

Pas de `\rowcolors` global dans le preamble — appliquer par table :
```latex
\rowcolors{2}{white}{tableRowAlt}
\begin{tabularx}{...}
\tableheader Col1 & Col2 \\
```

#### Card style tcolorbox

```latex
card/.style={
  enhanced,                              % en premier
  colback=cardBg, colframe=grayLight,
  boxrule=0.4pt,                         % PAS 0.5pt
  arc=6pt,
  left=12pt, right=12pt, top=10pt, bottom=10pt,
  fonttitle=\bfseries\sffamily,          % sffamily obligatoire
  coltitle=grayDark,                     % explicite
  drop shadow={shadow xshift=0.5pt, shadow yshift=-1.5pt, opacity=0.12},
  breakable,                             % UNITES EN PT, jamais mm
}
```

#### Color swatches (texte a cote, pas dedans)

```latex
\newcommand{\colorswatch}[3]{%           % 3 args : couleur, nom, hex
  \begin{tikzpicture}
    \fill[#1, rounded corners=4pt] (0,0) rectangle (1.2,1.2);
    \node[anchor=west, font=\small\bfseries, text=grayDark] at (1.45,0.75) {#2};
    \node[anchor=west, font=\footnotesize\ttfamily, text=grayMid] at (1.45,0.35) {#3};
  \end{tikzpicture}%
}
```

Espacement : `\hspace{18pt}` entre swatches. 3 par ligne max, puis `\vspace{6pt}\noindent` pour la ligne suivante.

#### Sections

```latex
\titleformat{\section}
  {\fontsize{22}{26}\selectfont\bfseries\sffamily\color{...}}
  {\thesection.}{0.5em}{}              % point apres le numero, 0.5em

\titleformat{\subsection}
  {\fontsize{14}{18}\selectfont\bfseries\sffamily\color{grayDark}}
  {\thesubsection}{0.5em}{}
```

Pas de `\titlespacing*` — laisser LaTeX gerer l'espacement naturellement.

#### Do's / Don'ts

```latex
\newcommand{\doitem}[1]{\item[\color{green}\ding{51}] #1}
\newcommand{\dontitem}[1]{\item[\color{red}\ding{55}] #1}
% leftmargin=16pt dans l'itemize
```

#### Footer

```latex
\fancyfoot[L]{\small\color{grayMid}[Nom Podcast] Design System — Denis Henin · uixbydenis.eu}
% Derniere page : "Bleen Consulting"
```

### Phase 3 — Cover page

Layout identique a Velotaf :

```latex
\vspace*{0.8cm}
\includegraphics[width=9cm]{../covers/layers/cover-xxx-text.png}   % PNG du titre
\\[6pt]
{\Large\color{white}\bfseries Cover Art — Design System}\\[4pt]
{\small\color{white!60}Version 1.0 — [Mois Annee]}\\[2pt]
{\small\color{white!40}Denis Henin — Graphiste Designer @ bleen}

\vspace{0.4cm}

\begin{tikzpicture}
  \node[drop shadow={shadow xshift=1pt, shadow yshift=-2pt, opacity=0.3, fill=black},
        inner sep=0pt] {%
    \includegraphics[width=7.5cm]{../covers/cover-xxx.png}%
  };
\end{tikzpicture}
```

- Titre = **PNG** depuis `layers/` (pas du texte LaTeX)
- Image composite = **7.5cm** avec drop shadow TikZ
- Zone gradient = top 9cm, zone dark = reste
- `\vfill` + footnote en bas

### Phase 4 — Les 9 sections

Chaque section doit remplir >60% de sa page. Objectif : aucune page avec plus de 40% de blanc.

| # | Section | Contenu minimum | Piege courant |
|---|---------|----------------|---------------|
| 1 | Contexte du podcast | Table 9+ lignes (nom, tagline, concept, producteur, format, ton, audience, themes, univers visuel) + Positionnement + "Ce que la marque est/n'est pas" | Table trop courte |
| 2 | Palette de couleurs | Gradient preview + CSS snippet + swatches principales + swatches secondaires + roles des couleurs (table) + contraste/lisibilite | Gradient gris (manque shadings) |
| 3 | Typographie | Hierarchie typo (table 4 colonnes) + cover image a **0.75\linewidth** + table proprietes + traitement du texte (enumerate) | Image trop grande = debordement |
| 4 | Illustration | Table style + description personnage + table fichier source + nettoyage image | Moitie basse vide |
| 5 | Composition | Schema TikZ (gradient `left color`/`right color`) + regles de composition + table calques export | Schema gris |
| 6 | Logo Bleen | Subsection "Composition du bloc logo" + table + subsection "Regles" | Table seule = 75% vide |
| 7 | Effets & overlays | Paragraphe d'intro + table effets | Pas d'intro |
| 8 | Specs techniques | Table format + CSS de reference (verbatim sur fond dark) | OK en general |
| 9 | Declinaisons | Table formats reseaux (type `llX` pas `lll`) + Do's & Don'ts en multicols | Mauvais type de colonne |

### Phase 5 — Audit page par page

Apres la premiere compilation, ouvrir le PDF et verifier CHAQUE page :

1. **Cover** : titre PNG visible ? Image dans la zone dark ? Credit auteur lisible ?
2. **TOC** : toutes les sections listees ? Pas d'entrees dupliquees ?
3. **Chaque page de contenu** :
   - Remplissage >60% ?
   - Tables avec lignes alternees ?
   - Cards avec ombre ?
   - Pas de gradients gris ?
   - Pas de subsections dupliquees ?
4. **Derniere page** : ligne gradient + "Bleen Consulting" ?

**Si une page est >40% vide :**
- Enrichir le contenu (ajouter subsections, descriptions)
- Supprimer le `\newpage` avant la section (laisser LaTeX enchaIner)
- Fusionner les sections courtes

### Phase 6 — Compilation

```bash
cd [podcast]/design-system/
xelatex -interaction=nonstopmode design-system-xxx.tex   # passe 1
xelatex -interaction=nonstopmode design-system-xxx.tex   # passe 2 (TOC)
open design-system-xxx.pdf
```

---

## Gotchas connus

| Probleme | Cause | Fix |
|----------|-------|-----|
| Gradient TikZ gris | `upper left`/`lower right` sans shadings lib | Utiliser `left color`/`right color` |
| Ombres trop lourdes | Unites en `mm` au lieu de `pt` | `0.5mm = 1.4pt`, toujours utiliser `pt` |
| Alternance lignes sur TOC | `\rowcolors` global dans le preamble | Appliquer `\rowcolors` par table |
| Checkmarks invisibles | `\symbol{"2713"}` unicode dans Avenir Next | Utiliser `\ding{51}` de pifont |
| Image cover deborde | `\linewidth` dans un card | Utiliser `0.75\linewidth` ou `width=7.5cm` |
| "I can't find Knewave" | Font pas installee | Attendu — fallback Marker Felt fonctionne |
| Subsections dupliquees | Erreur d'edition | Verifier la TOC apres compilation |

---

## Assets partages

| Fichier | Usage |
|---------|-------|
| `assets/bleen-tokens.css` | Source de verite pour les tokens Bleen (brand #2ed5a3, fonts Satoshi/Chillax, spacing, shadows) |
| `assets/logo/bleen-icone.svg` | Icone bb seule (currentColor) |
| `assets/logo/bleen-icone-noir.svg` | Icone bb noire |
| `assets/logo/bleen-logo-blanc.svg` | Logo complet blanc (pour fonds sombres) |

---

## Checklist avant livraison

- [ ] 2 passes xelatex sans erreur bloquante
- [ ] Cover : titre PNG + image 7.5cm + credit dans zone dark
- [ ] TOC : pas de doublons, numeros de page corrects
- [ ] Toutes les pages remplies a >60%
- [ ] Tables : lignes alternees + header gris
- [ ] Swatches : texte a cote (pas dedans), rounded corners
- [ ] Gradients TikZ : couleurs visibles (pas gris)
- [ ] Do's/Don'ts : checkmarks vert/rouge via pifont
- [ ] Footer brande sur chaque page
- [ ] Derniere page : "Bleen Consulting"
