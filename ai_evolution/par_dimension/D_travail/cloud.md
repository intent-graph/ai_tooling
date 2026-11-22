# D. Travail et emploi — Cloud 2005-2015

Ce que le travail a connu pendant la fenêtre du choc cloud, sous-dimension par sous-dimension :
faits sourcés, jalons cités, trajectoire année par année, narratif court. Le travail est le
domaine le plus pauvre en jalons des deux chronologies : trois jalons sur soixante-seize pour
cette fenêtre, tous centrés sur les métiers informatiques (`J.CLD.2007.03`, `J.CLD.2010.06`,
`J.CLD.2015.06`). Le changement s'y lit en **tendance mesurée**, pas en événement ; cette cellule
compense par des séries chiffrées ce que les jalons ne captent pas. Ligne de base : état des deux
années précédant 2005. La crise financière de 2008 (`X.CLD.03`) est un confondant massif sur tout
le domaine : presque tout mouvement d'emploi 2008-2010 lui doit une part, et l'attribution en
tient compte systématiquement. La comparaison avec l'autre choc est dans le `README.md` du
domaine, pas ici.

## Table of Contents

1. [D1 Volume et structure de l'emploi](#d1-volume-et-structure-de-lemploi) _(Lines 44-46)_
   1. [Faits](#faits) _(Lines 49-62)_
   1. [Jalons cités](#jalons-cités) _(Lines 65-69)_
   1. [Trajectoire `T.CLD.D1`](#trajectoire-tcldd1) _(Lines 72-87)_
   1. [Narratif](#narratif) _(Lines 90-112)_
1. [D2 Métiers, compétences et formation](#d2-métiers-compétences-et-formation) _(Lines 115-118)_
   1. [Faits](#faits-1) _(Lines 121-134)_
   1. [Jalons cités](#jalons-cités-1) _(Lines 137-142)_
   1. [Trajectoire `T.CLD.D2`](#trajectoire-tcldd2) _(Lines 145-160)_
   1. [Narratif](#narratif-1) _(Lines 163-183)_
1. [D3 Organisation du travail](#d3-organisation-du-travail) _(Lines 186-188)_
   1. [Faits](#faits-2) _(Lines 191-203)_
   1. [Jalons cités](#jalons-cités-2) _(Lines 206-211)_
   1. [Trajectoire `T.CLD.D3`](#trajectoire-tcldd3) _(Lines 214-229)_
   1. [Narratif](#narratif-2) _(Lines 232-253)_
1. [D4 Salaires, polarisation et rapport de force](#d4-salaires-polarisation-et-rapport-de-force) _(Lines 256-258)_
   1. [Faits](#faits-3) _(Lines 261-272)_
   1. [Jalons cités](#jalons-cités-3) _(Lines 275-280)_
   1. [Trajectoire `T.CLD.D4`](#trajectoire-tcldd4) _(Lines 283-298)_
   1. [Narratif](#narratif-3) _(Lines 301-321)_
1. [Sources](#sources) _(Lines 324-357)_



---

## D1 Volume et structure de l'emploi
<!-- Lines 44-46 -->

**Question :** Combien d'emplois créés, détruits, déplacés, dans quels secteurs, à quel rythme ?

### Faits
<!-- Lines 49-62 -->

| id | année | bloc | énoncé | valeur | acteurs | attribution | source | statut |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| F.CLD.D1.001 | 2003-2004 | US | Avant t0 : l'emploi dans les professions informatiques croît sur une base restreinte à la sortie de la correction du début des années 2000 (X.INT.05), effectifs très inférieurs au pic de 2000-2001. | effectifs en deçà du pic 2000-2001 | M1 | exo | [S1] | K |
| F.CLD.D1.002 | 2003, 2005, 2008, 2009, 2010, 2015, 2016 | US | Série annuelle d'emploi du secteur des services informatiques (NAICS 5415, « Computer Systems Design and Related Services »), U.S. Bureau of Labor Statistics : croissance quasi continue sur la fenêtre, y compris pendant la crise, avec un seul recul net en 2009. | 1 291 800 (2003) ; 1 368 600 (2005) ; 1 611 400 (2008) ; 1 586 400 (2009) ; 1 610 200 (2010) ; 2 043 400 (2015) ; 2 153 700 (2016) | M1, O2, O4 | choc | [S1] | V |
| F.CLD.D1.003 | 2003, 2005, 2008, 2009, 2010, 2015 | US | Série annuelle d'emploi du sous-secteur du traitement de données et de l'hébergement (NAICS 518, « Data Processing, Hosting, and Related Services »), U.S. Bureau of Labor Statistics : recul de l'emploi entre 2003 et 2010 malgré la construction massive de centres de données (A1), puis reprise modérée jusqu'en 2015, sans jamais retrouver l'échelle du secteur des services informatiques au sens large. | 288 600 (2003) ; 265 300 (2005) ; 262 100 (2008) ; 252 500 (2009) ; 248 000 (2010, creux de la fenêtre) ; 300 100 (2015) | M1 | choc | [S2] | V |
| F.CLD.D1.004 | 2008-2011 | US | Le taux de chômage des professions informatiques et mathématiques passe de 2,6 % en 2008 à 5,2 % en 2009 et en 2010, puis à 4,1 % en 2011, et reste chaque année inférieur au taux de chômage de l'ensemble des actifs américains. | 2,6 % (2008) ; 5,2 % (2009) ; 5,2 % (2010) ; 4,1 % (2011), contre 5,8 % ; 9,3 % ; 9,6 % ; 8,9 % pour l'ensemble | M1 | co:X.CLD.03 | [S24] | V |
| F.CLD.D1.005 | 2003, 2005, 2007, 2009, 2010, 2015 | US | Série annuelle d'emploi à temps plein des développeurs de logiciels (salariés, 16 ans et plus), Current Population Survey, U.S. Bureau of Labor Statistics : quasi-doublement des effectifs sur la fenêtre, croissance plus rapide que celle de l'ensemble des professions informatiques et mathématiques sur la même période. | 701 000 (2003) ; 778 000 (2005) ; 872 000 (2007) ; 902 000 (2009) ; 973 000 (2010) ; 1 287 000 (2015) | M1 | choc | [S20] | V |
| F.CLD.D1.006 | 2013 | US | Un grand centre de données peut occuper des milliers d'ouvriers du bâtiment pendant un à deux ans de construction, mais son personnel d'exploitation se compte en général en quelques dizaines de salariés ; pour le site d'un grand réseau social à Prineville (Oregon), une étude commandée par l'entreprise chiffre à environ 650 les emplois de construction dans le centre de l'Oregon sur cinq ans, et à plus de 200 les emplois hors construction en 2013. | cas général : milliers d'ouvriers pendant 1 à 2 ans ; exploitation : quelques dizaines de salariés ; Prineville : ~650 emplois de construction sur 5 ans, plus de 200 emplois hors construction (2013) | M1, M7, O2 | choc | [S26] | A |
| F.CLD.D1.007 | 2008-2012 | EMERG | Série annuelle des effectifs employés dans les métiers qualifiés du secteur indien IT-BPO (services informatiques, exportations, marché domestique), reprise d'une étude académique citant le Strategic Review 2012 de l'association professionnelle du secteur : croissance continue sur la période malgré la crise financière mondiale, sans rupture de tendance attribuable à une automatisation de l'exploitation. | 1 962 000 (2008) ; 2 196 000 (2009) ; 2 300 000 (2010) ; 2 540 000 (2011) ; 2 770 000 (2012, estimation) | M1, T5 | co:X.CLD.03 | [S21] | V |
| F.CLD.D1.008 | 2003, 2005, 2009, 2015 | US | Au creux de la récession consécutive à la crise financière (2009), l'emploi des services informatiques (NAICS 5415) recule de 1,5 % par rapport à 2008 quand l'emploi salarié total américain recule beaucoup plus fortement sur la même période, ce qui est cohérent avec un secteur en croissance structurelle amorti par un choc exogène plutôt que retourné par lui. | recul NAICS 5415 : 1 611 400 (2008) à 1 586 400 (2009), soit -1,5 % | M1 | co:X.CLD.03 | [S1] | V |
| F.CLD.D1.009 | 2005-2015 | US | Série annuelle d'emploi du sous-secteur du commerce électronique et de la vente par correspondance (NAICS 4541, « Electronic Shopping and Mail-Order Houses »), U.S. Bureau of Labor Statistics : l'emploi passe de 283 600 en 2005 à 377 000 en 2015, avec un recul en 2006 puis en 2009 ; la série ne sépare pas la part due à l'infrastructure en nuage de celle due à la vente en ligne elle-même (produit dérivé, X.CLD.01 en partie). | 239 300 (2003) ; 283 600 (2005) ; 266 300 (2006) ; 263 800 (2009) ; 269 500 (2010) ; 377 000 (2015) | M1, M7, O2 | co:X.CLD.01 | [S25] | V |
| F.CLD.D1.010 | 2012 | EMERG | Le secteur indien IT-BPO emploie directement 2,8 millions de professionnels et génère 8,9 millions d'emplois indirects selon l'association professionnelle du secteur (Strategic Review 2012), soit un total de 11,7 millions ; aucune série officielle unifiée de comptage mondial des emplois créés directement par l'industrie des centres de données proprement dite (hors sous-traitance de services) n'a été identifiée sur la fenêtre. | 2,8 M emplois directs, 8,9 M indirects, 11,7 M au total (secteur IT-BPO indien, 2012) | M1, T5 | choc | [S21] | V |

### Jalons cités
<!-- Lines 65-69 -->

Aucun jalon de `par_annee/cloud_2005_2015.md` ne porte spécifiquement sur le volume d'emploi
(D1) ; le jalon le plus proche, `J.CLD.2008.01` (crise financière), sert de repère de rupture de
ligne de base plutôt que de bascule propre à D1.

### Trajectoire `T.CLD.D1`
<!-- Lines 72-87 -->

| année | phase | intensité | ce qui change | faits et jalons |
| --- | --- | --- | --- | --- |
| avant t0 | latent | 1 | Emploi informatique en reconstitution après la correction du début des années 2000 ; le sous-secteur hébergement et traitement de données recule déjà depuis 2001-2002. | F.CLD.D1.001, F.CLD.D1.002, F.CLD.D1.003 |
| 2005 | émergence | 1 | Croissance de l'emploi des services informatiques (1,37 M) ; l'hébergement et le traitement de données poursuivent leur recul (265 300) malgré les premiers services facturés à l'usage. | F.CLD.D1.002, F.CLD.D1.003 |
| 2006 | émergence | 1 | Poursuite de la croissance sectorielle (NAICS 5415), sans rupture documentée cette année pour D1. | F.CLD.D1.002 |
| 2007 | accélération | 1 | Premiers cursus et recherches en calcul distribué, signe d'une demande de compétence naissante en amont de l'emploi ; l'emploi des services informatiques atteint 1,54 M, celui des développeurs 872 000. | J.CLD.2007.03, F.CLD.D1.005 |
| 2008 | crise | 2 | La crise financière (X.CLD.03) casse la ligne de base de l'emploi total américain ; l'emploi des services informatiques atteint son pic pré-recul à 1,61 M. | J.CLD.2008.01, F.CLD.D1.002 |
| 2009 | crise | 2 | Creux de la récession : recul limité de -1,5 % de l'emploi des services informatiques (1,59 M), recul plus marqué du sous-secteur hébergement (252 500) ; chômage informatique en hausse mais sous la moyenne nationale. | F.CLD.D1.008, F.CLD.D1.004 |
| 2010 | accélération | 2 | Point bas du sous-secteur hébergement et traitement de données (248 000) alors que les services informatiques ont déjà dépassé leur niveau de 2008 (1,61 M) ; le métier d'administrateur système bascule vers le code de configuration. | J.CLD.2010.06, F.CLD.D1.002, F.CLD.D1.003, F.CLD.D1.005 |
| 2011 | accélération | 1 | Poursuite de la croissance de l'emploi des services informatiques ; reprise du sous-secteur hébergement. | F.CLD.D1.002, F.CLD.D1.003 |
| 2012 | consolidation | 1 | La sous-traitance indienne se réoriente sectoriellement (voir A5, F.CLD.A5.005) tout en continuant de croître en effectifs (2,77 M direct estimé, 11,7 M avec l'emploi indirect). | F.CLD.D1.007, F.CLD.D1.010 |
| 2013 | consolidation | 1 | Poursuite de la croissance de l'emploi des services informatiques ; un site de centre de données d'un grand réseau social compte plus de 200 emplois hors construction, pour environ 650 emplois de construction sur cinq ans. | F.CLD.D1.002, F.CLD.D1.006 |
| 2014 | consolidation | 1 | Poursuite de la croissance sectorielle, sans bascule nouvelle documentée pour D1. | F.CLD.D1.002 |
| 2015 | banalisation | 2 | Écart de trajectoire confirmé entre développeurs (1,29 M, quasi-doublement depuis 2003) et le sous-secteur hébergement (300 000, retour au-dessus du niveau de 2008 seulement). | F.CLD.D1.005, F.CLD.D1.003 |

### Narratif
<!-- Lines 90-112 -->

L'emploi informatique américain part d'une base restreinte par la correction du début des années
2000 [F.CLD.D1.001] et croît de façon continue sur la fenêtre dans les services informatiques au
sens large, de 1,37 million en 2005 à 2,04 millions en 2015, avec un seul recul net de 1,5 % en
2009 [F.CLD.D1.002, F.CLD.D1.008]. Le sous-secteur de l'hébergement et du traitement de données au
sens strict suit une trajectoire inverse et contre-intuitive : son emploi recule de 265 300 en 2005
à un creux de 248 000 en 2010, précisément les années de construction massive des centres de
données (A1), avant de ne remonter qu'à 300 100 en 2015, ce qui contredit l'image d'une industrie
de centres de données massivement employeuse [F.CLD.D1.003]. Un fait notable complémentaire : la
construction d'un grand centre de données peut occuper des milliers d'ouvriers pendant un à deux
ans, alors que son personnel d'exploitation se compte en quelques dizaines de salariés ; sur un site
d'Oregon, une étude chiffre à plus de 200 les emplois hors construction en 2013 [F.CLD.D1.006]. Les
développeurs de logiciels, eux, voient leurs effectifs presque doubler sur la fenêtre, de 701 000
en 2003 à 1,29 million en 2015, croissance plus rapide que celle du sous-secteur d'exploitation, ce
qui traduit la bascule du métier vers le code de configuration [J.CLD.2010.06, F.CLD.D1.005]. La
sous-traitance indienne IT-BPO continue de croître en effectifs sur toute la fenêtre malgré la
crise financière mondiale, de 1,96 million en 2008 à 2,77 millions estimés en 2012 pour l'emploi
direct, et jusqu'à 11,7 millions en comptant l'emploi indirect [F.CLD.D1.007, F.CLD.D1.010], sans
signe net d'un effet de substitution par l'automatisation de l'exploitation documenté sur la
fenêtre.

---

## D2 Métiers, compétences et formation
<!-- Lines 115-118 -->

**Question :** Quels métiers apparaissent, disparaissent, se transforment ; quelles compétences
sont demandées ; comment on se forme ?

### Faits
<!-- Lines 121-134 -->

| id | année | bloc | énoncé | valeur | acteurs | attribution | source | statut |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| F.CLD.D2.001 | 2003-04, 2004-05, 2005-06, 2006-07, 2007-08, 2008-09, 2009-10, 2010-11, 2011-12, 2012-13, 2013-14, 2014-15 | US | Série des diplômes conférés en sciences informatiques et de l'information (tous niveaux confondus, licence à doctorat), National Center for Education Statistics, IPEDS : recul continu de 2003-04 à 2009-10, puis reprise continue jusqu'à retrouver quasiment le niveau de départ en 2014-15. | 2003-04 : ~59 500 (total tous niveaux, dont 59 488 en licence) ; creux 2008-09 : 37 992 (licence) ; 2014-15 : 59 581 (licence), niveau proche de 2003-04 | M1, P2 | co:X.INT.05 | [S6] | V |
| F.CLD.D2.002 | 2007 | US | Le 8 octobre 2007, Google et IBM annoncent une initiative qui met des centaines de processeurs à la disposition d'universités américaines (dont Washington, Carnegie Mellon, MIT, Stanford, Berkeley, Maryland) pour des cours de programmation à très grande échelle, issue d'un cours pilote de l'université de Washington, que celle-ci présente comme les premiers cours de programmation à l'échelle d'Internet. | centaines de processeurs mis à disposition (octobre 2007) | M1, O7 | choc | [S7] | A |
| F.CLD.D2.003 | 2003, 2009 | US, MONDE | Le premier devopsdays, rencontre consacrée au rapprochement des équipes de développement et d'exploitation, se tient à Gand (Belgique) en 2009, et le terme « DevOps » s'en répand ; chez Google, l'ingénierie de fiabilité des sites (SRE) est décrite par son fondateur, entré dans l'entreprise en 2003 pour diriger une équipe de production de sept ingénieurs, comme ce qui arrive quand on demande à un ingénieur logiciel de concevoir une équipe d'exploitation. | premier devopsdays : Gand, 2009 ; équipe de production de 7 ingénieurs chez Google en 2003 | M1 | choc | [S27] | A |
| F.CLD.D2.004 | 2013 | US | Le 30 avril 2013, Amazon Web Services lance un programme de certifications par rôle dont le premier examen est « AWS Certified Solutions Architect – Associate Level ». | 30 avril 2013 | M1 | choc | [S9] | V |
| F.CLD.D2.005 | 2013 | US | Le communiqué de lancement du programme de certification d'Amazon Web Services annonce pour la suite de 2013 d'autres certifications par rôle, dont administrateur systèmes (SysOps) et développeur, passées dans des centres de test de plus de 100 pays et de 750 sites ; il ne donne aucun nombre de certifiés. | examens en centres de test : plus de 100 pays, 750 sites ; nombre de certifiés non communiqué | M1 | choc | [S9] | V |
| F.CLD.D2.006 | 2005-2009 | US, EU | Avec la croissance de l'informatique en nuage, la configuration des systèmes est de plus en plus décrite dans un langage déclaratif et traitée comme du logiciel (versionnée, déployée automatiquement) plutôt que saisie à la main (« infrastructure as code »), avec des outils comme Puppet (2005) et Chef (2009) ; aucune source lue ne mesure ce que ce mouvement change au métier d'administrateur système. | outils : Puppet (2005), Chef (2009) | M1 | choc | [S28] | A |
| F.CLD.D2.007 | 2006-2016 | US | Le Bureau of Labor Statistics projette pour 2006-2016 un recul de 24,7 % de l'emploi des opérateurs informatiques (« computer operators »), qu'il attribue à l'usage croissant de logiciels qui automatisent l'exploitation ; aucune source lue ne relie ce recul à la migration vers des services loués. | -24,7 % (projection 2006-2016) | M1 | choc | [S29] | A |
| F.CLD.D2.008 | 2008-2012 | US, MONDE | Le terme « MOOC » est forgé en 2008 pour un cours en ligne ouvert, « Connectivism and Connective Knowledge » ; à l'automne 2011, l'université Stanford lance trois cours en ligne ouverts, dont un réunit 160 000 inscrits ; en juin 2012, plus de 1,5 million de personnes se sont inscrites à des cours d'Udacity, de Coursera ou d'edX. | 160 000 inscrits (premier cours Stanford, automne 2011) ; plus de 1,5 million d'inscrits (juin 2012) | M1, P2, P3 | co:X.CLD.06 | [S10] | A |
| F.CLD.D2.009 | 2014-2015 | US | Selon un fournisseur de supervision d'infrastructure, sur un échantillon de 7 000 de ses clientes (qui tendent à être des adoptantes précoces), la part ayant adopté Docker passe de 1,8 % début septembre 2014 à 8,3 % un an plus tard, et la part ayant essayé Docker est de 11 %, 28 % et 56 % selon que l'infrastructure compte 1 à 99, 100 à 499, 500 hôtes ou plus. | 1,8 % (09/2014) → 8,3 % (09/2015) des clientes de l'échantillon ; essai de Docker : 11 % (1-99 hôtes), 28 % (100-499), 56 % (500 et plus) | M1 | choc | [S22] | A |
| F.CLD.D2.010 | 2003-2004 | US | Avant t0 : la compétence recherchée dans les métiers informatiques reste centrée sur l'administration de matériel possédé et de réseaux internes, la certification de référence portant sur les systèmes d'exploitation et le matériel réseau plutôt que sur des services loués. | — | M1 | exo | [S3] | K |

### Jalons cités
<!-- Lines 137-142 -->

`J.CLD.2007.03` (premiers cursus et recherches sur le calcul distribué à très grande échelle),
`J.CLD.2010.06` (bascule du métier d'administrateur système vers le code de configuration),
`J.CLD.2015.06` (réorientation du métier de direction informatique vers la gestion de
fournisseurs).

### Trajectoire `T.CLD.D2`
<!-- Lines 145-160 -->

| année | phase | intensité | ce qui change | faits et jalons |
| --- | --- | --- | --- | --- |
| avant t0 | latent | 1 | Compétence centrée sur le matériel et le réseau possédés ; recul des inscriptions en informatique déjà entamé depuis le pic de 2003-04. | F.CLD.D2.010, F.CLD.D2.001 |
| 2005 | émergence | 0 | Poursuite du recul des diplômes informatiques, sans bascule de métier nouvelle documentée. | F.CLD.D2.001 |
| 2006 | émergence | 0 | Poursuite du recul des diplômes ; aucune bascule de métier nouvelle documentée. | F.CLD.D2.001 |
| 2007 | accélération | 2 | Google et IBM annoncent en octobre une initiative qui met des centaines de processeurs à la disposition d'universités américaines pour des cours de programmation à très grande échelle. | F.CLD.D2.002, J.CLD.2007.03 |
| 2008 | crise | 1 | Creux des diplômes informatiques proche du plancher de la décennie, en pleine crise financière ; le terme « MOOC » est forgé pour un premier cours ouvert en ligne. | F.CLD.D2.001, F.CLD.D2.008 |
| 2009 | crise | 2 | Point bas des diplômes ; premier devopsdays à Gand, d'où le terme « DevOps » se répand. | F.CLD.D2.001, F.CLD.D2.003 |
| 2010 | accélération | 3 | Reprise des inscriptions en informatique ; la configuration des systèmes tend à être traitée comme du code (outils Puppet, 2005, et Chef, 2009). | F.CLD.D2.001, F.CLD.D2.006, J.CLD.2010.06 |
| 2011 | accélération | 2 | Stanford lance à l'automne trois cours en ligne ouverts ; l'emploi des opérateurs informatiques est projeté en recul de 24,7 % sur 2006-2016. | F.CLD.D2.007, F.CLD.D2.008 |
| 2012 | consolidation | 1 | Plus de 1,5 million d'inscrits à des cours d'Udacity, de Coursera ou d'edX en juin. | F.CLD.D2.008 |
| 2013 | consolidation | 1 | Poursuite de la reprise des diplômes informatiques ; Amazon Web Services lance en avril son programme de certifications par rôle. | F.CLD.D2.001, F.CLD.D2.004, F.CLD.D2.005 |
| 2014 | consolidation | 2 | Poursuite de la reprise des diplômes ; début de la mesure de l'adoption de Docker parmi les clientes d'un fournisseur de supervision, encore marginale à cette date (1,8 %). | F.CLD.D2.001, F.CLD.D2.009 |
| 2015 | banalisation | 3 | Les diplômes informatiques retrouvent quasiment leur niveau de 2003-04 ; la part des clientes d'un fournisseur de supervision ayant adopté Docker atteint 8,3 % en septembre ; la direction informatique devient un métier de gestion de fournisseurs. | F.CLD.D2.001, F.CLD.D2.009, J.CLD.2015.06 |

### Narratif
<!-- Lines 163-183 -->

Les diplômes universitaires en informatique reculent de 2003-04 à 2009-10 avant de regagner sur
cinq ans presque tout le terrain perdu, mouvement en U qui traverse toute la fenêtre du choc
cloud sans lui être entièrement imputable puisqu'il commence avant t0, dans le prolongement de la
correction du début des années 2000 [F.CLD.D2.001]. La formation et le vocabulaire des
métiers évoluent par étapes : en octobre 2007, Google et IBM équipent des universités américaines
pour des cours de programmation à très grande échelle [F.CLD.D2.002, J.CLD.2007.03] ; le premier
devopsdays se tient à Gand en 2009, d'où se répand le terme « DevOps » [F.CLD.D2.003] ; en avril
2013, Amazon Web Services lance des certifications par rôle, dont un examen d'architecte de
solutions [F.CLD.D2.004, F.CLD.D2.005]. La configuration des systèmes est de plus en plus traitée
comme du code, avec des outils comme Puppet et Chef, sans qu'aucune source lue mesure ce que cela
change au métier d'administrateur système [F.CLD.D2.006, J.CLD.2010.06]. Le Bureau of Labor
Statistics projette pour 2006-2016 un recul de 24,7 % de l'emploi des opérateurs informatiques,
qu'il attribue à des logiciels qui automatisent l'exploitation [F.CLD.D2.007]. Les cours en ligne
ouverts à grande échelle prennent de l'ampleur à partir de l'automne 2011 et réunissent plus de
1,5 million d'inscrits en juin 2012 [F.CLD.D2.008]. En fin de fenêtre, selon un fournisseur de
supervision, la part de ses clientes ayant adopté Docker passe de 1,8 % à 8,3 % en un an, sur un
échantillon de 7 000 entreprises qui tendent à être des adoptantes précoces [F.CLD.D2.009].

---

## D3 Organisation du travail
<!-- Lines 186-188 -->

**Question :** Où, quand, avec quels outils et sous quel statut travaille-t-on ?

### Faits
<!-- Lines 191-203 -->

| id | année | bloc | énoncé | valeur | acteurs | attribution | source | statut |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| F.CLD.D3.001 | 2005 | US | Lors du premier financement en capital-risque d'un service de partage vidéo, fin 2005, l'entreprise ne compte que ses trois fondateurs, qui travaillent dans un garage ; le service s'appuie alors sur un hébergeur tiers offrant une bande passante illimitée, avant de passer plus tard à ses propres centres de données. | 3 personnes (fin 2005) | M1, O1 | choc | [S11] | A |
| F.CLD.D3.002 | 2012 | MONDE | Au moment de l'annonce de son rachat par un grand réseau social, en avril 2012, une application de partage de photographies grand public compte 13 employés et plus de 25 millions d'usagers, et son infrastructure est hébergée chez un fournisseur de nuage public (Amazon Web Services). | 13 employés ; plus de 25 millions d'usagers | M1, O1 | choc | [S12] | A |
| F.CLD.D3.003 | 2003-2015 | US | Aux États-Unis, la part des personnes en emploi qui font tout ou partie de leur travail à leur domicile les jours où elles travaillent passe de 19 % en 2003 à 24 % en 2015 selon l'American Time Use Survey, et la part des travailleurs qui travaillent chez eux la majeure partie de la semaine passe de 3,6 % en 2005 à 4,3 % en 2010 selon l'American Community Survey ; en juillet 2012, Google déclare, selon Fortune, que cinq millions d'entreprises utilisent désormais son service de courriel. | 19 % (2003) → 24 % (2015) ; 3,6 % (2005) → 4,3 % (2010) ; 5 millions d'entreprises (2012, déclaration de l'éditeur) | M1, M4, P3 | choc | [S13] | A |
| F.CLD.D3.004 | 2008-2015 | US | Une plateforme de location de logements entre particuliers, qui commence à fonctionner en 2008, migre presque toutes ses fonctions informatiques chez un fournisseur de nuage public un an après son lancement et y utilise, selon l'étude de cas du fournisseur, 200 instances de calcul pour ses serveurs d'application, de cache et de recherche ; fin 2015, les travailleurs qui offrent leurs services par des intermédiaires en ligne (plateformes de transport ou de tâches à la demande) représentent 0,5 % de l'ensemble des travailleurs américains. | 0,5 % des travailleurs américains (fin 2015) ; 200 instances de calcul (étude de cas du fournisseur, non datée) | M7, O1 | co:X.CLD.08 | [S14] | A |
| F.CLD.D3.005 | 2008-2009 | US | Fin 2008, un analyste d'un cabinet d'études cité par Computerworld décrit la crise du crédit comme une « capex crisis », la technologie étant pour beaucoup d'entreprises le premier poste de dépense en capital ; en janvier 2009, Network World présente le nuage comme un moyen d'éviter le surdimensionnement du matériel et de décharger les administrateurs du provisionnement et de la gestion des serveurs, et en février 2009 un rapport de l'université de Californie à Berkeley note que l'intérêt économique du nuage est souvent décrit comme la conversion de dépenses en capital en dépenses d'exploitation. | « capex crisis » (décembre 2008) | M1, O4 | co:X.CLD.03 | [S15] | A |
| F.CLD.D3.006 | 2015 | US | Un chapitre de l'ouvrage de Google sur l'ingénierie de fiabilité des sites, dont une version paraît dans ;login: en octobre 2015, décrit l'astreinte comme un devoir que de nombreuses équipes d'exploitation et d'ingénierie assument, organisé en rotations primaire et secondaire, avec des tours d'une semaine et un appareil de réception des alertes fourni par l'entreprise, et précise que ces astreintes « ont historiquement été assurées par des équipes d'exploitation dédiées ». | rotations primaire et secondaire ; tours d'une semaine ; délai de réponse typique de 5 minutes pour un service critique | M1 | choc | [S8] | A |
| F.CLD.D3.007 | 2009, 2011 | US | En juin 2009, un site de partage de photographies indique effectuer environ dix mises en production complètes du site par jour, dans un cadre de coopération entre développeurs et exploitants ; en mai 2011, un grand détaillant en ligne effectue en moyenne un changement en production toutes les 11,6 secondes, selon ce que rapporte Jez Humble en 2014. | environ 10 mises en production par jour (2009) ; un changement en production toutes les 11,6 secondes en moyenne (mai 2011) | M1 | choc | [S16] | A |
| F.CLD.D3.008 | 2012-2013 | EMERG | Selon des analystes rapportés par la presse en 2013, les grands sous-traitants informatiques indiens adoptent des services liés au nuage, dont ce que Gartner appelle le courtage de services en nuage, c'est-à-dire l'intégration et la gestion de plusieurs plateformes d'un client ; l'un de ces analystes estime que l'adoption du nuage, qui permet une forte automatisation de la gestion des systèmes, a absorbé du travail qui serait autrement parti en sous-traitance à l'étranger ; les cinq premiers sous-traitants indiens voient leur chiffre d'affaires croître de 13,3 % en 2012, contre 2 % pour le marché mondial des services informatiques. | 13,3 % (2012, cinq premiers sous-traitants indiens) contre 2 % (marché mondial des services informatiques) | M1, T5 | choc | [S5] | A |
| F.CLD.D3.009 | 2003-2004 | US | Avant t0 : l'exploitation informatique d'une organisation est réalisée par son propre personnel sur son propre matériel, dans ses propres locaux, la frontière entre développement et exploitation étant nettement marquée par des équipes et des responsabilités distinctes. | — | M1, O4 | exo | [S3] | K |

### Jalons cités
<!-- Lines 206-211 -->

Aucun jalon de `par_annee/cloud_2005_2015.md` ne porte spécifiquement sur l'organisation du
travail (D3) ; les jalons `J.CLD.2010.06` (D2, cité en secondaire pour le déplacement de tâche) et
`J.CLD.2011.06` (A4, cité en secondaire pour le rythme de mise en production) éclairent la
sous-dimension sans lui être primaires.

### Trajectoire `T.CLD.D3`
<!-- Lines 214-229 -->

| année | phase | intensité | ce qui change | faits et jalons |
| --- | --- | --- | --- | --- |
| avant t0 | latent | 1 | Exploitation interne par du personnel dédié, frontière nette entre développement et exploitation. | F.CLD.D3.009 |
| 2005 | émergence | 2 | Un service de partage vidéo ne compte que ses trois fondateurs à son premier financement, fin 2005, et s'appuie alors sur un hébergeur tiers. | F.CLD.D3.001 |
| 2006 | émergence | 1 | Une suite bureautique en ligne gratuite est proposée aux organisations ; aux États-Unis, 3,6 % des travailleurs travaillent chez eux la majeure partie de la semaine en 2005. | F.CLD.A5.003, F.CLD.D3.003 |
| 2007 | accélération | 0 | Diffusion continue des outils, pas de bascule organisationnelle nouvelle documentée cette année. | — |
| 2008 | crise | 2 | La crise du crédit est décrite fin 2008 comme une crise de la dépense en capital, que le nuage est présenté comme réduisant. | F.CLD.D3.005, F.CLD.D1.008 |
| 2009 | crise | 0 | Poursuite de la diffusion, pas de bascule organisationnelle nouvelle documentée cette année pour D3. | — |
| 2010 | accélération | 2 | Le rapprochement des équipes de développement et d'exploitation s'organise en rencontres (premier devopsdays à Gand en 2009). | F.CLD.D2.003 |
| 2011 | accélération | 2 | En mai 2011, un grand détaillant en ligne effectue en moyenne un changement en production toutes les 11,6 secondes ; un site de photographies en faisait déjà une dizaine par jour en 2009. | F.CLD.D3.007 |
| 2012 | consolidation | 2 | Une application de photographies hébergée sur un nuage public compte 13 employés et plus de 25 millions d'usagers à l'annonce de son rachat ; des analystes décrivent en 2013 l'adoption de services liés au nuage par la sous-traitance indienne. | F.CLD.D3.002, F.CLD.D3.008 |
| 2013 | consolidation | 0 | Diffusion continue des pratiques précédentes, sans bascule nouvelle documentée. | — |
| 2014 | consolidation | 0 | Diffusion continue, sans bascule nouvelle documentée pour D3. | — |
| 2015 | banalisation | 1 | Les travailleurs passant par des intermédiaires en ligne représentent 0,5 % des travailleurs américains fin 2015 ; une plateforme de logement s'appuie sur un nuage public ; l'astreinte organisée est décrite par un grand opérateur. | F.CLD.D3.004, F.CLD.D3.006 |

### Narratif
<!-- Lines 232-253 -->

Un service de partage vidéo ne compte encore que ses trois fondateurs à son premier financement,
fin 2005, et s'appuie alors sur un hébergeur tiers [F.CLD.D3.001] ; en 2012, une application de
photographies hébergée sur un nuage public compte 13 employés et plus de 25 millions d'usagers à
l'annonce de son rachat [F.CLD.D3.002]. Le travail à domicile progresse
lentement aux États-Unis : 19 % des personnes en emploi y font tout ou partie de leur travail les
jours travaillés en 2003, 24 % en 2015, et 3,6 % puis 4,3 % des travailleurs y passent la majeure
partie de la semaine en 2005 puis en 2010 [F.CLD.D3.003]. La frontière entre développement et
exploitation, nette avant t0, se brouille par étapes : fin 2008, la crise du crédit est décrite comme
une crise de la dépense en capital et le nuage comme un moyen de décharger les administrateurs de la
gestion des serveurs [F.CLD.D3.005] ; des mises en production quotidiennes en 2009, puis une toutes
les 11,6 secondes en moyenne en 2011, sont rapportées dans des cadres associant développeurs et
exploitants [F.CLD.D3.007] ; en 2015, un grand opérateur décrit l'astreinte comme un devoir que
des équipes d'exploitation dédiées assuraient historiquement [F.CLD.D3.006]. Les intermédiaires en
ligne du travail à la tâche restent marginaux fin 2015 (0,5 % des travailleurs américains) et leurs
services s'appuient sur des serveurs loués ; cette organisation du travail est rattachée au
confondant produit dérivé [F.CLD.D3.004, X.CLD.08]. Des analystes décrivent en 2013 l'adoption de
services liés au nuage par la sous-traitance indienne, sans chiffrage du déplacement de la tâche
[F.CLD.D3.008].

---

## D4 Salaires, polarisation et rapport de force
<!-- Lines 256-258 -->

**Question :** Qui gagne plus, qui gagne moins, et comment le rapport de force évolue-t-il ?

### Faits
<!-- Lines 261-272 -->

| id | année | bloc | énoncé | valeur | acteurs | attribution | source | statut |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| F.CLD.D4.001 | 2003, 2005, 2008, 2010, 2013, 2015 | US | Série annuelle de la part du travail dans le secteur privé non agricole américain (« Private Nonfarm Business Sector: Labor Share »), U.S. Bureau of Labor Statistics via séries FRED : baisse continue sur toute la fenêtre, de 63,5 % en 2005 à un plancher de 60,7 % en 2013, avant une légère remontée à 61,5 % en 2015 ; la tendance est déjà amorcée avant t0 et se poursuit sans rupture visible attribuable au choc cloud lui-même. | 65,5 % (2003) ; 63,5 % (2005) ; 63,0 % (2008) ; 61,2 % (2010) ; 60,7 % (2013, creux) ; 61,5 % (2015) | M1, M9 | co:X.CLD.03 | [S17] | V |
| F.CLD.D4.002 | 2011, 2016 | US | Le salaire annuel médian des développeurs de logiciels d'applications aux États-Unis est de 88 120 $ en mai 2011, puis de 100 080 $ en mai 2016, contre 79 700 $ en mai 2016 pour les administrateurs de systèmes et de réseaux informatiques, selon le Bureau of Labor Statistics. | 88 120 $ (développeurs d'applications, mai 2011) ; 100 080 $ contre 79 700 $ (mai 2016) | M1 | choc | [S30] | V |
| F.CLD.D4.003 | 2014 | US | Dans une enquête en ligne menée de fin septembre à fin novembre 2014 par un site d'emploi technologique auprès de 23 470 professionnels techniques, la compétence de plateforme en tant que service arrive en tête des salaires annuels moyens (130 081 $), devant des compétences de données massives, contre 89 450 $ pour l'ensemble des répondants ; le site écrit que le nuage et les données massives dominent les compétences les mieux payées ; artefact d'un site d'emploi, faute de série officielle désagrégée par métier du nuage. | 130 081 $ (plateforme en tant que service) contre 89 450 $ (moyenne de l'ensemble des répondants), enquête 2014 | M1 | choc | [S23] | A |
| F.CLD.D4.004 | 2006 | US | En 2006, le New York Times rapporte que Google construit un centre de données à The Dalles (Oregon), site où se rejoignent électricité bon marché et accès aux réseaux de données, et que Microsoft et Yahoo ont annoncé des centres à Wenatchee et à Quincy (État de Washington). | — | M1, M9 | choc | [S4] | A |
| F.CLD.D4.005 | 2015 | US | En 2015, le taux de syndicalisation est de 3,9 % dans les professions informatiques et mathématiques et de 1,7 % dans les services professionnels et techniques, contre 6,7 % dans l'ensemble du secteur privé et 11,1 % pour l'ensemble des salariés américains, selon la Current Population Survey du Bureau of Labor Statistics. | 3,9 % ; 1,7 % ; 6,7 % ; 11,1 % | M1, O8 | exo | [S18] | V |
| F.CLD.D4.006 | 2011 | US | En septembre 2011, un quotidien local de Pennsylvanie publie une enquête, fondée sur des entretiens avec une vingtaine de salariés actuels et anciens d'un entrepôt de logistique d'un grand détaillant en ligne, qui décrit des exigences de productivité jugées impossibles à tenir, une main-d'œuvre en grande partie intérimaire, une chaleur dangereuse et des ambulances stationnées devant l'entrepôt pour soigner les salariés. | environ 20 personnes interrogées | M7 | co:X.CLD.01 | [S19] | A |
| F.CLD.D4.007 | 2007-2010 | US | Aux États-Unis, la hausse sur douze mois des salaires et traitements du secteur privé, mesurée par l'indice du coût de l'emploi, passe de 3,3 % en décembre 2007 à 2,6 % en décembre 2008, à 1,3 % en décembre 2009, puis à 1,8 % en décembre 2010. | 3,3 % (déc. 2007) ; 2,6 % (déc. 2008) ; 1,3 % (déc. 2009) ; 1,8 % (déc. 2010) | M1 | co:X.CLD.03 | [S31] | V |
| F.CLD.D4.008 | 1998, 2000, 2002, 2003, 2004 | US | Avant t0 : la part du travail dans le secteur privé non agricole américain est déjà en tendance baissière depuis 2001, après un pic local en 2000, tendance antérieure au choc cloud et attribuable pour partie à l'autre choc et à son cycle macroéconomique. | 67,4 % (1998) ; 67,7 % (2000, pic local) ; 66,6 % (2002) ; 65,5 % (2003) ; 65,1 % (2004) | M1, M9 | exo | [S17] | V |

### Jalons cités
<!-- Lines 275-280 -->

Aucun jalon de `par_annee/cloud_2005_2015.md` ne porte spécifiquement sur les salaires ou le
rapport de force (D4) ; le jalon `J.CLD.2015.06` (D2/D3, réorientation du métier de direction
informatique) est cité en secondaire pour son implication sur la structure des postes et donc
indirectement sur l'échelle salariale de ce métier.

### Trajectoire `T.CLD.D4`
<!-- Lines 283-298 -->

| année | phase | intensité | ce qui change | faits et jalons |
| --- | --- | --- | --- | --- |
| avant t0 | latent | 1 | La part du travail dans le secteur privé non agricole recule déjà depuis le pic de 2000 (67,7 %) jusqu'à 65,1 % en 2004, tendance antérieure au choc cloud liée à l'autre choc. | F.CLD.D4.008 |
| 2005 | émergence | 1 | La part du travail poursuit son recul à 63,5 % ; pas de bascule salariale nouvelle documentée pour D4 cette année. | F.CLD.D4.001 |
| 2006 | émergence | 0 | Poursuite de la tendance antérieure, sans bascule nouvelle documentée. | F.CLD.D4.001 |
| 2007 | accélération | 0 | Poursuite de la tendance antérieure, sans bascule salariale nouvelle documentée cette année. | — |
| 2008 | crise | 2 | La part du travail reste proche de 63,0 % ; la hausse sur douze mois des salaires du secteur privé tombe à 2,6 % en décembre, contre 3,3 % un an plus tôt. | F.CLD.D4.001, F.CLD.D4.007, F.CLD.D1.008 |
| 2009 | crise | 2 | La hausse sur douze mois des salaires du secteur privé tombe à 1,3 % en décembre. | F.CLD.D4.007 |
| 2010 | accélération | 2 | La part du travail chute à 61,2 %, accélération nette de la baisse pendant la reprise ; la hausse sur douze mois des salaires du secteur privé remonte à 1,8 % en décembre. | F.CLD.D4.001, F.CLD.D4.007 |
| 2011 | accélération | 1 | Des centres de données sont implantés où l'électricité est bon marché (The Dalles, Oregon, 2006) ; le salaire annuel médian des développeurs d'applications est de 88 120 $ en mai. | F.CLD.D4.004, F.CLD.D4.002 |
| 2012 | consolidation | 0 | Poursuite des tendances précédentes, sans bascule salariale nouvelle documentée pour D4 cette année. | — |
| 2013 | consolidation | 1 | La part du travail atteint son plancher de la fenêtre à 60,7 %, sans bascule salariale nouvelle documentée par ailleurs pour D4. | F.CLD.D4.001 |
| 2014 | consolidation | 2 | Une enquête d'un site d'emploi technologique classe en tête des salaires la compétence de plateforme en tant que service, devant des compétences de données massives. | F.CLD.D4.003 |
| 2015 | banalisation | 1 | La part du travail remonte légèrement à 61,5 %, premier infléchissement de la fenêtre ; le taux de syndicalisation des professions informatiques et mathématiques est de 3,9 %, contre 6,7 % pour le secteur privé, et la réorientation du métier de direction informatique consolide une nouvelle échelle salariale de gestion de fournisseurs. | F.CLD.D4.001, F.CLD.D4.005, J.CLD.2015.06 |

### Narratif
<!-- Lines 301-321 -->

La part du travail dans le secteur privé non agricole américain recule sans interruption de 65,1 %
en 2004 à un plancher de 60,7 % en 2013, avant une légère remontée à 61,5 % en 2015 ; le recul
commence avant t0, dès 2001, ce qui interdit d'attribuer ce mouvement de longue durée au cloud sans
réserve, la crise financière de 2008-2010 en expliquant une part importante de l'accélération
observée entre 2008 (63,0 %) et 2010 (61,2 %) [F.CLD.D4.008, F.CLD.D4.001]. Le salaire annuel
médian des développeurs d'applications est de 88 120 $ en mai 2011 et dépasse en mai 2016 de plus
de 20 000 $ celui des administrateurs de systèmes et de réseaux (100 080 $ contre 79 700 $)
[F.CLD.D4.002], et une enquête de 2014 d'un site d'emploi technologique classe en tête des salaires
la compétence de plateforme en tant que service (130 081 $), contre 89 450 $ pour l'ensemble des
répondants [F.CLD.D4.003]. Aux États-Unis, la hausse sur douze mois des salaires du secteur privé
passe de 3,3 % en décembre 2007 à 1,3 % en décembre 2009, puis 1,8 % en décembre 2010
[F.CLD.D4.007]. Des centres de données sont implantés où l'électricité est bon marché, comme à The
Dalles (Oregon) en 2006 [F.CLD.D4.004], et la syndicalisation est de 3,9 % dans les professions
informatiques et mathématiques en 2015, contre 6,7 % pour le secteur privé [F.CLD.D4.005]. Une
enquête de presse de 2011 sur un entrepôt de logistique d'un grand détaillant en ligne décrit des
exigences de productivité jugées impossibles à tenir et une chaleur dangereuse, sans indicateur
chiffré de salaire ou de rapport de force [F.CLD.D4.006].

---

## Sources
<!-- Lines 324-357 -->

| clé | type | référence | note |
| --- | --- | --- | --- |
| [S1] | stat | U.S. Bureau of Labor Statistics, série d'emploi annuel « Employment for Professional, Scientific, and Technical Services: Computer Systems Design and Related Services (NAICS 5415) », diffusée via FRED (Federal Reserve Bank of St. Louis), série IPUMN5415W200000000, milliers d'emplois, non désaisonnalisée, 1987-2024 | Vérifié directement par WebFetch sur le point de sortie CSV de FRED (fredgraph.csv?id=IPUMN5415W200000000) et sur la page de la série : titre exact, unité et valeurs annuelles confirmés. |
| [S2] | stat | U.S. Bureau of Labor Statistics, série d'emploi annuel « Employment for Information: Data Processing, Hosting, and Related Services (NAICS 518) », diffusée via FRED, série IPUJN518W200000000, milliers d'emplois, non désaisonnalisée, 1987-2024 | Vérifié directement par WebFetch sur le point de sortie CSV de FRED (fredgraph.csv?id=IPUJN518W200000000) et sur la page de la série : titre exact, unité et valeurs annuelles confirmés. |
| [S3] | stat | U.S. Bureau of Labor Statistics, Occupational Employment and Wage Statistics (OEWS/OES) et Occupational Outlook Handbook, professions « Network and Computer Systems Administrators » (SOC 15-1142) et « Software Developers » (SOC 15-1132/15-1133), éditions et séries 2007-2016 | Repris en partie de [S31] de `par_dimension/A_industrie/cloud.md`. Les pages BLS consultées par WebFetch (oes/tables.htm, oes/current/*.htm, data.bls.gov/oes) ne rendent que des liens vers des fichiers XLSX ou des données très récentes (2025-2026) ; les valeurs 2005-2015 par occupation n'ont pas pu être extraites par ce canal. Statut K, à vérifier sur les fichiers XLSX archivés hors WebFetch. |
| [S4] | presse | John Markoff et Saul Hansell, « Hiding in Plain Sight, Google Seeks More Power », The New York Times, 14 juin 2006 (texte lu sur une copie : https://bio.nic.funet.fi/pub/mirrors/lcs.mit.edu/telecom-archives/TELECOM_Digest_Online2006-1/2519.html) | Page ouverte et lue : le site de The Dalles (Oregon) réunit « cheap electricity and readily accessible data networking », avec « a large surplus of fiber optic networking » ; Microsoft et Yahoo ont annoncé des centres de données à Wenatchee et à Quincy (État de Washington), « playing catch-up ». Le texte n'a pas été lu sur le site du journal mais sur une copie reproduite dans les archives d'une liste de diffusion ; presse de l'événement lui-même. Aucune source lue ne mesure la concentration géographique de l'emploi du nuage sur la fenêtre : l'énoncé ne l'affirme plus. Le chiffre d'emplois de l'Oregon (Data Center Knowledge, 22 mai 2014, page rouverte et lue : environ 650 emplois de construction dans l'Oregon central sur cinq ans, plus de 200 emplois d'exploitation en 2013) est déjà porté par F.CLD.D1.006 et n'est pas répété ici. |
| [S5] | presse | Phil Muncaster, « India's outsourcers battle for customers in a cloudy universe », The Register, 27 mars 2013, https://www.theregister.com/2013/03/27/india_outsourcing_change_cloud_threat/ ; Alan Dobie, « India's IT industry: feeling the heat », Information Age, 2 juillet 2013, https://www.information-age.com/?p=28422 | Pages ouvertes et lues : The Register, l'analyste de Gartner Arup Roy dit que les prestataires indiens « are already adopting » des techniques non linéaires qui « include cloud computing-related services » ; l'intégration et la gestion de plusieurs plateformes d'un client est « what Gartner calls "cloud services brokerage" » ; Information Age, un analyste d'ISG juge que « IT infrastructure management services are especially vulnerable to disruption by automated systems » et que l'adoption du nuage « has absorbed work » qui serait parti à l'étranger ; Gartner : les cinq premiers sous-traitants indiens (TCS, Cognizant, Infosys, Wipro, HCL) « collectively grew revenues by 13.3% » en 2012, le marché mondial des services informatiques à 2 %. Source faible : presse relayant des analystes, pas les rapports annuels des entreprises ni le rapport de Gartner. Les mots « se réoriente de la gestion de parcs de serveurs vers l'intégration » ne figurent dans aucune page lue. |
| [S6] | off | National Center for Education Statistics, *Digest of Education Statistics*, Table 325.35, « Degrees in computer and information sciences conferred by postsecondary institutions, by level of degree and sex of student: 1970-71 through 2014-15 » | Vérifié directement par WebFetch sur nces.ed.gov (dt16_325.35.asp) : titre de table, source IPEDS Completions component, et série de valeurs par année académique confirmés. Valeurs de licence citées : 59 488 (2003-04) à 37 992 (2008-09, creux) puis 59 581 (2014-15). |
| [S7] | presse | University of Washington, « 'Google 101' class at UW inspires first Internet-scale programming courses », actualités de l'université, 8 octobre 2007, https://www.washington.edu/news/2007/10/08/google-101-class-at-uw-inspires-first-internet-scale-programming-courses/ | Page ouverte et lue : « Google and IBM announced an initiative Monday to promote new programming methods » ; « Google and IBM decided to donate and maintain hundreds of processors » ; partenaires « the UW, Carnegie Mellon University, the Massachusetts Institute of Technology » ainsi que Stanford, Berkeley et Maryland ; « A pilot course taught at the University of Washington has been expanded into a national program ». Le mot « first » ne figure que dans le titre de l'université. |
| [S8] | livre | Andrea Spadaccini, « Being On-Call », in Betsy Beyer et al., Site Reliability Engineering, O'Reilly, 2017 (une version antérieure paraît dans ;login: en octobre 2015), https://sre.google/sre-book/being-on-call/ | Page ouverte et lue : « Being on-call is a critical duty that many operations and engineering teams must undertake » ; « Many teams have both a primary and a secondary on-call rotation » ; « week-long shifts » ; « The company provides the page-receiving device, which is typically a phone » ; délai de réponse typique de « 5 minutes for user-facing or otherwise highly time-critical services » ; « on-call activities have historically been performed by dedicated Ops teams ». Le texte ne date pas le début de la pratique ; il décrit celle de Google, non celle de clients de services loués, et l'énoncé ne dit plus que l'astreinte devient pratique organisée à mesure que les services loués fonctionnent sans interruption. Quatre tentatives de source sur 2010-2013 (entretien ACM Queue avec le directeur technique d'Amazon, copie de cet entretien, deux billets du blog d'AWS) n'ont rendu aucun texte. |
| [S9] | off | Amazon Web Services, communiqué « Amazon Web Services Announces Launch of Certification Program for AWS Cloud Computing Professionals », 30 avril 2013, https://press.aboutamazon.com/2013/4/amazon-web-services-announces-launch-of-certification-program-for-aws-cloud-computing-professionals | Communiqué ouvert et lu : lancement le 30 avril 2013 ; « The first available AWS Certification Exam is for the “AWS Certified Solutions Architect – Associate Level” certification » ; autres certifications par rôle (SysOps, développeur) annoncées pour plus tard en 2013 ; examens « administered through testing centers in more than 100 countries and 750 testing locations worldwide ». Aucun nombre de certifiés. Seul le programme d'un fournisseur a été lu ; les pages de blog d'AWS tentées (programme mondial, mises à jour) ne rendaient que la navigation du site. |
| [S10] | livre | Wikipedia, « Massive open online course », https://en.wikipedia.org/wiki/Massive_open_online_course (lu en 2026) | Page de référence ouverte et lue, première partie (100 000 premiers caractères sur 173 637) : « The term MOOC was coined in 2008 by Dave Cormier » à propos de « Connectivism and Connective Knowledge » ; « In the fall of 2011 Stanford University launched three courses » dont un à 160 000 inscrits ; « By June 2012, more than 1.5 million people had registered for classes through Coursera, Udacity or edX ». La page ne dit pas que l'offre initiale était orientée vers la programmation ; l'énoncé ne le dit donc plus. |
| [S11] | presse | Sequoia Capital, « YouTube ft. Steve Chen – 18 Months That Changed the Internet », épisode du podcast Crucible Moments, https://sequoiacap.com/podcast/crucible-moments-youtube | Page ouverte et lue : « When Sequoia led the initial funding for YouTube, the company comprised just the three founders », financement de fin 2005, « working out of Chad's garage in Menlo Park » ; hébergeur ServerBeach, « we got some kind of deal where we got unlimited bandwidth » ; plus tard, passage à un centre de données propre (« we would operate our own infrastructure »). Page d'un investisseur, récit rétrospectif des acteurs. |
| [S12] | presse | Al Jazeera, « Facebook updates status with Instagram deal », 10 avril 2012, https://www.aljazeera.com/economy/2012/4/10/facebook-updates-status-with-instagram-deal ; Mike Krieger, « A Brief, Rapid History of Scaling Instagram (with a tiny team) », QConSF 2013, diapositives (InfoQ sur SlideShare) ; ByteByteGo, « How Instagram Scaled Its Infrastructure To Support a Billion Users », https://blog.bytebytego.com/p/how-instagram-scaled-its-infrastructure | Ouverts et lus : Al Jazeera, « a three-year-old company with 13 employees » et « more than 25 million of its own users » ; communiqué de Facebook du 9 avril 2012 (https://about.fb.com/news/2012/04/facebook-to-acquire-instagram/) : « Millions of people around the world love the Instagram app », sans chiffre ni effectif ; diapositives de Krieger : « Amazon EC2 », « old Amazon EBS », « 2 total engineers » ; ByteByteGo : « Instagram was still operating on a relatively small-scale infrastructure hosted on Amazon Web Services (AWS) » à l'époque du rachat. Le chiffre de 30 millions d'usagers cité dans la presse (CNN Money) n'a pas été ouvert (503). Les 25 millions sont un ordre de grandeur de presse contemporaine. |
| [S13] | stat | U.S. Bureau of Labor Statistics, The Economics Daily, « 24 percent of employed people did some or all of their work at home in 2015 », 8 juillet 2016 (American Time Use Survey), https://www.bls.gov/opub/ted/2016/24-percent-of-employed-people-did-some-or-all-of-their-work-at-home-in-2015.htm ; U.S. Census Bureau, Home-Based Workers in the United States: 2010, P70-132, octobre 2012, https://www.census.gov/library/publications/2012/demo/p70-132.html ; Michal Lev-Ram, « Google enterprise is something to fear », Fortune, 5 juillet 2012, https://fortune.com/2012/07/05/google-enterprise-is-something-to-fear | Pages ouvertes et lues : BLS, la part des travailleurs qui font tout ou partie de leur travail à domicile « grew from 19 percent in 2003 to 24 percent in 2015 » ; Census, la part des travailleurs qui travaillent la majeure partie de la semaine à domicile « increased from 3.6 percent to 4.3 percent of the population between 2005 and 2010 » (ACS) ; Fortune, « Google says five million businesses across the country now use it » (le pronom désigne, d'après la page lue, le courriel de Google). Six pages (deux de Google, puis Redmond Magazine, eWeek, TechRadar et AOL), tentées pour préciser ce chiffre, n'ont rendu que la navigation ou une erreur : la formulation de Fortune est donc la seule lue, et le périmètre du chiffre (courriel seul ou suite) reste incertain. Source faible pour ce chiffre. Aucune page lue ne compare le rythme de diffusion des outils à celui du télétravail mesuré : l'énoncé ne le fait plus. |
| [S14] | acad | Lawrence F. Katz et Alan B. Krueger, « The Rise and Nature of Alternative Work Arrangements in the United States, 1995-2015 », NBER Working Paper 22667, septembre 2016, https://www.nber.org/papers/w22667 ; Amazon Web Services, étude de cas « Airbnb », https://aws.amazon.com/solutions/case-studies/airbnb-case-study | Pages ouvertes et lues : NBER, les travailleurs « who provide services through online intermediaries, such as Uber or Task Rabbit, accounted for 0.5 percent of all workers in 2015 » ; AWS, « A year after Airbnb launched », l'entreprise décide de migrer presque toutes ses fonctions informatiques vers AWS pour des « service administration challenges » chez son premier fournisseur ; elle « began operation in 2008 » ; 200 instances EC2 « for its application, memcache, and search servers » ; la page ne donne pas d'année pour cette migration ni pour le nombre d'instances. Étude de cas d'un fournisseur : valable pour ce que le fournisseur dit de son client, non pour une tendance. Aucune page lue ne mesure l'emploi des plateformes à la demande avant 2015 : l'énoncé ne chiffre pas 2008-2014. |
| [S15] | presse | Mary Brandel, « Six budget tips for surviving 2009 », Computerworld, 30 décembre 2008, https://www.computerworld.com/article/1683860/six-budget-tips-for-surviving-2009.html ; Kathleen Lau, « Seven reasons cloud computing works in a tough economy », Network World, 9 janvier 2009, https://www.networkworld.com/article/796678/saas-seven-reasons-cloud-computing-works-in-a-tough-economy.html ; Michael Armbrust et al., « Above the Clouds: A Berkeley View of Cloud Computing », UCB/EECS-2009-28, 10 février 2009, https://www2.eecs.berkeley.edu/Pubs/TechRpts/2009/EECS-2009-28.pdf | Pages ouvertes et lues (le PDF avec pdftotext) : Computerworld, un analyste de Gartner : « What's different about this crisis is it's a capex crisis » et « for many companies, technology is the No. 1 'capex' (capital expenditure) item » ; Network World, « Cloud computing leverages commodity hardware, so IT departments can avoid overprovisioning » et « IT administrators are not so belaboured with tasks like provisioning and management of servers » ; Berkeley, « the economic appeal of Cloud Computing is often described as converting capital expenses to operating expenses (CapEx to OpEx) », l'auteur préférant « pay as you go ». Aucune page lue ne dit que les directions informatiques commencent en 2008 à séparer dépense en capital et dépense de fonctionnement dans l'arbitrage acheter ou louer, ni qu'une tâche d'exploitation passe à des fournisseurs : ces clauses sont retirées. |
| [S16] | presse | Rich Miller, « Velocity: Flickr on Devs, Ops and Teamwork », Data Center Knowledge, 25 juin 2009, https://datacenterknowledge.com/business/velocity-flickr-on-devs-ops-and-teamwork ; Jez Humble, « The case for continuous delivery », O'Reilly Radar, 20 février 2014, https://www.oreilly.com/content/the-case-for-continuous-delivery/ | Pages ouvertes et lues : Data Center Knowledge, séance de John Allspaw et Paul Hammond (Flickr) à Velocity 2009, « on a normal day there are 10 full deployments of the site to our servers », titre « 10+ Deploys A Day: Devs & Ops Cooperation at Flickr » ; O'Reilly Radar, « Amazon is on record as making changes to production every 11.6 seconds on average in May of 2011 ». Une recherche signale que le sens de « changement » dans le chiffre d'Amazon est discuté (déploiements distincts ou réplications sur des hôtes) ; la présentation d'origine n'a pas été lue. Aucune page lue ne mentionne un outil de conteneurisation, ni un passage du trimestre à la journée : ces clauses sont retirées. |
| [S17] | stat | U.S. Bureau of Labor Statistics, série annuelle « Private Nonfarm Business Sector: Labor Share », diffusée via FRED, série MPU4910141, pourcentage, non désaisonnalisée, 1987-2024 | Vérifié directement par WebFetch sur le point de sortie CSV de FRED (fredgraph.csv?id=MPU4910141) : fichier brut lu intégralement (observation_date, valeur), série continue de 1987 à 2024 confirmée. Une première tentative sur les pages HTML de bea.gov et sur la page interactive de FRED avait échoué (404, ou seules les valeurs les plus récentes rendues) ; le point de sortie CSV direct a résolu le blocage. |
| [S18] | stat | U.S. Bureau of Labor Statistics, « Union Members — 2015 », USDL-16-0158, 28 janvier 2016, table 3 (Current Population Survey), https://www.bls.gov/news.release/archives/union2_01282016.pdf | Communiqué ouvert et lu (PDF, pdftotext) : taux de syndicalisation 2015, ensemble des salariés 11,1 % ; secteur privé 6,7 % ; professions informatiques et mathématiques 3,9 % ; services professionnels et techniques 1,7 % ; information 8,6 %. Le secteur « traitement de données et hébergement » n'est pas séparé dans la table : l'énoncé ne le cite pas. Seule l'année 2015 est lue ; « toute la fenêtre » et « sans négociation collective » sont retirés. Document primaire. |
| [S19] | presse | Hillman Foundation, notice du Sidney Award d'octobre 2011 à Spencer Soper, https://hillmanfoundation.org/node/1393 ; Ryan Chittum, « The Morning Call probes Amazon », Columbia Journalism Review, 23 septembre 2011, https://www.cjr.org/the_audit/the_morning_call_probes_amazon.php (enquête de Spencer Soper, The Morning Call, Allentown, 17 septembre 2011) | Pages ouvertes et lues : Hillman, l'enquête porte sur l'entrepôt de la vallée de la Lehigh (Pennsylvanie) ouvert en 2010, Soper a interrogé « 20 current and former Amazon employees », travail « punishing », quotas, chaleur qui « rose dangerously high », une société d'ambulances sur place ; CJR, « ever-increasing, and impossible-to-meet, productivity demands » pour une main-d'œuvre « largely temp », paramédicaux en ambulance devant l'entrepôt, plainte à l'OSHA : « the heat index hit 102 degrees in the warehouse and 15 workers collapsed ». L'article original du Morning Call n'a pas été lu : les deux pages sont des comptes rendus de l'enquête. Un seul entrepôt, un seul quotidien, 2011 : l'énoncé ne généralise pas à 2011-2015 ni à la logistique du commerce en ligne. |
| [S20] | stat | U.S. Bureau of Labor Statistics, Current Population Survey, série annuelle « Employed full time: Wage and salary workers: Software developers, applications and systems software occupations: 16 years and over », diffusée via FRED, série LEU0254477200A, milliers de personnes, 2000-2019 | Vérifié directement par WebFetch sur le point de sortie CSV de FRED (fredgraph.csv?id=LEU0254477200A) : valeurs annuelles 2003-2015 confirmées. Série apparentée pour l'ensemble des professions informatiques et mathématiques (LEU0254476900A) consultée de la même façon pour comparaison, non reprise en fait séparé. |
| [S21] | acad | Sundharan, Sajikumar, « Structure, Growth and Performance of Indian IT-BPO Industry », *International Journal of Economics, Commerce and Management*, vol. I, n° 2, 2013, citant National Association of Software and Service Companies (NASSCOM), *Strategic Review 2012* | Article académique ouvert et lu intégralement en PDF (WebFetch puis lecture directe du fichier) : Table 6 (« Knowledge professionals in IT-BPO sector », milliers, 2008-2012) et texte p. 11 (2,8 millions d'emplois directs et 8,9 millions indirects en 2012) confirmés. Donnée de seconde main (NASSCOM via l'article), non le rapport NASSCOM original ; limite de fiabilité signalée par l'auteur lui-même (note 3 de l'article) faute de source de validation croisée pour les chiffres NASSCOM. |
| [S22] | presse | Datadog, « 8 Surprising Facts About Real Docker Adoption », 2015, https://www.datadoghq.com/docker-adoption-2015/ | Page rouverte et lue : échantillon de « 7,000 companies » ; « 1.8 percent of Datadog's customers had adopted Docker » au début de septembre 2014, « 8.3 percent » un an plus tard ; part des entreprises ayant essayé Docker selon la taille (coupures 1-99, 100-499, 500+ hôtes) : 11 %, 28 %, 56 % ; d'autres coupures donnent 11 %/22 %/43 % et 12 %/37 %/58 %. L'éditeur écrit que ses clients « skew toward early adopters » : l'échantillon n'est pas représentatif du marché. Étude d'un fournisseur sur sa propre clientèle (artefact au sens de R2) : l'énoncé la cite comme telle et ne généralise pas. Statut `A` : décision à confirmer par le coordinateur, la version précédente classait la ligne `K` pour ce motif. |
| [S23] | stat | Dice.com, Dice Tech Salary Survey, enquête menée du 29 septembre au 26 novembre 2014 auprès de 23 470 professionnels techniques, publiée le 22 janvier 2015, https://www.dice.com/career-advice/dice-salary-survey-good-times-for-tech-pros | Page rouverte et lue : « 23,470 employed technology professionals responding between September 29 and November 26, 2014 » ; « earning $89,450 on average annually » ; PaaS en tête à 130 081 $, suivi de Cassandra (128 646 $), MapReduce (127 315 $), Cloudera (126 816 $), HBase, Pig, ABAP, Chef, Flume, Hadoop (121 313 $) ; « Big Data and cloud dominate the skills which earned the highest paychecks in 2014 ». La page ne donne pas de moyenne séparée pour le nuage ni ne précise que les répondants sont américains (bloc US inféré du site). Source faible : enquête en ligne d'un site d'emploi sur ses propres visiteurs (artefact au sens de R2), statut A au titre du seuil D21, à confirmer par le coordinateur. |
| [S24] | stat | U.S. Bureau of Labor Statistics, Current Population Survey, annual averages, tableau 25 « Unemployed persons by occupation and sex » : édition 2009 (colonnes 2008 et 2009), https://www.bls.gov/cps/aa2009/cpsaat25.pdf ; édition 2011 (colonnes 2010 et 2011), https://www.bls.gov/cps/aa2011/cpsaat25.htm | Tableaux ouverts et lus (le PDF 2009 avec `pdftotext`) : ligne « Computer and mathematical occupations », taux de chômage 2,6 % (2008), 5,2 % (2009), 5,2 % (2010), 4,1 % (2011) ; ligne « Total, 16 years and over », 5,8 %, 9,3 %, 9,6 %, 8,9 %. Document primaire. |
| [S25] | stat | U.S. Bureau of Labor Statistics, série d'emploi annuel « Employment for Retail Trade: Electronic Shopping and Mail-Order Houses (NAICS 4541) », diffusée via FRED, série IPUHN4541W200000000, 1987-2024, https://fred.stlouisfed.org/graph/fredgraph.csv?id=IPUHN4541W200000000 | Fichier CSV ouvert et lu (2003-2016) : 239,3 (2003) ; 245,9 (2004) ; 283,6 (2005) ; 266,3 (2006) ; 263,8 (2009) ; 269,5 (2010) ; 377,0 (2015) ; 383,2 (2016), en milliers d'emplois (unité et libellé de la série repris du listing FRED de la série, comme pour [S1] et [S2]). Le sous-secteur 4541 inclut la vente par correspondance, pas seulement la vente en ligne. |
| [S26] | presse | Yevgeniy Sverdlik, « Study: Facebook's Data Center Created Thousands of Jobs in Oregon », Data Center Knowledge, 22 mai 2014 (étude d'ECONorthwest pour Facebook), https://datacenterknowledge.com/data-center-career-development/study-facebook-s-data-center-created-thousands-of-jobs-in-oregon ; Christopher Tozzi, « How Many Jobs Do Data Centers Create? It Depends », Data Center Knowledge, 28 août 2025, https://www.datacenterknowledge.com/operations-and-management/how-many-jobs-do-data-centers-create-it-depends | Pages ouvertes et lues : Sverdlik, la construction « has created about 650 jobs in Central Oregon and nearly 3,600 jobs in the State of Oregon overall » sur cinq ans ; opérations hors construction : « more than 200 jobs in Central Oregon » en 2013 ; Tozzi, « A large facility might keep thousands of construction workers busy, at least for the year or two that it takes to build » et « the total data center staff number is only several dozen ». Presse spécialisée, la seconde rétrospective de 2025 et générale, non datée de la fenêtre. |
| [S27] | presse | InfoQ, entretien sur les cinq ans des devopsdays (titre repris de l'adresse : « 5 years devops days qa »), décembre 2014, https://www.infoq.com/news/2014/12/5-years-devops-days-qa/ ; Chef, « 10 Years of DevOps », https://www.chef.io/blog/10-years-of-devops ; Benjamin Treynor Sloss, « Introduction », in Beyer et al., *Site Reliability Engineering*, O'Reilly, 2017, https://sre.google/sre-book/introduction/ | Pages ouvertes et lues : InfoQ, « initial conference in Ghent in 2009 » ; Chef, « then in 2009, the first DevOps Days ran in Ghent, Belgium » ; livre de Google, « When I joined Google in 2003 and was tasked with running a "Production Team" of seven engineers » et « SRE is what happens when you ask a software engineer to design an operations team ». Aucune des pages lues ne date de 2010 une publication de Google sur la fiabilité des sites. |
| [S28] | livre | Wikipedia, « Infrastructure as code », https://en.wikipedia.org/wiki/Infrastructure_as_code | Page de référence ouverte et lue : l'idée vient avec « the growth of cloud computing and the need to provision resources consistently and at scale » ; CFEngine (1993) introduit la description de la configuration « in a declarative language rather than executing manual commands » ; « Treating infrastructure configuration like software » ; Puppet (2005) et Chef (2009) figurent dans le tableau des outils. La page ne parle ni des administrateurs systèmes ni de leur métier. Les éditions du manuel du BLS, citées auparavant, n'ont pas été lues. |
| [S29] | presse | Boston.com, « 30 of the fastest declining occupations », 30 décembre 2013, citant le Bureau of Labor Statistics, Occupational Outlook Handbook, projections 2006-2016, https://www.boston.com/jobs/untagged/2013/12/30/30-of-the-fastest-declining-occupations | Page ouverte et lue : opérateurs informatiques, « -24.7 percent » en 2016 par rapport à 2006 ; « The growing use of software that automates computer operations has made systems more efficient ». La page du manuel du BLS lui-même (copie d'archive UNT en PDF) a été tentée et n'a rendu aucun texte. |
| [S30] | stat | U.S. Bureau of Labor Statistics, Occupational Employment and Wages, May 2016, professions 15-1132 (Software Developers, Applications) et 15-1142 (Network and Computer Systems Administrators), https://www.bls.gov/oes/2016/May/oes151132.htm et https://www.bls.gov/oes/2016/May/oes151142.htm ; Lauren Csorny, « Careers in the growing field of information technology services », Beyond the Numbers, BLS, 9 avril 2013, https://www.bls.gov/opub/btn/volume-2/careers-in-growing-field-of-information-technology-services.htm | Pages ouvertes et lues : OES mai 2016, développeurs d'applications, emploi 794 000, salaire annuel médian 100 080 $ (moyen 104 300 $) ; administrateurs de systèmes et de réseaux, emploi 376 820, médian 79 700 $ (moyen 84 500 $) ; Beyond the Numbers, médian de mai 2011 des développeurs d'applications 88 120 $ (systèmes : 94 570 $), sans chiffre pour les administrateurs. Les pages OES de 2012, 2014 et 2015 rendent la page courante (2025) et non les tableaux d'époque, et les copies d'archive des éditions 2012-2013 du manuel n'ont rendu aucun texte : seul l'écart de mai 2016, hors fenêtre d'un an, est lu. Les valeurs 2005-2015 restent non extraites. Document primaire. |
| [S31] | stat | U.S. Bureau of Labor Statistics, Employment Cost Index, communiqués de décembre 2008 (30 janvier 2009, https://www.bls.gov/news.release/archives/eci_01302009.htm) et de décembre 2010 (28 janvier 2011, USDL-11-0086, https://www.bls.gov/news.release/archives/eci_01282011.htm) | Communiqués ouverts et lus : décembre 2008, « Private industry wages and salaries increased 2.6 percent in December 2008. In December 2007 the increase was 3.3 percent » ; décembre 2010, « The wage and salary series increased 1.8 percent for the current 12-month period. The change for the period ending December 2009 was 1.3 percent. » (section « Private Industry Workers »). Les 35 892 derniers caractères du communiqué 2010 et les 8 833 derniers de celui de 2008 n'ont pas été lus. Aucune page lue ne porte sur les salaires des métiers informatiques ou du nuage pendant la crise : « gel des embauches », « reprise inégale à partir de 2010-2011 dans les métiers du cloud » sont retirés. Document primaire. |
