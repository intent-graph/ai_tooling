# Thèse et méthode

Ce document fixe le niveau 0 du dossier : ce qu'on cherche à établir, comment on traite un choc
technologique comme un traitement expérimental observé sur dix ans, quelles fenêtres on étudie,
ce qui compte comme preuve, et quelles hypothèses de travail on se donne à tester.

## Table of Contents

1. [But et usage](#but-et-usage) _(Lines 23-41)_
1. [Hypothèse de départ](#hypoth-se-de-d-part) _(Lines 44-77)_
1. [Le choc comme traitement](#le-choc-comme-traitement) _(Lines 80-112)_
1. [Fenêtres temporelles et position actuelle](#fen-tres-temporelles-et-position-actuelle) _(Lines 115-143)_
1. [Ce qu'on produit](#ce-qu-on-produit) _(Lines 146-163)_
1. [Standard de preuve](#standard-de-preuve) _(Lines 166-189)_
1. [Hypothèses de travail à tester](#hypoth-ses-de-travail-tester) _(Lines 192-240)_
1. [Décisions](#d-cisions) _(Lines 243-266)_


---

## But et usage
<!-- Lines 23-41 -->

**Question du dossier :** quand une technologie d'ampleur civilisationnelle se généralise, qu'est-ce
qui change dans la société pendant les dix années qui suivent, dans quel ordre, à quel rythme,
et pour qui ?

**Pourquoi maintenant :** l'arrivée des LLM et des systèmes agentiques est vécue comme un choc de
cette ampleur. Plutôt que de spéculer sur ses conséquences, on documente rigoureusement deux
chocs comparables déjà achevés, puis, dans un second temps, on lit le choc actuel à leur lumière.

**Usages visés :**
- outil de pensée personnel, structuré, réutilisable ;
- base pour un résumé destiné à des collègues, un texte grand public, une publication courte ;
- socle factuel de la session 2 (parallèles et extrapolation encadrée).

Le public visé est large : le lecteur doit comprendre le *pourquoi* sans jargon, et pouvoir
remonter au fait précis derrière chaque affirmation.

---

## Hypothèse de départ
<!-- Lines 44-77 -->

L'arrivée des LLM et des agents est un **choc** : un changement majeur introduit dans le système
social, dont on peut observer les conséquences. Deux analogies historiques sont posées, chacune
pour un bloc de dimensions.

| Bloc de dimensions | Analogie primaire | Justification |
| --- | --- | --- |
| Économie, culture, société, politique | **Internet, 1995-2005** | Généralisation d'une technologie de mise en relation à l'échelle de toute la population ; rupture des intermédiaires, des modèles d'affaires et de l'accès à l'information. |
| Industrie, infrastructure | **Cloud, 2005-2015** | Industrialisation de l'informatique : des « usines » (centres de données, plateformes) produisent des services numériques consommés à la demande. Choc **industriel** : peu visible du grand public, il porte tous les acteurs et toutes les chaînes de production, et touche donc toute la société, directement ou indirectement. Rupture de même niveau qu'Internet, dans la manière de *produire*. |

L'analogie est **primaire, pas exclusive**. Chaque dimension est documentée pour les deux chocs ;
l'analogue primaire indique seulement où l'on attend le signal le plus riche. Une dimension
pauvre pour un choc (par exemple la culture pour le cloud) est un résultat, pas un défaut.

**Essence de chaque choc**, formulée au même niveau d'abstraction pour rendre la comparaison possible :

| Choc | Essence | Ce qui devient possible |
| --- | --- | --- |
| Internet | L'interconnexion universelle | N'importe quel nœud atteint n'importe quel autre ; distribuer une information ne coûte presque plus rien. |
| Cloud | L'industrialisation de l'informatique | Produire et exploiter un service numérique ne demande plus de posséder l'usine ; la capacité se loue à l'unité. |
| LLM et agents | L'arrivée du non-structuré | Des machines reçoivent, traitent et produisent du non-structuré, en **format** (texte libre, image, parole) et en **méthode** (le « programme » n'a plus à être précisément défini à l'avance). Par contraste avec l'informatique classique où tout doit être spécifié, y compris la procédure. |

Le choc IA est un choc **unique**, LLM et agents en étant deux facettes ; il commence avec
l'explosion de ChatGPT (novembre 2022). Il est **absent** des fichiers historiques.

**Axiome de production, posé par l'auteur :** la production est **humain + énergie**. Les deux
facteurs ont chacun leur domaine d'observation, D pour le travail, H pour l'énergie. Dans cette
lecture, un choc de productivité qui ne s'accompagnerait d'aucun changement énergétique serait
suspect ; le dossier vérifie donc, pour chaque fenêtre, ce qui a bougé du côté de l'énergie
(hypothèse H5). Les autres thèses macro de l'auteur, abondance future d'énergie renouvelable et
facteur démographique, sont hors du périmètre de ce dossier (décision D14).

---

## Le choc comme traitement
<!-- Lines 80-112 -->

On emprunte à l'évaluation d'impact l'idée d'un **traitement** : le choc est introduit, on
observe les conséquences en essayant de tenir compte des autres variables. C'est tout ce qu'on
emprunte ; on ne cherche ni identification causale formelle ni cadre théorique strict.

**Ce que « avec / sans » veut dire ici**, faute de contrefactuel observable :

1. **Ligne de base.** Pour chaque sous-dimension, l'état et la tendance des deux années
   précédant t0. Une variation n'est un effet que si elle s'écarte de cette tendance.
2. **Groupes de comparaison.** Là où ils existent : blocs géographiques, secteurs ou groupes
   d'acteurs touchés plus tard ou moins fort. Leur trajectoire sert de « sans » approché.
3. **Registre des confondants.** Les autres causes actives dans la fenêtre sont listées dans
   [04_confondants.md](04_confondants.md) ; chaque fait porte une attribution explicite.

**Ce qu'on refuse :** la réponse binaire. Sur dix ans, un changement de cette magnitude n'est
pas un interrupteur. Pour chaque dimension, on veut la **variation au cours des années** :
quand ça commence, quand ça accélère, quand ça se corrige, quand ça se banalise.

**Ce qu'on documente pour chaque cellule (sous-dimension × choc) :**

| Objet | Question à laquelle il répond |
| --- | --- |
| Faits | Que s'est-il passé, mesurablement, et quand ? |
| Jalons | Quels événements datés marquent une bascule ? |
| Trajectoire | Année par année, dans quelle phase est-on et avec quelle intensité de changement ? |
| Narratif | En quelques phrases, quelle est la forme du changement ? |

Le vocabulaire de phases est un outil de lecture partagé, pas un modèle imposé :
`latent`, `émergence`, `accélération`, `crise`, `consolidation`, `banalisation`.
Une trajectoire peut sauter des phases ou en répéter.

---

## Fenêtres temporelles et position actuelle
<!-- Lines 115-143 -->

| Choc | t0 retenu | Fenêtre | Justification du t0 |
| --- | --- | --- | --- |
| Internet | 1995 | 1995 → 2005 | Bascule grand marché : navigateur commercial, fin du réseau académique, premiers commerces en ligne, entrée massive des ménages. 1991 (Web public) est trop tôt : la technologie existe, le choc social n'a pas commencé. |
| Cloud | 2005 | 2005 → 2015 | Les premières briques à la demande sortent des grands acteurs du Web et l'idée d'informatique-utilité devient une offre. 2006 serait défendable ; 2005 capte l'année de bascule interne. |
| LLM et agents | Nov. 2022 | 2022 → 2032 | Explosion de ChatGPT : première adoption grand public massive d'un système à entrées et sorties non structurées. |

Les deux fenêtres historiques sont **contiguës et sans recouvrement** : 1995-2005 puis 2005-2015.
2005 sert de borne finale au premier choc et de borne initiale au second.

**Convention de comptage.** L'année t0 est l'année 0. La fenêtre compte onze années calendaires,
de t0 à t0+10 inclus ; t0+10 est « l'état final ». Les tableaux de trajectoire ont une ligne
« avant t0 » puis une ligne par année.

**Position actuelle du choc IA, à vérifier en session 2 :**

| Grandeur | Valeur |
| --- | --- |
| t0 | novembre 2022 |
| Temps écoulé à la date de rédaction | 3 ans et 10 mois |
| Année en cours (année 0 = nov. 2022 → oct. 2023) | année 3, à un mois de l'année 4 |
| Position équivalente, choc Internet | fin 1998 → 1999 |
| Position équivalente, choc cloud | fin 2008 → 2009 |

Ces équivalences supposent des rythmes comparables, ce qui est précisément une des choses que le
dossier doit tester (voir H1 et H3). Elles servent de repère, pas de conclusion.

---

## Ce qu'on produit
<!-- Lines 146-163 -->

Deux axes orthogonaux classent chaque fait, trois vues en dérivent.

| Axe | Fichier de définition | Question |
| --- | --- | --- |
| Dimensions | [01_dimensions.md](01_dimensions.md) | Quel aspect de la société a changé ? |
| Acteurs | [02_acteurs.md](02_acteurs.md) | Qui l'a vécu, et comment ? |

| Vue | Emplacement | Ce qu'elle montre |
| --- | --- | --- |
| Par dimension | `par_dimension/<domaine>/<choc>.md` | Faits, jalons, trajectoires, narratifs d'un domaine pour un choc. La comparaison des deux chocs va dans le `README.md` du domaine. |
| Par acteur | `par_acteur/<acteur>.md` | Le vécu d'un groupe à travers les deux chocs. |
| Par année | `par_annee/<choc>.md` | Le rythme : tous les jalons d'un choc, année par année, tous domaines. |

Le format exact des enregistrements est dans [03_modele_de_donnees.md](03_modele_de_donnees.md).

---

## Standard de preuve
<!-- Lines 166-189 -->

**Sources admissibles**, par ordre de préférence :

1. Séries statistiques officielles ou institutionnelles : BLS, BEA, Census, OCDE, UIT, Banque
   mondiale, Eurostat, INSEE, banques centrales, Pew Research.
2. Travaux académiques publiés ou documents de travail de référence (NBER, Brookings, banques
   centrales, revues à comité de lecture).
3. Rapports officiels, textes de loi, décisions de justice, dépôts réglementaires (SEC),
   rapports annuels d'entreprises.
4. Ouvrages de référence historiques ou économiques sur la période.
5. Presse contemporaine **de l'événement**, pour dater un jalon uniquement.

**Exclus :** tribunes, prévisions d'analystes, billets d'opinion, synthèses de vulgarisation
sans source, contenu généré ou agrégé sans provenance.

**Exception encadrée :** les prévisions faites *pendant* la fenêtre (par exemple en 1999 ou en
2009) sont admissibles comme **artefacts historiques** dans une annexe « prédictions contre
résultats », séparée des faits. Cette annexe est optionnelle et décidée en phase 5.

**Statuts :** `V` vérifié à la source citée ; `K` connaissance de l'agent, à vérifier ; `D` disputé.
Un narratif ne peut s'appuyer sur un fait `K` que si celui-ci est qualitatif et non controversé.

---

## Hypothèses de travail à tester
<!-- Lines 192-240 -->

Elles guident ce qu'on regarde. Elles ne sont pas supposées vraies ; les chronologies et
trajectoires servent à les confirmer, nuancer ou rejeter en phase 5.

**H1. Retard différencié par domaine.** Les domaines répondent au choc dans un ordre stable :
industrie et finance d'abord (mois à deux ou trois ans), économie et travail ensuite (deux à six
ans), vie quotidienne par courbe d'adoption (trois à huit ans), culture et politique en dernier
(cinq à dix ans et plus). L'ordre des domaines dans [01_dimensions.md](01_dimensions.md) suit
cette hypothèse.

**H2. Retard croissant avec la distance à l'épicentre.** Les acteurs qui construisent la
technologie la vivent en premier ; les intermédiaires qu'elle court-circuite ensuite ; les
groupes périphériques (monde rural, seniors, pays en développement) en dernier, et souvent par
un canal indirect. L'ordre des groupes dans [02_acteurs.md](02_acteurs.md) suit cette hypothèse.

**H3. Forme en deux temps.** Une phase d'emballement suivie d'une correction au milieu de la
fenêtre, puis d'une consolidation où les gains réels apparaissent. À tester : la correction
est-elle propre à Internet (2000-2002) ou se retrouve-t-elle, sous une autre forme, pour le cloud ?

**H4. Chaque choc effondre un coût.** Internet effondre le coût de *distribuer* ; le cloud
effondre le coût de *produire et exploiter* un service ; on notera en session 2 si le choc IA
effondre le coût de *formaliser*. Cette hypothèse structure la lecture des modèles d'affaires
(C4) et du mode de production (A4). Elle est de l'auteur du dossier, pas de la littérature.

**H5. Pas de choc de productivité sans changement énergétique.** Pour chaque fenêtre, la
variation de productivité (C1) coïncide avec un changement du côté de l'énergie : prix, mix,
efficacité par unité de service, ou nature même de l'appareil du choc comme convertisseur
d'énergie en service. Thèse de l'auteur, à tester en croisant H1 et H3 avec C1 ; sa réfutation
sur une fenêtre compte autant que sa confirmation.

**H6. Le choc est un habilitant.** Pour les deux chocs, les changements les plus grands ne
passent pas par l'usage direct de la technologie, mais par ce qu'elle rend possible : produits
dérivés (D9), chaînes de conditions de possibilité (D16), mondialisation des services rendue
praticable. À tester : pour chaque domaine, la part des changements documentés qui passe par
un canal indirect ; et, en C1, la part des gains de productivité qui revient à la
mondialisation (X.INT.03) plutôt qu'à l'usage du réseau. Thèse de l'auteur.

**H7. Uniformisation et accès à l'information.** Les deux chocs se résument, côté culture et
société, à deux mouvements : un choc d'information (accéder à l'information devient facile) et
un choc d'uniformisation. L'uniformisation prend la forme d'un passage d'une distribution des
consommations et des attentions à peu près centrée à une distribution concentrée sur quelques
valeurs, décroissant vite, mais avec une longue traîne très épaisse. La diffusion de la culture
américaine en fait partie, que la part de l'anglais dans les pages du réseau recule ou non. À
tester sur la concentration (tête et traîne) et sur la diffusion culturelle par blocs, en
cherchant aussi les contre-exemples (écosystèmes nationaux d'Asie de l'Est et de Chine). Thèse
de l'auteur.

---

## Décisions
<!-- Lines 243-266 -->

Journal des choix structurants, dans l'ordre où ils ont été pris. Git porte les dates.

| # | Décision | Motif |
| --- | --- | --- |
| D1 | « Choc » au sens de traitement observé, pas de cadre théorique strict | On veut les grands changements, leur rythme et leurs jalons, pas une réponse binaire ni une école. |
| D2 | Fenêtres 1995-2005 et 2005-2015, contiguës, sans recouvrement | 1991 trop tôt pour Internet ; 2005 capte la bascule interne du cloud. |
| D3 | Sept domaines ordonnés par retard attendu ; travail séparé de l'économie | Le travail a ses propres acteurs et indicateurs, et c'est le pivot de la lecture future. |
| D4 | Axe acteurs orthogonal à l'axe dimensions, avec portraits | Le vécu des groupes, y compris loin de l'épicentre, est une information que les dimensions seules ne donnent pas. |
| D5 | Analyse mondiale par blocs, récit centré sur l'Occident si choix nécessaire | Les deux chocs sont nés aux États-Unis mais ont été vécus partout. |
| D6 | Choc IA unique, t0 novembre 2022, essence « arrivée du non-structuré » | Formulation de l'auteur ; sert de cible à la session 2 uniquement. |
| D7 | Français, sources dans leur langue ; dossier grand public | Outil de pensée réutilisable pour résumés, publications courtes. |
| D8 | Jalons avant faits (phase 1 avant phase 2) | Le rythme doit être fixé avant que le détail ne remplisse les cases. |
| D9 | Le téléphone intelligent et les réseaux sociaux sont des produits dérivés d'Internet et du cloud, pas des co-chocs ; le grand public est un acteur minoritaire en poids | L'importance du téléphone intelligent est une idée de culture populaire, pas un fait mesuré. Le cloud est un choc industriel qui porte toutes les chaînes de production. Vérification par les chiffres inscrite en phase 2, voir [04_confondants.md](04_confondants.md). |
| D10 | Les sous-agents de collecte tournent sur le modèle Opus, pas Fable | Choix de l'auteur. |
| D11 | Le cycle spéculatif d'Internet (pic 2000, correction 2000-2002) est un effet du choc, classé en B2, pas un confondant | Le cycle naît du choc et s'y résorbe ; X.INT.04 couvre déjà le cycle macroéconomique. Question remontée par la phase 1, tranchée. |
| D12 | Ajout de X.CLD.10, baisse continue du coût du matériel, comme prérequis de la fenêtre cloud ; pas de sous-dimension énergie, A1 la couvre (**partie énergie annulée par D13**) | Sans identifiant, les baisses de prix des services loués étaient attribuées au choc en entier. Questions remontées par la phase 1. |
| D13 | Ajout du domaine **H Énergie**, quatre sous-dimensions H1 à H4, hors de l'ordre de retard ; confondants X.INT.10 et X.CLD.11 pour le contexte énergétique ; hypothèse H5 | L'énergie est primordiale pour l'auteur : la production est humain + énergie, et un choc de productivité sans changement énergétique est suspect. Le sujet dépasse un indicateur de A1. |
| D14 | Hors périmètre : la thèse d'un choc futur d'abondance d'énergie renouvelable et le facteur démographique (arrivée d'un milliard d'Africains sur le marché mondial) | Idées de l'auteur pour d'autres travaux. Pour ce dossier, seule compte l'énergie comme dimension d'observation des deux chocs passés. |
| D15 | Sous-agents de collecte en Sonnet à partir de la phase 2 (remplace D10) ; première vague : H et A pour le cloud, H et C pour Internet | Choix de l'auteur. La première vague porte le test de H5, croisement de H1, H3 et C1. |
| D16 | L'impact culturel du cloud est **indirect** et se documente comme une **chaîne de conditions de possibilité**, dans un dossier transversal `par_dimension/F_culture/cloud_condition_de_possibilite.md`, et non en gonflant les cellules | Thèse de l'auteur : le cloud est ce qui a rendu possibles les réseaux sociaux, le partage d'images et de vidéos, et les messageries de masse. La règle d'attribution D9 empêchait de le dire ; la cellule F×CLD l'a constaté sans l'établir. La chaîne se documente par les coûts et les échelles, pas par l'usage des services dérivés. |
| D17 | La productivité (C1) ne se lit pas sur la seule série américaine. Deux motifs : la place à part des États-Unis dans l'économie mondiale, et le biais d'une productivité mesurée comme variation de la richesse produite (valeur ajoutée déflatée), qui confond efficacité, prix et marges. La lecture de C1 s'appuie sur les panels multi-pays qui croisent intensité d'adoption des TIC et productivité, et sur la littérature de mesure (productivité en valeur contre productivité physique). La série américaine reste un fait, pas une conclusion | Choix de l'auteur. Le résultat acquis n° 1 du README porte cette réserve. |
| D18 | Refonte de la taxonomie après relecture de la fenêtre Internet, sans renumérotation : **A** en deux blocs, bâtisseurs A1-A4 et utilisatrices A5-A8 (A6 canaux de vente, A7 adoption et usage interne, A8 services rendus possibles) ; **B** par composante du capital, B1 privé domestique, B4 étranger, B5 public et régulation, B2 et B3 transversales ; **D3** renommée « organisation du travail et outils en réseau » ; **F5** concentration et diversité des consommations (test de H7) ; **G1-G3 gelées**, géopolitique en G4 souveraineté et sécurité, G5 domination d'infrastructure, G6 fracture entre pays ; X.INT.03 requalifié « partiellement endogène ». Les faits existants gardent leur identifiant et leur sous-dimension ; les nouvelles sous-dimensions les citent. Pour le cloud, les nouvelles sous-dimensions sont à collecter | Relecture de l'auteur : le dossier confondait bâtisseurs et industries utilisatrices ; la finance appelait une lecture par origine du capital ; le travail était réduit au secteur informatique ; la politique intérieure intéresse moins que la géopolitique. Six recherches ciblées du 2026-09-23 ont fondé le découpage. |
| D19 | Ajout d'un **axe transversal « accaparement »** (ruée sur un territoire neuf : terrain, accapareur, mécanisme, temporalité), dans `par_dimension/transversal/accaparement.md`. Le fichier cite les faits par identifiant et n'en crée aucun (R7) ; les épisodes absents deviennent des cibles de collecte dans leur sous-dimension de rattachement. Taxonomies inchangées (R9) | Question de l'auteur, posée pour les deux chocs. Précédent : le dossier transversal de D16. |
