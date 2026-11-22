# A. Industrie et infrastructure — Cloud 2005-2015

Ce que l'industrie informatique a connu pendant la fenêtre du choc cloud, sous-dimension par
sous-dimension : faits sourcés, jalons cités, trajectoire année par année, narratif court. Le
cloud est un choc **industriel** : des usines (centres de données, plateformes) produisent des
services numériques consommés à la demande par toutes les organisations. Le téléphone
intelligent et les réseaux sociaux y apparaissent seulement comme produits dérivés et clients de
l'usine, jamais comme le sujet. Ligne de base : état des deux années précédant 2005. La
comparaison avec l'autre choc est dans le `README.md` du domaine, pas ici.

## Table of Contents

1. [A1 Infrastructure physique et capacité](#a1-infrastructure-physique-et-capacité) _(Lines 46-48)_
   1. [Faits](#faits) _(Lines 51-64)_
   1. [Jalons cités](#jalons-cités) _(Lines 67-70)_
   1. [Trajectoire `T.CLD.A1`](#trajectoire-tclda1) _(Lines 73-88)_
   1. [Narratif](#narratif) _(Lines 91-105)_
1. [A2 Pile technique, standards et plateformes](#a2-pile-technique-standards-et-plateformes) _(Lines 108-111)_
   1. [Faits](#faits-1) _(Lines 114-125)_
   1. [Jalons cités](#jalons-cités-1) _(Lines 128-131)_
   1. [Trajectoire `T.CLD.A2`](#trajectoire-tclda2) _(Lines 134-149)_
   1. [Narratif](#narratif-1) _(Lines 152-166)_
1. [A3 Structure du secteur technologique](#a3-structure-du-secteur-technologique) _(Lines 169-171)_
   1. [Faits](#faits-2) _(Lines 174-185)_
   1. [Jalons cités](#jalons-cités-2) _(Lines 188-191)_
   1. [Trajectoire `T.CLD.A3`](#trajectoire-tclda3) _(Lines 194-209)_
   1. [Narratif](#narratif-2) _(Lines 212-228)_
1. [A4 Mode de production du logiciel et des services](#a4-mode-de-production-du-logiciel-et-des-services) _(Lines 231-234)_
   1. [Faits](#faits-3) _(Lines 237-250)_
   1. [Jalons cités](#jalons-cités-3) _(Lines 253-256)_
   1. [Trajectoire `T.CLD.A4`](#trajectoire-tclda4) _(Lines 259-274)_
   1. [Narratif](#narratif-3) _(Lines 277-295)_
1. [A5 Reconfiguration des autres secteurs](#a5-reconfiguration-des-autres-secteurs) _(Lines 298-301)_
   1. [Faits](#faits-4) _(Lines 304-315)_
   1. [Jalons cités](#jalons-cités-4) _(Lines 318-321)_
   1. [Trajectoire `T.CLD.A5`](#trajectoire-tclda5) _(Lines 324-339)_
   1. [Narratif](#narratif-4) _(Lines 342-357)_
1. [Sources](#sources) _(Lines 360-401)_



---

## A1 Infrastructure physique et capacité
<!-- Lines 46-48 -->

**Question :** Qu'est-ce qui a été construit, à quel rythme, avec quelles surcapacités ?

### Faits
<!-- Lines 51-64 -->

| id | année | bloc | énoncé | valeur | acteurs | attribution | source | statut |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| F.CLD.A1.001 | 2007, 2009, 2012 | US | Les dépenses en immobilisations corporelles (« purchases of property and equipment ») d'un grand détaillant en ligne exploitant sa propre usine cloud croissent d'un ordre de grandeur sur la période. | 224 M$ (2007) ; 373 M$ (2009) ; 3 785 M$ (2012) | O2 | choc | [S15] | V |
| F.CLD.A1.002 | 2010, 2011 | US | Les dépenses en immobilisations corporelles du même exploitant poursuivent leur hausse continue entre 2009 et 2012, sans année de recul. | 979 M$ (2010) ; 1 811 M$ (2011) | O2 | choc | [S15] | V |
| F.CLD.A1.003 | 2006 | US | Un service de stockage d'objets loué au gigaoctet est ouvert sans contrat préalable ni engagement de durée. | lancement 14 mars 2006, 0,15 $/Go/mois, aucun minimum | O2, O1 | choc | [S10] | V |
| F.CLD.A1.004 | 2006 | US | Un service de machines virtuelles loué à l'heure est ouvert en version d'essai, démarrable et arrêtable par appel programmatique. | lancement bêta 24-25 août 2006, capacité facturée à l'usage | O2, O1, M1 | choc | [S11] | V |
| F.CLD.A1.005 | 2007 | US | Le stockage d'objets loué franchit le cap de plusieurs milliards d'objets hébergés, chiffre publié par le fournisseur. | 14 milliards d'objets fin 2007 (contre 2,9 Md fin 2006) | O2 | choc | [S10] | V |
| F.CLD.A1.006 | 2012, 2014, 2015 | US | Les fournisseurs de capacité louée réduisent leurs tarifs de stockage et de calcul plusieurs fois par an, tendance continue jusqu'en fin de fenêtre. | baisses tarifaires répétées | O1, O2, O4 | co:X.CLD.10 | [S60] | A |
| F.CLD.A1.007 | 2015 | MONDE | La dépense en capital consacrée aux centres de données par les quelques plus grands opérateurs mondiaux dépasse celle du reste de l'industrie informatique réunie. | dépassement au niveau agrégat | O2, O3, O4 | choc | [S15] | K |
| F.CLD.A1.008 | 2007 | US | L'agence américaine de protection de l'environnement chiffre la consommation électrique des serveurs et centres de données à 61 TWh en 2006, soit 1,5 % de l'électricité nationale, le double de 2000 ; capacité rapportée sur une pointe d'environ 7 GW. Fait cité en A1 pour la capacité installée ; le détail énergétique relève de H1. | 61 TWh, 1,5 %, 4,5 Md$ | O6, O2 | choc | [S51] | V |
| F.CLD.A1.009 | 2011 | EU | Un grand réseau social annonce le 27 octobre 2011 la construction d'un centre de données à Luleå, dans le nord de la Suède, dont le climat froid et sec permet le refroidissement par l'air extérieur et dont l'électricité est principalement renouvelable (hydroélectricité) et, selon les autorités, parmi les moins chères d'Europe. Fait cité en A1 pour la capacité et sa localisation ; le motif énergétique relève de H2. | annonce du 27 octobre 2011 (Luleå, Suède) | O2, T2 | choc | [S59] | A |
| F.CLD.A1.010 | 2003-2004 | US, MONDE | Avant t0 : l'informatique d'entreprise reste très majoritairement possédée, chaque organisation achetant ses propres serveurs pour sa propre salle machine. | — | O4, M1 | exo | [S1] | K |

### Jalons cités
<!-- Lines 67-70 -->

`J.CLD.2007.02`, `J.CLD.2006.01`, `J.CLD.2006.02`, `J.CLD.2007.04`, `J.CLD.2007.06`,
`J.CLD.2010.07`, `J.CLD.2011.08`, `J.CLD.2015.05`.

### Trajectoire `T.CLD.A1`
<!-- Lines 73-88 -->

| année | phase | intensité | ce qui change | faits et jalons |
| --- | --- | --- | --- | --- |
| avant t0 | latent | 1 | Informatique possédée ; virtualisation détache déjà le service de la machine sans changer le mode d'achat. | F.CLD.A1.010, J.CLD.2003.01 |
| 2005 | émergence | 1 | Réorganisation interne en services appelables, condition préalable à la location externe. | J.CLD.2005.01 |
| 2006 | émergence | 2 | Ouverture des premiers services de capacité facturés à l'usage, sans contrat. | F.CLD.A1.003, F.CLD.A1.004 |
| 2007 | accélération | 3 | Les dépenses en capital basculent massivement vers la construction de centres de données ; premier chiffrage officiel de la consommation électrique. | F.CLD.A1.001, F.CLD.A1.005, F.CLD.A1.008, J.CLD.2007.02 |
| 2008 | crise | 2 | La crise financière (X.CLD.03) freine le crédit mais ne ralentit pas la bascule vers la location. | J.CLD.2008.01 |
| 2009 | accélération | 2 | Reprise de la croissance des dépenses en capital après le creux de la crise. | F.CLD.A1.001 |
| 2010 | accélération | 2 | Poursuite continue de la hausse des dépenses en capital ; l'exploitant devient acheteur d'électricité de gros. | F.CLD.A1.002, J.CLD.2010.07 |
| 2011 | consolidation | 2 | Poursuite de la hausse des dépenses en capital ; un centre de données est annoncé dans le nord de la Suède pour son climat froid et son électricité principalement renouvelable. | F.CLD.A1.002, F.CLD.A1.009 |
| 2012 | consolidation | 3 | Les dépenses en capital d'un seul exploitant dépassent quinze fois leur niveau de 2007. | F.CLD.A1.001 |
| 2013 | consolidation | 0 | Poursuite de la course à la capacité sans bascule nouvelle documentée cette année pour A1. | — |
| 2014 | consolidation | 2 | Baisses tarifaires coordonnées ; poursuite de la construction. | F.CLD.A1.006 |
| 2015 | banalisation | 3 | La dépense en capital des plus grands opérateurs dépasse celle du reste de l'industrie informatique réunie. | F.CLD.A1.007 |

### Narratif
<!-- Lines 91-105 -->

En dix ans, la dépense en capital d'un seul exploitant passe de 224 millions à plus de 3,8
milliards de dollars par an, avant de continuer sa progression jusqu'en 2015 [F.CLD.A1.001,
F.CLD.A1.002]. L'infrastructure démarre par des services facturés à l'unité sans contrat
[F.CLD.A1.003, F.CLD.A1.004], franchit rapidement une échelle mesurable en milliards d'objets
[F.CLD.A1.005], puis devient assez grande pour entrer dans les statistiques énergétiques
nationales [F.CLD.A1.008]. La crise financière de 2008 ne casse pas la tendance de fond
[J.CLD.2008.01], et un centre de données est annoncé en 2011 dans le nord de la Suède pour son
climat froid et son électricité principalement renouvelable [F.CLD.A1.009]. À t0+10, la capacité
installée par une poignée d'opérateurs dépasse celle du reste de l'industrie informatique réunie
[F.CLD.A1.007], signe d'une concentration de l'appareil productif inédite pour une industrie née
dix ans plus tôt de simples salles machines possédées [F.CLD.A1.010].

---

## A2 Pile technique, standards et plateformes
<!-- Lines 108-111 -->

**Question :** Quelles briques logicielles et quels standards se sont imposés, ouverts ou
propriétaires, et qui les a fixés ?

### Faits
<!-- Lines 114-125 -->

| id | année | bloc | énoncé | valeur | acteurs | attribution | source | statut |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| F.CLD.A2.001 | 2003 | US | La virtualisation de serveurs x86 devient un produit d'entreprise courant, découplant le service de la machine physique. | — | M1, O4, O2 | exo | [S1] | K |
| F.CLD.A2.002 | 2004-2005 | US | Un article de recherche publié par un grand opérateur du web décrit un cadre de calcul distribué sur grappes de machines banalisées, repris ensuite en projet ouvert. | publication 2004, implémentation ouverte à partir de 2006 | M1, O2, O7 | co:X.CLD.05 | [S8] | V |
| F.CLD.A2.003 | 2011 | US | L'institut américain de normalisation publie la définition normative de l'informatique en nuage (SP 800-145) : cinq caractéristiques, trois modèles de service, quatre modèles de déploiement. | NIST SP 800-145, 28 septembre 2011, Mell et Grance | O6 | choc | [S32] | V |
| F.CLD.A2.004 | 2010 | US | Un projet ouvert de logiciel d'infrastructure est lancé pour permettre à une organisation de bâtir sa propre usine de capacité à la demande, hors des fournisseurs propriétaires. | annonce 26 juillet 2010, code donné par Rackspace + technologie NASA Nebula | O6, O2, M1 | choc | [S28] | V |
| F.CLD.A2.005 | 2013 | MONDE | Un format de conteneur logiciel standardisé se diffuse rapidement comme unité de déploiement portable entre machines et entre fournisseurs, indifférente à l'usine qui l'exécute. | annonce publique mars 2013, publication open source rapportée le 1er avril 2013 | M1, O1, O4 | choc | [S37] | V |
| F.CLD.A2.006 | 2014 | US | Un système d'orchestration de conteneurs conçu pour l'exploitation à très grande échelle est publié en logiciel libre par un des trois grands exploitants. | publication juin 2014 | M1, O2, O1 | choc | [S46] | V |
| F.CLD.A2.007 | 2004-2005 | MONDE | La pile serveur ouverte (système, serveur web, base de données, langages de script) devient majoritaire sur le web public, supprimant le coût de licence à l'entrée. | majorité du parc serveur web public | M1, O1 | exo | [S3] | K |
| F.CLD.A2.008 | 2007-2009 | MONDE | 2007-2009 : Amazon (Dynamo, 2007) puis Facebook (Cassandra, 2009) décrivent des bases non relationnelles distribuées sur machines banalisées, conçues pour traiter la panne comme la norme à l'échelle de dizaines de milliers de serveurs ; Facebook a conçu Cassandra pour le stockage de la recherche dans la boîte de réception. | | M1, O1, O2 | choc | [S26] | V |

### Jalons cités
<!-- Lines 128-131 -->

`J.CLD.2011.01`, `J.CLD.2003.01`, `J.CLD.2004.01`, `J.CLD.2005.04`, `J.CLD.2006.05`,
`J.CLD.2009.03`, `J.CLD.2010.01`, `J.CLD.2011.06`, `J.CLD.2013.05`, `J.CLD.2014.03`.

### Trajectoire `T.CLD.A2`
<!-- Lines 134-149 -->

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
<!-- Lines 152-166 -->

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
<!-- Lines 169-171 -->

**Question :** Qui produit la technologie : anciens, nouveaux, intégrés, concentrés ?

### Faits
<!-- Lines 174-185 -->

| id | année | bloc | énoncé | valeur | acteurs | attribution | source | statut |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| F.CLD.A3.001 | 2015-04 | US | Un grand détaillant en ligne publie pour la première fois séparément le chiffre d'affaires et le résultat d'exploitation de son activité de services en nuage : 1 566 M$ de chiffre d'affaires au premier trimestre 2015, contre 1 050 M$ au premier trimestre 2014, et 265 M$ de résultat d'exploitation. | 1 566 M$ (T1 2015), 1 050 M$ (T1 2014), +49 %, 265 M$ de résultat d'exploitation | O2 | choc | [S48] | V |
| F.CLD.A3.002 | 2008 | US | L'éditeur historique des systèmes d'exploitation et logiciels d'entreprise annonce une offre de calcul et de stockage loués, entrée tardive d'un titulaire sur un marché ouvert deux ans plus tôt par un nouvel entrant. | annonce Windows Azure le 27 octobre 2008, PDC Los Angeles | O2, O4 | choc | [S20] | V |
| F.CLD.A3.003 | 2013 | MONDE | En 2013, le chiffre d'affaires mondial des serveurs recule de 4,5 % pour des livraisons en hausse de 2,1 % ; au quatrième trimestre, celui d'IBM recule de 28,9 % et celui d'Oracle de 4,7 %, le cabinet source relevant une croissance continue des déploiements « Web-scale IT » face à des entreprises « relativement contraintes ». | −4,5 % de chiffre d'affaires, +2,1 % de livraisons (2013) ; IBM −28,9 % au T4 2013 | O2, O4, M9 | choc | [S35] | A |
| F.CLD.A3.004 | 2014 | US | Trois fournisseurs de capacité louée annoncent successivement, les 25, 26 et 31 mars 2014, des baisses de prix du calcul et du stockage en nuage. | 25, 26 et 31 mars 2014 ; Microsoft : calcul jusqu'à −35 %, stockage jusqu'à −65 % | O2, O4, O1 | co:X.CLD.10 | [S38] | A |
| F.CLD.A3.005 | 2009 | CN | En 2009, un grand groupe chinois de commerce en ligne crée une filiale dédiée aux services de nuage. | filiale créée en septembre 2009 (Alibaba Cloud Computing) | T4, O2, O6 | choc | [S17] | A |
| F.CLD.A3.006 | 2009 | EU | Les groupes européens du numérique et les pouvoirs publics constatent qu'aucun fournisseur d'usines à l'échelle mondiale n'est européen. | absence constatée | T2, O6, O2 | choc | [S27] | K |
| F.CLD.A3.007 | 2012 | EU | En 2012, deux projets français de « cloud souverain » sont lancés ; le gouvernement les finance par l'intermédiaire de la Caisse des dépôts, qui détient 33,33 % du capital de l'un d'eux. | Caisse des dépôts : 33,33 % de Cloudwatt ; investissement total de 225 M€ pour chacun des deux projets (Cloudwatt, Numergy) | T2, O6, O2 | choc | [S61] | A |
| F.CLD.A3.008 | 2013 | MONDE | En 2013, un cabinet d'analystes publie une prévision de dépense mondiale en services de nuage public, qu'il suit comme un marché distinct découpé en six segments (publicité, processus métier, logiciel, infrastructure, plateforme, gestion et sécurité) ; chiffres d'analystes non repris, artefact de mesure. | marché suivi séparément, six segments | O2, O4 | choc | [S62] | A |

### Jalons cités
<!-- Lines 188-191 -->

`J.CLD.2015.01`, `J.CLD.2007.05`, `J.CLD.2008.03`, `J.CLD.2010.05`, `J.CLD.2011.04`,
`J.CLD.2012.03`, `J.CLD.2013.06`, `J.CLD.2014.01`.

### Trajectoire `T.CLD.A3`
<!-- Lines 194-209 -->

| année | phase | intensité | ce qui change | faits et jalons |
| --- | --- | --- | --- | --- |
| avant t0 | latent | 1 | L'entrée en bourse d'un moteur de recherche financé par la publicité fait apparaître l'usine informatique à grande échelle comme un actif finançable. | J.CLD.2004.02 |
| 2005 | émergence | 2 | Constructeurs et intégrateurs historiques promeuvent l'informatique « à la demande » en réponse à un modèle interne déjà en place chez un nouvel entrant. | J.CLD.2005.02 |
| 2006 | émergence | 0 | Aucune bascule de structure nouvelle documentée ; consolidation de l'offre du nouvel entrant. | — |
| 2007 | accélération | 0 | Aucune bascule de structure documentée cette année pour A3 (la création de la filiale chinoise est datée de 2009, F.CLD.A3.005). | — |
| 2008 | crise | 2 | Un titulaire historique entre tardivement sur le marché de la capacité louée. | F.CLD.A3.002, J.CLD.2008.03 |
| 2009 | crise | 2 | L'Europe constate l'absence d'un fournisseur d'usines à son échelle ; un groupe chinois crée une filiale dédiée aux services de nuage. | F.CLD.A3.005, F.CLD.A3.006 |
| 2010 | consolidation | 0 | Aucune bascule de structure nouvelle documentée cette année pour A3 (voir 2009 pour la filiale chinoise). | — |
| 2011 | consolidation | 0 | Aucune bascule de structure nouvelle documentée cette année pour A3 (le recul du chiffre d'affaires des serveurs est daté de 2013, F.CLD.A3.003). | — |
| 2012 | consolidation | 1 | Lancement en France de deux projets de « cloud souverain » financés par le gouvernement via la Caisse des dépôts. | F.CLD.A3.007, J.CLD.2012.03 |
| 2013 | consolidation | 2 | Un cabinet d'analystes suit le marché des services en nuage comme un marché distinct ; le chiffre d'affaires mondial des serveurs recule de 4,5 % pour des livraisons en hausse. | F.CLD.A3.003, F.CLD.A3.008, J.CLD.2013.06 |
| 2014 | consolidation | 2 | Trois fournisseurs annoncent en une semaine, fin mars, des baisses de prix du calcul et du stockage. | F.CLD.A3.004, J.CLD.2014.01 |
| 2015 | banalisation | 3 | Première publication séparée du chiffre d'affaires cloud d'un grand exploitant, révélant une activité de plusieurs milliards très rentable. | F.CLD.A3.001, J.CLD.2015.01 |

### Narratif
<!-- Lines 212-228 -->

Le secteur s'ouvre avec un nouvel entrant qui loue sa propre usine interne, pendant que les
constructeurs et éditeurs historiques répondent d'abord par un vocabulaire commercial adossé à
leurs centres de données existants [J.CLD.2005.01, J.CLD.2005.02]. Un titulaire majeur n'entre
sur le marché de la capacité louée qu'en 2008, avec deux ans de retard sur le nouvel entrant
[F.CLD.A3.002]. En 2013, le chiffre d'affaires mondial des serveurs recule de 4,5 % pour des
livraisons en hausse, le cabinet source relevant la croissance des déploiements « Web-scale IT »
[F.CLD.A3.003]. La Chine voit naître en 2009 une filiale dédiée aux services de nuage d'un groupe
de commerce en ligne [F.CLD.A3.005] ; l'Europe constate en 2009 l'absence d'un fournisseur à son
échelle [F.CLD.A3.006] et voit lancer en 2012 deux projets français de « cloud souverain »
financés par le gouvernement via la Caisse des dépôts [F.CLD.A3.007]. En mars 2014, trois
fournisseurs annoncent en une semaine des baisses de prix du calcul et du stockage
[F.CLD.A3.004], et un grand détaillant en ligne publie en 2015 séparément le chiffre d'affaires
et le résultat de son activité de services en nuage [F.CLD.A3.001].

---

## A4 Mode de production du logiciel et des services
<!-- Lines 231-234 -->

**Question :** Comment fabrique-t-on et exploite-t-on un service numérique, à quel coût, avec
quelle organisation ?

### Faits
<!-- Lines 237-250 -->

| id | année | bloc | énoncé | valeur | acteurs | attribution | source | statut |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| F.CLD.A4.001 | 2005-2006 | US | Un service de partage vidéo fondé en février 2005 par trois personnes dépasse 100 millions de vidéos vues par jour en octobre 2006 ; selon la presse spécialisée d'octobre 2006, la livraison de ses vidéos est assurée par un prestataire externe de diffusion de contenu. | 3 fondateurs ; plus de 100 millions de vidéos vues par jour (octobre 2006) | O1, M9 | choc | [S9] | A |
| F.CLD.A4.002 | 2012 | MONDE | Au moment de son rachat par un grand réseau social en avril 2012, une application de partage de photographies compte 13 employés et environ 30 millions d'usagers ; fin 2011, son exploitation reposait sur des services loués (instances EC2 et stockage S3 d'Amazon) avec trois ingénieurs. | 13 employés ; environ 30 millions d'usagers | O1, M1, M9 | choc | [S29] | A |
| F.CLD.A4.003 | 2008 | MONDE | Une plateforme d'exécution d'applications hébergée est ouverte, où le développeur ne gère plus ni machine ni système d'exploitation, deuxième étage de délégation après la capacité brute. | lancement en avant-première le 7 avril 2008 (Google App Engine) | O1, M1 | choc | [S19] | V |
| F.CLD.A4.004 | 2009 | US | En 2009, la presse spécialisée et un rapport universitaire présentent la location de capacité informatique comme le passage de la dépense en capital à la dépense de fonctionnement, la crise du crédit, qui prive de nombreuses entreprises de l'emprunt nécessaire aux gros investissements initiaux, étant avancée comme argument ; l'intérêt financier propre de ce passage est contesté. | — | O4, M1, M9 | co:X.CLD.03 | [S21] | A |
| F.CLD.A4.005 | 2006-2010 | US | Après le lancement d'Amazon Web Services en 2006, les jeunes entreprises américaines des secteurs pouvant louer leur capacité informatique (logiciel en ligne, réseaux sociaux, commerce en ligne) lèvent en moyenne 20 % de moins au premier tour de financement en capital-risque, et le nombre de premiers financements par an dans ces secteurs passe d'environ 375 à plus de 700. | −20 % du premier tour ; d'environ 375 à plus de 700 premiers financements par an | O1, M9, M1 | choc | [S24] | V |
| F.CLD.A4.006 | 2012 | MONDE | En juin 2012, un rapport d'un éditeur technique écrit que les administrateurs système à l'ancienne peuvent disparaître face à l'automatisation et à l'informatique en nuage, l'exploitation devenant un arrangement « DevOps » où les spécialistes d'exploitation rejoignent l'équipe de développement. | — | M1, O4 | choc | [S31] | A |
| F.CLD.A4.007 | 2013 | MONDE | L'outil Docker, né en logiciel libre chez dotCloud début 2013, permet d'empaqueter une application avec ses dépendances dans un conteneur qui s'exécute sans difficulté dans les environnements de développement, de test et de production dès lors qu'ils utilisent Docker. | — | M1, O1 | choc | [S64] | A |
| F.CLD.A4.008 | 2015 | US | En octobre 2015, lors de la conférence d'un fournisseur de nuage, deux grandes entreprises américaines, Capital One et GE, annoncent réduire leurs centres de données : Capital One de huit en 2014 à trois fin 2018, GE de 34 à quatre en trois ans avec le transfert de ses 9 000 charges de travail chez ce fournisseur. | Capital One : 8 (2014) → 3 (fin 2018) ; GE : 34 → 4 | O4, M1, M9 | choc | [S45] | A |
| F.CLD.A4.009 | 2014-11 | US | Un service d'exécution de code facturé à l'appel est ouvert, sans machine ni serveur à déclarer : l'unité facturée descend de la machine-heure à la fonction exécutée. | lancement AWS Lambda le 13 novembre 2014, facturation par tranche de 100 ms | M1, O1 | choc | [S47] | V |
| F.CLD.A4.010 | 2015 | US | Dans une enquête publiée en août 2015 auprès de directeurs informatiques de l'enseignement supérieur (230 répondants), ceux-ci anticipent à cinq puis dix ans un déplacement de leur gestion, de l'infrastructure et des ressources techniques vers la gestion de fournisseurs, de services et de contrats d'externalisation ; les postes en croissance sont les spécialistes d'intégration de données, de sécurité et de vie privée, les juristes, les négociateurs de contrats et les gestionnaires de fournisseurs. | 230 répondants | M1, M9, O4 | choc | [S63] | A |

### Jalons cités
<!-- Lines 253-256 -->

`J.CLD.2005.05`, `J.CLD.2008.02`, `J.CLD.2008.04`, `J.CLD.2009.01`, `J.CLD.2010.06`,
`J.CLD.2011.06`, `J.CLD.2014.02`, `J.CLD.2014.05`, `J.CLD.2015.06`.

### Trajectoire `T.CLD.A4`
<!-- Lines 259-274 -->

| année | phase | intensité | ce qui change | faits et jalons |
| --- | --- | --- | --- | --- |
| avant t0 | latent | 1 | Le logiciel loué à l'abonnement s'impose comme modèle crédible en gestion de la relation client, sans installation chez le client. | J.CLD.2003.02 |
| 2005 | émergence | 2 | Un service de partage vidéo est fondé par trois personnes ; la livraison de ses vidéos repose sur un prestataire externe de diffusion de contenu. | F.CLD.A4.001, J.CLD.2005.05 |
| 2006 | émergence | 0 | Diffusion des premiers services à l'usage ; pas de rupture de mode de production nouvelle cette année. | — |
| 2007 | accélération | 1 | Premiers cursus et recherches sur le calcul distribué à très grande échelle, hors des entreprises qui l'ont inventé. | J.CLD.2007.03 |
| 2008 | crise | 2 | Délégation de l'exploitation elle-même (plateforme hébergée) ; l'arbitrage entre dépense en capital et dépense de fonctionnement relève du jalon J.CLD.2008.04. | F.CLD.A4.003, J.CLD.2008.02, J.CLD.2008.04 |
| 2009 | accélération | 2 | La location de capacité est présentée comme le passage de la dépense en capital à la dépense de fonctionnement, la crise du crédit servant d'argument ; depuis 2006, la location de matériel abaisse le premier tour de financement des jeunes entreprises en ligne. | F.CLD.A4.004, F.CLD.A4.005, J.CLD.2009.01 |
| 2010 | accélération | 2 | Le métier d'administrateur système change de nature : de la machine au code (jalon J.CLD.2010.06). | J.CLD.2010.06 |
| 2011 | accélération | 2 | Un outil de conteneurisation et de livraison continue commence à réduire l'écart entre poste de développement et production (jalon J.CLD.2011.06). | J.CLD.2011.06 |
| 2012 | consolidation | 2 | Une équipe de 13 employés sert environ 30 millions d'usagers au moment du rachat, sur des services loués ; un rapport de juin 2012 décrit la disparition possible de l'administrateur système à l'ancienne au profit d'équipes « DevOps ». | F.CLD.A4.002, F.CLD.A4.006 |
| 2013 | consolidation | 0 | Diffusion des conteneurs comme unité de déploiement, sans rupture de mode de production nouvelle pour A4 ; l'outil Docker, né en logiciel libre début 2013, exécute à l'identique une application dans les environnements de développement, de test et de production. | F.CLD.A4.007 |
| 2014 | consolidation | 3 | L'unité facturée descend à la fonction exécutée (le jalon J.CLD.2014.02 porte sur la fermeture de centres de données). | F.CLD.A4.009, J.CLD.2014.02, J.CLD.2014.05 |
| 2015 | banalisation | 2 | Deux grandes entreprises américaines annoncent réduire leurs centres de données ; des directeurs informatiques de l'enseignement supérieur anticipent une gestion centrée sur les fournisseurs et les contrats. | F.CLD.A4.008, F.CLD.A4.010, J.CLD.2015.06 |

### Narratif
<!-- Lines 277-295 -->

Le mode de production change d'échelle humaine avant de changer de coût : un service de partage
vidéo fondé par trois personnes en 2005 dépasse 100 millions de vidéos vues par jour en 2006
en confiant sa diffusion à un prestataire externe [F.CLD.A4.001], et une équipe de 13 employés
sert environ 30 millions d'usagers en 2012 sur des services loués [F.CLD.A4.002]. En 2009, la location de capacité est présentée comme le passage de la dépense en capital à la
dépense de fonctionnement, la crise du crédit servant d'argument [F.CLD.A4.004]. Après 2006, la
location de matériel remplace l'investissement initial en serveurs : les jeunes entreprises en
ligne financées par le capital-risque lèvent en moyenne 20 % de moins au premier tour
[F.CLD.A4.005]. Le travail d'exploitation lui-même change : un rapport de 2012 décrit la
disparition possible de l'administrateur système à l'ancienne au profit d'équipes « DevOps »
[F.CLD.A4.006], un outil de conteneurs permet dès 2013 d'exécuter à l'identique la même
application du développement à la production [F.CLD.A4.007], puis, en 2014, l'unité facturée passe
du serveur à la fonction exécutée à l'appel [F.CLD.A4.009]. En 2015, deux grandes entreprises
américaines annoncent réduire leurs centres de données [F.CLD.A4.008], et des directeurs
informatiques de l'enseignement supérieur anticipent une gestion centrée sur les fournisseurs et
les contrats plutôt que sur l'infrastructure [F.CLD.A4.010].

---

## A5 Reconfiguration des autres secteurs
<!-- Lines 298-301 -->

**Question :** Comment les chaînes de valeur des autres industries se réorganisent-elles :
intermédiaires supprimés ou créés ?

### Faits
<!-- Lines 304-315 -->

| id | année | bloc | énoncé | valeur | acteurs | attribution | source | statut |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| F.CLD.A5.001 | 2003 | US | Un éditeur de gestion de la relation client démontre que le logiciel d'entreprise peut se vendre en abonnement hébergé sans installation, prérequis du basculement du secteur logiciel. | fondé 1999, service on-demand depuis février 2000, modèle "fully outsourced service accessible over the Internet" | O1, O4, M9 | exo | [S2] | V |
| F.CLD.A5.002 | 2009 | US | L'éditeur de gestion de la relation client hébergé dépasse le milliard de dollars de chiffre d'affaires annuel sans installer de logiciel chez ses clients, preuve de taille industrielle du modèle. | 1 077 M$ (exercice clos janvier 2009), contre 749 M$ (exercice clos janvier 2008) | O2, O4 | choc | [S2] | V |
| F.CLD.A5.003 | 2006 | US | Une suite bureautique en ligne gratuite est proposée aux organisations comme substitut à des logiciels installés poste par poste, faisant sortir le courriel et les documents des murs de l'organisation. | lancement 28 août 2006, Google Apps for Your Domain, gratuit en bêta | O4, O7, M4 | choc | [S13] | V |
| F.CLD.A5.004 | 2008 | EMERG | Un service de paiement par téléphone mobile simple, adossé à une plateforme centralisée d'opérateur, atteint plusieurs millions d'usagers en Afrique de l'Est sans réseau d'agences bancaires. | lancé mars 2007 ; environ 2 à 3 millions d'usagers courant 2008, 9 millions en janvier 2010 | T5, P8, O3 | choc | [S22] | V |
| F.CLD.A5.005 | 2012-2013 | EMERG | En 2012-2013, des analystes relèvent que les services d'infrastructure externalisés sont exposés à la perturbation par des systèmes automatisés et que des prestataires indiens orientent leur recherche vers l'intégration des activités qu'exige le passage au nuage, l'un d'eux notant que le potentiel du nuage ne s'est pas encore concrétisé. | — | T5, M1, O4 | choc | [S40] | A |
| F.CLD.A5.006 | 2012-2014 | MONDE | Trois offres de stockage grand public synchronisé annoncent des centaines de millions d'usagers : Dropbox passe de 100 millions en novembre 2012 à 300 millions en mai 2014, Google Drive compte 240 millions d'usagers actifs en septembre 2014, OneDrive plus de 250 millions selon Microsoft. | Dropbox : 100 M (nov. 2012), 200 M (nov. 2013), 300 M (mai 2014) ; Google Drive : 240 M actifs (sept. 2014) ; OneDrive : plus de 250 M | P2, P3, P4, O2 | choc | [S39] | A |
| F.CLD.A5.007 | 2014-2016 | EU | Des organismes publics de plusieurs pays européens publient des référentiels de sécurité des services en nuage : en avril 2014 un recueil de guides du CESG britannique pour les organisations publiques, en 2016 le catalogue C5 de l'office fédéral allemand de la sécurité de l'information et, le 12 décembre 2016, la première partie du référentiel de l'ANSSI française, expérimenté avec neuf prestataires depuis mars 2015. | CESG : 23 avril 2014 ; ANSSI : expérimentation dès mars 2015, publication le 12 décembre 2016 ; BSI C5 : 2016 | T2, O6, O2 | choc | [S36] | A |
| F.CLD.A5.008 | — | — | retiré : énoncé méta sur l'absence de série officielle unifiée, pas un fait daté et sourçable ; aucune source admissible ne peut l'étayer par construction (elle documenterait l'absence de source, pas un fait) ; seules des séries d'analystes existent ([S44]), insuffisantes pour fonder un fait daté. | — | — | — | — | — |

### Jalons cités
<!-- Lines 318-321 -->

`J.CLD.2015.01`, `J.CLD.2006.04`, `J.CLD.2008.05`, `J.CLD.2009.05`, `J.CLD.2012.04`,
`J.CLD.2012.05`, `J.CLD.2015.04`.

### Trajectoire `T.CLD.A5`
<!-- Lines 324-339 -->

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
| 2012 | consolidation | 3 | Le stockage synchronisé grand public atteint 100 millions d'usagers (novembre 2012) ; des analystes relèvent l'exposition des services d'infrastructure externalisés à l'automatisation et l'orientation de prestataires indiens vers l'intégration. | F.CLD.A5.005, F.CLD.A5.006, J.CLD.2012.04, J.CLD.2012.05 |
| 2013 | consolidation | 0 | Diffusion continue, pas de bascule sectorielle nouvelle documentée pour A5. | — |
| 2014 | consolidation | 0 | Diffusion continue, pas de bascule sectorielle nouvelle documentée pour A5. | — |
| 2015 | banalisation | 2 | Des organismes publics européens publient ou expérimentent des référentiels de sécurité des services en nuage (expérimentation française dès mars 2015). | F.CLD.A5.007, J.CLD.2015.04 |

### Narratif
<!-- Lines 342-357 -->

Le secteur logiciel bascule le premier : un modèle d'abonnement hébergé démontré dès 2003 dépasse
le milliard de dollars de chiffre d'affaires annuel en 2009 [F.CLD.A5.001, F.CLD.A5.002]. La
bureautique en ligne fait sortir le document et le courriel des murs de l'organisation dès 2006
[F.CLD.A5.003]. Dans les pays émergents, un service de paiement mobile adossé à une plateforme
centralisée crée un canal financier parallèle sans réseau bancaire physique [F.CLD.A5.004], et, en
2012-2013, des analystes relèvent que les services d'infrastructure externalisés sont exposés à
l'automatisation et que des prestataires indiens orientent leur recherche vers l'intégration des
activités liées au nuage [F.CLD.A5.005]. Le grand public passe par des comptes de stockage
synchronisé : trois offres annoncent en 2014 entre 240 et 300 millions d'usagers
[F.CLD.A5.006] ; ce vécu grand public reste un canal indirect et non le cœur du choc industriel
[X.CLD.01, X.CLD.02, voir 04_confondants.md]. Entre 2014 et 2016, des organismes publics
européens publient des référentiels de sécurité des services en nuage [F.CLD.A5.007].

---

## Sources
<!-- Lines 360-401 -->

| clé | type | référence | note |
| --- | --- | --- | --- |
| [S1] | off | VMware Inc., prospectus d'introduction en bourse (Form S-1, SEC, 2007) et rapports annuels ultérieurs | Reprise de [S1] de `par_annee/cloud_2005_2015.md`. Historique de l'adoption de la virtualisation x86 en entreprise. À vérifier. |
| [S2] | off | salesforce.com inc., rapports annuels (Form 10-K, SEC), exercices 2004 à 2010 ; CIK 0001108524 | Ouvert et lu le 2026-09-22 : 10-K exercice clos 31 janvier 2005 (accession 0001193125-05-061027, sec.gov/Archives/edgar/data/1108524/000119312505061027/d10k.htm) — fondation février 1999, service on-demand depuis février 2000, modèle « fully outsourced service accessible over the Internet », substitut au logiciel installé (F.CLD.A5.001) ; 10-K exercice clos 31 janvier 2009 (accession 0001193125-09-048665, sec.gov/Archives/edgar/data/1108524/000119312509048665/d10k.htm) — chiffre d'affaires 1 077 M$ (FY2009) contre 749 M$ (FY2008) (F.CLD.A5.002). |
| [S3] | stat | Netcraft, Web Server Survey, séries mensuelles 2003-2005 | Reprise de [S3] de la chronologie. Parts de marché des serveurs web. |
| [S8] | acad | Dean, J. et Ghemawat, S., « MapReduce: Simplified Data Processing on Large Clusters », OSDI, 2004 ; projet Apache Hadoop, premières versions 2006 | Ouvert et lu le 2026-09-22 : research.google/pubs (listing officiel Google Research) — titre, auteurs (Jeffrey Dean, Sanjay Ghemawat), venue (OSDI'04, San Francisco), année 2004 confirmés. Date 2006 pour l'implémentation ouverte (scission Hadoop du projet Nutch, 28 janvier 2006) corroborée par plusieurs rétrospectives secondaires, pas par une page Apache d'origine ouverte directement. |
| [S9] | off | Google Inc., « Google To Acquire YouTube for $1.65 Billion in Stock », communiqué, 9 octobre 2006, reproduit par https://hexus.net/business/news/internet/6972-google-buy-youtube-165-billion-share-swap-deal/?page=2 ; Wikipedia, « YouTube », https://en.wikipedia.org/wiki/YouTube ; Miller, R., « Google-YouTube: Bad News for Limelight? », Data Center Knowledge, 13 octobre 2006, https://datacenterknowledge.com/hyperscalers/google-youtube-bad-news-for-limelight- | Ouverts et lus le 2026-11-22. Communiqué Google (reproduction) : « Founded in February 2005 », « YouTube currently delivers more than 100 million video views every day with 65,000 new videos uploaded daily » ; il ne nomme pas les fondateurs et ne dit rien de l'hébergement. Wikipedia (ouvrage de référence, 100 000 premiers caractères de la page lus) : « YouTube was founded by Chad Hurley, Jawed Karim, and Steve Chen » (trois fondateurs) ; 8 millions de vues par jour à la sortie de bêta en décembre 2005. Data Center Knowledge (presse spécialisée contemporaine, qui cite MarketWatch) : « Limelight delivers the videos for YouTube » ; l'article décrit YouTube comme le « marquee client » de Limelight Networks (prestataire de diffusion de contenu). L'ancienne clause « sans posséder l'infrastructure de diffusion » n'est étayée par aucune de ces pages et a été retirée ; la formule « en quelques mois » aussi. |
| [S10] | off | Amazon Web Services, communiqué de lancement d'Amazon S3, press.aboutamazon.com, 14 mars 2006 ; AWS News Blog, « Amazon S3 — Bigger and Busier than Ever », 28 janvier 2011 (comptage annuel d'objets) | Ouvert et lu le 2026-09-22 : press.aboutamazon.com/2006/3/amazon-web-services-launches — lancement 14 mars 2006, 0,15 $/Go/mois de stockage, 0,20 $/Go transféré, aucun minimum (F.CLD.A1.003) ; aws.amazon.com/blogs/aws/amazon-s3-bigger-and-busier-than-ever — comptage officiel en fin d'année : 2,9 Md d'objets (2006), 14 Md (2007), 40 Md (2008), 102 Md (2009), 262 Md (2010) (F.CLD.A1.005 ; ancienne valeur « plusieurs milliards » remplacée par le chiffre exact 14 Md). |
| [S11] | off | Amazon Web Services, communiqué de lancement d'Amazon EC2 en version bêta limitée, aws.amazon.com/about-aws/whats-new/2006/08/24 | Ouvert et lu le 2026-09-22 : page officielle « Announcing Amazon Elastic Compute Cloud (Amazon EC2) — beta », datée 24 août 2006 (accès élargi le 25 août) ; capacité redimensionnable facturée à l'usage, provisionnement en quelques minutes. |
| [S13] | presse | Google Press, « Google Launches Hosted Communications Services », googlepress.blogspot.com, 28 août 2006 | Ouvert et lu le 2026-09-22 : googlepress.blogspot.com/2006/08 — lancement de Google Apps for Your Domain le 28 août 2006, édition standard gratuite en bêta (Gmail, Google Talk, Calendar, Page Creator), substitut à l'installation et la maintenance de logiciel/matériel local. |
| [S15] | off | Amazon.com Inc., rapports annuels (Form 10-K, SEC), rubrique « purchases of property and equipment, including internal-use software and website development », exercices 2007 à 2015 ; CIK 0001018724. Chiffres vérifiés sur EDGAR : 224 M$ (2007), 333 M$ (2008), 373 M$ (2009), 979 M$ (2010), 1 811 M$ (2011), 3 785 M$ (2012), 3 444 M$ (2013), ~4,9 Md$ (2014), ~4,6 Md$ (2015). | Série vérifiée directement sur les documents 10-K (accession 0001193125-10-016098 pour 2007-2009, 0001193125-13-028520 pour 2010-2012, 0001018724-14-000006 pour 2013, 0001018724-16-000172 pour 2014-2015). 2013 lu précisément (3 444 M$, en recul sur 2012) ; 2014-2015 lus au format arrondi tel que donné par Amazon dans le MD&A du 10-K FY2015 (« $4.6 billion, $4.9 billion, and $3.4 billion in 2015, 2014, and 2013 »), pas au million près. Le dépassement du reste de l'industrie en 2015 (F.CLD.A1.007) est un constat agrégé sectoriel non vérifiable sur un seul 10-K ; reste `K`. Session du 2026-11-22 : deux recherches (capex des hyperscale selon Synergy ; capex Amazon, Google, Microsoft, Facebook et part du marché des serveurs en 2015), aucune page ouverte ne porte l'énoncé ; les résultats ne donnent que des séries ultérieures (Synergy 2017-2025) et, pour 2015, un extrait de résultat de recherche (page non ouverte, donc non source) rapportant un relevé de Dell'Oro selon lequel les livraisons vers Google et Amazon « paused » et leurs dépenses ont pu baisser ; F.CLD.A1.007 reste `K`. |
| [S17] | livre | Wikipedia, « Alibaba Cloud », https://en.wikipedia.org/wiki/Alibaba_Cloud ; Alibaba Group Holding Ltd., prospectus d'introduction en bourse (Form F-1, SEC, 6 mai 2014, accession 0001193125-14-184994) ; Baidu Inc., rapport annuel (Form 20-F, SEC, exercice 2007, accession 0001145549-08-001006) | Ouvert et lu le 2026-11-22 : Wikipedia (ouvrage de référence en ligne) — Alibaba Cloud « was founded in September 2009 », nom officiel Alibaba Cloud Computing Co. Ltd. (Aliyun), filiale d'Alibaba Group. Pages officielles Alibaba Cloud (alibabacloud.com/about) et Alibaba Group ouvertes : aucune ne donne l'année de fondation (seule mention : « © 2009- »). Relevé d'une session antérieure (2026-09-22), F-1 non rouvert cette session : « In 2009, we established Alibaba Cloud Computing to handle the increasing data management needs on our platform » ; 20-F Baidu (exercice 2007) : ne confirme pas de centres de données propres en 2007, Baidu hébergeait ses serveurs chez des tiers (China Telecom, China Netcom, China Tietong). L'ancien énoncé (2007-2009, centres de données propres des fournisseurs de commerce et de recherche, séparation durable des marchés) n'est pas étayé et a été resserré à la création de la filiale en 2009. |
| [S19] | off | Google, « Introducing Google App Engine + our new blog », cloudplatform.googleblog.com, 7 avril 2008 | Ouvert et lu le 2026-09-22 : billet officiel Google Cloud Platform Blog daté du lundi 7 avril 2008, annonçant la préversion de Google App Engine. |
| [S20] | off | Microsoft, « Microsoft Unveils Windows Azure at Professional Developers Conference », news.microsoft.com/source, 27 octobre 2008 | Ouvert et lu le 2026-09-22 : communiqué officiel Microsoft daté du 27 octobre 2008, keynote de Ray Ozzie au PDC 2008 (Los Angeles), Windows Azure présenté comme socle d'hébergement, de stockage et de calcul en nuage. |
| [S21] | presse | Miller, R., « CapEx, OpEx and Cloudy Accounting », Data Center Knowledge, 12 janvier 2009, https://datacenterknowledge.com/cloud/capex-opex-and-cloudy-accounting ; Armbrust, M. et al., « Above the Clouds: A Berkeley View of Cloud Computing », UC Berkeley, rapport technique UCB/EECS-2009-28, 10 février 2009, https://www2.eecs.berkeley.edu/Pubs/TechRpts/2009/EECS-2009-28.pdf | Ouverts et lus le 2026-11-22. Data Center Knowledge : « Many companies simply don't have access to the borrowing that could support large up-front investments in infrastructure » ; « Others suggest that cloud computing and its pay-as-you-go billing will be a major beneficiary of the economic crisis » ; le technologue Geva Perry est rapporté : « There is nothing inherently financially beneficial in moving an expense from CapEx to OpEx ». Rapport de Berkeley (PDF converti en texte) : « the economic appeal of Cloud Computing is often described as “converting capital expenses to operating expenses” (CapEx to OpEx) », les auteurs préférant la formule « pay as you go ». Channel Insider (Davis, J., 8 décembre 2009) lu aussi : le nuage « add[s] operational expense while eliminating capital expense » (propos attribué à un dirigeant d'Accenture) ; il ne porte aucune clause de l'énoncé. L'ancienne clause (les directions informatiques des grandes entreprises séparent explicitement capital et fonctionnement dès 2008) n'est étayée par aucun document lu ; les documents lus datent de 2009, d'où l'année 2009 ; « grandes entreprises » et le bloc EU retirés. |
| [S22] | stat | Mas, I. et Radcliffe, D., « Mobile Payments Go Viral: M-PESA in Kenya », Bill & Melinda Gates Foundation, document de travail hébergé par la Banque mondiale, mars 2010 (documents1.worldbank.org/curated/en/638851468048259219) | Ouvert et lu le 2026-09-22 : lancement commercial par Safaricom (filiale Vodafone) en mars 2007 ; courbe officielle du nombre d'utilisateurs (Exhibit 2) franchissant environ 2 à 3 millions d'usagers courant 2008 et atteignant 9,0 millions en janvier 2010. |
| [S24] | acad | Ewens, M., Nanda, R. et Rhodes-Kropf, M., « Cost of Experimentation and the Evolution of Venture Capital », NBER Working Paper 24523, avril 2018 (publié au Journal of Financial Economics, 2018), https://www.nber.org/system/files/working_papers/w24523/w24523.pdf ; Blanding, M., « Amazon Web Services Changed the Way VCs Fund Startups », Harvard Business School Working Knowledge, 10 mai 2017, https://www.library.hbs.edu/working-knowledge/amazon-web-services-changed-the-way-vcs-fund-startups | Ouverts et lus le 2026-11-22 (PDF NBER converti en texte). Données VentureSource sur les startups américaines, premiers financements de 2002 à 2010 (période postérieure à 2005 comparée à 2002-2005). « initial funding size fell 20% » pour les secteurs bénéficiaires ; « investment into firms in treated sectors rose from about 375 firms per year to over 700 firms per year », contre environ 350 à 450 dans les secteurs témoins ; secteurs bénéficiaires : « software-as-a-service, social networks, or retail e-commerce websites » ; « Cloud computing allowed startups to ‘rent’ hardware space in small increments and scale up as demand grew, instead of making large fixed upfront investments in hardware ». Les auteurs précisent que l'effet porte sur le coût des premières expériences, non sur le coût total à l'échelle. La page HBS reprend les chiffres 375 et 700. L'ancien énoncé (norme d'amorçage dans les incubateurs, capital initial « effondré ») n'est étayé par aucun passage lu ; retiré. |
| [S26] | acad | DeCandia, G. et al., « Dynamo: Amazon's Highly Available Key-value Store », SOSP, 2007, https://www.allthingsdistributed.com/files/amazon-dynamo-sosp2007.pdf ; Lakshman, A., Malik, P., « Cassandra - A Decentralized Structured Storage System », LADIS, 2009, https://www.cs.cornell.edu/projects/ladis2009/papers/lakshman-ladis2009.pdf | Ouverts et lus (PDF convertis en texte) : Dynamo : « implemented on top of an infrastructure of tens of thousands of servers and network components located in many datacenters around the world. At this scale, small and large components fail continuously », « The system needs to function on a commodity hardware infrastructure » ; Cassandra : « designed to run on cheap commodity hardware », « treats failures as the norm rather than the exception », « designed to fulfill the storage needs of the Inbox Search problem ». Soutenu : la contrainte (machines nombreuses, faillibles, banales) qui commande la conception. Non vérifiable avec les sources ouvertes : « brique courante », « adoption large » et 2009 comme moment où ces bases deviennent courantes ; aucun chiffre d'adoption trouvé. |
| [S27] | off | Commission européenne, communication *Unleashing the Potential of Cloud Computing in Europe*, COM(2012) 529 ; documents nationaux sur les projets de nuage souverain français, 2011-2013 | Reprise de [S27] de la chronologie. Le constat de 2009 reste à sourcer plus précisément : lecture de COM(2012) 529 tentée le 2026-11-22 (miroir du parlement bulgare : page de redirection sans contenu ; EUR-Lex : contenu vide), aucun passage lu ; deux recherches sur l'absence d'un fournisseur européen à l'échelle mondiale n'ont trouvé aucun énoncé daté de 2009 ; F.CLD.A3.006 reste `K`. |
| [S28] | presse | Rackspace Hosting, « Rackspace Announces Plans to Collaborate with NASA on OpenStack Project », PR Newswire, 26 juillet 2010 | Ouvert et lu le 2026-09-22 : communiqué de presse daté du 26 juillet 2010 (Design Summit à Austin 13-16 juillet, annonce publique à l'OSCON de Portland le 21 juillet) ; Rackspace donne le code de Cloud Files/Cloud Servers, projet incorporant la technologie NASA Nebula. |
| [S29] | presse | Facebook, « Facebook to Acquire Instagram », 9 avril 2012, https://about.fb.com/news/2012/04/facebook-to-acquire-instagram/ ; CNBC, 24 septembre 2019, https://www.cnbc.com/2019/09/24/facebook-bought-instagram-because-it-was-scared-of-twitter-and-google.html ; Yahoo Finance Canada, « M&A flashback: Instagram joins Facebook in $1B deal », https://ca.finance.yahoo.com/news/m-flashback-instagram-joins-facebook-050000462.html ; High Scalability, « Instagram Architecture: 14 Million users, Terabytes of Photos, 100s of Instances, Dozens of Technologies », 6 décembre 2011, https://highscalability.com/instagram-architecture-14-million-users-terabytes-of-photos/ | Ouverts et lus le 2026-11-22. Communiqué Facebook : annonce du 9 avril 2012, ni effectif ni nombre d'usagers chiffrés. CNBC (rétrospective) : « a company with only 13 employees ». Yahoo Finance (rétrospective) : « only 13 employees » ; « some 30 million monthly active users » environ 18 mois après le lancement de 2010 ; rachat finalisé le 6 septembre 2012. High Scalability (relais d'un billet de l'équipe technique d'Instagram) : « with just 3 Instaneers, all on the Amazon stack », « 100+ EC2 instances », photos sur Amazon S3, 14 millions d'usagers fin 2011. Page d'ingénierie d'Instagram, CNN Money et NPR : non lues (connexion refusée, 503, délai dépassé). L'ancien énoncé « plusieurs centaines de millions d'usagers » est faux : environ 30 millions au rachat. « Entièrement » retiré, non étayé. |
| [S31] | livre | Loukides, M., What is DevOps?, O'Reilly Media, rapport, 5 juin 2012, notice https://books.apple.com/us/book/what-is-devops/id533505032 ; Leite, L., Rocha, C., Kon, F., Milojicic, D. et Meirelles, P., « A Survey of DevOps Concepts and Challenges », ACM Computing Surveys 52(6), article 127, novembre 2019, https://arxiv.org/abs/1909.05409 | Lus le 2026-11-22. Notice du rapport (page Apple Books ; la page O'Reilly a répondu 403 et le rapport lui-même n'a pas été lu) : « Old-style system administrators may be disappearing in the face of automation and cloud computing » ; « operations have become more significant than ever » ; arrangement « DevOps » où les spécialistes informatiques rejoignent l'équipe de développement ; sortie le 5 juin 2012. Revue de littérature (PDF converti en texte) : avant DevOps, l'interface entre développement et exploitation était « usually a ticket system » gérée à la main ; les opérateurs peuvent ranger leurs scripts d'automatisation dans la gestion de code source, « infrastructure-as-code style » ; les services en nuage « diminishing the need for dedicated operations teams ». Aucun des deux textes ne date de 2010 le basculement : l'année est ramenée à 2012 (date du rapport) et l'énoncé à ce que ces textes disent. Source faible : la notice d'un rapport dont le texte n'a pas été lu. L'ancienne référence (Occupational Outlook Handbook du BLS) n'a pas été ouverte et est retirée de cette entrée. |
| [S32] | off | Mell, P. et Grance, T., *The NIST Definition of Cloud Computing*, NIST Special Publication 800-145, 28 septembre 2011 | Vérifié directement sur nist.gov : titre, auteurs et date de publication (28 septembre 2011) confirmés. |
| [S35] | presse | Gartner, étude du marché mondial des serveurs 2013 (communiqué du 26 février 2014), rapportée par Wilson, D., TechRadar, « Server market grew in 2013, but revenue fell », 26 février 2014, https://techradar.com/news/computing/servers/server-market-grew-in-2013-but-revenue-fell-1228982 | Ouvert et lu le 2026-11-22 : livraisons mondiales 2013 +2,1 %, chiffre d'affaires −4,5 % ; au T4 2013, IBM −28,9 % (de plus de 5 Md$ à 3,6 Md$), Oracle −4,7 %, Dell −0,5 %, HP +6 %, Cisco +34,5 % ; citation de J. Hewitt (Gartner) : « We've seen ongoing growth in Web-scale IT deployments, while the enterprise remained relatively constrained ». La page originale du communiqué Gartner (403) et les 10-K de HP, Dell, IBM et Oracle n'ont pas été lus ; aucune source lue ne date de 2011 un ralentissement durable, d'où l'énoncé ramené à 2013. |
| [S36] | off | Bundesamt für Sicherheit in der Informationstechnik (BSI), page « Kriterienkatalog C5 », https://www.bsi.bund.de/EN/Themen/Unternehmen-und-Organisationen/Informationen-und-Empfehlungen/Empfehlungen-nach-Angriffszielen/Cloud-Computing/Kriterienkatalog-C5/kriterienkatalog-c5.html ; GOV.UK, CESG, collection « Cloud Security Guidance », https://www.gov.uk/government/collections/cloud-security-guidance ; Pépin, G., « Cloud de confiance : l'ANSSI sort son référentiel et lance un label avec l'Allemagne », Next INpact, 13 décembre 2016, https://next.ink/11497/102493-cloud-confiance-anssi-sort-son-referentiel-et-lance-label-avec-allemagne/ | Ouverts et lus le 2026-11-22. BSI : le catalogue C5 « was first published by the Federal Office for Information Security in 2016 », « specifies minimum requirements for secure cloud computing ». GOV.UK : collection du CESG « first published 23 April 2014 », « Guidance for public sector organisations who are considering using cloud services for handling OFFICIAL information » (retirée le 9 juin 2016, contenu déplacé sur le site du NCSC) ; les principes eux-mêmes n'ont pas été lus. Next INpact : appel à candidatures lancé en septembre 2014, expérimentation avec neuf prestataires de mars 2015 à novembre 2016, première partie du référentiel de l'ANSSI publiée le 12 décembre 2016. Pages de l'ANSSI (cyber.gouv.fr, trois adresses) : 404 ou vides, aucune date lue à la source ; la publication de 2016 repose sur la presse. Aucun référentiel lu n'est daté de 2015 : l'année 2015 de l'ancien énoncé est remplacée par 2014-2016 ; « certification » et « producteur de normes d'usage, pas de capacité » retirés (le CESG publie des guides, le BSI un catalogue d'exigences). |
| [S37] | presse | Presse technique contemporaine des lancements de Jenkins, Vagrant et Docker, 2011-2013 ; pour Docker : changelog.com, « Docker from dotCloud is now open source — the future of Linux containers? », 1er avril 2013 | Ouvert et lu le 2026-09-22 (volet Docker uniquement) : billet daté du 1er avril 2013 confirmant la publication open source de Docker (démonstration publique à PyCon mi-mars 2013) et son argument de portabilité (« runs unix processes with strong guarantees of isolation and repeatability across servers »). Volet Jenkins/Vagrant non ouvert cette session. |
| [S38] | presse | TechCrunch, « Microsoft Azure Matches Amazon's Price Cuts And Introduces New "Basic" Tier », 31 mars 2014, https://techcrunch.com/2014/03/31/microsoft-azure-matches-amazons-price-cuts-and-introduces-new-basic-tier | Ouvert et lu le 2026-11-22 : Microsoft, 31 mars 2014, calcul « up to 35 percent », stockage jusqu'à 65 %, prix en vigueur le 1er mai ; Google, 25 mars 2014 (calcul et App Engine plus de 30 %, stockage 68 % d'après le titre lié) ; Amazon, 26 mars 2014, qui a « quickly matched » Google (pourcentages non donnés dans l'article). Les pourcentages de Google et d'Amazon sont lus aussi dans [S60]. L'ancienne clause « structure à trois acteurs disposant seuls de l'échelle » est une interprétation que la source ne porte pas ; retirée. |
| [S39] | presse | Griffith, E., « Who's winning the consumer cloud storage wars? », Fortune, 6 novembre 2014, https://fortune.com/2014/11/06/dropbox-google-drive-microsoft-onedrive/ ; Protalinski, E., « Dropbox passes 400M users », VentureBeat, 24 juin 2015, https://venturebeat.com/business/dropbox-passes-400m-users ; Dropbox, « Thanks for a great 2014 », blog Dropbox, 31 décembre 2014, https://blog.dropbox.com/topics/company/thanks-for-a-great-2014 | Ouverts et lus le 2026-11-22. Fortune : Dropbox « 300 million users » en mai (annonce de Dropbox), Google Drive « 240 million users » en septembre, OneDrive « more than » 250 millions selon Microsoft (sans date) ; iCloud non mentionné. VentureBeat : « Dropbox hit 100 million users in November 2012, 200 million in November 2013, and 300 million in May 2014 ». Blog Dropbox : « more than 300 million people » (31 décembre 2014). Chiffres déclarés par les fournisseurs, de nature différente (comptes ouverts ou usagers actifs) ; iCloud non sourcé. L'ancienne clause sur le déplacement du document et de la photo d'un support local vers un centre distant, et le canal X.CLD.01, n'est portée par aucune page lue ; retirée. |
| [S40] | presse | Muncaster, P., « India's outsourcers battle for customers in a cloudy universe », The Register, 27 mars 2013, https://www.theregister.com/2013/03/27/india_outsourcing_change_cloud_threat/ ; Dobie, A., « India's IT industry: feeling the heat », Information Age, 2 juillet 2013, https://www.information-age.com/?p=28422 | Ouverts et lus le 2026-11-22. The Register, rapportant le rapport Gartner Predicts 2013 (fin 2012) : « globally, cloud-based offerings are estimated to cannibalise up to 15 per cent of top outsourcing players' revenue by 2015 » (prévision, non reprise comme valeur) ; un analyste de Gartner : les prestataires indiens pourraient « integrate and manage a customer's multiple cloud platforms » (« cloud services brokerage »), leur recherche portant sur « integrating the activities buyers need when they move to a cloud delivery model ». Information Age, analyste d'ISG Sid Pai : « IT infrastructure management services are especially vulnerable to disruption by automated systems » ; « There's lots of potential around the cloud [...] But the potential hasn't materialised yet ». Source faible : commentaires d'analystes rapportés par la presse ; aucun rapport de NASSCOM ni document d'entreprise lu. Une réorientation accomplie du secteur en 2012 n'est établie par aucune page lue : l'énoncé est ramené à ce que les analystes disent. Article de Knowledge at Wharton (10 décembre 2012) ouvert : ne traite ni du nuage ni de l'infrastructure ; non utilisé. |
| [S44] | stat | Gartner et IDC, séries de dépense mondiale en services en nuage publics, 2010-2016 | Reprise de [S44] de la chronologie. Chiffres d'analystes, non repris comme valeur ; utilisés uniquement pour dater l'émergence du segment comme catégorie suivie. Étiqueté artefact. |
| [S45] | presse | Kanaracus, C., « GE, Capital One Give AWS the Rub at re:Invent », Constellation Research, 7 octobre 2015, https://www.constellationr.com/content/ge-capital-one-give-aws-rub-reinvent ; O'Neill, J., « Dispatch from Vegas: Capital One places big bet on AWS », Celent, 16 octobre 2015, https://celent.com/insights/652526245 ; Amazon Web Services, étude de cas « Capital One: all in on AWS », https://aws.amazon.com/solutions/case-studies/capital-one-all-in-on-aws/ | Ouverts et lus le 2026-11-22. Constellation Research (7 octobre 2015, compte rendu de la conférence re:Invent) : Capital One « will be down to three by the end of 2018, compared to eight in 2014 » ; GE : 9 000 charges de travail vers AWS en trois ans, empreinte de centres de données de 34 à quatre. Celent (16 octobre 2015) : Capital One « from 8 in 2014 to 5 by 2016, to only 3 by 2018 ». Étude de cas AWS (sans date de publication) : Capital One « exited eight on-premises data centers ». Source faible : deux cabinets d'analystes relayant des keynotes, ni la presse d'origine ni un document des entreprises ; la nature « hors technologie » des deux entreprises n'est pas énoncée par ces pages. L'ancien énoncé (2014, « majorité » de leurs centres, entreprises non nommées) n'est étayé par aucune page lue pour 2014 ; deux recherches de cas de 2014 n'ont donné que des cas de 2015-2016. |
| [S46] | off | Brewer, E. (Google), « An update on container support on Google Cloud Platform », Google Open Source Blog, 11 juin 2014 (reprise ; l'original du blog Google Cloud Platform est daté du 10 juin 2014, date lue), https://opensource.googleblog.com/2014/06/an-update-on-container-support-on.html | Ouvert et lu : « Everything at Google, from Search to Gmail, is packaged and run in a Linux container » ; « Each week we launch more than 2 billion container instances across our global data centers » ; « a lean yet powerful open-source container manager that deploys containers into a fleet of machines » ; « Take a look at the source and documentation on GitHub ». Google est l'un des trois grands exploitants (AWS, Google, Microsoft) nommés par la presse de 2014 citée en [S60]. Non lu : le nom de la licence (absent de l'article). Page GitHub du premier commit : sans date, non utilisée. |
| [S47] | off | Amazon, « Amazon Web Services Announces AWS Lambda », press.aboutamazon.com, 13 novembre 2014 | Ouvert et lu le 2026-09-22 : communiqué officiel daté du 13 novembre 2014 ; facturation « for the requests served and compute time required », par tranches de 100 ms, sans provisionnement de serveur. |
| [S48] | off | Amazon.com Inc., rapport trimestriel (Form 10-Q, SEC), premier trimestre 2015, première publication séparée du segment Amazon Web Services ; accession 0001018724-15-000038 | Vérifié directement sur EDGAR : chiffre d'affaires AWS 1 566 M$ (T1 2015) contre 1 050 M$ (T1 2014), résultat d'exploitation 265 M$ (T1 2015) contre 245 M$ (T1 2014). |
| [S51] | off | U.S. Environmental Protection Agency, ENERGY STAR Program, *Report to Congress on Server and Data Center Energy Efficiency, Public Law 109-431*, 2 août 2007 | Reprise de [S51] de la chronologie, déjà vérifié à la source (61 TWh en 2006, 1,5 %, 4,5 Md$, doublement depuis 2000). |
| [S59] | presse | Miller, R., « Facebook Goes Global With Data Center in Sweden », Data Center Knowledge, 27 octobre 2011, https://datacenterknowledge.com/energy-power-supply/facebook-goes-global-with-data-center-in-sweden | Ouvert et lu le 2026-11-22 : article du jour de l'annonce, 27 octobre 2011 ; Luleå, « seaside town of 45,000 » dans le nord de la Suède ; porte-parole : « The cool, dry climate will allow us to continue our practice of using outside air to cool our data centers » ; « powered primarily by renewable energy » (hydroélectricité du fleuve Lule, environ 10 % de la demande électrique suédoise), des autorités indiquant des tarifs parmi les plus bas d'Europe. Rien lu sur l'Islande ni la Finlande : clause retirée. La phrase « la géographie de l'usine suit désormais l'énergie » est une interprétation que l'article ne porte pas ; retirée. |
| [S60] | presse | Vogels, W., All Things Distributed, 5 mars 2012, https://allthingsdistributed.com/2012/03/ec2-price-reduction.html ; TechCrunch, 21 janvier 2014, https://techcrunch.com/2014/01/21/amazon-drops-s3-prices-by-up-to-22-ebs-by-up-to-50-launches-new-ec2-instance-types/ ; TechCrunch, 25 mars 2014, https://techcrunch.com/2014/03/25/google-drops-prices-for-compute-and-app-engine-by-over-30-cloud-storage-by-68-introduces-sustained-use-discounts ; TechCrunch, 26 mars 2014, https://techcrunch.com/2014/03/26/in-response-to-google-amazon-announces-massive-price-cuts-for-s3-ec2-and-rds ; Fortune, 18 mai 2015, https://fortune.com/2015/05/18/google-cloud-price-cuts/ | Ouverts et lus (WebFetch) : blog du directeur technique d'Amazon (2012, source propre du fournisseur) : baisse de prix de 6 % pour m1.small à la demande ; TechCrunch : janvier 2014, stockage de plus de 5 000 To -22 %, EBS jusqu'à -50 % ; 25 mars 2014, Google Compute Engine -32 %, stockage -68 % ; 26 mars 2014, Amazon -36 % à -65 % au total, instances EC2 jusqu'à -40 %, en vigueur le 1er avril ; Fortune, mai 2015 : Google annonce des baisses de 40 % pour de nombreux calculs. Plusieurs baisses la même année (trois en 2014) et plusieurs fournisseurs. Niveau admis : 2014 et 2015 reposent sur la presse, seul 2012 sur la page du fournisseur. Non lu : « sans changement de contrat » (page AWS Price Reduction #42 tronquée par l'outil, clause retirée). Un article InfoQ du 29 mars 2014 (« 42nd cut since 2008 », secondaire) n'a servi que de recoupement. |
| [S61] | presse | Computerworld (IDG News Service), « French sovereign wealth funds invests in two local cloud computing providers », 6 septembre 2012, https://www.computerworld.com/article/1420282/french-sovereign-wealth-funds-invests-in-two-local-cloud-computing-providers.html ; Le Monde Informatique, « Cloud souverain : Fleur Pellerin défend les choix du précédent gouvernement », 4 octobre 2012, https://www.lemondeinformatique.fr/actualites/lire-cloud-souverain-fleur-pellerin-defend-les-choix-du-precedent-gouvernement-50709.html | Ouverts et lus le 2026-11-22. Computerworld : Numergy et Cloudwatt lancés début septembre 2012 ; la Caisse des dépôts (fonds souverain français) investit dans les deux et détient 33,33 % de Cloudwatt, dont l'investissement total est de 225 M€, « the same as Numergy's » ; le gouvernement détient des participations minoritaires chez les autres investisseurs ; argument avancé : garder les données en France, à l'abri des juridictions étrangères et du Patriot Act. Le Monde Informatique : deux projets français de « cloud souverain », « le gouvernement, via la Caisse des dépôts, finance les deux projets », « nés avec le gouvernement précédent » (date d'annonce et montants non donnés). Non lu : date d'annonce des projets, résultat des projets ; les clauses « en réponse au constat de 2009 » et « documente la difficulté de rattraper une industrie d'échelle » de l'ancien énoncé n'ont aucun appui lu et sont retirées. |
| [S62] | presse | Gartner, prévision « Forecast Overview: Public Cloud Services, Worldwide, 2011-2016, 4Q12 Update », communiqué de février-mars 2013, reproduit par StorageNewsletter, « WW Public Cloud Services Market at $131 Billion in 2013 – Gartner », 6 mars 2013, https://www.storagenewsletter.com/2013/03/06/ww-public-cloud-services-gartner | Ouvert et lu le 2026-11-22 : Gartner présente « the public cloud services market » comme un marché distinct, 131 Md$ prévus en 2013 contre 111 Md$ en 2012 (+18,5 %), découpé en publicité en nuage (48 % en 2012), BPaaS (28 %), SaaS (14,7 %), IaaS (5,5 %), gestion et sécurité (2,8 %), PaaS (1 %). Chiffres de cabinet : non repris comme valeur, artefact de mesure. Page originale Gartner non ouverte ; la reproduction est une édition du communiqué par un site de presse spécialisée. L'ancienne clause « atteint une taille où » est une interprétation non portée par la source ; retirée. |
| [S63] | acad | Brooks, D. C., The Changing Face of IT Service Delivery in Higher Education, EDUCAUSE Center for Analysis and Research (ECAR), Louisville (Colorado), août 2015, https://library.educause.edu/~/media/files/library/2015/5/ers1501b.pdf | Ouvert et lu le 2026-11-22 (PDF converti en texte). Enquête auprès de directeurs informatiques, 230 répondants ; échelle de 0 (« managing infrastructure and technical resources ») à 100 (« managing vendors, services, and outsourced contracts ») : aujourd'hui centrée sur l'infrastructure, « in the next five years, CIOs expect a significant shift toward the vendor, services, and outsourcing management end of the spectrum », décalage plus fort à dix ans. Postes en croissance liés aux projets en nuage : spécialistes d'intégration de données, de sécurité et de vie privée, juristes, négociateurs de contrats, gestionnaires de fournisseurs. Limites : enseignement supérieur seulement ; pays des répondants non indiqué (rapport publié par une association basée aux États-Unis). Rien lu sur les coûts variables : clause retirée. L'ancienne référence [S31] (BLS) n'a pas été ouverte. |
| [S64] | presse | Merkel, D., « Docker: Lightweight Linux Containers for Consistent Development and Deployment », Linux Journal, 19 mai 2014, https://www.linuxjournal.com/content/docker-lightweight-linux-containers-consistent-development-and-deployment | Ouvert et lu le 2026-11-22. Docker « started life as an open-source project at dotCloud » début 2013 ; objectif : empaqueter une application avec ses dépendances pour qu'elle fonctionne dans des environnements de développement, de test et de production distincts ; « If both systems run Docker, the same container will execute without issues » ; au moment de l'article, version 0.7.x, Docker « still not officially production-ready ». Ne dit rien de la livraison continue ni du rythme de mise en production : la clause « du trimestre à la journée » n'a aucun appui lu et est retirée ; l'année passe de 2011 à 2013. |
