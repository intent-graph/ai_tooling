# Arbre des effets — remonter chaque changement à sa racine

Statut : ébauche. Internet refait selon la pratique du niveau de détail ; cloud encore dans
l'ancien format. Vue expérimentale, hors des phases 1 à 5 : ne modifie ni `par_dimension/`, ni
`par_annee/`, ni les taxonomies.

## Table of Contents

1. [Ce que c'est](#ce-que-c-est)
1. [Deux structures superposées](#deux-structures-superpos-es)
1. [Règles vérifiées](#r-gles-v-rifi-es)
1. [Ce que dit l'arbre Internet](#ce-que-dit-l-arbre-internet)
1. [Journal](#journal)
1. [Questions ouvertes](#questions-ouvertes)
1. [Fichiers](#fichiers)

---

## Ce que c'est
<!-- Lines 21-28 -->

Les vues par dimension, par acteur et par année disent ce qui a changé, pour qui, quand. Cette
vue dit **à cause de quoi**, et à quelle résolution : on lit un choc en une phrase, en six
branches, ou jusqu'aux faits. Un **changement** est quelque chose d'important qui a changé pour
quelqu'un, d'un groupe au monde entier.

---

## Deux structures superposées
<!-- Lines 31-49 -->

- **Un arbre de résolution.** Chaque boîte énonce ce que ses enfants additionnent ; les enfants
  la partitionnent, par *qui vit le changement* (deux à six enfants) ; les feuilles citent des
  faits du dossier, chaque fait sous une seule feuille. C'est ce qui permet de lire à n'importe
  quelle hauteur.
- **Des flèches causales entre boîtes**, comme les flux d'un diagramme SADT. Chaque boîte a une
  seule cause `principale` ; les autres causes sont pesées `fort` (sans elle, plus de la moitié du
  changement disparaît), `moyen` (un quart à la moitié), `faible` (moins d'un quart). Une cause
  peut être une autre boîte, de n'importe quelle branche, ou un confondant du registre
  ([04_confondants.md](../04_confondants.md)). `boucle` marque une rétroaction.
- **L'arbre des effets au sens strict** est la superposition des deux : en remontant de cause
  principale en cause principale, chaque feuille aboutit soit à la racine du choc, soit à un
  confondant, soit à une cause hors registre. Le vérificateur imprime ces chaînes.

Les deux structures sont séparées parce qu'un effet a souvent plusieurs causes : un arbre dont
les parents seraient les causes ne peut ni partitionner, ni se lire à plusieurs hauteurs.

---

## Règles vérifiées
<!-- Lines 52-68 -->

`python3 verifier_arbre.py` (dossier `internet/` par défaut) vérifie, puis réécrit un diagramme
par niveau ; `--check` vérifie sans écrire ; `--elagues` liste les faits du choc qu'aucune feuille
ne cite.

1. Deux à six enfants par boîte ; faits aux feuilles seulement.
2. Tout fait cité existe dans le dossier et n'est cité qu'une fois.
3. Une et une seule cause principale par boîte, sauf quand la cause est hors fenêtre (`amont`).
4. Toute cause désigne une boîte existante ou un confondant du registre, avec un poids.
5. Une cause qui atteint une boîte profonde depuis une autre branche figure aussi sur chaque
   ancêtre traversé.
6. Pas de cycle entre causes, hors boucles.

Les diagrammes ne montrent pas les causes `faible`, qui restent dans le texte.

---

## Ce que dit l'arbre Internet
<!-- Lines 71-99 -->

Inférences tirées de la structure (causes et poids sont des jugements de l'agent). Détail :
[internet/README.md](internet/README.md).

1. **La racine tient en deux leviers.** Transmettre ne coûte presque plus rien, à toute distance
   et à toute durée (13 feuilles y remontent) ; personne ne possède les protocoles ni ne filtre
   l'entrée (15 feuilles). Copier, trouver et observer ne deviennent bon marché qu'ensuite, par
   d'autres mécanismes : copie de masse en 1999 avec la musique déjà numérisée, recherche comme
   service en 1998, publicité sur mots-clés dominante en 2003.
2. **Le capital parie sur la racine entière, pas sur un levier** (8 feuilles, dont l'emploi
   informatique qui suit le capital). Son krach brade la
   fibre, qui abaisse encore le coût de transmettre : la forme en deux temps (H3) est une boucle.
3. **Neuf feuilles sur 45 ont leur cause principale hors du choc** : l'ordinateur (X.INT.01 :
   empreinte électrique, fracture d'accès, productivité, emplois de routine), la mondialisation
   (délocalisation vers l'Inde), la déréglementation (privatisations), la trajectoire chinoise,
   le 11 septembre, et une cause absente du registre, les réseaux privés d'échange de données
   antérieurs à 1995.
4. **Le plus gros changement mesuré n'est ni le plus visible, ni le réseau.** Le commerce
   électronique entre entreprises fait plus de 90 % de tout le commerce électronique, mais passe
   surtout par ces réseaux antérieurs (83,5 % du commerce électronique de gros en 2005) ; le commerce de détail en ligne, visible, pèse 2,3 %.
5. **Addition avant substitution.** La télévision reste dominante, le courrier postal croît
   jusqu'en 2001, la plupart des banques en ligne ont moins de 10 % de clients actifs, le
   télétravail reste marginal. La destruction se concentre sur les intermédiaires dont la rente
   était l'accès (agences de voyages : −35 %).
6. **Tête et traîne ont la même cause, et la concentration précède la recherche.** Le trafic suit
   une loi de puissance dès 1997, avant le classement par liens ; la recherche l'amplifie.

---

## Journal
<!-- Lines 102-118 -->

**Première version, abandonnée.** Tableaux plats ; cinq leviers tirés d'une décomposition de la
littérature non ouverte, placés sous la racine avec des effets (la racine n'était pas partitionnée) ;
quatre racines disjointes ; 89 faits cités sur 345, dix sous deux nœuds ; une ligne d'une clause
par nœud, toutes à la même hauteur ; poids à deux décimales, plus précis que leurs appuis, et
parts calculées à partir d'eux.

**Écartés.** Un arbre dont les parents sont les causes (un effet à plusieurs causes casse la
partition). Une partition par levier : la plupart des changements avaient deux ou trois leviers
pour parents, signe que la coupe était fausse.

**Deuxième version (Internet).** Partition par qui vit le changement, causes en flèches pesées
grossièrement, racine décomposée depuis les faits, 296 faits cités sur 410, les autres élagués
(doublons d'énoncé, contexte exogène, points intermédiaires de séries, discours) et listables.

---

## Questions ouvertes
<!-- Lines 121-133 -->

1. **Registre.** Deux causes hors registre portent des branches : la pile de protocoles financée
   sur fonds publics avant 1995, et les réseaux privés d'échange de données entre entreprises.
   Proposition : deux confondants X.INT.11 et X.INT.12, à décider dans la collecte.
2. **Attribution à revoir dans le dossier.** F.INT.F4.012 (domination des films américains en
   Europe en 2000) est attribué `choc` ; l'arbre ne le rattache pas, cette domination précède le
   réseau.
3. **Cloud.** À refaire au même format. Le pont entre les deux chocs (premiers services hébergés,
   grandes entreprises qui gardent leurs centres de calcul) se construira à ce moment-là.
4. **Relecture** par un modèle distinct avant de s'appuyer sur les causes.

---

## Fichiers
<!-- Lines 136-141 -->

| fichier | contenu |
| --- | --- |
| [internet/](internet/README.md) | arbre Internet : vue d'ensemble et racine, puis une branche par fichier |
| [cloud.md](cloud.md) | arbre cloud, première version, format abandonné |
| [verifier_arbre.py](verifier_arbre.py) | vérification des règles, chaînes principales, diagrammes |
