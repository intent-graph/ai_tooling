# A. Industrie et infrastructure — Cloud 2005-2015

Ce que l'industrie informatique a connu pendant la fenêtre du choc cloud, sous-dimension par
sous-dimension : faits sourcés, jalons cités, trajectoire année par année, narratif court. Le
cloud est un choc **industriel** : des usines (centres de données, plateformes) produisent des
services numériques consommés à la demande par toutes les organisations. Le téléphone
intelligent et les réseaux sociaux y apparaissent seulement comme produits dérivés et clients de
l'usine, jamais comme le sujet. Ligne de base : état des deux années précédant 2005. La
comparaison avec l'autre choc est dans le `README.md` du domaine, pas ici.

## Table of Contents

1. [A1 Infrastructure physique et capacité](#a1-infrastructure-physique-et-capacit) _(Lines 45-47)_
   1. [Faits](#faits) _(Lines 50-63)_
   1. [Jalons cités](#jalons-cit-s) _(Lines 66-69)_
   1. [Trajectoire `T.CLD.A1`](#trajectoire-t-cld-a1) _(Lines 72-87)_
   1. [Narratif](#narratif) _(Lines 90-104)_
1. [A2 Pile technique, standards et plateformes](#a2-pile-technique-standards-et-plateformes) _(Lines 107-110)_
   1. [Faits](#faits-1) _(Lines 113-124)_
   1. [Jalons cités](#jalons-cit-s-1) _(Lines 127-130)_
   1. [Trajectoire `T.CLD.A2`](#trajectoire-t-cld-a2) _(Lines 133-148)_
   1. [Narratif](#narratif-1) _(Lines 151-165)_
1. [A3 Structure du secteur technologique](#a3-structure-du-secteur-technologique) _(Lines 168-170)_
   1. [Faits](#faits-2) _(Lines 173-184)_
   1. [Jalons cités](#jalons-cit-s-2) _(Lines 187-190)_
   1. [Trajectoire `T.CLD.A3`](#trajectoire-t-cld-a3) _(Lines 193-208)_
   1. [Narratif](#narratif-2) _(Lines 211-226)_
1. [A4 Mode de production du logiciel et des services](#a4-mode-de-production-du-logiciel-et-des-services) _(Lines 229-232)_
   1. [Faits](#faits-3) _(Lines 235-248)_
   1. [Jalons cités](#jalons-cit-s-3) _(Lines 251-254)_
   1. [Trajectoire `T.CLD.A4`](#trajectoire-t-cld-a4) _(Lines 257-272)_
   1. [Narratif](#narratif-3) _(Lines 275-291)_
1. [A5 Reconfiguration des autres secteurs](#a5-reconfiguration-des-autres-secteurs) _(Lines 294-297)_
   1. [Faits](#faits-4) _(Lines 300-311)_
   1. [Jalons cités](#jalons-cit-s-4) _(Lines 314-317)_
   1. [Trajectoire `T.CLD.A5`](#trajectoire-t-cld-a5) _(Lines 320-335)_
   1. [Narratif](#narratif-4) _(Lines 338-353)_
1. [Sources](#sources) _(Lines 356-392)_


---

## A1 Infrastructure physique et capacité
<!-- Lines 45-47 -->

**Question :** Qu'est-ce qui a été construit, à quel rythme, avec quelles surcapacités ?

### Faits
<!-- Lines 50-63 -->

| id | année | bloc | énoncé | valeur | acteurs | attribution | source | statut |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| F.CLD.A1.001 | 2007, 2009, 2012 | US | Les dépenses en immobilisations corporelles (« purchases of property and equipment ») d'un grand détaillant en ligne exploitant sa propre usine cloud croissent d'un ordre de grandeur sur la période. | 224 M$ (2007) ; 373 M$ (2009) ; 3 785 M$ (2012) | O2 | choc | [S15] | V |
| F.CLD.A1.002 | 2010, 2011 | US | Les dépenses en immobilisations corporelles du même exploitant poursuivent leur hausse continue entre 2009 et 2012, sans année de recul. | 979 M$ (2010) ; 1 811 M$ (2011) | O2 | choc | [S15] | V |
| F.CLD.A1.003 | 2006 | US | Un service de stockage d'objets loué au gigaoctet est ouvert sans contrat préalable ni engagement de durée. | lancement 14 mars 2006, 0,15 $/Go/mois, aucun minimum | O2, O1 | choc | [S10] | V |
| F.CLD.A1.004 | 2006 | US | Un service de machines virtuelles loué à l'heure est ouvert en version d'essai, démarrable et arrêtable par appel programmatique. | lancement bêta 24-25 août 2006, capacité facturée à l'usage | O2, O1, M1 | choc | [S11] | V |
| F.CLD.A1.005 | 2007 | US | Le stockage d'objets loué franchit le cap de plusieurs milliards d'objets hébergés, chiffre publié par le fournisseur. | 14 milliards d'objets fin 2007 (contre 2,9 Md fin 2006) | O2 | choc | [S10] | V |
| F.CLD.A1.006 | 2012, 2014, 2015 | US | Les fournisseurs de capacité louée réduisent leurs tarifs de stockage et de calcul plusieurs fois par an sans changement de contrat pour le client, tendance continue jusqu'en fin de fenêtre. | baisses tarifaires répétées | O1, O2, O4 | co:X.CLD.10 | [S38] | K |
| F.CLD.A1.007 | 2015 | MONDE | La dépense en capital consacrée aux centres de données par les quelques plus grands opérateurs mondiaux dépasse celle du reste de l'industrie informatique réunie. | dépassement au niveau agrégat | O2, O3, O4 | choc | [S15] | K |
| F.CLD.A1.008 | 2007 | US | L'agence américaine de protection de l'environnement chiffre la consommation électrique des serveurs et centres de données à 61 TWh en 2006, soit 1,5 % de l'électricité nationale, le double de 2000 ; capacité rapportée sur une pointe d'environ 7 GW. Fait cité en A1 pour la capacité installée ; le détail énergétique relève de H1. | 61 TWh, 1,5 %, 4,5 Md$ | O6, O2 | choc | [S51] | V |
| F.CLD.A1.009 | 2011 | EU | Des implantations de centres de données s'ouvrent en Scandinavie et en Islande, motivées par le refroidissement naturel et une électricité abondante ; la géographie de l'usine suit désormais l'énergie autant que la proximité des usagers. Fait cité en A1 pour la capacité et sa localisation ; le motif énergétique relève de H2. | ouvertures de sites | O2, T2 | choc | [S59] | K |
| F.CLD.A1.010 | 2003-2004 | US, MONDE | Avant t0 : l'informatique d'entreprise reste très majoritairement possédée, chaque organisation achetant ses propres serveurs pour sa propre salle machine. | — | O4, M1 | exo | [S1] | K |

### Jalons cités
<!-- Lines 66-69 -->

`J.CLD.2007.02`, `J.CLD.2006.01`, `J.CLD.2006.02`, `J.CLD.2007.04`, `J.CLD.2007.06`,
`J.CLD.2010.07`, `J.CLD.2011.08`, `J.CLD.2015.05`.

### Trajectoire `T.CLD.A1`
<!-- Lines 72-87 -->

| année | phase | intensité | ce qui change | faits et jalons |
| --- | --- | --- | --- | --- |
| avant t0 | latent | 1 | Informatique possédée ; virtualisation détache déjà le service de la machine sans changer le mode d'achat. | F.CLD.A1.010, J.CLD.2003.01 |
| 2005 | émergence | 1 | Réorganisation interne en services appelables, condition préalable à la location externe. | J.CLD.2005.01 |
| 2006 | émergence | 2 | Ouverture des premiers services de capacité facturés à l'usage, sans contrat. | F.CLD.A1.003, F.CLD.A1.004 |
| 2007 | accélération | 3 | Les dépenses en capital basculent massivement vers la construction de centres de données ; premier chiffrage officiel de la consommation électrique. | F.CLD.A1.001, F.CLD.A1.005, F.CLD.A1.008, J.CLD.2007.02 |
| 2008 | crise | 2 | La crise financière (X.CLD.03) freine le crédit mais ne ralentit pas la bascule vers la location. | J.CLD.2008.01 |
| 2009 | accélération | 2 | Reprise de la croissance des dépenses en capital après le creux de la crise. | F.CLD.A1.001 |
| 2010 | accélération | 2 | Poursuite continue de la hausse des dépenses en capital ; l'exploitant devient acheteur d'électricité de gros. | F.CLD.A1.002, J.CLD.2010.07 |
| 2011 | consolidation | 2 | Poursuite de la hausse des dépenses en capital ; la géographie de l'implantation suit l'énergie. | F.CLD.A1.002, F.CLD.A1.009 |
| 2012 | consolidation | 3 | Les dépenses en capital d'un seul exploitant dépassent quinze fois leur niveau de 2007. | F.CLD.A1.001 |
| 2013 | consolidation | 0 | Poursuite de la course à la capacité sans bascule nouvelle documentée cette année pour A1. | — |
| 2014 | consolidation | 2 | Baisses tarifaires coordonnées ; poursuite de la construction. | F.CLD.A1.006 |
| 2015 | banalisation | 3 | La dépense en capital des plus grands opérateurs dépasse celle du reste de l'industrie informatique réunie. | F.CLD.A1.007 |

### Narratif
<!-- Lines 90-104 -->

En dix ans, la dépense en capital d'un seul exploitant passe de 224 millions à plus de 3,8
milliards de dollars par an, avant de continuer sa progression jusqu'en 2015 [F.CLD.A1.001,
F.CLD.A1.002]. L'infrastructure démarre par des services facturés à l'unité sans contrat
[F.CLD.A1.003, F.CLD.A1.004], franchit rapidement une échelle mesurable en milliards d'objets
[F.CLD.A1.005], puis devient assez grande pour entrer dans les statistiques énergétiques
nationales [F.CLD.A1.008]. La crise financière de 2008 ne casse pas la tendance de fond
[J.CLD.2008.01], et la géographie des implantations commence à suivre la disponibilité
énergétique plutôt que la seule proximité des usagers [F.CLD.A1.009]. À t0+10, la capacité
installée par une poignée d'opérateurs dépasse celle du reste de l'industrie informatique réunie
[F.CLD.A1.007], signe d'une concentration de l'appareil productif inédite pour une industrie née
dix ans plus tôt de simples salles machines possédées [F.CLD.A1.010].

---

## A2 Pile technique, standards et plateformes
<!-- Lines 107-110 -->

**Question :** Quelles briques logicielles et quels standards se sont imposés, ouverts ou
propriétaires, et qui les a fixés ?

### Faits
<!-- Lines 113-124 -->

| id | année | bloc | énoncé | valeur | acteurs | attribution | source | statut |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| F.CLD.A2.001 | 2003 | US | La virtualisation de serveurs x86 devient un produit d'entreprise courant, découplant le service de la machine physique. | — | M1, O4, O2 | exo | [S1] | K |
| F.CLD.A2.002 | 2004-2005 | US | Un article de recherche publié par un grand opérateur du web décrit un cadre de calcul distribué sur grappes de machines banalisées, repris ensuite en projet ouvert. | publication 2004, implémentation ouverte à partir de 2006 | M1, O2, O7 | co:X.CLD.05 | [S8] | V |
| F.CLD.A2.003 | 2011 | US | L'institut américain de normalisation publie la définition normative de l'informatique en nuage (SP 800-145) : cinq caractéristiques, trois modèles de service, quatre modèles de déploiement. | NIST SP 800-145, 28 septembre 2011, Mell et Grance | O6 | choc | [S32] | V |
| F.CLD.A2.004 | 2010 | US | Un projet ouvert de logiciel d'infrastructure est lancé pour permettre à une organisation de bâtir sa propre usine de capacité à la demande, hors des fournisseurs propriétaires. | annonce 26 juillet 2010, code donné par Rackspace + technologie NASA Nebula | O6, O2, M1 | choc | [S28] | V |
| F.CLD.A2.005 | 2013 | MONDE | Un format de conteneur logiciel standardisé se diffuse rapidement comme unité de déploiement portable entre machines et entre fournisseurs, indifférente à l'usine qui l'exécute. | annonce publique mars 2013, publication open source rapportée le 1er avril 2013 | M1, O1, O4 | choc | [S37] | V |
| F.CLD.A2.006 | 2014 | US | Un système d'orchestration de conteneurs conçu pour l'exploitation à très grande échelle est publié en logiciel libre par un des trois grands exploitants. | publication juin 2014 | M1, O2, O1 | choc | [S46] | K |
| F.CLD.A2.007 | 2004-2005 | MONDE | La pile serveur ouverte (système, serveur web, base de données, langages de script) devient majoritaire sur le web public, supprimant le coût de licence à l'entrée. | majorité du parc serveur web public | M1, O1 | exo | [S3] | K |
| F.CLD.A2.008 | 2009 | MONDE | Une base de données non relationnelle distribuée sur machines banalisées devient une brique courante des services en ligne, contrainte directe de l'usine louée (machines nombreuses, faillibles, banales). | adoption large | M1, O1, O2 | choc | [S26] | K |

### Jalons cités
<!-- Lines 127-130 -->

`J.CLD.2011.01`, `J.CLD.2003.01`, `J.CLD.2004.01`, `J.CLD.2005.04`, `J.CLD.2006.05`,
`J.CLD.2009.03`, `J.CLD.2010.01`, `J.CLD.2011.06`, `J.CLD.2013.05`, `J.CLD.2014.03`.

### Trajectoire `T.CLD.A2`
<!-- Lines 133-148 -->

| année | phase | intensité | ce qui change | faits et jalons |
| --- | --- | --- | --- | --- |
| avant t0 | émergence | 1 | Virtualisation et pile ouverte s'imposent en entreprise et sur le web public. | F.CLD.A2.001, F.CLD.A2.007, J.CLD.2004.01 |
| 2005 | émergence | 2 | Publication du cadre de calcul distribué qui rendra la capacité louée exploitable en grand nombre d'unités bon marché. | F.CLD.A2.002, J.CLD.2005.04 |
| 2006 | accélération | 1 | Diffusion d'un cadre libre de calcul distribué adopté par les opérateurs du web. | J.CLD.2006.05 |
| 2007 | accélération | 0 | Pas de rupture technique nouvelle documentée cette année pour A2 ; consolidation des briques précédentes. | — |
| 2008 | accélération | 1 | Deuxième étage de délégation : les plateformes hébergées retirent au développeur la gestion de la machine. | J.CLD.2008.02 |
| 2009 | accélération | 2 | Le modèle de données s'adapte à la contrainte de l'usine louée (machines nombreuses, faillibles). | F.CLD.A2.008 |
| 2010 | consolidation | 2 | Un projet ouvert vise à empêcher que la pile d'infrastructure soit possédée par deux ou trois fournisseurs seulement. | F.CLD.A2.004 |
| 2011 | rupture | 3 | Définition normative officielle du cloud, vocabulaire commun et opposable pour tout achat, y compris public. | F.CLD.A2.003, J.CLD.2011.01 |
| 2012 | consolidation | 0 | Pas de bascule nouvelle documentée ; diffusion continue des briques ouvertes. | — |
| 2013 | accélération | 2 | Les conteneurs standardisés deviennent l'unité de déploiement portable, premier contrepoids à la dépendance à un fournisseur. | F.CLD.A2.005, J.CLD.2013.05 |
| 2014 | consolidation | 2 | L'orchestration de conteneurs des plus grands exploitants devient un bien commun logiciel libre. | F.CLD.A2.006, J.CLD.2014.03 |
| 2015 | banalisation | 0 | Pas de bascule nouvelle documentée pour A2 ; la pile à trois couches est stabilisée comme vocabulaire du secteur. | — |

### Narratif
<!-- Lines 151-165 -->

La pile technique du cloud se construit sur deux prérequis antérieurs à t0 : la virtualisation
des serveurs et la généralisation de la pile serveur ouverte [F.CLD.A2.001, F.CLD.A2.007]. Le
calcul distribué sur machines banalisées, publié en 2004-2005 puis diffusé en open source,
rend la capacité louée exploitable à grande échelle par des équipes qui ne sont pas des géants
[F.CLD.A2.002]. La décennie empile ensuite trois couches — capacité brute, plateforme
d'exécution, logiciel en ligne — avant que l'interface de programmation ne devienne elle-même un
standard de fait entre fournisseurs et clients [J.CLD.2005.01]. La définition officielle
américaine de 2011 fixe un vocabulaire commun et rend le cloud achetable par des organisations
réglementées [F.CLD.A2.003]. En fin de fenêtre, les conteneurs standardisés et leur orchestration
en logiciel libre offrent un premier contrepoids technique à la dépendance à un seul fournisseur
[F.CLD.A2.005, F.CLD.A2.006].

---

## A3 Structure du secteur technologique
<!-- Lines 168-170 -->

**Question :** Qui produit la technologie : anciens, nouveaux, intégrés, concentrés ?

### Faits
<!-- Lines 173-184 -->

| id | année | bloc | énoncé | valeur | acteurs | attribution | source | statut |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| F.CLD.A3.001 | 2015-04 | US | Un grand détaillant en ligne publie pour la première fois séparément le chiffre d'affaires et le résultat d'exploitation de son activité de services en nuage : 1 566 M$ de chiffre d'affaires au premier trimestre 2015, contre 1 050 M$ au premier trimestre 2014, et 265 M$ de résultat d'exploitation. | 1 566 M$ (T1 2015), 1 050 M$ (T1 2014), +49 %, 265 M$ de résultat d'exploitation | O2 | choc | [S48] | V |
| F.CLD.A3.002 | 2008 | US | L'éditeur historique des systèmes d'exploitation et logiciels d'entreprise annonce une offre de calcul et de stockage loués, entrée tardive d'un titulaire sur un marché ouvert deux ans plus tôt par un nouvel entrant. | annonce Windows Azure le 27 octobre 2008, PDC Los Angeles | O2, O4 | choc | [S20] | V |
| F.CLD.A3.003 | 2011 | US, EU | Les acteurs historiques de la vente de serveurs et de logiciels d'entreprise enregistrent un ralentissement durable de leurs ventes de matériel aux entreprises, visible dans leurs comptes. | ralentissement des ventes matériel | O2, O4, M9 | choc | [S35] | K |
| F.CLD.A3.004 | 2014 | US | Baisses de prix coordonnées dans le temps entre les trois principaux fournisseurs de capacité louée, signe d'une structure à trois acteurs disposant seuls de l'échelle nécessaire pour soutenir la guerre des prix. | trois fournisseurs dominants | O2, O4, O1 | co:X.CLD.10 | [S38] | K |
| F.CLD.A3.005 | 2007-2009 | CN | Les fournisseurs nationaux chinois de commerce et de recherche engagent la construction de leurs propres centres de données, hors des fournisseurs américains, séparant durablement les deux marchés. | filiale dédiée créée en 2009 (Alibaba Cloud Computing) ; date de 2007 et cas Baidu non confirmés à la source (voir note [S17]) | T4, O2, O6 | choc | [S17] | K |
| F.CLD.A3.006 | 2009 | EU | Les groupes européens du numérique et les pouvoirs publics constatent qu'aucun fournisseur d'usines à l'échelle mondiale n'est européen. | absence constatée | T2, O6, O2 | choc | [S27] | K |
| F.CLD.A3.007 | 2012 | EU | Une administration nationale européenne annonce un projet de « nuage souverain » financé sur fonds publics, en réponse au constat de 2009 ; le résultat de ce projet documente la difficulté de rattraper une industrie d'échelle. | projet public annoncé | T2, O6, O2 | choc | [S27] | K |
| F.CLD.A3.008 | 2013 | MONDE | Le marché des services en nuage atteint une taille où des cabinets de mesure privés le suivent comme un segment industriel distinct de l'informatique d'entreprise ; chiffres d'analystes non repris, artefact de mesure. | segment suivi séparément | O2, O4 | choc | [S44] | K |

### Jalons cités
<!-- Lines 187-190 -->

`J.CLD.2015.01`, `J.CLD.2007.05`, `J.CLD.2008.03`, `J.CLD.2010.05`, `J.CLD.2011.04`,
`J.CLD.2012.03`, `J.CLD.2013.06`, `J.CLD.2014.01`.

### Trajectoire `T.CLD.A3`
<!-- Lines 193-208 -->

| année | phase | intensité | ce qui change | faits et jalons |
| --- | --- | --- | --- | --- |
| avant t0 | latent | 1 | L'entrée en bourse d'un moteur de recherche financé par la publicité fait apparaître l'usine informatique à grande échelle comme un actif finançable. | J.CLD.2004.02 |
| 2005 | émergence | 2 | Constructeurs et intégrateurs historiques promeuvent l'informatique « à la demande » en réponse à un modèle interne déjà en place chez un nouvel entrant. | J.CLD.2005.02 |
| 2006 | émergence | 0 | Aucune bascule de structure nouvelle documentée ; consolidation de l'offre du nouvel entrant. | — |
| 2007 | accélération | 2 | La Chine engage une trajectoire d'usines nationales séparées du marché américain. | F.CLD.A3.005, J.CLD.2007.05 |
| 2008 | crise | 2 | Un titulaire historique entre tardivement sur le marché de la capacité louée. | F.CLD.A3.002, J.CLD.2008.03 |
| 2009 | crise | 1 | L'Europe constate l'absence d'un fournisseur d'usines à son échelle. | F.CLD.A3.006 |
| 2010 | consolidation | 1 | La Chine se dote d'un fournisseur dédié séparant durablement les deux marchés. | J.CLD.2010.05 |
| 2011 | consolidation | 2 | Les ventes de matériel des titulaires historiques ralentissent durablement : transfert de valeur visible dans les comptes. | F.CLD.A3.003, J.CLD.2011.04 |
| 2012 | consolidation | 1 | Réponse industrielle publique européenne au constat de 2009. | F.CLD.A3.007, J.CLD.2012.03 |
| 2013 | consolidation | 2 | Le marché devient statistiquement observable comme branche distincte. | F.CLD.A3.008, J.CLD.2013.06 |
| 2014 | consolidation | 2 | Structure à trois grands fournisseurs qui mènent seuls la guerre des prix. | F.CLD.A3.004, J.CLD.2014.01 |
| 2015 | banalisation | 3 | Première publication séparée du chiffre d'affaires cloud d'un grand exploitant, révélant une activité de plusieurs milliards très rentable. | F.CLD.A3.001, J.CLD.2015.01 |

### Narratif
<!-- Lines 211-226 -->

Le secteur s'ouvre avec un nouvel entrant qui loue sa propre usine interne, pendant que les
constructeurs et éditeurs historiques répondent d'abord par un vocabulaire commercial adossé à
leurs centres de données existants [J.CLD.2005.01, J.CLD.2005.02]. Un titulaire majeur n'entre
sur le marché de la capacité louée qu'en 2008, avec deux ans de retard sur le nouvel entrant
[F.CLD.A3.002]. Les ventes de matériel des acteurs historiques ralentissent durablement à partir
de 2011, signe d'un transfert de valeur des salles machines vers les usines louées
[F.CLD.A3.003]. La Chine et l'Europe répondent différemment à l'absence d'un fournisseur à leur
échelle : la première construit ses propres usines dès 2007, la seconde le constate en 2009 sans
device industriel équivalent [F.CLD.A3.005, F.CLD.A3.006, F.CLD.A3.007]. À t0+10, la structure du
secteur s'est resserrée sur trois grands fournisseurs qui coordonnent leurs baisses de prix
[F.CLD.A3.004], et le premier d'entre eux révèle publiquement que son activité de location est de
taille industrielle et très rentable [F.CLD.A3.001].

---

## A4 Mode de production du logiciel et des services
<!-- Lines 229-232 -->

**Question :** Comment fabrique-t-on et exploite-t-on un service numérique, à quel coût, avec
quelle organisation ?

### Faits
<!-- Lines 235-248 -->

| id | année | bloc | énoncé | valeur | acteurs | attribution | source | statut |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| F.CLD.A4.001 | 2005 | US | Un service de partage vidéo atteint une audience mondiale en quelques mois avec une équipe de trois fondateurs, sans posséder l'infrastructure de diffusion correspondante. | 3 fondateurs | O1, M9 | choc | [S9] | K |
| F.CLD.A4.002 | 2012 | MONDE | Une application de partage de photographies grand public atteint plusieurs centaines de millions d'usagers avec une équipe d'environ treize personnes au moment de son rachat, en s'appuyant entièrement sur des services loués. | équipe d'environ 13 personnes | O1, M1, M9 | choc | [S29] (contexte) | K |
| F.CLD.A4.003 | 2008 | MONDE | Une plateforme d'exécution d'applications hébergée est ouverte, où le développeur ne gère plus ni machine ni système d'exploitation, deuxième étage de délégation après la capacité brute. | lancement en avant-première le 7 avril 2008 (Google App Engine) | O1, M1 | choc | [S19] | V |
| F.CLD.A4.004 | 2008 | US, EU | Les directions informatiques des grandes entreprises commencent à séparer explicitement dépense en capital et dépense de fonctionnement dans l'arbitrage « acheter ou louer », la crise financière servant d'argument budgétaire immédiat. | — | O4, M1, M9 | co:X.CLD.03 | [S21] | K |
| F.CLD.A4.005 | 2009 | US | La création d'une entreprise de logiciel sans achat de serveur devient la norme attendue dans les incubateurs et auprès des investisseurs en amorçage, effondrant le capital initial nécessaire. | norme d'amorçage | O1, M9, M1 | choc | [S24] | K |
| F.CLD.A4.006 | 2010 | US, EU | Le métier d'administrateur système bascule vers l'écriture de code de configuration et d'automatisation plutôt que l'intervention manuelle sur machine. | bascule de pratique | M1, O4 | choc | [S31] | K |
| F.CLD.A4.007 | 2011 | US | Un outil de conteneurisation et de livraison continue réduit l'écart entre la machine du développeur et la machine de production, faisant passer le rythme de mise en production du trimestre à la journée dans les équipes qui l'adoptent. | trimestre → jour | M1, O1 | choc | [S37] | K |
| F.CLD.A4.008 | 2014 | US | Des grandes entreprises établies hors technologie annoncent publiquement la fermeture de la majorité de leurs centres de données au profit de fournisseurs externes. | fermetures annoncées | O4, M1, M9 | choc | [S45] | K |
| F.CLD.A4.009 | 2014-11 | US | Un service d'exécution de code facturé à l'appel est ouvert, sans machine ni serveur à déclarer : l'unité facturée descend de la machine-heure à la fonction exécutée. | lancement AWS Lambda le 13 novembre 2014, facturation par tranche de 100 ms | M1, O1 | choc | [S47] | V |
| F.CLD.A4.010 | 2015 | US, EU | Le métier de direction informatique se réoriente de l'exploitation d'un parc de machines vers la gestion de contrats, de coûts variables et de sécurité fournisseur. | réorientation du métier | M1, M9, O4 | choc | [S31] | K |

### Jalons cités
<!-- Lines 251-254 -->

`J.CLD.2005.05`, `J.CLD.2008.02`, `J.CLD.2008.04`, `J.CLD.2009.01`, `J.CLD.2010.06`,
`J.CLD.2011.06`, `J.CLD.2014.02`, `J.CLD.2014.05`, `J.CLD.2015.06`.

### Trajectoire `T.CLD.A4`
<!-- Lines 257-272 -->

| année | phase | intensité | ce qui change | faits et jalons |
| --- | --- | --- | --- | --- |
| avant t0 | latent | 1 | Le logiciel loué à l'abonnement s'impose comme modèle crédible en gestion de la relation client, sans installation chez le client. | J.CLD.2003.02 |
| 2005 | émergence | 2 | Une équipe de trois personnes atteint une audience mondiale sans infrastructure propre : premier exemple frappant du mode de production allégé. | F.CLD.A4.001, J.CLD.2005.05 |
| 2006 | émergence | 0 | Diffusion des premiers services à l'usage ; pas de rupture de mode de production nouvelle cette année. | — |
| 2007 | accélération | 1 | Premiers cursus et recherches sur le calcul distribué à très grande échelle, hors des entreprises qui l'ont inventé. | J.CLD.2007.03 |
| 2008 | crise | 2 | Délégation de l'exploitation elle-même (plateforme hébergée) ; la crise financière impose l'arbitrage capex/opex comme discipline budgétaire. | F.CLD.A4.003, F.CLD.A4.004, J.CLD.2008.02, J.CLD.2008.04 |
| 2009 | accélération | 2 | L'absence de serveur devient la norme d'amorçage pour les jeunes entreprises. | F.CLD.A4.005, J.CLD.2009.01 |
| 2010 | accélération | 2 | Le métier d'administrateur système change de nature : de la machine au code. | F.CLD.A4.006, J.CLD.2010.06 |
| 2011 | accélération | 2 | Le rythme de mise en production passe du trimestre à la journée dans les équipes outillées. | F.CLD.A4.007, J.CLD.2011.06 |
| 2012 | consolidation | 2 | Une équipe d'une douzaine de personnes sert plusieurs centaines de millions d'usagers, cas limite du mode de production allégé. | F.CLD.A4.002 |
| 2013 | consolidation | 0 | Diffusion des conteneurs comme unité de déploiement, sans rupture de mode de production nouvelle pour A4. | — |
| 2014 | consolidation | 3 | Des grandes entreprises non technologiques ferment leurs centres de données ; l'unité facturée descend à la fonction exécutée. | F.CLD.A4.008, F.CLD.A4.009, J.CLD.2014.02, J.CLD.2014.05 |
| 2015 | banalisation | 2 | La direction informatique devient un métier de gestion de fournisseurs plutôt que d'exploitation de machines. | F.CLD.A4.010, J.CLD.2015.06 |

### Narratif
<!-- Lines 275-291 -->

Le mode de production change d'échelle humaine avant de changer de coût : une équipe de trois
personnes diffuse une audience mondiale dès 2005 sans posséder d'infrastructure [F.CLD.A4.001],
et une équipe d'une douzaine de personnes sert plusieurs centaines de millions d'usagers en 2012
[F.CLD.A4.002]. La crise financière de 2008 agit comme accélérateur budgétaire d'un déplacement
déjà amorcé des dépenses en capital vers les dépenses de fonctionnement [F.CLD.A4.004]. Le
capital nécessaire pour lancer un service s'effondre au point que l'absence de serveur devient la
norme d'amorçage attendue par les investisseurs dès 2009 [F.CLD.A4.005]. Le travail d'exploitation
lui-même se transforme deux fois : d'abord de la machine vers le code de configuration
[F.CLD.A4.006], puis du serveur vers la fonction exécutée à l'appel, dernière étape où
l'infrastructure disparaît de la vue du développeur [F.CLD.A4.009]. En fin de fenêtre, des grandes
entreprises non technologiques ferment leurs propres centres de données [F.CLD.A4.008], et la
direction informatique devient un métier de pilotage de fournisseurs plutôt que d'exploitation
d'un parc [F.CLD.A4.010].

---

## A5 Reconfiguration des autres secteurs
<!-- Lines 294-297 -->

**Question :** Comment les chaînes de valeur des autres industries se réorganisent-elles :
intermédiaires supprimés ou créés ?

### Faits
<!-- Lines 300-311 -->

| id | année | bloc | énoncé | valeur | acteurs | attribution | source | statut |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| F.CLD.A5.001 | 2003 | US | Un éditeur de gestion de la relation client démontre que le logiciel d'entreprise peut se vendre en abonnement hébergé sans installation, prérequis du basculement du secteur logiciel. | fondé 1999, service on-demand depuis février 2000, modèle "fully outsourced service accessible over the Internet" | O1, O4, M9 | exo | [S2] | V |
| F.CLD.A5.002 | 2009 | US | L'éditeur de gestion de la relation client hébergé dépasse le milliard de dollars de chiffre d'affaires annuel sans installer de logiciel chez ses clients, preuve de taille industrielle du modèle. | 1 077 M$ (exercice clos janvier 2009), contre 749 M$ (exercice clos janvier 2008) | O2, O4 | choc | [S2] | V |
| F.CLD.A5.003 | 2006 | US | Une suite bureautique en ligne gratuite est proposée aux organisations comme substitut à des logiciels installés poste par poste, faisant sortir le courriel et les documents des murs de l'organisation. | lancement 28 août 2006, Google Apps for Your Domain, gratuit en bêta | O4, O7, M4 | choc | [S13] | V |
| F.CLD.A5.004 | 2008 | EMERG | Un service de paiement par téléphone mobile simple, adossé à une plateforme centralisée d'opérateur, atteint plusieurs millions d'usagers en Afrique de l'Est sans réseau d'agences bancaires. | lancé mars 2007 ; environ 2 à 3 millions d'usagers courant 2008, 9 millions en janvier 2010 | T5, P8, O3 | choc | [S22] | V |
| F.CLD.A5.005 | 2012 | EMERG | Le secteur indien de la sous-traitance informatique se réoriente de la gestion de parcs de serveurs pour compte de tiers vers l'intégration et l'exploitation de services loués. | réorientation sectorielle | T5, M1, O4 | choc | [S40] | K |
| F.CLD.A5.006 | 2012-2014 | MONDE | Les offres de stockage grand public synchronisé atteignent des centaines de millions de comptes, déplaçant le document et la photo personnels d'un support local vers un centre de données distant ; canal principal X.CLD.01 (téléphone intelligent) en secondaire. | centaines de millions de comptes | P2, P3, P4, O2 | choc | [S39] | K |
| F.CLD.A5.007 | 2015 | EU | Des administrations et organisations réglementées de plusieurs pays européens publient des référentiels de certification de services en nuage : le secteur public répond au choc côté producteur de normes d'usage, pas de capacité. | référentiels publiés | T2, O6, O2 | choc | [S36] | K |
| F.CLD.A5.008 | — | — | retiré : énoncé méta sur l'absence de série officielle unifiée, pas un fait daté et sourçable ; aucune source admissible ne peut l'étayer par construction (elle documenterait l'absence de source, pas un fait) ; seules des séries d'analystes existent ([S44]), insuffisantes pour fonder un fait daté. | — | — | — | — | — |

### Jalons cités
<!-- Lines 314-317 -->

`J.CLD.2015.01`, `J.CLD.2006.04`, `J.CLD.2008.05`, `J.CLD.2009.05`, `J.CLD.2012.04`,
`J.CLD.2012.05`, `J.CLD.2015.04`.

### Trajectoire `T.CLD.A5`
<!-- Lines 320-335 -->

| année | phase | intensité | ce qui change | faits et jalons |
| --- | --- | --- | --- | --- |
| avant t0 | latent | 1 | Le logiciel de gestion en abonnement hébergé démontre la viabilité du modèle pour le secteur logiciel. | F.CLD.A5.001 |
| 2005 | émergence | 0 | Aucune reconfiguration sectorielle nouvelle hors logiciel documentée cette année. | — |
| 2006 | émergence | 2 | La bureautique en ligne gratuite atteint le poste de travail ordinaire des organisations. | F.CLD.A5.003, J.CLD.2006.04 |
| 2007 | accélération | 0 | Diffusion continue, pas de bascule sectorielle nouvelle documentée. | — |
| 2008 | crise | 2 | Un secteur financier parallèle émerge dans les pays émergents via une plateforme mobile centralisée, hors du système bancaire classique. | F.CLD.A5.004, J.CLD.2008.05 |
| 2009 | accélération | 2 | Le modèle d'abonnement hébergé atteint une taille industrielle dans le logiciel de gestion. | F.CLD.A5.002, J.CLD.2009.05 |
| 2010 | consolidation | 0 | Diffusion continue vers d'autres secteurs (médias, réseaux sociaux) sans rupture nouvelle en A5. | — |
| 2011 | consolidation | 0 | Pas de bascule sectorielle nouvelle documentée. | — |
| 2012 | consolidation | 3 | Le stockage synchronisé grand public et la réorientation de la sous-traitance indienne reconfigurent deux chaînes de valeur en même temps. | F.CLD.A5.005, F.CLD.A5.006, J.CLD.2012.04, J.CLD.2012.05 |
| 2013 | consolidation | 0 | Diffusion continue, pas de bascule sectorielle nouvelle documentée pour A5. | — |
| 2014 | consolidation | 0 | Diffusion continue, pas de bascule sectorielle nouvelle documentée pour A5. | — |
| 2015 | banalisation | 2 | Les organisations réglementées européennes répondent par la certification côté producteur de normes d'usage. | F.CLD.A5.007, J.CLD.2015.04 |

### Narratif
<!-- Lines 338-353 -->

Le secteur logiciel bascule le premier : un modèle d'abonnement hébergé démontré dès 2003 dépasse
le milliard de dollars de chiffre d'affaires annuel en 2009 [F.CLD.A5.001, F.CLD.A5.002]. La
bureautique en ligne fait sortir le document et le courriel des murs de l'organisation dès 2006
[F.CLD.A5.003]. Dans les pays émergents, un service de paiement mobile adossé à une plateforme
centralisée crée un canal financier parallèle sans réseau bancaire physique [F.CLD.A5.004], et la
sous-traitance informatique indienne se réoriente de la gestion de machines vers l'intégration de
services loués [F.CLD.A5.005]. Le grand public consomme l'usine sans la nommer, à travers des
comptes de stockage synchronisé qui déplacent ses documents vers des centres de données distants
[F.CLD.A5.006] ; ce vécu grand public reste un canal indirect et non le cœur du choc industriel
[X.CLD.01, X.CLD.02, voir 04_confondants.md]. En fin de fenêtre, les organisations réglementées
répondent par la certification, affirmant un rôle de producteur de normes d'usage plutôt que de
capacité [F.CLD.A5.007].

---

## Sources
<!-- Lines 356-392 -->

| clé | type | référence | note |
| --- | --- | --- | --- |
| [S1] | off | VMware Inc., prospectus d'introduction en bourse (Form S-1, SEC, 2007) et rapports annuels ultérieurs | Reprise de [S1] de `par_annee/cloud_2005_2015.md`. Historique de l'adoption de la virtualisation x86 en entreprise. À vérifier. |
| [S2] | off | salesforce.com inc., rapports annuels (Form 10-K, SEC), exercices 2004 à 2010 ; CIK 0001108524 | Ouvert et lu le 2026-09-22 : 10-K exercice clos 31 janvier 2005 (accession 0001193125-05-061027, sec.gov/Archives/edgar/data/1108524/000119312505061027/d10k.htm) — fondation février 1999, service on-demand depuis février 2000, modèle « fully outsourced service accessible over the Internet », substitut au logiciel installé (F.CLD.A5.001) ; 10-K exercice clos 31 janvier 2009 (accession 0001193125-09-048665, sec.gov/Archives/edgar/data/1108524/000119312509048665/d10k.htm) — chiffre d'affaires 1 077 M$ (FY2009) contre 749 M$ (FY2008) (F.CLD.A5.002). |
| [S3] | stat | Netcraft, Web Server Survey, séries mensuelles 2003-2005 | Reprise de [S3] de la chronologie. Parts de marché des serveurs web. |
| [S8] | acad | Dean, J. et Ghemawat, S., « MapReduce: Simplified Data Processing on Large Clusters », OSDI, 2004 ; projet Apache Hadoop, premières versions 2006 | Ouvert et lu le 2026-09-22 : research.google/pubs (listing officiel Google Research) — titre, auteurs (Jeffrey Dean, Sanjay Ghemawat), venue (OSDI'04, San Francisco), année 2004 confirmés. Date 2006 pour l'implémentation ouverte (scission Hadoop du projet Nutch, 28 janvier 2006) corroborée par plusieurs rétrospectives secondaires, pas par une page Apache d'origine ouverte directement. |
| [S9] | presse | Presse économique contemporaine du lancement et du rachat de YouTube, 2005-2006 | Reprise de [S9] de la chronologie. Taille de l'équipe fondatrice à vérifier précisément. |
| [S10] | off | Amazon Web Services, communiqué de lancement d'Amazon S3, press.aboutamazon.com, 14 mars 2006 ; AWS News Blog, « Amazon S3 — Bigger and Busier than Ever », 28 janvier 2011 (comptage annuel d'objets) | Ouvert et lu le 2026-09-22 : press.aboutamazon.com/2006/3/amazon-web-services-launches — lancement 14 mars 2006, 0,15 $/Go/mois de stockage, 0,20 $/Go transféré, aucun minimum (F.CLD.A1.003) ; aws.amazon.com/blogs/aws/amazon-s3-bigger-and-busier-than-ever — comptage officiel en fin d'année : 2,9 Md d'objets (2006), 14 Md (2007), 40 Md (2008), 102 Md (2009), 262 Md (2010) (F.CLD.A1.005 ; ancienne valeur « plusieurs milliards » remplacée par le chiffre exact 14 Md). |
| [S11] | off | Amazon Web Services, communiqué de lancement d'Amazon EC2 en version bêta limitée, aws.amazon.com/about-aws/whats-new/2006/08/24 | Ouvert et lu le 2026-09-22 : page officielle « Announcing Amazon Elastic Compute Cloud (Amazon EC2) — beta », datée 24 août 2006 (accès élargi le 25 août) ; capacité redimensionnable facturée à l'usage, provisionnement en quelques minutes. |
| [S13] | presse | Google Press, « Google Launches Hosted Communications Services », googlepress.blogspot.com, 28 août 2006 | Ouvert et lu le 2026-09-22 : googlepress.blogspot.com/2006/08 — lancement de Google Apps for Your Domain le 28 août 2006, édition standard gratuite en bêta (Gmail, Google Talk, Calendar, Page Creator), substitut à l'installation et la maintenance de logiciel/matériel local. |
| [S15] | off | Amazon.com Inc., rapports annuels (Form 10-K, SEC), rubrique « purchases of property and equipment, including internal-use software and website development », exercices 2007 à 2015 ; CIK 0001018724. Chiffres vérifiés sur EDGAR : 224 M$ (2007), 333 M$ (2008), 373 M$ (2009), 979 M$ (2010), 1 811 M$ (2011), 3 785 M$ (2012), 3 444 M$ (2013), ~4,9 Md$ (2014), ~4,6 Md$ (2015). | Série vérifiée directement sur les documents 10-K (accession 0001193125-10-016098 pour 2007-2009, 0001193125-13-028520 pour 2010-2012, 0001018724-14-000006 pour 2013, 0001018724-16-000172 pour 2014-2015). 2013 lu précisément (3 444 M$, en recul sur 2012) ; 2014-2015 lus au format arrondi tel que donné par Amazon dans le MD&A du 10-K FY2015 (« $4.6 billion, $4.9 billion, and $3.4 billion in 2015, 2014, and 2013 »), pas au million près. Le dépassement du reste de l'industrie en 2015 (F.CLD.A1.007) est un constat agrégé sectoriel non vérifiable sur un seul 10-K ; reste `K`. |
| [S17] | off | Alibaba Group Holding Ltd., prospectus d'introduction en bourse (Form F-1, SEC, 6 mai 2014, accession 0001193125-14-184994) ; Baidu Inc., rapport annuel (Form 20-F, SEC, exercice 2007, accession 0001145549-08-001006) | Ouvert et lu le 2026-09-22 : F-1 Alibaba — « In 2009, we established Alibaba Cloud Computing to handle the increasing data management needs on our platform » (filiale créée en 2009, pas 2010). 20-F Baidu (exercice 2007) — ne confirme pas de construction de centres de données propres en 2007 ; au contraire, le document indique que Baidu hébergeait ses serveurs chez des tiers (China Telecom, China Netcom, China Tietong) à cette date. Le volet Tencent et la date de 2007 pour Alibaba n'ont pas été vérifiés cette session ; fait laissé en `K` avec ce garde-fou. |
| [S19] | off | Google, « Introducing Google App Engine + our new blog », cloudplatform.googleblog.com, 7 avril 2008 | Ouvert et lu le 2026-09-22 : billet officiel Google Cloud Platform Blog daté du lundi 7 avril 2008, annonçant la préversion de Google App Engine. |
| [S20] | off | Microsoft, « Microsoft Unveils Windows Azure at Professional Developers Conference », news.microsoft.com/source, 27 octobre 2008 | Ouvert et lu le 2026-09-22 : communiqué officiel Microsoft daté du 27 octobre 2008, keynote de Ray Ozzie au PDC 2008 (Los Angeles), Windows Azure présenté comme socle d'hébergement, de stockage et de calcul en nuage. |
| [S21] | acad | Travaux et enquêtes sur l'arbitrage dépenses en capital contre dépenses de fonctionnement dans les directions informatiques, 2008-2012 | Reprise de [S21] de la chronologie. Généralité qualitative. |
| [S22] | stat | Mas, I. et Radcliffe, D., « Mobile Payments Go Viral: M-PESA in Kenya », Bill & Melinda Gates Foundation, document de travail hébergé par la Banque mondiale, mars 2010 (documents1.worldbank.org/curated/en/638851468048259219) | Ouvert et lu le 2026-09-22 : lancement commercial par Safaricom (filiale Vodafone) en mars 2007 ; courbe officielle du nombre d'utilisateurs (Exhibit 2) franchissant environ 2 à 3 millions d'usagers courant 2008 et atteignant 9,0 millions en janvier 2010. |
| [S24] | stat | NVCA/PitchBook, séries de capital-risque américain par stade, 2005-2012 | Reprise de [S24] de la chronologie. |
| [S26] | acad | DeCandia, G. et al., « Dynamo: Amazon's Highly Available Key-value Store », SOSP, 2007 ; projets Apache Cassandra et HBase, 2008-2010 | Reprise de [S26] de la chronologie. |
| [S27] | off | Commission européenne, communication *Unleashing the Potential of Cloud Computing in Europe*, COM(2012) 529 ; documents nationaux sur les projets de nuage souverain français, 2011-2013 | Reprise de [S27] de la chronologie. Le constat de 2009 reste à sourcer plus précisément. |
| [S28] | presse | Rackspace Hosting, « Rackspace Announces Plans to Collaborate with NASA on OpenStack Project », PR Newswire, 26 juillet 2010 | Ouvert et lu le 2026-09-22 : communiqué de presse daté du 26 juillet 2010 (Design Summit à Austin 13-16 juillet, annonce publique à l'OSCON de Portland le 21 juillet) ; Rackspace donne le code de Cloud Files/Cloud Servers, projet incorporant la technologie NASA Nebula. |
| [S29] | off | Facebook Inc. et communiqués de rachat d'Instagram (avril 2012) | Utilisé ici pour le contexte de la taille d'équipe d'Instagram au moment du rachat ; le chiffre de treize personnes est `K`, à vérifier sur la presse contemporaine du rachat plutôt que sur le S-1 Facebook. |
| [S31] | acad | U.S. Bureau of Labor Statistics, *Occupational Outlook Handbook*, professions de l'administration système et des réseaux, éditions 2008-2016 | Reprise de [S31] de la chronologie. |
| [S32] | off | Mell, P. et Grance, T., *The NIST Definition of Cloud Computing*, NIST Special Publication 800-145, 28 septembre 2011 | Vérifié directement sur nist.gov : titre, auteurs et date de publication (28 septembre 2011) confirmés. |
| [S35] | off | Rapports annuels (Form 10-K, SEC) de HP, Dell, IBM et Oracle, segments serveurs et logiciels d'entreprise, 2010-2015 | Reprise de [S35] de la chronologie ; non extraite ligne à ligne dans cette cellule. |
| [S36] | off | Groupe de travail « Article 29 », avis sur l'informatique en nuage (WP196, juillet 2012) ; référentiels nationaux de certification cloud, 2015 | Reprise de [S36] de la chronologie. |
| [S37] | presse | Presse technique contemporaine des lancements de Jenkins, Vagrant et Docker, 2011-2013 ; pour Docker : changelog.com, « Docker from dotCloud is now open source — the future of Linux containers? », 1er avril 2013 | Ouvert et lu le 2026-09-22 (volet Docker uniquement) : billet daté du 1er avril 2013 confirmant la publication open source de Docker (démonstration publique à PyCon mi-mars 2013) et son argument de portabilité (« runs unix processes with strong guarantees of isolation and repeatability across servers »). Volet Jenkins/Vagrant non ouvert cette session. |
| [S38] | off | Historiques publics des tarifs d'Amazon Web Services, Google Cloud Platform et Microsoft Azure, 2012-2015 | Reprise de [S38] de la chronologie. |
| [S39] | off | Rapports annuels et communiqués de Dropbox, Google et Apple sur le nombre de comptes de stockage synchronisé, 2012-2014 | Reprise de [S39] de la chronologie. |
| [S40] | stat | NASSCOM, rapports annuels sur le secteur indien des services informatiques, 2010-2015 | Reprise de [S40] de la chronologie. |
| [S44] | stat | Gartner et IDC, séries de dépense mondiale en services en nuage publics, 2010-2016 | Reprise de [S44] de la chronologie. Chiffres d'analystes, non repris comme valeur ; utilisés uniquement pour dater l'émergence du segment comme catégorie suivie. Étiqueté artefact. |
| [S45] | off | Communiqués et rapports annuels d'entreprises hors technologie annonçant la fermeture de leurs centres de données, 2014-2016 | Reprise de [S45] de la chronologie. Cas nommés non identifiés dans cette cellule. |
| [S46] | off | Google Inc. et Cloud Native Computing Foundation, publication initiale de Kubernetes en logiciel libre, juin 2014 | Reprise de [S46] de la chronologie. |
| [S47] | off | Amazon, « Amazon Web Services Announces AWS Lambda », press.aboutamazon.com, 13 novembre 2014 | Ouvert et lu le 2026-09-22 : communiqué officiel daté du 13 novembre 2014 ; facturation « for the requests served and compute time required », par tranches de 100 ms, sans provisionnement de serveur. |
| [S48] | off | Amazon.com Inc., rapport trimestriel (Form 10-Q, SEC), premier trimestre 2015, première publication séparée du segment Amazon Web Services ; accession 0001018724-15-000038 | Vérifié directement sur EDGAR : chiffre d'affaires AWS 1 566 M$ (T1 2015) contre 1 050 M$ (T1 2014), résultat d'exploitation 265 M$ (T1 2015) contre 245 M$ (T1 2014). |
| [S51] | off | U.S. Environmental Protection Agency, ENERGY STAR Program, *Report to Congress on Server and Data Center Energy Efficiency, Public Law 109-431*, 2 août 2007 | Reprise de [S51] de la chronologie, déjà vérifié à la source (61 TWh en 2006, 1,5 %, 4,5 Md$, doublement depuis 2000). |
| [S59] | presse | Communiqués et presse contemporaine des implantations de centres de données en Finlande, Suède et Islande, 2010-2013 | Reprise de [S59] de la chronologie. |
