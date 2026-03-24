# Feedback V1 — Debrief Client (2026-03-23)

## Contexte

Debrief avec le client sur les 53 covers V1 + palettes. Notes brutes retranscrites.

## Feedback général

### Titre
- Le nom pourrait être raccourci : "La Grande Dem'" (sans accent sur le é)
- Inspiré de "Vélotaf" — nom court, punchy
- **Font retenue** : Knewave (Google Fonts) — brush/handwritten, peps et enfantine
- **Hiérarchie typo** : "La Grande" en plus petit/sérieux, "Démission" (ou "Dem'") en plus grand/peps
- Les deux en Knewave, la taille fait la différence

### Logo & Branding
- Favicon : le B de Bleen (icône BB)
- Mot "bleen" visible sur la cover
- Icône BB et texte "bleen" peuvent être séparés (BB en haut gauche, bleen en bas)

### Style visuel
- Texte globalement plus grand que la V1
- **Flat design** : transformer les photos en personnages flat/illustrés
- Anonymiser sans dépersonnaliser (lisser le personnage pour le rendre impersonnel mais humain)
- Fond uni (pas de photo/gradient complexe dans V1)

### Covers de référence
- G8 et G9 comme point de départ (versions coral avec papiers/saut)
- G5 (Terracotta & Lavande) — la plus poétique, couleurs à intégrer
- G32 (L'Élan) — référence pour la taille du texte et le centrage

### Couleurs
- Palette Lavande & Gris retenue initialement : #9B8EC4 #C4B1D4 #4A4A5A
- Combiner avec Terracotta Solaire : #C2704A #3D1C11 #FAE8D0
- Le client aime les gradients (gradient Bleen : linear-gradient 90° #e76366 → #8355eb)

### Référence externe
- S'inspirer du style Vélotaf (orange chaleureux, clean, moderne)
- Même approche : fond couleur + personnage illustré + titre brush

## Décisions prises

1. Font : Knewave pour tout le titre
2. Images flat design via Gemini (à partir des photos existantes)
3. Remove bg avec flood fill scipy (meilleur résultat sur illustrations)
4. Gradient backgrounds au lieu de fonds unis
5. Logo BB séparé du texte "bleen"
6. "Podcast" → remplacé par SVG "bleen" en bas

## Points non résolus

- Détourage des doigts/mains (petits résidus blancs entre les doigts)
- Contraste texte/fond sur les gradients clairs (amélioré avec paint-order stroke)
- Choix final du gradient pour le set Lavande & Terracotta (4 options testées)
