# Covers — La Conso

## Fichiers

| Fichier | Contenu |
|---------|---------|
| `cover-1-homo-consumens.png` | Cover "Homo Consumens" — 3000x3000 |
| `cover-2-trop.png` | Cover "TROP" — 3000x3000 |
| `generate.py` | Script de generation automatique |

## Comment regenerer les covers

```bash
cd "La conso"
python3 covers/generate.py            # 3000x3000 (defaut)
python3 covers/generate.py --size 1500  # taille custom
```

Prerequis : `pip install playwright Pillow` + `playwright install chromium`

## Source de verite

Le design vit dans `index.html` (section `#v1-2`). C'est la reference.
Le script `generate.py` reproduit les memes proportions en standalone.

## Proportions — deux facteurs de scale

Le HTML card fait 280x280 dans la grille du navigateur. Le script utilise
**deux facteurs** pour garder les proportions correctes a haute resolution :

```
S  = TARGET / 280          # ~10.7x a 3000px — pour les tailles
SB = sqrt(S) * 1.5         # ~4.9x  a 3000px — pour les blurs/ombres
```

### Pourquoi deux facteurs ?

Les blurs et ombres ne scalent pas lineairement. Un `text-shadow` de 30px
a 280px donne un effet subtil. Multiplie par 10.7 (= 321px) et tu obtiens
un halo enorme qui mange le texte. La racine carree donne un resultat
visuellement equivalent.

### Quoi utilise quoi

| Propriete | Facteur | Raison |
|-----------|---------|--------|
| `font-size` | **S** (lineaire) | Le texte doit remplir le meme % de l'espace |
| `margin`, `gap`, `padding` | **S** (lineaire) | L'espacement suit la taille |
| `width`, `height`, `position` | **%** | Auto-scale, pas besoin de facteur |
| `text-shadow` (blur) | **SB** (sqrt) | Blur perceptuel, pas lineaire |
| `text-stroke` | **SB** (sqrt) | Contour trop epais si lineaire |
| `drop-shadow` (image, logo) | **SB** (sqrt) | Meme raison que text-shadow |
| SVG `width` (logo) | **S** (lineaire) | Taille physique du logo |

### Piege classique

Si tu ajoutes une nouvelle cover avec des ombres, utilise `SB` pour les
blur/shadow et `S` pour les tailles. Si le resultat a un halo trop gros,
c'est que tu as utilise `S` au lieu de `SB`.

## Modifier une cover

Si tu changes les valeurs CSS dans `index.html` :

1. Trouver la valeur de base (ex: `font-size: 50px` dans le card a 280px)
2. Dans `generate.py`, reporter : `font-size:{int(50 * S)}px`
3. Pour les shadows : `text-shadow: 0 {int(3 * SB)}px {int(10 * SB)}px`
4. Regenerer et verifier

## Workflow

1. Modifier le design dans `index.html`
2. Verifier dans le navigateur (les cards dans la section v1-2)
3. Lancer `python3 covers/generate.py`
4. Verifier les PNGs dans `covers/`
5. Si blur trop gros → ajuster les valeurs `SB` dans generate.py
