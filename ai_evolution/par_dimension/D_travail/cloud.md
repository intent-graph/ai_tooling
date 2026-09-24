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

1. [D1 Volume et structure de l'emploi](#d1-volume-et-structure-de-l-emploi) _(Lines 43-45)_
   1. [Faits](#faits) _(Lines 48-61)_
   1. [Jalons cités](#jalons-cit-s) _(Lines 64-68)_
   1. [Trajectoire `T.CLD.D1`](#trajectoire-t-cld-d1) _(Lines 71-86)_
   1. [Narratif](#narratif) _(Lines 89-110)_
1. [D2 Métiers, compétences et formation](#d2-m-tiers-comp-tences-et-formation) _(Lines 113-116)_
   1. [Faits](#faits-1) _(Lines 119-132)_
   1. [Jalons cités](#jalons-cit-s-1) _(Lines 135-140)_
   1. [Trajectoire `T.CLD.D2`](#trajectoire-t-cld-d2) _(Lines 143-158)_
   1. [Narratif](#narratif-1) _(Lines 161-181)_
1. [D3 Organisation du travail](#d3-organisation-du-travail) _(Lines 184-186)_
   1. [Faits](#faits-2) _(Lines 189-201)_
   1. [Jalons cités](#jalons-cit-s-2) _(Lines 204-209)_
   1. [Trajectoire `T.CLD.D3`](#trajectoire-t-cld-d3) _(Lines 212-227)_
   1. [Narratif](#narratif-2) _(Lines 230-249)_
1. [D4 Salaires, polarisation et rapport de force](#d4-salaires-polarisation-et-rapport-de-force) _(Lines 252-254)_
   1. [Faits](#faits-3) _(Lines 257-268)_
   1. [Jalons cités](#jalons-cit-s-3) _(Lines 271-276)_
   1. [Trajectoire `T.CLD.D4`](#trajectoire-t-cld-d4) _(Lines 279-294)_
   1. [Narratif](#narratif-3) _(Lines 297-318)_
1. [Sources](#sources) _(Lines 321-346)_


---

## D1 Volume et structure de l'emploi
<!-- Lines 43-45 -->

**Question :** Combien d'emplois créés, détruits, déplacés, dans quels secteurs, à quel rythme ?

### Faits
<!-- Lines 48-61 -->

| id | année | bloc | énoncé | valeur | acteurs | attribution | source | statut |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| F.CLD.D1.001 | 2003-2004 | US | Avant t0 : l'emploi dans les professions informatiques croît sur une base restreinte à la sortie de la correction du début des années 2000 (X.INT.05), effectifs très inférieurs au pic de 2000-2001. | effectifs en deçà du pic 2000-2001 | M1 | exo | [S1] | K |
| F.CLD.D1.002 | 2003, 2005, 2008, 2009, 2010, 2015, 2016 | US | Série annuelle d'emploi du secteur des services informatiques (NAICS 5415, « Computer Systems Design and Related Services »), U.S. Bureau of Labor Statistics : croissance quasi continue sur la fenêtre, y compris pendant la crise, avec un seul recul net en 2009. | 1 291 800 (2003) ; 1 368 600 (2005) ; 1 611 400 (2008) ; 1 586 400 (2009) ; 1 610 200 (2010) ; 2 043 400 (2015) ; 2 153 700 (2016) | M1, O2, O4 | choc | [S1] | V |
| F.CLD.D1.003 | 2003, 2005, 2008, 2009, 2010, 2015 | US | Série annuelle d'emploi du sous-secteur du traitement de données et de l'hébergement (NAICS 518, « Data Processing, Hosting, and Related Services »), U.S. Bureau of Labor Statistics : recul de l'emploi entre 2003 et 2010 malgré la construction massive de centres de données (A1), puis reprise modérée jusqu'en 2015, sans jamais retrouver l'échelle du secteur des services informatiques au sens large. | 288 600 (2003) ; 265 300 (2005) ; 262 100 (2008) ; 252 500 (2009) ; 248 000 (2010, creux de la fenêtre) ; 300 100 (2015) | M1 | choc | [S2] | V |
| F.CLD.D1.004 | 2008-2010 | US | Le taux de chômage des professions informatiques et mathématiques augmente pendant la crise et la reprise qui suit, mais reste inférieur au taux de chômage global américain sur toute la période, tendance déjà connue avant t0. | chômage professions informatiques inférieur au taux national | M1 | co:X.CLD.03 | [S3] | K |
| F.CLD.D1.005 | 2003, 2005, 2007, 2009, 2010, 2015 | US | Série annuelle d'emploi à temps plein des développeurs de logiciels (salariés, 16 ans et plus), Current Population Survey, U.S. Bureau of Labor Statistics : quasi-doublement des effectifs sur la fenêtre, croissance plus rapide que celle de l'ensemble des professions informatiques et mathématiques sur la même période. | 701 000 (2003) ; 778 000 (2005) ; 872 000 (2007) ; 902 000 (2009) ; 973 000 (2010) ; 1 287 000 (2015) | M1 | choc | [S20] | V |
| F.CLD.D1.006 | 2008-2011 | US | La construction d'un centre de données de grande taille emploie plusieurs centaines à quelques milliers de travailleurs du bâtiment pendant la phase de chantier, mais l'exploitation courante du site une fois ouvert n'occupe qu'un nombre réduit de salariés permanents, de l'ordre de quelques dizaines à quelques centaines selon la taille. | chantier : centaines à ~2 000 emplois temporaires ; exploitation : dizaines à quelques centaines d'emplois permanents | M1, M7, O2 | choc | [S4] | K |
| F.CLD.D1.007 | 2008-2012 | EMERG | Série annuelle des effectifs employés dans les métiers qualifiés du secteur indien IT-BPO (services informatiques, exportations, marché domestique), reprise d'une étude académique citant le Strategic Review 2012 de l'association professionnelle du secteur : croissance continue sur la période malgré la crise financière mondiale, sans rupture de tendance attribuable à une automatisation de l'exploitation. | 1 962 000 (2008) ; 2 196 000 (2009) ; 2 300 000 (2010) ; 2 540 000 (2011) ; 2 770 000 (2012, estimation) | M1, T5 | co:X.CLD.03 | [S21] | V |
| F.CLD.D1.008 | 2003, 2005, 2009, 2015 | US | Au creux de la récession consécutive à la crise financière (2009), l'emploi des services informatiques (NAICS 5415) recule de 1,5 % par rapport à 2008 quand l'emploi salarié total américain recule beaucoup plus fortement sur la même période, ce qui est cohérent avec un secteur en croissance structurelle amorti par un choc exogène plutôt que retourné par lui. | recul NAICS 5415 : 1 611 400 (2008) à 1 586 400 (2009), soit -1,5 % | M1 | co:X.CLD.03 | [S1] | V |
| F.CLD.D1.009 | 2005-2015 | US | Le nombre d'établissements et l'emploi du commerce de détail en ligne (une partie de NAICS 454110 et activités connexes) progressent sur la fenêtre, tirés en partie par des opérateurs qui construisent leur propre informatique en centre de données ; la part attribuable au cloud proprement dit contre la vente en ligne elle-même (produit dérivé, X.CLD.01 en partie) n'est pas séparée dans les séries disponibles. | croissance non désagrégée par cause | M1, M7, O2 | co:X.CLD.01 | [S1] | K |
| F.CLD.D1.010 | 2012 | EMERG | Le secteur indien IT-BPO emploie directement 2,8 millions de professionnels et génère 8,9 millions d'emplois indirects selon l'association professionnelle du secteur (Strategic Review 2012), soit un total de 11,7 millions ; aucune série officielle unifiée de comptage mondial des emplois créés directement par l'industrie des centres de données proprement dite (hors sous-traitance de services) n'a été identifiée sur la fenêtre. | 2,8 M emplois directs, 8,9 M indirects, 11,7 M au total (secteur IT-BPO indien, 2012) | M1, T5 | choc | [S21] | V |

### Jalons cités
<!-- Lines 64-68 -->

Aucun jalon de `par_annee/cloud_2005_2015.md` ne porte spécifiquement sur le volume d'emploi
(D1) ; le jalon le plus proche, `J.CLD.2008.01` (crise financière), sert de repère de rupture de
ligne de base plutôt que de bascule propre à D1.

### Trajectoire `T.CLD.D1`
<!-- Lines 71-86 -->

| année | phase | intensité | ce qui change | faits et jalons |
| --- | --- | --- | --- | --- |
| avant t0 | latent | 1 | Emploi informatique en reconstitution après la correction du début des années 2000 ; le sous-secteur hébergement et traitement de données recule déjà depuis 2001-2002. | F.CLD.D1.001, F.CLD.D1.002, F.CLD.D1.003 |
| 2005 | émergence | 1 | Croissance de l'emploi des services informatiques (1,37 M) ; l'hébergement et le traitement de données poursuivent leur recul (265 300) malgré les premiers services facturés à l'usage. | F.CLD.D1.002, F.CLD.D1.003 |
| 2006 | émergence | 1 | Poursuite de la croissance sectorielle (NAICS 5415), sans rupture documentée cette année pour D1. | F.CLD.D1.002 |
| 2007 | accélération | 1 | Premiers cursus et recherches en calcul distribué, signe d'une demande de compétence naissante en amont de l'emploi ; l'emploi des services informatiques atteint 1,54 M, celui des développeurs 872 000. | J.CLD.2007.03, F.CLD.D1.005 |
| 2008 | crise | 2 | La crise financière (X.CLD.03) casse la ligne de base de l'emploi total américain ; l'emploi des services informatiques atteint son pic pré-recul à 1,61 M. | J.CLD.2008.01, F.CLD.D1.002 |
| 2009 | crise | 2 | Creux de la récession : recul limité de -1,5 % de l'emploi des services informatiques (1,59 M), recul plus marqué du sous-secteur hébergement (252 500) ; chômage informatique en hausse mais sous la moyenne nationale. | F.CLD.D1.008, F.CLD.D1.004 |
| 2010 | accélération | 2 | Point bas du sous-secteur hébergement et traitement de données (248 000) alors que les services informatiques ont déjà dépassé leur niveau de 2008 (1,61 M) ; le métier d'administrateur système bascule vers le code de configuration. | J.CLD.2010.06, F.CLD.D1.002, F.CLD.D1.003, F.CLD.D1.005 |
| 2011 | accélération | 1 | Poursuite de la croissance de l'emploi des services informatiques et de la construction de centres de données ; reprise du sous-secteur hébergement. | F.CLD.D1.006 |
| 2012 | consolidation | 1 | La sous-traitance indienne se réoriente sectoriellement (voir A5, F.CLD.A5.005) tout en continuant de croître en effectifs (2,77 M direct estimé, 11,7 M avec l'emploi indirect). | F.CLD.D1.007, F.CLD.D1.010 |
| 2013 | consolidation | 1 | Poursuite de la croissance de l'emploi des services informatiques ; effectifs d'exploitation des centres de données restant réduits par site. | F.CLD.D1.006 |
| 2014 | consolidation | 1 | Poursuite de la croissance sectorielle, sans bascule nouvelle documentée pour D1. | F.CLD.D1.002 |
| 2015 | banalisation | 2 | Écart de trajectoire confirmé entre développeurs (1,29 M, quasi-doublement depuis 2003) et le sous-secteur hébergement (300 000, retour au-dessus du niveau de 2008 seulement). | F.CLD.D1.005, F.CLD.D1.003 |

### Narratif
<!-- Lines 89-110 -->

L'emploi informatique américain part d'une base restreinte par la correction du début des années
2000 [F.CLD.D1.001] et croît de façon continue sur la fenêtre dans les services informatiques au
sens large, de 1,37 million en 2005 à 2,04 millions en 2015, avec un seul recul net de 1,5 % en
2009 [F.CLD.D1.002, F.CLD.D1.008]. Le sous-secteur de l'hébergement et du traitement de données au
sens strict suit une trajectoire inverse et contre-intuitive : son emploi recule de 265 300 en 2005
à un creux de 248 000 en 2010, précisément les années de construction massive des centres de
données (A1), avant de ne remonter qu'à 300 100 en 2015, ce qui contredit l'image d'une industrie
de centres de données massivement employeuse [F.CLD.D1.003]. Un fait notable complémentaire : la
construction d'un centre de données mobilise beaucoup de main-d'œuvre de chantier pendant quelques
mois, puis très peu d'emplois permanents une fois le site en exploitation [F.CLD.D1.006]. Les
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
<!-- Lines 113-116 -->

**Question :** Quels métiers apparaissent, disparaissent, se transforment ; quelles compétences
sont demandées ; comment on se forme ?

### Faits
<!-- Lines 119-132 -->

| id | année | bloc | énoncé | valeur | acteurs | attribution | source | statut |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| F.CLD.D2.001 | 2003-04, 2004-05, 2005-06, 2006-07, 2007-08, 2008-09, 2009-10, 2010-11, 2011-12, 2012-13, 2013-14, 2014-15 | US | Série des diplômes conférés en sciences informatiques et de l'information (tous niveaux confondus, licence à doctorat), National Center for Education Statistics, IPEDS : recul continu de 2003-04 à 2009-10, puis reprise continue jusqu'à retrouver quasiment le niveau de départ en 2014-15. | 2003-04 : ~59 500 (total tous niveaux, dont 59 488 en licence) ; creux 2008-09 : 37 992 (licence) ; 2014-15 : 59 581 (licence), niveau proche de 2003-04 | M1, P2 | co:X.INT.05 | [S6] | V |
| F.CLD.D2.002 | 2007 | US | Le premier cursus universitaire de calcul distribué à très grande échelle et les premiers programmes de recherche associés sont ouverts en partenariat avec des opérateurs de centres de données, marquant l'apparition d'une filière de formation dédiée à l'exploitation d'usines informatiques. | premier cursus documenté en 2007 | M1, O7 | choc | [S7] | K |
| F.CLD.D2.003 | 2009-2011 | US, MONDE | Les termes « ingénierie de fiabilité des sites » et « exploitation par le développement » (DevOps) entrent dans le vocabulaire professionnel documenté par la presse technique et les premières conférences dédiées, désignant une fusion des rôles de développement et d'exploitation. | apparition documentée 2009 (terme DevOps, conférence dédiée) et pratique de « site reliability engineering » publiée à partir de 2010 par un grand opérateur | M1 | choc | [S8] | K |
| F.CLD.D2.004 | 2010-2013 | US | Le rôle d'« architecte cloud », distinct de l'administrateur système classique, apparaît dans les intitulés de poste et les référentiels de certification des grands fournisseurs de capacité louée. | apparition documentée dans les catalogues de certification à partir de 2010-2013 | M1 | choc | [S9] | K |
| F.CLD.D2.005 | 2010-2015 | US | Les principaux fournisseurs de capacité louée lancent des programmes de certification professionnelle sur leurs propres plateformes, dont le volume de certifiés délivrés croît sur la période sans qu'un chiffre agrégé comparable entre fournisseurs soit disponible dans une source officielle. | croissance du nombre de certifiés, valeur agrégée non disponible en source admissible | M1 | choc | [S9] | K |
| F.CLD.D2.006 | 2010 | US, EU | Le métier d'administrateur système bascule vers l'écriture de code de configuration et d'automatisation plutôt que l'intervention manuelle sur machine, changement documenté par les éditions successives du manuel professionnel de référence du Bureau of Labor Statistics. | bascule de pratique documentée dans les éditions 2008-2016 du manuel de référence | M1 | choc | [S3] | K |
| F.CLD.D2.007 | 2011-2015 | US | Le métier de « responsable de salle machine » ou d'opérateur de centre informatique interne à une organisation, courant avant t0, cesse d'apparaître comme catégorie distincte dans les descriptions de poste des grandes entreprises qui migrent vers des services loués, sans que son remplacement soit documenté par un chiffre agrégé unique. | déclin qualitatif documenté, pas de série chiffrée agrégée trouvée | M1 | choc | [S3] | K |
| F.CLD.D2.008 | 2008-2015 | US, MONDE | Les cours en ligne ouverts à grande échelle apparaissent à partir de 2008 et se multiplient à partir de 2011-2012, avec une offre orientée en bonne partie vers les compétences de programmation et d'administration de systèmes, canal de reconversion professionnelle vers les métiers informatiques. | apparition 2008, expansion à partir de 2011-2012 | M1, P2, P3 | co:X.CLD.06 | [S10] | K |
| F.CLD.D2.009 | 2014-2015 | US | L'adoption des conteneurs par les entreprises (Docker), mesurée sur un panel de 7 000 sociétés clientes d'un fournisseur de supervision d'infrastructure, passe de 1,8 % à 8,3 % des sociétés en un an, avec une adoption nettement plus forte chez les grandes infrastructures (43 % des sociétés à 100 hôtes ou plus, contre 11 % à moins de 50) ; signe indirect, faute de série officielle sur les intitulés de poste, de la diffusion rapide des compétences de conteneurisation et d'orchestration après celle des outils eux-mêmes (F.CLD.A2.005, F.CLD.A2.006). | 1,8 % (09/2014) → 8,3 % (09/2015) des sociétés du panel ; 43 % (≥100 hôtes) contre 11 % (<50 hôtes) | M1 | choc | [S22] | K |
| F.CLD.D2.010 | 2003-2004 | US | Avant t0 : la compétence recherchée dans les métiers informatiques reste centrée sur l'administration de matériel possédé et de réseaux internes, la certification de référence portant sur les systèmes d'exploitation et le matériel réseau plutôt que sur des services loués. | — | M1 | exo | [S3] | K |

### Jalons cités
<!-- Lines 135-140 -->

`J.CLD.2007.03` (premiers cursus et recherches sur le calcul distribué à très grande échelle),
`J.CLD.2010.06` (bascule du métier d'administrateur système vers le code de configuration),
`J.CLD.2015.06` (réorientation du métier de direction informatique vers la gestion de
fournisseurs).

### Trajectoire `T.CLD.D2`
<!-- Lines 143-158 -->

| année | phase | intensité | ce qui change | faits et jalons |
| --- | --- | --- | --- | --- |
| avant t0 | latent | 1 | Compétence centrée sur le matériel et le réseau possédés ; recul des inscriptions en informatique déjà entamé depuis le pic de 2003-04. | F.CLD.D2.010, F.CLD.D2.001 |
| 2005 | émergence | 0 | Poursuite du recul des diplômes informatiques, sans bascule de métier nouvelle documentée. | F.CLD.D2.001 |
| 2006 | émergence | 0 | Poursuite du recul des diplômes ; aucune bascule de métier nouvelle documentée. | F.CLD.D2.001 |
| 2007 | accélération | 2 | Premier cursus universitaire dédié au calcul distribué à très grande échelle, apparition d'une filière de formation propre au choc. | F.CLD.D2.002, J.CLD.2007.03 |
| 2008 | crise | 1 | Creux des diplômes informatiques proche du plancher de la décennie, en pleine crise financière. | F.CLD.D2.001 |
| 2009 | crise | 2 | Point bas des diplômes ; apparition des premiers cours en ligne ouverts à grande échelle et du vocabulaire DevOps. | F.CLD.D2.001, F.CLD.D2.003, F.CLD.D2.008 |
| 2010 | accélération | 3 | Reprise des inscriptions en informatique ; bascule documentée du métier d'administrateur système vers le code ; apparition du rôle d'architecte cloud. | F.CLD.D2.001, F.CLD.D2.004, F.CLD.D2.006, J.CLD.2010.06 |
| 2011 | accélération | 2 | Expansion des cours en ligne ouverts ; déclin documenté du métier d'opérateur de salle machine interne. | F.CLD.D2.007, F.CLD.D2.008 |
| 2012 | consolidation | 1 | Croissance des certifications de fournisseurs. | F.CLD.D2.005 |
| 2013 | consolidation | 1 | Poursuite de la reprise des diplômes informatiques ; poursuite de la diffusion des certifications. | F.CLD.D2.001, F.CLD.D2.005 |
| 2014 | consolidation | 2 | Poursuite de la reprise des diplômes ; début de la mesure de l'adoption des conteneurs par les entreprises, encore marginale à cette date (1,8 %). | F.CLD.D2.001, F.CLD.D2.009 |
| 2015 | banalisation | 3 | Les diplômes informatiques retrouvent quasiment leur niveau de 2003-04 ; l'adoption des conteneurs par les entreprises quintuple en un an (8,3 %), signe de la diffusion rapide des compétences associées ; la direction informatique devient un métier de gestion de fournisseurs. | F.CLD.D2.001, F.CLD.D2.009, J.CLD.2015.06 |

### Narratif
<!-- Lines 161-181 -->

Les diplômes universitaires en informatique reculent de 2003-04 à 2009-10 avant de regagner sur
cinq ans presque tout le terrain perdu, mouvement en U qui traverse toute la fenêtre du choc
cloud sans lui être entièrement imputable puisqu'il commence avant t0, dans le prolongement de la
correction du début des années 2000 [F.CLD.D2.001]. De nouveaux métiers apparaissent par étapes :
un cursus dédié au calcul distribué dès 2007 [F.CLD.D2.002, J.CLD.2007.03], un vocabulaire de
fusion entre développement et exploitation autour de 2009-2010 [F.CLD.D2.003], puis un rôle
d'architecte cloud distinct de l'administrateur système classique à partir de 2010
[F.CLD.D2.004]. Le métier le plus proche du choc change de nature documentée : l'administrateur
système passe de l'intervention manuelle sur machine à l'écriture de code de configuration
[F.CLD.D2.006, J.CLD.2010.06], pendant que le poste d'opérateur de salle machine interne décline
sans laisser de série chiffrée agrégée [F.CLD.D2.007]. Les cours en ligne ouverts à grande échelle
et les certifications de fournisseurs deviennent, à partir de 2011-2012, un canal de formation et
de reconversion vers ces métiers, sans qu'un volume agrégé comparable soit disponible en source
admissible [F.CLD.D2.005, F.CLD.D2.008]. En toute fin de fenêtre, l'adoption des conteneurs par les
entreprises quintuple en un an, de 1,8 % à 8,3 % d'un panel de 7 000 sociétés, signe indirect que la
diffusion des compétences de conteneurisation et d'orchestration suit de près celle des outils
eux-mêmes [F.CLD.D2.009].

---

## D3 Organisation du travail
<!-- Lines 184-186 -->

**Question :** Où, quand, avec quels outils et sous quel statut travaille-t-on ?

### Faits
<!-- Lines 189-201 -->

| id | année | bloc | énoncé | valeur | acteurs | attribution | source | statut |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| F.CLD.D3.001 | 2005 | US | Une équipe de trois personnes construit et exploite un service de partage vidéo à audience mondiale sans posséder d'infrastructure de diffusion, exemple documenté d'une équipe réduite par l'outillage loué. | 3 personnes | M1, O1 | choc | [S11] | K |
| F.CLD.D3.002 | 2012 | MONDE | Une application de partage de photographies grand public est exploitée par une équipe d'environ treize personnes au moment de son rachat, pour plusieurs centaines de millions d'usagers, en s'appuyant entièrement sur des services loués. | ~13 personnes | M1, O1 | choc | [S12] | K |
| F.CLD.D3.003 | 2006-2015 | MONDE | Les outils de bureautique et de communication hébergés (courriel, documents partagés, visioconférence) se diffusent sur la fenêtre comme condition technique du travail à distance, sans que la mesure statistique officielle du télétravail effectif progresse au même rythme sur cette période aux États-Unis. | diffusion technique documentée, mesure du télétravail effectif non disponible en série continue admissible | M1, M4, P3 | choc | [S13] | K |
| F.CLD.D3.004 | 2008-2015 | MONDE | L'économie de plateforme (hébergement de logement, transport, livraison) se développe sur la fenêtre en s'appuyant sur des services loués pour son fonctionnement technique ; le travail organisé par ces plateformes relève pour l'essentiel du confondant produit dérivé X.CLD.08, la contribution propre du cloud se limitant à l'infrastructure technique sous-jacente. | développement documenté qualitativement, pas de série d'emploi propre au cloud isolée | M7, O1 | co:X.CLD.08 | [S14] | K |
| F.CLD.D3.005 | 2008 | US | Les directions informatiques commencent à séparer explicitement dépense en capital et dépense de fonctionnement dans l'arbitrage « acheter ou louer », ce qui s'accompagne d'un déplacement de tâches auparavant internes (exploitation de matériel) vers des fournisseurs externes. | — | M1, O4 | co:X.CLD.03 | [S15] | K |
| F.CLD.D3.006 | 2010-2015 | US | L'astreinte et la surveillance continue de systèmes hébergés deviennent une pratique organisée et documentée (rotation d'astreinte, tableaux de service), à mesure que les services loués fonctionnent sans interruption planifiée par l'organisation cliente. | pratique documentée dans la littérature professionnelle, non chiffrée en heures agrégées | M1 | choc | [S8] | K |
| F.CLD.D3.007 | 2011 | US | Un outil de conteneurisation et de livraison continue réduit l'écart entre la machine du développeur et la machine de production, faisant passer le rythme de mise en production du trimestre à la journée dans les équipes qui l'adoptent, ce qui modifie l'organisation du travail de développement et d'exploitation en un seul flux. | trimestre → jour, dans les équipes adoptantes | M1 | choc | [S16] | K |
| F.CLD.D3.008 | 2012 | EMERG | Le secteur indien de sous-traitance informatique se réoriente de la gestion de parcs de serveurs pour compte de tiers vers l'intégration et l'exploitation de services loués, déplacement de nature de la tâche plutôt que de volume documenté sur cette seule année. | réorientation de la nature du travail | M1, T5 | choc | [S5] | K |
| F.CLD.D3.009 | 2003-2004 | US | Avant t0 : l'exploitation informatique d'une organisation est réalisée par son propre personnel sur son propre matériel, dans ses propres locaux, la frontière entre développement et exploitation étant nettement marquée par des équipes et des responsabilités distinctes. | — | M1, O4 | exo | [S3] | K |

### Jalons cités
<!-- Lines 204-209 -->

Aucun jalon de `par_annee/cloud_2005_2015.md` ne porte spécifiquement sur l'organisation du
travail (D3) ; les jalons `J.CLD.2010.06` (D2, cité en secondaire pour le déplacement de tâche) et
`J.CLD.2011.06` (A4, cité en secondaire pour le rythme de mise en production) éclairent la
sous-dimension sans lui être primaires.

### Trajectoire `T.CLD.D3`
<!-- Lines 212-227 -->

| année | phase | intensité | ce qui change | faits et jalons |
| --- | --- | --- | --- | --- |
| avant t0 | latent | 1 | Exploitation interne par du personnel dédié, frontière nette entre développement et exploitation. | F.CLD.D3.009 |
| 2005 | émergence | 2 | Une équipe de trois personnes exploite un service à audience mondiale sans infrastructure propre : premier exemple net d'équipe réduite par l'outillage loué. | F.CLD.D3.001 |
| 2006 | émergence | 1 | Diffusion des outils de bureautique hébergée comme condition technique du travail à distance. | F.CLD.D3.003 |
| 2007 | accélération | 0 | Diffusion continue des outils, pas de bascule organisationnelle nouvelle documentée cette année. | — |
| 2008 | crise | 2 | La crise financière accélère l'arbitrage capex/opex et le déplacement de tâches d'exploitation vers l'externe. | F.CLD.D3.005, F.CLD.D1.008 |
| 2009 | crise | 0 | Poursuite de la diffusion, pas de bascule organisationnelle nouvelle documentée cette année pour D3. | — |
| 2010 | accélération | 2 | L'astreinte et la surveillance continue de systèmes hébergés deviennent une pratique organisée. | F.CLD.D3.006 |
| 2011 | accélération | 2 | Le rythme de mise en production passe du trimestre à la journée, fusion opérationnelle du développement et de l'exploitation. | F.CLD.D3.007 |
| 2012 | consolidation | 2 | Cas limite d'équipe réduite (treize personnes pour plusieurs centaines de millions d'usagers) ; réorientation de la sous-traitance indienne vers l'intégration. | F.CLD.D3.002, F.CLD.D3.008 |
| 2013 | consolidation | 0 | Diffusion continue des pratiques précédentes, sans bascule nouvelle documentée. | — |
| 2014 | consolidation | 0 | Diffusion continue, sans bascule nouvelle documentée pour D3. | — |
| 2015 | banalisation | 1 | L'économie de plateforme adossée aux services loués est une pratique installée en fin de fenêtre, largement portée par le confondant produit dérivé. | F.CLD.D3.004 |

### Narratif
<!-- Lines 230-249 -->

L'outillage loué permet dès 2005 à une équipe de trois personnes d'exploiter un service à
audience mondiale, exemple limite d'une réduction de la taille d'équipe nécessaire pour produire
un service numérique [F.CLD.D3.001], confirmé en 2012 par une équipe d'une douzaine de personnes
servant plusieurs centaines de millions d'usagers [F.CLD.D3.002]. Le travail à distance est rendu
techniquement possible par la diffusion d'outils de bureautique et de communication hébergés dès
le milieu de la fenêtre, mais sa mesure statistique officielle ne progresse pas au même rythme sur
la période, ce qui empêche de chiffrer l'ampleur du changement [F.CLD.D3.003]. La frontière entre
développement et exploitation, nette avant t0, se dissout par étapes : délégation de la machine
[F.CLD.D3.005], astreinte organisée sur des systèmes en fonctionnement continu [F.CLD.D3.006],
puis fusion opérationnelle des deux métiers avec un rythme de mise en production quotidien
[F.CLD.D3.007]. L'économie du travail à la tâche adossée à des plateformes se développe sur la
même fenêtre, mais cette organisation du travail doit l'essentiel de sa forme au confondant
produit dérivé plutôt qu'à l'infrastructure louée elle-même [F.CLD.D3.004, X.CLD.08]. La
sous-traitance indienne change la nature de sa tâche, de la gestion de machines vers
l'intégration de services, sans que ce déplacement soit encore chiffré en volume sur la fenêtre
[F.CLD.D3.008].

---

## D4 Salaires, polarisation et rapport de force
<!-- Lines 252-254 -->

**Question :** Qui gagne plus, qui gagne moins, et comment le rapport de force évolue-t-il ?

### Faits
<!-- Lines 257-268 -->

| id | année | bloc | énoncé | valeur | acteurs | attribution | source | statut |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| F.CLD.D4.001 | 2003, 2005, 2008, 2010, 2013, 2015 | US | Série annuelle de la part du travail dans le secteur privé non agricole américain (« Private Nonfarm Business Sector: Labor Share »), U.S. Bureau of Labor Statistics via séries FRED : baisse continue sur toute la fenêtre, de 63,5 % en 2005 à un plancher de 60,7 % en 2013, avant une légère remontée à 61,5 % en 2015 ; la tendance est déjà amorcée avant t0 et se poursuit sans rupture visible attribuable au choc cloud lui-même. | 65,5 % (2003) ; 63,5 % (2005) ; 63,0 % (2008) ; 61,2 % (2010) ; 60,7 % (2013, creux) ; 61,5 % (2015) | M1, M9 | co:X.CLD.03 | [S17] | V |
| F.CLD.D4.002 | 2005-2015 | US | Les salaires moyens publiés par les enquêtes Occupational Employment Statistics pour les développeurs de logiciels se situent sur toute la fenêtre au-dessus de ceux des administrateurs systèmes et réseaux, écart documenté par le Bureau of Labor Statistics sans que la série année par année ait été extraite ici. | écart positif en faveur des développeurs, valeurs annuelles non extraites | M1 | choc | [S3] | K |
| F.CLD.D4.003 | 2014 | US | Les compétences liées au cloud et aux grands volumes de données (plateforme en tant que service, bases de données distribuées) figurent parmi les mieux payées du secteur informatique américain dans une enquête de rémunération d'un cabinet privé de recrutement technologique, avec un salaire annuel moyen très supérieur au salaire moyen tous métiers informatiques confondus de la même enquête (89 450 $) ; artefact de cabinet, faute de série officielle desagrégée par métier cloud en source admissible. | ex. 130 081 $ (PaaS) contre 89 450 $ (moyenne tous métiers informatiques), enquête 2014 | M1 | choc | [S23] | K |
| F.CLD.D4.004 | 2005-2015 | US | Les emplois des métiers du cloud et des grands opérateurs de centres de données se concentrent géographiquement dans un nombre restreint de métropoles technologiques et de régions à électricité bon marché, ce qui recoupe la concentration déjà connue de l'industrie technologique (A3) sans qu'un indice de concentration salariale officiel dédié n'ait été extrait ici. | concentration qualitative documentée | M1, M9 | choc | [S4] | K |
| F.CLD.D4.005 | 2005-2015 | US | Le taux de syndicalisation dans le secteur des services informatiques et de l'hébergement de données reste, sur toute la fenêtre, très inférieur à la moyenne du secteur privé américain, selon les séries de l'enquête sur la population active du Bureau of Labor Statistics, sans négociation collective significative documentée dans ce secteur sur la période. | taux de syndicalisation très inférieur à la moyenne du secteur privé | M1, O8 | exo | [S18] | K |
| F.CLD.D4.006 | 2011-2015 | US | Le personnel des entrepôts de logistique adossés au commerce en ligne (une partie du commerce que l'informatique en nuage rend possible via ses opérateurs) fait l'objet de reportages et d'enquêtes documentant des conditions de travail et un rythme de travail intenses, sans qu'un indicateur salarial ou de rapport de force chiffré et sourcé de façon admissible n'ait été identifié pour cette fenêtre précise. | conditions documentées qualitativement, indicateur chiffré non identifié en source admissible | M7 | co:X.CLD.01 | [S19] | K |
| F.CLD.D4.007 | 2008-2010 | US | La crise financière comprime les salaires nominaux et le pouvoir de négociation de la plupart des secteurs, y compris indirectement les métiers informatiques par le gel des embauches et des budgets, avant une reprise inégale des rémunérations à partir de 2010-2011 dans les métiers du cloud en croissance. | compression puis reprise inégale, valeurs non extraites | M1 | co:X.CLD.03 | [S17] | K |
| F.CLD.D4.008 | 1998, 2000, 2002, 2003, 2004 | US | Avant t0 : la part du travail dans le secteur privé non agricole américain est déjà en tendance baissière depuis 2001, après un pic local en 2000, tendance antérieure au choc cloud et attribuable pour partie à l'autre choc et à son cycle macroéconomique. | 67,4 % (1998) ; 67,7 % (2000, pic local) ; 66,6 % (2002) ; 65,5 % (2003) ; 65,1 % (2004) | M1, M9 | exo | [S17] | V |

### Jalons cités
<!-- Lines 271-276 -->

Aucun jalon de `par_annee/cloud_2005_2015.md` ne porte spécifiquement sur les salaires ou le
rapport de force (D4) ; le jalon `J.CLD.2015.06` (D2/D3, réorientation du métier de direction
informatique) est cité en secondaire pour son implication sur la structure des postes et donc
indirectement sur l'échelle salariale de ce métier.

### Trajectoire `T.CLD.D4`
<!-- Lines 279-294 -->

| année | phase | intensité | ce qui change | faits et jalons |
| --- | --- | --- | --- | --- |
| avant t0 | latent | 1 | La part du travail dans le secteur privé non agricole recule déjà depuis le pic de 2000 (67,7 %) jusqu'à 65,1 % en 2004, tendance antérieure au choc cloud liée à l'autre choc. | F.CLD.D4.008 |
| 2005 | émergence | 1 | La part du travail poursuit son recul à 63,5 % ; pas de bascule salariale nouvelle documentée pour D4 cette année. | F.CLD.D4.001 |
| 2006 | émergence | 0 | Poursuite de la tendance antérieure, sans bascule nouvelle documentée. | F.CLD.D4.001 |
| 2007 | accélération | 1 | Écart de rémunération entre développeurs et administrateurs systèmes déjà documenté par les séries professionnelles de la période. | F.CLD.D4.002 |
| 2008 | crise | 2 | La part du travail reste proche de 63,0 % ; la crise financière comprime les salaires et le pouvoir de négociation de la plupart des secteurs, y compris indirectement l'informatique. | F.CLD.D4.001, F.CLD.D4.007, F.CLD.D1.008 |
| 2009 | crise | 2 | Poursuite de la compression salariale au creux de la récession. | F.CLD.D4.007 |
| 2010 | accélération | 2 | La part du travail chute à 61,2 %, accélération nette de la baisse pendant la reprise ; reprise inégale des rémunérations, plus marquée dans les métiers du cloud en croissance. | F.CLD.D4.001, F.CLD.D4.007 |
| 2011 | accélération | 1 | Concentration géographique des emplois qualifiés du cloud dans un nombre restreint de métropoles et de régions énergétiques. | F.CLD.D4.004 |
| 2012 | consolidation | 0 | Poursuite des tendances précédentes, sans bascule salariale nouvelle documentée pour D4 cette année. | — |
| 2013 | consolidation | 1 | La part du travail atteint son plancher de la fenêtre à 60,7 %, sans bascule salariale nouvelle documentée par ailleurs pour D4. | F.CLD.D4.001 |
| 2014 | consolidation | 2 | Une enquête de rémunération de cabinet privé confirme la prime salariale des compétences cloud et données massives sur la moyenne des métiers informatiques. | F.CLD.D4.003 |
| 2015 | banalisation | 1 | La part du travail remonte légèrement à 61,5 %, premier infléchissement de la fenêtre ; le taux de syndicalisation du secteur reste très inférieur à la moyenne du secteur privé et la réorientation du métier de direction informatique consolide une nouvelle échelle salariale de gestion de fournisseurs. | F.CLD.D4.001, F.CLD.D4.005, J.CLD.2015.06 |

### Narratif
<!-- Lines 297-318 -->

La part du travail dans le secteur privé non agricole américain recule sans interruption de 65,1 %
en 2004 à un plancher de 60,7 % en 2013, avant une légère remontée à 61,5 % en 2015 ; le recul
commence avant t0, dès 2001, ce qui interdit d'attribuer ce mouvement de longue durée au cloud sans
réserve, la crise financière de 2008-2010 en expliquant une part importante de l'accélération
observée entre 2008 (63,0 %) et 2010 (61,2 %) [F.CLD.D4.008, F.CLD.D4.001]. Un écart de
rémunération entre développeurs et administrateurs systèmes et réseaux se maintient sur toute la
période dans les séries professionnelles consultées [F.CLD.D4.002], et une enquête de cabinet privé
de 2014 situe les compétences cloud et données massives parmi les mieux payées du secteur
informatique américain, très au-dessus du salaire moyen tous métiers informatiques confondus de la
même enquête [F.CLD.D4.003]. La crise financière comprime les salaires et le rapport de force de
la plupart des secteurs entre 2008 et 2010, avant une reprise inégale qui favorise davantage les
métiers du cloud en croissance que les métiers informatiques traditionnels [F.CLD.D4.007]. Les
emplois qualifiés du secteur se concentrent géographiquement dans un nombre restreint de
métropoles, et la syndicalisation y reste marginale sur toute la fenêtre, sans négociation
collective documentée [F.CLD.D4.004, F.CLD.D4.005]. Le rapport de force dans les entrepôts de
logistique adossés au commerce en ligne fait l'objet de constats qualitatifs répétés, mais aucun
indicateur chiffré et sourcé de façon admissible n'a été identifié pour cette fenêtre précise, ce
qui laisse cette partie du domaine sans mesure directe [F.CLD.D4.006].

---

## Sources
<!-- Lines 321-346 -->

| clé | type | référence | note |
| --- | --- | --- | --- |
| [S1] | stat | U.S. Bureau of Labor Statistics, série d'emploi annuel « Employment for Professional, Scientific, and Technical Services: Computer Systems Design and Related Services (NAICS 5415) », diffusée via FRED (Federal Reserve Bank of St. Louis), série IPUMN5415W200000000, milliers d'emplois, non désaisonnalisée, 1987-2024 | Vérifié directement par WebFetch sur le point de sortie CSV de FRED (fredgraph.csv?id=IPUMN5415W200000000) et sur la page de la série : titre exact, unité et valeurs annuelles confirmés. |
| [S2] | stat | U.S. Bureau of Labor Statistics, série d'emploi annuel « Employment for Information: Data Processing, Hosting, and Related Services (NAICS 518) », diffusée via FRED, série IPUJN518W200000000, milliers d'emplois, non désaisonnalisée, 1987-2024 | Vérifié directement par WebFetch sur le point de sortie CSV de FRED (fredgraph.csv?id=IPUJN518W200000000) et sur la page de la série : titre exact, unité et valeurs annuelles confirmés. |
| [S3] | stat | U.S. Bureau of Labor Statistics, Occupational Employment and Wage Statistics (OEWS/OES) et Occupational Outlook Handbook, professions « Network and Computer Systems Administrators » (SOC 15-1142) et « Software Developers » (SOC 15-1132/15-1133), éditions et séries 2007-2016 | Repris en partie de [S31] de `par_dimension/A_industrie/cloud.md`. Les pages BLS consultées par WebFetch (oes/tables.htm, oes/current/*.htm, data.bls.gov/oes) ne rendent que des liens vers des fichiers XLSX ou des données très récentes (2025-2026) ; les valeurs 2005-2015 par occupation n'ont pas pu être extraites par ce canal. Statut K, à vérifier sur les fichiers XLSX archivés hors WebFetch. |
| [S4] | acad | Travaux et rapports d'ingénierie sur l'emploi de construction et d'exploitation des centres de données de grande taille, 2008-2015 | Ordre de grandeur qualitatif largement rapporté dans la littérature professionnelle et académique sur l'emploi local des centres de données ; pas de chiffre unique agrégé trouvé en source admissible sur la fenêtre. À vérifier. |
| [S5] | stat | NASSCOM, rapports annuels sur le secteur indien des services informatiques, 2008-2015 | Repris de [S40] de `par_dimension/A_industrie/cloud.md`. Effectifs sectoriels à extraire précisément ; non fait dans cette cellule. |
| [S6] | off | National Center for Education Statistics, *Digest of Education Statistics*, Table 325.35, « Degrees in computer and information sciences conferred by postsecondary institutions, by level of degree and sex of student: 1970-71 through 2014-15 » | Vérifié directement par WebFetch sur nces.ed.gov (dt16_325.35.asp) : titre de table, source IPEDS Completions component, et série de valeurs par année académique confirmés. Valeurs de licence citées : 59 488 (2003-04) à 37 992 (2008-09, creux) puis 59 581 (2014-15). |
| [S7] | acad | Programmes universitaires en calcul distribué à grande échelle, partenariats avec des opérateurs de centres de données, 2007 | Repris de [S16] de `par_dimension/A_industrie/cloud.md` et de `par_annee/cloud_2005_2015.md` (J.CLD.2007.03). À vérifier. |
| [S8] | presse | Presse technique et actes de conférence sur l'apparition des termes « DevOps » (2009) et « site reliability engineering » (publication d'un grand opérateur à partir de 2010) | Dates à vérifier précisément ; formulé au niveau du mouvement plutôt que d'un événement unique. |
| [S9] | off | Catalogues de certification professionnelle des principaux fournisseurs de capacité louée, 2010-2015 | Existence des programmes vérifiable publiquement ; volumes de certifiés délivrés non publiés de façon comparable entre fournisseurs sur la fenêtre. |
| [S10] | presse | Presse technique contemporaine du lancement des premières plateformes de cours en ligne ouverts à grande échelle, 2008 puis 2011-2012 | Dates à vérifier ; le contenu orienté vers les compétences informatiques est une caractéristique documentée qualitativement. |
| [S11] | presse | Presse économique contemporaine du lancement de YouTube, 2005-2006 | Repris de [S9] de `par_dimension/A_industrie/cloud.md`. |
| [S12] | off | Communiqués et presse contemporaine du rachat d'Instagram, avril 2012 | Repris de [S29] (note) de `par_dimension/A_industrie/cloud.md`. Taille d'équipe à vérifier précisément sur la presse contemporaine du rachat. |
| [S13] | acad | Enquêtes sur le télétravail et les technologies de collaboration hébergées dans les organisations américaines et européennes, 2006-2015 | Généralité qualitative ; l'absence de série continue et comparable de mesure du télétravail sur la fenêtre est elle-même le constat retenu. |
| [S14] | off | Documentation et rapports sur l'économie de plateforme (hébergement, transport, livraison), 2008-2015, voir X.CLD.08 dans 04_confondants.md | Le cloud y apparaît comme infrastructure technique sous-jacente, non comme cause principale de l'organisation du travail documentée. |
| [S15] | acad | Travaux et enquêtes sur l'arbitrage dépenses en capital contre dépenses de fonctionnement dans les directions informatiques, 2008-2012 | Repris de [S21] de `par_dimension/A_industrie/cloud.md`. |
| [S16] | presse | Presse technique contemporaine des lancements de Jenkins, Vagrant et Docker, 2011-2013 | Repris de [S37] de `par_dimension/A_industrie/cloud.md`. |
| [S17] | stat | U.S. Bureau of Labor Statistics, série annuelle « Private Nonfarm Business Sector: Labor Share », diffusée via FRED, série MPU4910141, pourcentage, non désaisonnalisée, 1987-2024 | Vérifié directement par WebFetch sur le point de sortie CSV de FRED (fredgraph.csv?id=MPU4910141) : fichier brut lu intégralement (observation_date, valeur), série continue de 1987 à 2024 confirmée. Une première tentative sur les pages HTML de bea.gov et sur la page interactive de FRED avait échoué (404, ou seules les valeurs les plus récentes rendues) ; le point de sortie CSV direct a résolu le blocage. |
| [S18] | stat | U.S. Bureau of Labor Statistics, Current Population Survey, taux de syndicalisation par secteur d'activité, séries 2003-2015 | Série publique connue (taux de syndicalisation du secteur de l'information et des services informatiques très inférieur à la moyenne du secteur privé) ; non extraite ligne à ligne. À vérifier. |
| [S19] | presse | Reportages et enquêtes contemporains sur les conditions de travail dans les entrepôts de logistique du commerce en ligne, 2011-2015 | Généralité qualitative largement documentée dans la presse économique et sociale de la période ; pas d'indicateur chiffré unique et sourcé de façon admissible identifié pour cette fenêtre précise. |
| [S20] | stat | U.S. Bureau of Labor Statistics, Current Population Survey, série annuelle « Employed full time: Wage and salary workers: Software developers, applications and systems software occupations: 16 years and over », diffusée via FRED, série LEU0254477200A, milliers de personnes, 2000-2019 | Vérifié directement par WebFetch sur le point de sortie CSV de FRED (fredgraph.csv?id=LEU0254477200A) : valeurs annuelles 2003-2015 confirmées. Série apparentée pour l'ensemble des professions informatiques et mathématiques (LEU0254476900A) consultée de la même façon pour comparaison, non reprise en fait séparé. |
| [S21] | acad | Sundharan, Sajikumar, « Structure, Growth and Performance of Indian IT-BPO Industry », *International Journal of Economics, Commerce and Management*, vol. I, n° 2, 2013, citant National Association of Software and Service Companies (NASSCOM), *Strategic Review 2012* | Article académique ouvert et lu intégralement en PDF (WebFetch puis lecture directe du fichier) : Table 6 (« Knowledge professionals in IT-BPO sector », milliers, 2008-2012) et texte p. 11 (2,8 millions d'emplois directs et 8,9 millions indirects en 2012) confirmés. Donnée de seconde main (NASSCOM via l'article), non le rapport NASSCOM original ; limite de fiabilité signalée par l'auteur lui-même (note 3 de l'article) faute de source de validation croisée pour les chiffres NASSCOM. |
| [S22] | presse | Datadog, « 8 Surprising Facts About Real Docker Adoption », rapport annuel, 2015 (datadoghq.com/docker-adoption-2015) | Ouvert et lu le 2026-09-22 : datadoghq.com/docker-adoption-2015 ; panel de 7 000 sociétés clientes, adoption de Docker en hausse de 1,8 % (09/2014) à 8,3 % (09/2015) des sociétés, présence sur 6 % des hôtes supervisés ; adoption croissante avec la taille d'infrastructure (11 % pour 1-49 hôtes, 22 % pour 50-99, 43 % pour 100+). Rapport d'entreprise assimilé à un rapport annuel d'activité pour cette mesure ; pas de série officielle équivalente identifiée sur les intitulés de poste. Statut `K`, étiqueté **artefact** (coordinateur, 2026-09-22) : étude d'un fournisseur sur sa propre clientèle, non admissible comme source `V` (R2) ; seule mesure disponible. |
| [S23] | stat | Dice.com, *Dice Tech Salary Survey*, enquête menée du 29 septembre au 26 novembre 2014 auprès de 23 470 professionnels techniques, publiée le 22 janvier 2015 (dice.com/career-advice/dice-salary-survey-good-times-for-tech-pros) | Ouvert et lu le 2026-09-22 : dice.com/career-advice/dice-salary-survey-good-times-for-tech-pros ; salaire moyen 2014 tous métiers informatiques confondus 89 450 $ ; salaires les plus élevés pour les compétences cloud et données massives, dont PaaS à 130 081 $. K, artefact de cabinet de recrutement (R2, exception « artefact ») faute de série officielle desagrégée par métier cloud. |
