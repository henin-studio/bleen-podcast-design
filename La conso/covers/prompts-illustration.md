# Prompts d'illustration — Podcast Conso

> Prompts Gemini pour les covers du podcast consommation (Bleen).
> Derniere mise a jour : 13 avril 2026.

---

## Sommaire

1. [V6 — Sobre & Sexy](#v6) (direction actuelle, avril 2026)
2. [V5 — Absurde + Fanzine](#v5) (archivee, mars 2026)

---

# V6 — Direction "Sobre & Sexy" {#v6}

## Contexte

Feedback Olivier (avril 2026) :
- La cover 11 (crop 250% de `fille-noyee-objets.png`) a le bon cadrage
- Mais le visage fait **tristounet** a cote de LGD et Velotaf
- Pivot : "Make the transition sexy" — donner envie, pas deprimer
- Noms preferes : La Vie en Sobre, Juste Assez, Zero Superflu, La Deconsommation
- Si "La Vie en Sobre" : grosse touche de rose, rappel Piaf

## Strategie

On **varie la cover 11** plutot que repartir de zero :
- Meme composition (crop 250%, fragment visible, titre en haut)
- Changer le visage (joyeux), les couleurs (rose Piaf), l'emotion (liberte)
- Joindre `images/used/fille-noyee-objets.png` a Gemini comme reference

## Consignes globales

Copier ce bloc **avant** chaque prompt specifique :

```
CONTEXTE : Illustration pour une cover de podcast (consommation responsable).
Sera croppee a 250% — on ne verra que le visage + haut du corps.
L'expression du visage est CRITIQUE.

STYLE : Bold flat editorial illustration, thick outlines, saturated colors.
Famille de podcasts Bleen (Velotaf, La Grande Demission).
Clean shapes, pas hyperrealiste, pas cartoon.

EMOTION : Joyeuse, libre, confiante.
PAS triste, PAS accablee, PAS militante.
"La sobriete, c'est la liberte."

PALETTE :
- Rose Piaf #E8396B (dominant)
- Rose corail #FF4D6A
- Rose chaud #FF6B8A
- Creme chaud #FFF5E1
- Navy #221C46 (outlines)
- Jaune solaire #FFDC37 (accents)

TECHNIQUE : Black background. PNG. 3000x3000 min.
Pas de : purple gradients, floating particles, dreamy glow.
```

---

## Prompts V6

### V6-R1 — Meme pose, visage joyeux

> Variation directe. Le plus sur — on sait que la compo marche.
> **Joindre** `fille-noyee-objets.png`.

```
[Joindre l'image fille-noyee-objets.png]

Refais cette illustration en gardant la meme composition et le meme style
(femme entouree d'objets de consommation, vue plongeante / trois-quarts,
bold flat illustration, thick outlines, saturated colors).

CHANGEMENTS :
1. VISAGE : Remplace l'expression accablee par un SOURIRE FRANC.
   Yeux petillants, joie, legerete. Elle vient de decider de lacher prise.
2. COULEURS : Tons ROSES CHAUDS au lieu de sombres/froids.
   Rose dominant (#E8396B, #FF4D6A, #FF6B8A).
   Objets en creme (#FFF5E1) et jaune (#FFDC37).
   Outlines navy (#221C46).
3. OBJETS : Memes objets MAIS ils s'eloignent d'elle, flottent vers
   l'exterieur — elle les LACHE, pas elle est submergee.
4. ENERGIE : Donner ENVIE, pas deprimer. "Make the transition sexy."

GARDER : cadrage (vue plongeante), style flat bold, thick outlines.

Black background. PNG. Haute resolution.
```

---

### V6-R2 — Direction Piaf, rose tendre

> Specifique a "La Vie en Sobre". Rappel Piaf.
> **Joindre** `fille-noyee-objets.png`.

```
[Joindre l'image fille-noyee-objets.png]

Refais cette illustration mais dans une direction "LA VIE EN SOBRE" :

1. VISAGE : Sourire chaud, yeux mi-clos ou regard complice.
   Pas commercial — INTIME, comme Piaf qui chante.
   Quelqu'un qui a trouve ce qui compte vraiment.
2. COULEURS : Rose Piaf DOMINANT (#E8396B).
   Degrade #FF6B8A vers #F2A0B0. Creme #FFF5E1 pour accents clairs.
   Navy #221C46 outlines. PAS de bleu ciel.
3. ELEMENTS PIAF (subtils) : Une rose dans les cheveux OU a la main.
   Rappel retro/parisien (beret, mariniere) MAIS modernise. Pas un costume.
4. OBJETS : Moins que l'originale. Quelques-uns qui s'eloignent.
   L'espace vide est VOULU — c'est le message.
5. AMBIANCE : Romantique, chaleureuse, elegante.
   La sobriete comme choix desirable, pas sacrifice.

GARDER : style flat bold, thick outlines, cadrage serre.
Sera croppee a 250% — le visage doit etre lisible en miniature.

Black background. PNG. Haute resolution.
```

---

### V6-R3 — Liberation, bras ouverts

> Inversion emotionnelle de la cover 11. Le plus ambitieux.
> **Joindre** `fille-noyee-objets.png`.

```
[Joindre l'image fille-noyee-objets.png]

Refais cette illustration mais INVERSEE emotionnellement :

AVANT (image jointe) : submergee, passive, les objets l'envahissent.
APRES (ce que je veux) : LIBRE, active, les objets s'envolent loin d'elle.

1. POSE : Bras ouverts ou leves, corps detendu, en mouvement.
   Elle REPOUSSE les objets — geste d'ouverture, pas de noyade.
2. VISAGE : Grand sourire, yeux fermes de bonheur ou regard vers le haut.
   Quelqu'un qui retire un poids de ses epaules.
3. OBJETS : Memes objets MAIS en mouvement VERS L'EXTERIEUR.
   Ils s'eloignent, rapetissent, deviennent flous. Centre = elle, libre.
4. COULEURS : Rose Piaf (#E8396B, #FF4D6A), creme (#FFF5E1),
   jaune (#FFDC37) sur les objets qui partent. Navy outlines (#221C46).
5. ENERGIE : Joyeuse, dynamique. "La liberte de lacher prise."

GARDER : style flat bold, thick outlines, composition serree.
Crop 250% — visage + haut du corps = seules parties visibles.

Black background. PNG. Haute resolution.
```

---

### V6-R4 — Sobriete chic (from scratch)

> Pas de reference image. Style different a tester.

```
Editorial illustration of a young woman standing confidently with
almost nothing in her hands — just one beautiful object (a book,
a reusable cup, a plant). Dressed simply but stylishly.
Relaxed posture, slight smile, one hand in pocket or on hip.
She looks like she has her life figured out. Cool, not preachy.

Around her: lots of empty space. The emptiness IS the statement.
Maybe a few tiny consumer objects far away, faded, irrelevant.

Style: bold flat editorial illustration, thick outlines.
Colors: dominant rose Piaf (#E8396B), coral (#FF4D6A),
warm cream (#FFF5E1). Navy outlines (#221C46).

Expression: quiet confidence. "I chose this." Slight smirk.
French girl aesthetic meets sustainability.

Will be cropped to 250% — face and upper body are key.

Black background. High resolution. PNG.
```

---

### V6-R5 — Danse libre (from scratch)

> Pas de reference image. Energie pure, zero objet.

```
Editorial illustration of a young woman dancing or mid-twirl,
full of energy and joy. Hair in movement, clothes flowing.
No consumer objects — just her, in motion, free.
Maybe a few abstract shapes or confetti-like elements for energy.

Style: bold flat illustration, dynamic pose, thick outlines.
Colors: rose Piaf (#E8396B) dominant, coral (#FF4D6A),
rose chaud (#FF6B8A), cream (#FFF5E1). Navy outlines.

Movement frozen in time. Pure joy, laughter, eyes crinkled.
NOT a model pose — genuine, spontaneous movement.

The feeling of walking out of a store without buying anything
and feeling GREAT about it.

Will be cropped to 250% — upper body and face are anchor.

Black background. High resolution. PNG.
```

---

## Process Gemini

| Etape | Action |
|-------|--------|
| 1 | Copier les **consignes globales** V6 |
| 2 | Copier le **prompt specifique** (R1, R2, etc.) |
| 3 | **Joindre** `images/used/fille-noyee-objets.png` pour R1/R2/R3 |
| 4 | Generer |
| 5 | **Test crop** : zoomer a 250% sur le visage — l'expression se lit ? |
| 6 | Si non : re-generer en demandant un zoom sur le haut du corps |

**Ordre de priorite :**

1. **V6-R1** — variation directe, le plus sur
2. **V6-R2** — direction Piaf, specifique a "La Vie en Sobre"
3. **V6-R3** — liberation, bras ouverts
4. V6-R4 / V6-R5 — alternatives from scratch

**Black background** (pas transparent) : plus fiable sur Gemini. On retire le fond apres dans Photoshop ou via `background-removal-js`.

**Format :** 3000x3000px minimum, PNG.

---
---

# V5 — Direction "Absurde + Fanzine" (mars 2026) {#v5}

> **Archivee.** Direction precedente, avant le pivot d'Olivier.
> Les illustrations generees sont dans `images/used/`.
> Gardee comme reference — ne pas supprimer.

## Consignes globales V5

```
Style: editorial illustration, bold flat colors, slightly rough edges,
punk-pop aesthetic inspired by French fanzine Climax.
Not realistic, not cartoon, not cute. Satirical, energetic, graphic.
Black background. PNG with alpha channel.
High contrast. Thick outlines where appropriate.
No AI-slop: no purple gradients, no floating particles, no dreamy glow.
```

---

## 1. Personnage central

7 variantes generees. Toutes dans `images/used/`.

| Fichier | Prompt | Description |
|---------|--------|-------------|
| `fille-globe-dechets.png` | A | Femme tenant la Terre, dechets qui tombent |
| `fille-porte-globe.png` | C | Femme portant le globe, penchee sous le poids |
| `fille-ensevelie-achats.png` | A | Femme ensevelie sous sacs, colis, bouteilles |
| `fille-noyee-objets.png` | B | Femme noyee dans une mer d'objets (vue plongeante) |
| `fille-courses-frenetiques.png` | E | Femme aux bras charges, objets en equilibre |
| `fille-entouree-colis.png` | F | Femme entouree de colis et paquets |
| `chariot-surconsommation.png` | G | Homme poussant un caddie surcharge |

<details>
<summary>Prompts detailles (A-G)</summary>

### Prompt A — Femme submergee par des objets

```
Editorial illustration of a young woman seen from the waist up,
looking overwhelmed but not sad — more like "can you believe this?".
She's surrounded by and buried under consumer objects: shopping bags,
a smartphone, coffee cups, fast fashion clothes, delivery boxes,
plastic bottles. The objects are piling up around her, almost swallowing her.

Style: bold flat illustration, thick black outlines, saturated colors
(sky blue, coral pink, bright yellow accents). Punk-pop editorial aesthetic,
like a French satirical fanzine cover. NOT cute, NOT minimalist.
Energetic, slightly messy, graphic.

Expression: raised eyebrow, slight smirk — "stupefaction lucide".
Not angry, not crying, not smiling. Bewildered.

Black background. High resolution. PNG.
```

### Prompt B — Vue plongeante, noyee dans les objets

```
Editorial illustration, top-down view of a young woman lying on her back,
almost drowning in a sea of consumer objects. Seen from above. Her face
and one hand are visible above the surface of stuff — the rest is buried.
Objects everywhere: clothes, phones, coffee cups, shoes, packaging, cables,
plastic bags, food containers. She looks up at the viewer with a
"help me but also I bought all of this" expression.

Style: bold flat illustration, thick outlines, saturated colors
(sky blue, coral pink, bright yellow). Punk-pop fanzine aesthetic.
The composition should feel like looking into a pit of stuff.
Chaotic but visually organized — the objects radiate outward from her face.

Black background. High resolution. PNG.
```

### Prompt C — Femme portant la planete

```
Editorial illustration of a young woman carrying planet Earth
under her arm like a grocery bag. The Earth is heavy, she's leaning
to one side from the weight. Consumer objects are falling out of the
planet like it's an overstuffed bag — clothes, phones, plastic,
food packaging tumbling to the ground.

She looks at the viewer like "yeah, this is what we're doing."
Eyebrow raised, dry expression. Not dramatic, not sad. Deadpan.

Style: bold flat editorial illustration, thick black outlines,
saturated colors (sky blue, coral pink, yellow accents).
Punk-pop, satirical, like a French fanzine cover.

Black background. High resolution. PNG.
```

### Prompt D — Assise sur montagne de dechets

```
Editorial illustration of a young woman sitting casually on top of
a huge pile of consumer waste. She's scrolling on her phone,
unbothered, while the pile beneath her is massive — clothes, electronics,
plastic, packaging, broken toys, fast fashion, delivery boxes.
The contrast between her casual attitude and the absurd pile is the point.

She's dressed normally (jeans, sneakers, t-shirt). Not a caricature.
The absurdity comes from the situation, not the character.

Style: bold flat illustration, thick outlines. Saturated colors —
sky blue, coral pink, bright yellow. Punk-pop editorial, fanzine.
The pile should feel monumental, not depressing. Absurd, not dystopian.

Black background. High resolution. PNG.
```

### Prompt E — Bras charges (chaos)

```
Editorial illustration of a young woman trying to carry too many things
at once. Both arms full. Objects stacked impossibly high — balancing
coffee cups, shoe boxes, a laptop, shopping bags, a phone between
shoulder and ear, a delivery box under her chin. Some things are
mid-fall. She's mid-step, off-balance, about to lose everything.

The moment right before the crash. Frozen in time.
Expression: concentrated, determined, slightly panicked.

Style: bold flat editorial illustration, thick outlines, dynamic pose.
Saturated colors (sky blue, coral pink, yellow).
Punk-pop fanzine aesthetic. Energetic, not static.

Black background. High resolution. PNG.
```

### Prompt F — Mur de colis

```
Editorial illustration of a young woman standing in front of a giant
wall of delivery boxes. The boxes are stacked floor to ceiling behind her,
some with "24h" and "FREE SHIPPING" labels. She's holding one more box,
about to add it to the wall. She looks tiny compared to the wall.

The wall is slightly leaning forward, about to topple.
She doesn't seem to notice.

Style: bold flat illustration, thick outlines. Saturated colors.
Punk-pop, editorial, fanzine aesthetic. NOT realistic.
The scale disparity (small person / huge wall) is exaggerated.

Black background. High resolution. PNG.
```

### Prompt G — Caddie qui deborde

```
Editorial illustration of a person pushing an overflowing shopping cart.
The cart is absurdly overfull — objects spilling out in every direction:
clothes, electronics, food packaging, plastic bags, shoes, coffee cups.
The person looks small compared to the mountain of stuff in the cart.

Style: bold flat editorial illustration. Saturated colors (blues, pinks,
yellows). Thick outlines. Punk-pop fanzine aesthetic. Slightly tilted
composition for dynamic energy. NOT realistic, NOT 3D render.

Black background. PNG.
```

</details>

---

## 2. Elements de collage

<details>
<summary>Objets, ticket, Terre, dechets, stickers, texture</summary>

### Objets de consommation (pack de 8)

```
Set of 8 separate consumer objects, each on Black background,
in bold flat editorial illustration style. Thick outlines, saturated colors,
slightly rough/imperfect edges like cut-out magazine collage pieces.

Objects:
1. A takeaway coffee cup (overflowing, lid popping off)
2. A smartphone with cracked screen and notification bubbles
3. A pair of sneakers with a giant price tag
4. A delivery box with "24h" stamped on it
5. A fast fashion t-shirt with a barcode printed on it
6. A plastic bottle crushed and leaking
7. A shopping bag stuffed to bursting
8. A credit card bent/breaking

Style: punk-pop, editorial, fanzine. Each object like a magazine cut-out.
Colors: sky blue (#00B4F0), coral pink (#FF4D6A), yellow (#FFDC37),
navy (#221C46) outlines.

Each object separate. Black background. PNG.
```

### Ticket de caisse geant

```
Illustration of a giant supermarket receipt, slightly crumpled,
long, curling at the bottom. Editorial illustration with realistic
receipt texture but illustrated/graphic treatment. Yellowed paper,
thermal print font.

Text is NOT important (added in CSS). Just the visual of a long receipt
with lines, a barcode at bottom, and a TOTAL line in red/pink.

Style: cut-out collage piece, slight shadow, slightly tilted.
Black background. PNG.
```

### La Terre comme produit (3 variantes)

**A — Terre + code-barres :**
```
Planet Earth with a barcode stamped across it and a "-70%" price sticker.
The Earth looks like a supermarket product — faded, scratched, handled too much.
Flat editorial illustration, thick outlines. Pink price sticker.
Black background. PNG.
```

**B — Terre dans un caddie :**
```
Planet Earth sitting inside a shopping cart, too big, overflowing.
Cart dented, one wheel broken. Other consumer objects crammed around.
Bold flat illustration, punk-pop fanzine. Satirical, not cute.
Black background. PNG.
```

**C — Terre emballee sous plastique :**
```
Planet Earth wrapped in plastic shrink wrap like a supermarket product.
Barcode label stuck on. Slightly compressed/deformed by wrapping.
Bold editorial illustration, thick outlines, flat colors.
Black background. PNG.
```

### Montagne de dechets

```
Massive mountain/pile of consumer waste: clothes, electronics, plastic,
food packaging, shopping bags, broken toys, old smartphones.
Taller than buildings.

NOT depressing — saturated colors that pop (pinks, blues, yellows + grays).
Absurd and overwhelming, not dark and dystopian.
Fanzine/collage aesthetic, slightly chaotic.
Small human figure at base for scale (optional).

Black background. PNG.
```

### Stickers et tampons (pack de 6)

```
6 graphic sticker/stamp elements for a punk-pop fanzine:
1. Rubber stamp "EPUISE" (SOLD OUT) — red ink
2. Hand-drawn arrow pointing down with "2.9 TERRES"
3. Crossed-out Earth symbol (no sign over planet)
4. Torn price tag "TROP CHER"
5. Circle stamp "MADE IN EXPLOITATION"
6. Warning triangle + "SURCONSO"

Hand-stamped, rough edges, imperfect ink, punk aesthetic.
Colors: red, black, navy. Some yellow.
Each separate. Black background. PNG.
```

### Fond texture (optionnel)

```
Subtle paper texture overlay — slightly grainy, recycled paper / newsprint.
Very light, semi-transparent overlay on gradient background.
Just texture/grain, NOT a solid color.
Light gray on black background. PNG. 3000x3000px.
```

</details>

---

## Assemblage (pour les deux directions)

1. Detourer (fond transparent, pas de halo)
2. Assembler en HTML/CSS (remplacer les emojis par les illustrations)
3. Superposer sur le gradient (V6 = rose Piaf, V5 = bleu-rose)
4. Titre Knewave + contour par-dessus
5. Logo bleen discret en bas-droite
6. Exporter 3000x3000 via `covers/generate.py`

Les elements doivent pouvoir etre redimensionnes et repositionnes librement.
Chaque element doit fonctionner seul ET en composition.
