# Confondants — les autres causes actives dans chaque fenêtre

Registre des changements concomitants qui peuvent expliquer une variation observée aussi bien
que le choc étudié. C'est l'outil du « en contrôlant les autres variables » de la méthode : chaque
fait porte une attribution qui renvoie ici. Les dates sont indicatives et à vérifier lors de la
collecte (statut `K` par défaut).

## Table of Contents

1. [Types de confondants et règles d'attribution](#types-de-confondants-et-r-gles-d-attribution) _(Lines 22-41)_
1. [Fenêtre Internet 1995-2005](#fen-tre-internet-1995-2005) _(Lines 44-65)_
1. [Fenêtre cloud 2005-2015](#fen-tre-cloud-2005-2015) _(Lines 68-91)_
1. [Cas difficile : le téléphone intelligent, produit dérivé et non co-choc](#cas-difficile-le-t-l-phone-intelligent-produit-d-riv-et-non-co-choc) _(Lines 94-129)_
1. [Test de séparabilité](#test-de-s-parabilit) _(Lines 132-142)_



---

## Types de confondants et règles d'attribution
<!-- Lines 22-41 -->

| Type | Définition | Attribution des faits qui en dépendent |
| --- | --- | --- |
| **Prérequis** | Tendance antérieure au choc, sans laquelle il n'aurait pas lieu (équipement, technologie de base). | `exo` par défaut. `choc` seulement si le choc a visiblement changé la pente du prérequis. |
| **Co-choc** | Changement majeur indépendant, actif dans la même fenêtre, qui produit des effets dans les mêmes dimensions. | `co:<ID>`. Le narratif doit dire quelle part revient au choc étudié. |
| **Exogène** | Événement sans lien causal avec le choc : crise, guerre, ouverture commerciale, politique monétaire. | `exo`. Sert surtout à expliquer une rupture de ligne de base. |
| **Réponse endogène** | Décision prise *à cause* du choc : loi, déréglementation, stratégie publique. | `choc`. C'est un effet, classé en G, même s'il amplifie ensuite le choc. |
| **Produit dérivé** | Ce que le choc a rendu possible et qui devient à son tour une cause. | `choc` si le choc est condition nécessaire ; `co:` si un co-choc l'est aussi. |

**Règle de prudence.** En cas de doute entre `choc` et `co:`, choisir `co:`. Une attribution trop
généreuse au choc est l'erreur qui rend un dossier de ce type non crédible.

**Règle de la ligne de base.** Quand un exogène casse la tendance (récession de 2001, crise de
2008), la trajectoire de la sous-dimension le signale explicitement dans la colonne « ce qui
change » de l'année concernée, avec l'identifiant du confondant.

**Registre fermé pendant la collecte.** On peut ajouter un confondant ; on ne renumérote pas.

---

## Fenêtre Internet 1995-2005
<!-- Lines 44-65 -->

| ID | Type | Confondant | Période | Dimensions touchées | Statut |
| --- | --- | --- | --- | --- | --- |
| X.INT.01 | Prérequis | Diffusion du micro-ordinateur dans les ménages et les entreprises ; baisse continue du coût du calcul | Années 1980 → 2005 | A1, C2, E1, D2 | K |
| X.INT.02 | Co-choc | Téléphonie mobile de deuxième génération et messagerie courte : abonnements de masse, usage du texto | 1995 → 2005 | E2, E5, A1, A5 (télécoms) | K |
| X.INT.03 | Exogène, partiellement endogène | Ouverture commerciale et mondialisation : accords régionaux, création de l'OMC, entrée de la Chine, monnaie unique européenne. La mondialisation des **services** est en partie rendue praticable par le choc (baisse du coût des télécoms internationales, travail à distance), après des prérequis nationaux antérieurs (réformes indiennes de 1991) et un déclencheur daté (passage à l'an 2000) | 1994 → 2002 | C3, C1, D1, D3, G4 | K |
| X.INT.04 | Exogène, partiellement endogène | Cycle macroéconomique américain : longue expansion, récession de 2001, politique monétaire accommodante | 1991 → 2003 | B2, C1, D1 | K |
| X.INT.05 | Partiellement endogène | Passage à l'an 2000 : dépenses informatiques anticipées, puis creux | 1997 → 2001 | A4, B1, D1 (informatique) | K |
| X.INT.06 | Réponse endogène | Déréglementation des télécoms aux États-Unis puis en Europe | 1996 → 1998 | A1, A3, G1 | K |
| X.INT.07 | Exogène | Attentats du 11 septembre 2001 et guerres qui suivent : sécurité, surveillance, dépenses publiques | 2001 → 2005 | G4, G1, F3 | K |
| X.INT.08 | Prérequis | Numérisation des contenus hors réseau : disque compact, compression audio, disque vidéo numérique, photographie numérique | 1993 → 2005 | F1, A5 (médias), E4 | K |
| X.INT.09 | Exogène, parallèle | Trajectoire chinoise séparée : contrôle du réseau, écosystème national | 1998 → 2005 | G4, A3, T4 | K |
| X.INT.10 | Exogène | Ère de l'énergie bon marché : pétrole à son plus bas réel vers 1998-1999, électricité stable ; crise électrique californienne 2000-2001 comme exception locale ; remontée pétrolière à partir de 2003 | 1995 → 2005 | H3, H2, C1, C2 | K |

**Lecture de X.INT.03 (décision D18).** Pour la productivité (C1), la mondialisation agit par deux mécanismes documentés et de sens opposés : un gain réel par la délocalisation de services vers l'industrie, et un biais de mesure qui gonfle la productivité officielle quand les achats basculent vers des fournisseurs étrangers moins chers. Les deux ne s'additionnent pas. Un fait de productivité qui touche ces mécanismes porte `co:X.INT.03`. Voir `C_economie/internet.md` § C1 et C3.

**Lecture.** Le confondant le plus délicat est X.INT.02 : le mobile change la communication
quotidienne (E2, E5) en même temps qu'Internet, par un autre canal et une autre industrie. Les
faits de communication interpersonnelle de la fenêtre porteront souvent `co:X.INT.02`.

---

## Fenêtre cloud 2005-2015
<!-- Lines 68-91 -->

| ID | Type | Confondant | Période | Dimensions touchées | Statut |
| --- | --- | --- | --- | --- | --- |
| X.CLD.01 | Produit dérivé | Téléphone intelligent et magasins d'applications : terminal connecté permanent, produit dérivé d'Internet (réseau, services) et des usines cloud (services en arrière-plan), pas un co-choc | 2007 → 2015 | E1 à E5, A5, C4, D3, F4 | K |
| X.CLD.02 | Produit dérivé | Réseaux sociaux de masse : ouverture au grand public, vidéo amateur, flux ; services hébergés dans les usines cloud | 2005 → 2015 | E2, E4, F1, F3, F4, G3 | K |
| X.CLD.03 | Exogène majeur | Crise financière de 2008, récession, puis taux proches de zéro et assouplissement quantitatif | 2008 → 2015 | B1, B2, C1, D1, D4 | K |
| X.CLD.04 | Prérequis, co-choc | Haut débit mobile et fixe : troisième puis quatrième génération, fibre | 2005 → 2015 | A1, E1 | K |
| X.CLD.05 | Compagnon technique | Données massives et apprentissage automatique : cadres de calcul distribué, renaissance des réseaux de neurones | 2006 → 2015 | A2, A4, F2 | K |
| X.CLD.06 | Prérequis | Maturité de l'open source et plateformes de code partagé | 2005 → 2015 | A2, A4, D2 | K |
| X.CLD.07 | Exogène | Géopolitique : révélations sur la surveillance de masse, soulèvements arabes, crise de la zone euro, montée de la Chine | 2010 → 2015 | G4, G1, F3 | K |
| X.CLD.08 | Produit dérivé | Économie à la demande et du partage : hébergement, transport, livraison par plateformes | 2008 → 2015 | D3, C4, A5, E3 | K |
| X.CLD.09 | Prérequis | Virtualisation des serveurs dans les entreprises | 2001 → 2008 | A2, A4 | K |
| X.CLD.10 | Prérequis | Baisse continue du coût du matériel : calcul, stockage, bande passante ; pendant de X.INT.01 pour la seconde fenêtre. Une part des baisses de prix des services loués lui revient. | 2005 → 2015 | A1, C2, A4 | K |
| X.CLD.11 | Exogène | Bascule énergétique : flambée pétrolière jusqu'en 2008 puis repli, révolution du gaz de schiste aux États-Unis, chute du coût du solaire photovoltaïque | 2005 → 2015 | H3, H2, C1, G4 | K |

Le contexte énergétique lui-même est documenté comme faits dans la sous-dimension H3 ; X.INT.10
et X.CLD.11 servent à la co-attribution depuis les autres domaines, notamment C1.

**Lecture.** X.CLD.05 est à traiter avec retenue : c'est le précurseur du choc suivant, et le
dossier ne doit pas le développer au-delà de son rôle dans la fenêtre (règle R1). On note qu'il
existe, on n'en tire rien pour la session 1.

---

## Cas difficile : le téléphone intelligent, produit dérivé et non co-choc
<!-- Lines 94-129 -->

Le téléphone intelligent (X.CLD.01) et les réseaux sociaux (X.CLD.02) sont les changements les
plus visibles de la fenêtre 2005-2015 pour le grand public. Le dossier les traite comme des
**produits dérivés** d'Internet et des usines cloud, et non comme des co-chocs : sans réseau
universel et sans capacité louée en arrière-plan, ni le terminal ni les services qu'il porte
n'existent sous cette forme. L'inverse n'est pas vrai.

**Piège à éviter.** L'importance accordée au téléphone intelligent vient de la culture populaire,
pas d'une mesure. Son impact est réel sur le grand public ; mais le grand public est un acteur
**minoritaire en poids** face aux organisations et aux chaînes de production que le cloud
transforme. Le cloud n'est pas un usage grand public : c'est une infrastructure fondamentale
qui porte tous les acteurs et toutes les chaînes de production, et touche donc toute la société,
directement ou indirectement. C'est un choc **industriel**, moins spectaculaire qu'Internet,
pas moins profond.

**Vérification inscrite au plan de collecte** (phase 2, sous-dimensions B1, C2, A5) : mettre en
regard, année par année, le chiffre d'affaires des terminaux mobiles, celui des services cloud,
et la dépense informatique totale des organisations que le cloud transforme. Le dossier ne
préjuge pas du résultat ; l'argument de poids passe autant par le canal indirect que par les
chiffres directs, et la comparaison doit le montrer ou le nuancer.

**Règle d'attribution retenue :**

| Le fait porte sur… | Attribution | Exemple de forme |
| --- | --- | --- |
| L'**usage** ou l'**ampleur** d'un service mobile ou social hébergé | `choc` (produit dérivé : le service n'existe que par des usines externes), X.CLD.01 noté en secondaire comme canal | Nombre d'utilisateurs, temps passé, part de la population. |
| La **manière dont ce service a été produit et mis à l'échelle** | `choc` | Taille de l'équipe, absence de serveurs propres, délai de lancement, coût marginal d'un utilisateur. |
| Le **marché des terminaux** lui-même | `co:X.CLD.04` ; documenté en A5 (électronique, télécoms) comme secteur reconfiguré, jamais comme cause | Ventes d'appareils, constructeurs, systèmes d'exploitation mobiles. |
| Le **réseau d'accès** | `co:X.CLD.04` | Couverture, débits, abonnements mobiles. |

Le narratif du domaine E pour le cloud dira que le grand public a vécu la fenêtre à travers ces
produits dérivés, et rappellera le poids limité de ce vécu dans le choc lui-même. Le cœur du
choc se lit dans A, C, D et dans les portraits d'organisations.

---

## Test de séparabilité
<!-- Lines 132-142 -->

Avant d'attribuer `choc` à un fait, poser les trois questions :

1. **Le fait serait-il arrivé sans le choc, à la même date ?** Si oui, `exo` ou `co:`.
2. **Le fait serait-il arrivé sans le co-choc actif dans la fenêtre ?** Si non, `co:`.
3. **Existe-t-il un groupe de comparaison** (bloc, secteur, acteur) touché plus tard par le choc
   mais autant par le confondant ? Si sa trajectoire diverge, cela soutient `choc` ; si elle suit,
   cela soutient `co:` ou `exo`. Noter le groupe dans la colonne « note » de la source.

Ces questions sont un garde-fou, pas une méthode d'identification. Le dossier reste une analyse
historique structurée ; il n'a pas vocation à établir des effets causals au sens économétrique.
