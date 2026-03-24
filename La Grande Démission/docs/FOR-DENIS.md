# La Grande Démission — Documentation Projet

> Tout ce qu'il faut savoir pour reprendre le travail à n'importe quel moment.

---

## Le projet en clair

On crée l'identité visuelle complète du podcast "La Grande Démission" pour Bleen (bleen.be). Le podcast interview des gens qui ont quitté le corporate pour un métier à impact — boulanger solaire, écologie radicale, écoles de transition.

Le design doit être sérieux mais chaleureux, entre Sismique (grave, éditorial) et 2030 Glorieuses (engagé, accessible). Jamais corporate, jamais coaching "feel-good".

## Ce qui existe

### Fichiers du projet

```
La Grande Démission/
├── index.html                        → Page principale avec TOUT le travail visuel
├── instructions.md                   → Brief complet (positionnement, invités, direction)
├── RESEARCH-podcast-cover-design.md  → Recherche marché (podcasts concurrents, tendances 2026)
├── AUDIO-IDENTITE-SONORE.md          → Brief audio (mood, sources, prompts Suno.ai)
├── FOR-DENIS.md                      → Ce fichier
├── *.jpg                             → ~80 photos (Unsplash/Pexels libre de droits + iStock previews)
```

### Ce qui a été produit

| Quoi | Quantité | Détail |
|------|----------|--------|
| Covers podcast général | 96 | G1 à G96, dans `index.html` |
| Covers épisode | 12 | E1 à E12, avec invitée fictive Marie Lefort |
| Propositions de palette | 6 | D à I (Bleu Conviction, Charbon & Or, Terracotta, Sarcelle, Indigo & Pêche, Olive & Crème) |
| Esquisses initiales | 6 | Directions 1 à 6 (dans un `<details>` collapsible) |
| Photos téléchargées | ~80 | Unsplash + Pexels (libre de droits) + iStock (previews watermark) |
| Documents de recherche | 3 | instructions.md, RESEARCH, AUDIO |

### GitHub Pages (public)

- **Repo** : https://github.com/henin-studio/la-grande-demission
- **Page live** : https://henin-studio.github.io/la-grande-demission/
- Contient : `index.html` + photos. PAS les fichiers internes (.md).
- Pour mettre à jour : copier le nouveau `index.html` + photos dans `/tmp/la-grande-demission/`, commit, push.

---

## Architecture de la page

La page `index.html` est organisée avec une **nav sticky** en haut :

```
Contexte | Palettes (6) | Cover Generale (96) | Cover Episode (12)
```

Chaque section a un ID pour le scroll :
- `#contexte` — le podcast, les invités, les inspirations
- `#palettes` — 6 propositions chromatiques (D à I) + ref Vélotaf
- `#cover-general` — 96 covers en grille (contient aussi les esquisses dans un `<details>`)
- `#cover-episode` — 12 covers avec invitée fictive

### Polices chargées (Google Fonts)

- **Plus Jakarta Sans** (300-800) — police Bleen, utilisée pour les titres sans-serif
- **DM Serif Display** — serif éditorial, la plus utilisée dans les covers récentes
- **Fraunces** (300-900) — serif "wonky", organique, personnalité forte
- **Playfair Display** (400-900) — serif classique, style magazine
- **Space Grotesk** (400-700) — sous-titres, labels, metadata

### Palettes

| Code | Nom | Couleurs principales | Utilisée dans |
|------|-----|---------------------|---------------|
| Nuit & Terre | (principale) | #1B2838, #2C3E50, #E8D5B7, #C9956B | G1-G54, G55-G66, G73-G84 |
| D | Bleu Conviction | #001A4D → #0066FF + blanc | G72 |
| E | Charbon & Or | #1A1A1A + #D4AF37 | G69, G75, G87 |
| F | Terracotta | #3D1C11 → #CD7F32 + #FAE8D0 | G71, G76, G90 |
| G | Sarcelle | #0A2A2A → #14B8A6 + #CCFBF1 | G67, G81 |
| H | Indigo & Pêche | #1E1B4B → #6366F1 + #FDBA8C | G66, G68 |
| I | Olive & Crème | #1a1c16 → #6B7F4A + #F5F0E1 | G70, G80 |
| Bleen | (corporate) | #0D2B1E + #1EE8A0 | G62 (terminal vert) |

---

## Comment reprendre le travail

### Ajouter de nouvelles covers

1. Ouvrir `index.html`
2. Chercher la dernière cover (`G96`) — juste avant `</div>` + `<hr class="section-separator">` + `<!-- COVER EPISODE -->`
3. Ajouter le HTML d'une nouvelle cover (format ci-dessous)
4. Mettre à jour les compteurs : chercher `nav-badge">96` et `section-count">96`, remplacer par le nouveau nombre
5. Vérifier que les tags `<div>` sont équilibrés : `/usr/bin/grep -c '<div\|<details' fichier` doit être = `/usr/bin/grep -c '</div>\|</details>' fichier`

**Template d'une cover :**
```html
<!-- Cover GXX — Nom -->
<div class="design-card" onclick="selectCover(this,'gXX')">
  <div style="aspect-ratio:1;overflow:hidden;">
    <div style="width:100%;height:100%;background:#1B2838;position:relative;overflow:hidden;display:flex;align-items:center;justify-content:center;padding:40px;">
      <!-- Contenu visuel ici -->
      <!-- Titre -->
      <div style="position:absolute;bottom:28px;left:0;right:0;text-align:center;z-index:2;">
        <div style="font-size:9px;color:rgba(201,149,107,0.5);letter-spacing:0.2em;text-transform:uppercase;margin-bottom:10px;font-family:'Space Grotesk',sans-serif;">Podcast Bleen</div>
        <div style="font-size:36px;font-weight:400;color:#E8D5B7;line-height:0.95;font-family:'DM Serif Display',serif;">La Grande</div>
        <div style="font-size:36px;font-weight:400;color:#C9956B;line-height:0.95;font-family:'DM Serif Display',serif;font-style:italic;margin-top:2px;">Démission</div>
      </div>
      <div style="position:absolute;bottom:10px;font-size:10px;font-weight:800;color:rgba(232,213,183,0.05);font-family:'Plus Jakarta Sans',sans-serif;">bleen</div>
    </div>
  </div>
  <div class="design-body">
    <span class="design-num" style="background:#1B2838;">GXX</span>
    <h3>Nom de la Cover</h3>
    <p>Description courte.</p>
  </div>
</div>
```

### Ajouter une photo

1. Télécharger dans le dossier `La Grande Démission/`
2. Nommer clairement : `unsplash-description.jpg` ou `pexels-description.jpg`
3. Utiliser dans une cover avec `<img src="nom-fichier.jpg" alt="" style="width:100%;height:100%;object-fit:cover;">`
4. Toujours ajouter un overlay : `<div style="position:absolute;inset:0;background:linear-gradient(180deg,rgba(13,17,23,0.4),...);"></div>`

### Mettre à jour GitHub Pages

```bash
# Copier les fichiers publics
cp "La Grande Démission/index.html" /tmp/la-grande-demission/
cp "La Grande Démission/"*.jpg /tmp/la-grande-demission/

# Commit et push
cd /tmp/la-grande-demission
git add -A
git commit -m "Update covers"
git push
```

Le site se met à jour en ~1 minute.

### Lancer le serveur local

```bash
cd /Volumes/home/JOBs/Bleen && node server.js
# → http://localhost:3400/projects/podcast_design/La%20Grande%20D%C3%A9mission/
```

Ou via le dashboard (cliquer "Start" sur Bleen).

---

## Décisions de design prises

### Palette retenue : Nuit & Terre
- Bleu nuit #1B2838 — "le ciel à 5h du matin quand tu réfléchis à ta vie"
- Cuivre #C9956B — "la chaleur humaine dans l'obscurité, le métal qui patine"
- Sable #E8D5B7 — "la respiration, l'espace, la page blanche d'après"

### Typo dominante : DM Serif Display
- "La Grande" en regular, "Démission" en italic
- Accent cuivre sur "Démission"
- Sous-titres en Space Grotesk

### Règles absolues
- **JAMAIS couper le mot "Démission"** sur deux lignes
- **JAMAIS de micro/casque/ondes sonores** en illustration (cliché podcast)
- **JAMAIS de gradient violet** (cliché AI/startup)
- **JAMAIS de sourire "tout va bien"** (manque de gravité pour le sujet)
- Logo "bleen" toujours discret (petit, bas, opacity faible)
- Tester chaque cover en miniature (100px) et en dark mode

### Ce qui marche le mieux (d'après les agents)
- **Typo pure** : le titre est assez puissant pour porter la cover seul
- **Photos de dos / silhouettes** : pas de visage identifiable pour la cover générale
- **Le concret** : pain, terre, outils — pas des métaphores abstraites
- **La tension** : ancien monde (froid, N&B, grille) vs nouveau monde (chaud, couleur, organique)

---

## Agents mobilisés pendant la session

| Agent | Mission | Résultat |
|-------|---------|----------|
| Trend Researcher | Podcasts concurrents FR, tendances covers 2026 | `RESEARCH-podcast-cover-design.md` (320 lignes) |
| Explorer (brand) | Analyse identité Bleen, palettes, Vélotaf | Rapport complet brand tokens |
| Analyste Psy/Com | Psychologie du public, sémiologie couleurs, archétypes | Analyse des 3 profils d'auditeurs, 4 émotions visuelles |
| UI Designer / DA | 10 concepts créatifs originaux | Tampon, Badge, Organigramme, Terminal, Carte postale, etc. |
| Explorer (invités) | Contexte NeoLoco, Vinz Kanté, ÊTRE | Positionnement podcast |
| Frontend Specialist | 6 covers HTML (Cinéma, Vinyle, Livre, Magazine, Carte, Ticket) | G91-G96 insérées dans index.html |
| Agents photos (x3) | Téléchargement photos Unsplash/Pexels | ~40 photos téléchargées |

### Insights clés des agents

**Public cible (3 profils) :**
1. Le Ruminant Actif (35-45, cadre, cherche "la permission")
2. Le Fraîchement Démissionnaire (28-40, cherche la validation)
3. Le Curieux Engagé (25-50, fascination intellectuelle)

**Émotion pivot :** l'envie mêlée de peur. Le public veut et redoute la même chose.

**Archétype principal :** l'Explorateur (pas le Rebelle, pas le Gourou, pas le Héros)

**Tension narrative :** la gravité (ce qui retient) vs le saut (accepter de tomber)

---

## Prochaines étapes

### Visuel
- [ ] Choisir 3-5 covers favorites parmi les 96
- [ ] Affiner les favorites (taille réelle 3000x3000, polices ajustées)
- [ ] Créer les covers épisode correspondantes
- [ ] Acheter les photos iStock nécessaires (si cover retenue les utilise)
- [ ] Export PNG via Puppeteer (`/api/export-png/`)

### Audio
- [ ] Lire `AUDIO-IDENTITE-SONORE.md`
- [ ] Générer jingle intro/outro avec Suno.ai (prompts prêts dans le fichier)
- [ ] Tester en contexte (monter un faux début d'épisode)
- [ ] Valider sur téléphone + casque + enceinte

### Production
- [ ] Enregistrer le premier épisode (NeoLoco ?)
- [ ] Monter avec jingle + bed + stingers
- [ ] Publier sur Spotify / Apple Podcasts
- [ ] Créer les covers épisode avec les vraies photos des invités

### Système multi-podcasts
- [ ] Définir le format commun Bleen (position titre, zone logo, structure)
- [ ] Couleur propre à chaque podcast (coral pour Vélotaf, Nuit & Terre pour LGD)
- [ ] Template déclinable pour les futurs podcasts

---

## Leçons apprises

### Ce qui a bien marché
- **Les agents en parallèle** : lancer psy + DA + brand explorer en même temps = 3 perspectives riches en 2 minutes
- **Les photos d'abord, les covers ensuite** : avoir un stock de photos avant de designer permet d'itérer vite
- **Les palettes multiples** : proposer 6 palettes puis les exploiter toutes dans des covers donne un panorama complet
- **Le brief enrichi progressivement** : `instructions.md` est passé de 25 lignes à un document complet grâce aux agents

### Pièges rencontrés
- **Le mot "Démission" coupé** : facile d'oublier avec des grandes tailles de typo. Toujours vérifier avec `grep 'émis-'`
- **Les IDs Unsplash** : les URLs ne correspondent pas toujours à ce qu'on attend. Toujours vérifier les photos après téléchargement
- **Le fichier HTML devient énorme** (4300+ lignes) : la nav sticky aide mais il faudrait probablement paginer si on continue
- **RTK filtre les réponses curl** : utiliser `/usr/bin/curl` pour les appels API qui retournent du JSON
- **Les agents n'ont pas toujours accès à Bash** : les agents de type "general-purpose" peuvent être bloqués sur curl. Mieux vaut télécharger les photos soi-même

### Outils utiles découverts
- **Suno.ai** : le meilleur générateur de musique AI pour podcast
- **DM Serif Display** : la police qui a le plus de personnalité pour ce projet
- **Le concept de "fissure"** : la métaphore visuelle la plus forte selon l'analyste psy
- **Le format "objet détourné"** (tampon, badge, ticket, carte) : les covers les plus distinctives dans un feed podcast
