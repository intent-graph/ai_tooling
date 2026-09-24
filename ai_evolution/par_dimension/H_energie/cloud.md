# H. Énergie — Cloud 2005-2015

Ce que le domaine énergie a connu pendant la fenêtre cloud, sous-dimension par sous-dimension :
faits sourcés, jalons cités, trajectoire année par année, narratif court. Le cloud est
l'industrialisation de l'informatique : ses usines — centres de données, plateformes — sont, au
sens propre, des convertisseurs d'électricité en service numérique. Cette cellule porte la
matière du test de l'hypothèse H5 (pas de choc de productivité sans changement énergétique) ; elle
documente, elle ne conclut pas. Ligne de base : état des deux années précédant t0 (2003-2004).

## Table of Contents

1. [H1 Consommation et efficacité de l'appareil numérique](#h1-consommation-et-efficacit-de-l-appareil-num-rique) _(Lines 40-43)_
   1. [Faits](#faits) _(Lines 46-58)_
   1. [Jalons cités](#jalons-cit-s) _(Lines 61-66)_
   1. [Trajectoire `T.CLD.H1`](#trajectoire-t-cld-h1) _(Lines 69-84)_
   1. [Narratif](#narratif) _(Lines 87-106)_
1. [H2 Énergie comme contrainte et facteur de localisation](#h2-nergie-comme-contrainte-et-facteur-de-localisation) _(Lines 109-112)_
   1. [Faits](#faits-1) _(Lines 115-125)_
   1. [Jalons cités](#jalons-cit-s-1) _(Lines 128-132)_
   1. [Trajectoire `T.CLD.H2`](#trajectoire-t-cld-h2) _(Lines 135-150)_
   1. [Narratif](#narratif-1) _(Lines 153-168)_
1. [H3 Contexte énergétique macro : prix, mix, abondance](#h3-contexte-nerg-tique-macro-prix-mix-abondance) _(Lines 171-174)_
   1. [Faits](#faits-2) _(Lines 177-189)_
   1. [Jalons cités](#jalons-cit-s-2) _(Lines 192-196)_
   1. [Trajectoire `T.CLD.H3`](#trajectoire-t-cld-h3) _(Lines 199-214)_
   1. [Narratif](#narratif-2) _(Lines 217-234)_
1. [H4 Effets du choc sur l'énergie du reste de l'économie](#h4-effets-du-choc-sur-l-nergie-du-reste-de-l-conomie) _(Lines 237-239)_
   1. [Faits](#faits-3) _(Lines 242-250)_
   1. [Jalons cités](#jalons-cit-s-3) _(Lines 253-256)_
   1. [Trajectoire `T.CLD.H4`](#trajectoire-t-cld-h4) _(Lines 259-274)_
   1. [Narratif](#narratif-3) _(Lines 277-292)_
1. [Sources](#sources) _(Lines 295-315)_



---

## H1 Consommation et efficacité de l'appareil numérique
<!-- Lines 40-43 -->

**Question :** Combien d'énergie consomment réseaux, terminaux et centres de données, et à quel
rythme l'efficacité par unité de service progresse-t-elle ?

### Faits
<!-- Lines 46-58 -->

| id | année | bloc | énoncé | valeur | acteurs | attribution | source | statut |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| F.CLD.H1.001 | 2000-2006 | US | La consommation électrique des serveurs et centres de données double aux États-Unis, avant de se stabiliser en croissance sur la décennie 2000. | 61 TWh en 2006, contre environ 30 TWh en 2000 ; 1,5 % de l'électricité nationale | O6, O2, M10 | choc | [S1] | V |
| F.CLD.H1.002 | 2000-2005 | MONDE, US | La consommation électrique des centres de données double au début de la fenêtre (installations et croissance de l'électricité par serveur), avant l'inflexion mesurée ensuite. | doublement 2000-2005, monde et US | O2, O7 | choc | [S2] | V |
| F.CLD.H1.003 | 2005-2010 | MONDE, US | La consommation électrique des centres de données continue de croître mais à un rythme nettement inférieur à celui de 2000-2005 (doublement), malgré la forte hausse du nombre de services hébergés. | +56 % monde, +36 % US sur 2005-2010 (estimation médiane entre bornes basse et haute) | O2, O7 | choc | [S2] | V |
| F.CLD.H1.004 | 2000-2014 | US | Une étude couvrant 2000-2014 confirme un découplage : le nombre de serveurs installés et le trafic de données croissent bien plus vite que la consommation électrique des centres de données sur la seconde moitié de la période. | consommation des centres de données américains ~70 milliards de kWh en 2014 (environ 1,8 % de l'électricité américaine), quasi stable depuis 2010 après un plateau amorcé en 2008 | O2, O7 | choc | [S3] | V |
| F.CLD.H1.005 | 2007-2008 | US | Une métrique commune d'efficacité des installations est adoptée par un consortium industriel, rapportant l'énergie totale du site à celle des équipements informatiques. | indicateur PUE, valeur de référence 1,0 = efficacité parfaite | O2, O3, M1 | choc | [S4] | K |
| F.CLD.H1.006 | 2008-2014 | US, MONDE | Le PUE moyen déclaré par un grand exploitant pour sa flotte de centres de données passe d'environ 1,20 en 2008 à environ 1,12 en 2014, contre une moyenne sectorielle alors estimée entre 1,8 et 2,0 pour les installations d'entreprise plus anciennes. | PUE flotte : ~1,20 (2008, T4) → 1,12 (2014, constant sur l'année) | O2 | choc | [S5] | V |
| F.CLD.H1.007 | 2010 | US | Un exploitant publie que ses centres de données consomment moins d'électricité par requête que ne l'affirment les estimations publiques contemporaines, en s'appuyant sur ses propres compteurs. | non chiffré ici, écart qualitatif entre estimation externe et mesure interne ; cohérent avec Koomey 2011 qui chiffre l'électricité de ce même exploitant à moins de 1 % de la consommation mondiale des centres de données en 2010 | O2 | choc | [S2] | K |
| F.CLD.H1.008 | 2011 | US, MONDE | Une étude indépendante conclut que la croissance de la consommation électrique des centres de données entre 2005 et 2010 (+56 % monde, +36 % US, estimation médiane) est très inférieure aux projections faites en 2007 sur la base de la tendance 2000-2005 (doublement), qui annonçaient elles-mêmes un nouveau doublement d'ici 2010-2011. | croissance réelle 2005-2010 : +56 % monde / +36 % US, contre un doublement projeté | O2, O7 | choc | [S2] | V |
| F.CLD.H1.009 | 2013-2014 | US | Les centres de données représentent une part stable de l'électricité consommée aux États-Unis malgré la croissance du nombre de services hébergés. | environ 1,8 % de l'électricité américaine en 2014 (70 milliards de kWh) | O2, O6 | choc | [S3] | V |

### Jalons cités
<!-- Lines 61-66 -->

`J.CLD.2007.06` (bascule principale : premier chiffrage officiel américain, 2007), `J.CLD.2007.07`
(métrique d'efficacité PUE), `J.CLD.2008.07` (premier exploitant publiant son PUE mesuré),
`J.CLD.2010.04` (les centres de données entrent dans les comptes énergétiques nationaux),
`J.CLD.2011.07` (étude indépendante sur le découplage 2005-2010).

### Trajectoire `T.CLD.H1`
<!-- Lines 69-84 -->

| année | phase | intensité | ce qui change | faits et jalons |
| --- | --- | --- | --- | --- |
| avant t0 | latent | 1 | La consommation des serveurs et centres de données double entre 2000 et 2004-2006 aux États-Unis, sans mesure officielle ni métrique d'efficacité partagée ; le sujet reste technique et interne. | F.CLD.H1.001, F.CLD.H1.002 |
| 2005 | émergence | 1 | Un opérateur commence à publier ses gains de densité et d'efficacité comme avantage industriel : l'énergie devient une variable de compétitivité affichée. | J.CLD.2005.03 |
| 2006 | émergence | 1 | Pas de rupture de mesure ; la croissance de la consommation se poursuit sur sa tendance de la première moitié de la décennie. | F.CLD.H1.002 |
| 2007 | accélération | 3 | Premier chiffrage officiel américain de la consommation des serveurs et centres de données (61 TWh, 1,5 % de l'électricité nationale) ; un consortium publie la métrique PUE. Le sujet entre dans la statistique publique et se dote d'un outil de mesure comparable. | F.CLD.H1.001, J.CLD.2007.06, J.CLD.2007.07, F.CLD.H1.005 |
| 2008 | accélération | 2 | Un grand exploitant publie pour la première fois son PUE mesuré, nettement meilleur que la moyenne du secteur ; l'efficacité devient un argument public. | J.CLD.2008.07, F.CLD.H1.006 |
| 2009 | consolidation | 0 | Pas de jalon propre à H1 ; la trajectoire d'efficacité se poursuit sans rupture visible. | |
| 2010 | consolidation | 2 | Le nombre et la consommation des très grands centres de données deviennent un objet de mesure publique et de politique énergétique ; un exploitant conteste les estimations externes avec ses propres compteurs. | J.CLD.2010.04, F.CLD.H1.007 |
| 2011 | consolidation | 3 | Une étude indépendante établit le résultat central pour H5 : la consommation 2005-2010 a crû bien moins que projeté et bien moins que 2000-2005, malgré l'explosion du service rendu — découplage mesuré. | J.CLD.2011.07, F.CLD.H1.003, F.CLD.H1.008 |
| 2012 | banalisation | 0 | Pas de jalon propre ; la trajectoire d'efficacité se poursuit, moins commentée publiquement que la contrainte de localisation (H2). | |
| 2013 | banalisation | 1 | La part des centres de données dans l'électricité américaine reste stable en proportion malgré la croissance du service hébergé. | F.CLD.H1.009 |
| 2014 | banalisation | 2 | Une étude couvrant 2000-2014 confirme la quasi-stabilité de la consommation mondiale des centres de données sur 2010-2014, malgré la poursuite de la croissance du trafic et des serveurs. | F.CLD.H1.004 |
| 2015 | banalisation | 1 | État final : le PUE moyen des grands exploitants s'est rapproché de 1,1-1,2 ; la mesure de l'efficacité et le découplage consommation/service sont des faits établis pour l'épicentre du choc, moins documentés hors des très grands exploitants. | F.CLD.H1.006 |

### Narratif
<!-- Lines 87-106 -->

La consommation électrique des centres de données double aux États-Unis entre 2000 et 2006, avant
qu'un chiffrage officiel n'entre dans la statistique publique en 2007 [F.CLD.H1.001][J.CLD.2007.06].
La même année, un consortium industriel publie une métrique d'efficacité commune, ce qui rend
l'amélioration mesurable et pilotable [J.CLD.2007.07][F.CLD.H1.005]. Entre 2005 et 2010, la
consommation croît beaucoup moins vite qu'entre 2000 et 2005 (doublement) : +56 % au niveau
mondial et +36 % aux États-Unis, un résultat confirmé par une étude indépendante de 2011 qui
contredit les projections faites en 2007 sur la simple extrapolation de tendance, lesquelles
annonçaient un nouveau doublement [F.CLD.H1.002][F.CLD.H1.003][J.CLD.2011.07][F.CLD.H1.008]. Le
PUE moyen trimestriel du plus grand exploitant suivi passe de 1,20 fin 2008 à 1,12 en 2014, contre
une moyenne sectorielle alors estimée à près du double [F.CLD.H1.006]. Une étude couvrant
2000-2014 prolonge ce constat : la consommation des centres de données américains atteint un
plateau autour de 67-70 milliards de kWh entre 2008 et 2014 (environ 1,8 % de l'électricité
américaine en 2014), quasi stable depuis 2010 malgré la croissance continue du trafic et du
nombre de serveurs [F.CLD.H1.004]. La fenêtre montre donc un écart croissant entre affirmations
publiques anciennes sur une consommation qui doublerait mécaniquement et mesures qui montrent un
découplage progressif [F.CLD.H1.007][F.CLD.H1.009].

---

## H2 Énergie comme contrainte et facteur de localisation
<!-- Lines 109-112 -->

**Question :** Où et pourquoi les usines s'installent-elles ; l'accès à l'électricité borne-t-il
la croissance ?

### Faits
<!-- Lines 115-125 -->

| id | année | bloc | énoncé | valeur | acteurs | attribution | source | statut |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| F.CLD.H2.001 | 2006-2008 | US | Des exploitants implantent de nouveaux centres de données près de barrages hydroélectriques dans le nord-ouest des États-Unis, motivés par le prix bas et la stabilité de l'électricité. | non chiffré | O2 | choc | [S7] | K |
| F.CLD.H2.002 | 2010 | EU | Des implantations sont ouvertes en Scandinavie et en Islande, motivées par le refroidissement naturel du climat froid et une électricité abondante et largement décarbonée (hydroélectricité, géothermie). | non chiffré | O2, T2 | choc | [S8] | K |
| F.CLD.H2.003 | 2010 | US | Un exploitant d'usines signe un contrat d'achat d'électricité éolienne de longue durée, en direct avec un producteur, hors du réseau public standard. | premier contrat de ce type identifié pour un exploitant de centres de données, volume non retrouvé | O2, O3 | choc | [S9] | K |
| F.CLD.H2.004 | 2011-2015 | US, MONDE | Le nombre cumulé de contrats d'achat d'électricité renouvelable de long terme signés par des exploitants de centres de données croît chaque année sur la période, sans qu'un décompte annuel précis soit disponible dans cette collecte. | tendance croissante, valeurs annuelles non retrouvées | O2, O3 | choc | [S9] | K |
| F.CLD.H2.005 | 2010-2013 | US, EU | Le prix de l'électricité industrielle reste durablement inférieur aux États-Unis par rapport à l'Europe pendant la période, un écart qui pèse sur les choix de localisation des exploitants américains. | écart en faveur des États-Unis ; valeurs précises en H3 (F.CLD.H3.006 à H3.008) | O2, O3, T1, T2 | co:X.CLD.11 | [S10] | K |
| F.CLD.H2.006 | 2010 | MONDE | Une organisation environnementale publie un classement des grands exploitants selon l'origine (mix) de l'électricité de leurs centres de données, ce qui rend la localisation un sujet d'opinion publique en plus d'un choix industriel. | non chiffré | O8, O2 | choc | [S11] | K |
| F.CLD.H2.007 | 2007-2015 | US | Des raccordements électriques dédiés de forte puissance sont négociés directement entre exploitants et distributeurs locaux pour les plus grands sites, indiquant que l'accès à une capacité électrique suffisante devient un critère de site au même titre que le foncier et la fibre. | puissances de site rapportées en dizaines à centaines de mégawatts pour les plus grands campus en fin de période, valeur non vérifiée précisément | O2, O3 | choc | [S7] | K |

### Jalons cités
<!-- Lines 128-132 -->

`J.CLD.2010.07` (bascule principale : premier contrat d'achat d'électricité éolienne d'un
exploitant), `J.CLD.2011.08` (implantations Scandinavie/Islande, refroidissement et électricité
décarbonée), `J.CLD.2010.08` (classement Greenpeace du mix électrique des exploitants).

### Trajectoire `T.CLD.H2`
<!-- Lines 135-150 -->

| année | phase | intensité | ce qui change | faits et jalons |
| --- | --- | --- | --- | --- |
| avant t0 | latent | 0 | Les centres de données sont dimensionnés pour la proximité des usagers et le coût immobilier ; l'électricité est un intrant de réseau standard, non un critère de site différenciant. | |
| 2005 | latent | 1 | Un opérateur commence à publier ses gains de densité et d'efficacité, signe que l'énergie devient un paramètre de conception d'usine. | J.CLD.2005.03 |
| 2006 | émergence | 2 | Des implantations près de sources hydroélectriques bon marché apparaissent dans le nord-ouest américain. | F.CLD.H2.001 |
| 2007 | émergence | 1 | Pas de jalon propre à H2 ; la logique de localisation par le prix de l'électricité se poursuit (implantations hydroélectriques toujours actives) et les raccordements dédiés de forte puissance commencent à être négociés. | F.CLD.H2.001, F.CLD.H2.007 |
| 2008 | émergence | 1 | Pas de jalon propre à H2 ; contexte de prix de l'énergie très volatil (voir H3) ; implantations hydroélectriques et raccordements dédiés se poursuivent. | F.CLD.H2.001, F.CLD.H2.007 |
| 2009 | émergence | 0 | Pas de jalon propre à H2. | |
| 2010 | accélération | 3 | Bascule : l'exploitant devient acheteur d'électricité de gros par contrat direct plutôt que simple abonné du réseau ; le mix électrique des exploitants devient un sujet de campagne publique. | J.CLD.2010.07, J.CLD.2010.08, F.CLD.H2.006 |
| 2011 | accélération | 3 | Des implantations en Scandinavie et en Islande confirment que climat froid et électricité décarbonée sont des facteurs de localisation à part entière. | J.CLD.2011.08, F.CLD.H2.002 |
| 2012 | consolidation | 0 | Pas de jalon propre à H2 identifié dans la chronologie. | |
| 2013 | consolidation | 2 | L'écart de prix de l'électricité industrielle entre États-Unis et Europe, ouvert par le gaz de schiste, pèse sur la localisation des nouvelles usines. | F.CLD.H2.005 |
| 2014 | consolidation | 1 | Pas de jalon propre à H2 identifié dans la chronologie ; les raccordements électriques dédiés de forte puissance continuent d'être négociés pour les plus grands campus. | F.CLD.H2.007 |
| 2015 | banalisation | 2 | État final : les contrats d'achat d'électricité renouvelable et le choix du site par le climat et le prix de l'électricité sont des pratiques établies chez les grands exploitants ; la baisse du coût du solaire (H3) desserre la contrainte. | F.CLD.H2.004, J.CLD.2015.07 |

### Narratif
<!-- Lines 153-168 -->

Le facteur énergétique de localisation apparaît tôt dans la fenêtre avec des implantations près de
barrages hydroélectriques bon marché [F.CLD.H2.001], mais la bascule se produit en 2010 quand un
exploitant signe un contrat d'achat d'électricité renouvelable de longue durée, devenant acheteur
de gros plutôt que simple abonné du réseau [J.CLD.2010.07]. La même année, une organisation
environnementale fait du mix électrique des exploitants un sujet d'opinion publique
[J.CLD.2010.08][F.CLD.H2.006]. En 2011, des implantations en Scandinavie et en Islande confirment
que le climat froid et une électricité décarbonée sont devenus des critères de site à part entière
[J.CLD.2011.08]. À partir de 2013, l'écart de prix de l'électricité industrielle entre les
États-Unis et l'Europe, ouvert par le gaz de schiste, pèse sur les choix de localisation
[F.CLD.H2.005][co:X.CLD.11]. La collecte n'a pas retrouvé de décompte annuel précis des volumes
cumulés d'électricité renouvelable contractée : la tendance est établie qualitativement, pas
chiffrée année par année [F.CLD.H2.004].

---

## H3 Contexte énergétique macro : prix, mix, abondance
<!-- Lines 171-174 -->

**Question :** Dans quel environnement énergétique le choc se déploie-t-il, et cet environnement
change-t-il pendant la fenêtre ?

### Faits
<!-- Lines 177-189 -->

| id | année | bloc | énoncé | valeur | acteurs | attribution | source | statut |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| F.CLD.H3.001 | 2004, 2008, 2015 | US, MONDE | Le prix au comptant du pétrole brut WTI passe d'un niveau modéré en 2004 à un sommet en 2008 puis retombe à un creux en fin de fenêtre. | 41,51 $/baril (2004) ; 99,67 $/baril (2008) ; 48,66 $/baril (2015) | T1, T2 | exo | [S12] | V |
| F.CLD.H3.002 | 2008 | MONDE | Le prix du baril de WTI atteint son point le plus haut de la fenêtre avant de s'effondrer avec la crise financière et la récession. | pic annuel moyen 99,67 $/baril en 2008 | T1 | exo | [S12] | V |
| F.CLD.H3.003 | 2005, 2009, 2015 | US | Le prix au comptant du gaz naturel Henry Hub recule fortement entre le sommet du milieu de fenêtre et sa fin, sous l'effet de la production de gaz de schiste. | 8,69 $/MBtu (2005) ; 3,94 $/MBtu (2009) ; 2,52 $/MBtu (2015) | T1 | exo | [S13] | V |
| F.CLD.H3.004 | 2005-2015 | US | Le prix du gaz Henry Hub, après un sommet en 2008, entame une baisse quasi continue jusqu'à la fin de la fenêtre, portée par l'essor de l'extraction non conventionnelle. | 8,86 $/MBtu (2008) → 2,52 $/MBtu (2015), soit une division par environ 3,5 | T1 | exo | [S13] | V |
| F.CLD.H3.005 | 2014, 2015 | US | Le prix moyen de l'électricité au secteur industriel américain recule légèrement en fin de fenêtre. | 7,10 ¢/kWh (2014) ; 6,91 ¢/kWh (2015) | T1 | exo | [S14] | V |
| F.CLD.H3.006 | 2005-2015 | US, EU | Le prix de l'électricité industrielle demeure sur toute la période sensiblement plus bas aux États-Unis qu'en Europe, écart documenté par les séries de l'agence américaine de l'énergie et d'Eurostat sans qu'une valeur précise par année ait été extraite dans cette collecte pour les années antérieures à 2014. | écart qualitatif confirmé pour 2014-2015 (F.CLD.H3.005) ; séries complètes 2005-2013 non extraites | T1, T2 | exo | [S10] | K |
| F.CLD.H3.007 | 2009-2015 | MONDE | Le coût actualisé de l'électricité solaire photovoltaïque baisse fortement sur la période, portée par la chute du prix des modules amorcée fin 2009 ; la baisse se poursuit après la fenêtre jusqu'à dépasser les trois quarts. | LCOE moyen mondial utility-scale : 0,36 $/kWh (2010) → 0,10 $/kWh (2017), soit -73 % ; prix des modules -81 % depuis fin 2009 (mesuré jusqu'en 2017, au-delà de la fenêtre) | O2, O3 | exo | [S15] | V |
| F.CLD.H3.008 | 2013 | US | La production américaine de gaz de schiste fait baisser durablement le prix du gaz et de l'électricité industrielle aux États-Unis, en écart croissant avec l'Europe, selon les commentateurs contemporains de la période. | non chiffré précisément dans cette collecte, cohérent avec F.CLD.H3.004 | T1, T2 | exo | [S13] | K |
| F.CLD.H3.009 | 2005-2015 | MONDE | L'intensité énergétique du produit intérieur brut mondial poursuit sa baisse tendancielle sur la période, une tendance antérieure au choc cloud et non spécifique à lui. | tendance qualitative, valeurs non retrouvées dans cette collecte | MONDE | exo | [S16] | K |

### Jalons cités
<!-- Lines 192-196 -->

`J.CLD.2008.08` (bascule principale : pic puis effondrement du pétrole en 2008), `J.CLD.2013.07`
(baisse durable du prix du gaz et de l'électricité industrielle américaine par le gaz de schiste),
`J.CLD.2015.07` (chute du coût du solaire photovoltaïque depuis 2009).

### Trajectoire `T.CLD.H3`
<!-- Lines 199-214 -->

| année | phase | intensité | ce qui change | faits et jalons |
| --- | --- | --- | --- | --- |
| avant t0 | latent | 1 | Le pétrole est à un niveau modéré (WTI 41,51 $/baril en 2004) après une remontée depuis le creux de la fin des années 1990 ; le gaz Henry Hub est déjà élevé (8,69 $/MBtu en 2005). Contexte exogène, sans lien avec le cloud. | F.CLD.H3.001 |
| 2005 | latent | 1 | Le gaz Henry Hub est à son plus haut de la fenêtre ; le pétrole poursuit sa hausse. Contexte exogène. | F.CLD.H3.003 |
| 2006 | latent | 1 | Poursuite de la hausse modérée du pétrole (66,05 $/baril) ; recul du gaz depuis le pic de 2005. | F.CLD.H3.001 |
| 2007 | latent | 1 | Poursuite de la hausse du pétrole (72,34 $/baril) ; pas de bascule propre à H3. | F.CLD.H3.001 |
| 2008 | crise | 3 | Bascule exogène majeure : le pétrole atteint son sommet de la fenêtre (99,67 $/baril) puis s'effondre à l'automne avec la crise financière ; le gaz atteint aussi son sommet (8,86 $/MBtu). | J.CLD.2008.08, F.CLD.H3.001, F.CLD.H3.002 |
| 2009 | crise | 2 | Le pétrole et le gaz reculent fortement avec la récession mondiale (WTI 61,95 $/baril, gaz 3,94 $/MBtu). | F.CLD.H3.001, F.CLD.H3.003 |
| 2010 | consolidation | 1 | Reprise modérée du pétrole (79,48 $/baril) ; le gaz reste bas. | F.CLD.H3.001 |
| 2011 | consolidation | 1 | Le pétrole se stabilise à un niveau élevé (94,88 $/baril) ; le gaz continue de reculer (4,00 $/MBtu). | F.CLD.H3.001, F.CLD.H3.003 |
| 2012 | consolidation | 1 | Le pétrole reste stable et élevé (94,05 $/baril) ; le gaz atteint un creux (2,75 $/MBtu). | F.CLD.H3.001, F.CLD.H3.003 |
| 2013 | consolidation | 3 | Bascule exogène : la production de gaz de schiste fait baisser durablement le prix du gaz et de l'électricité industrielle américaine, ouvrant un écart avec l'Europe. | J.CLD.2013.07, F.CLD.H3.008 |
| 2014 | consolidation | 2 | Le pétrole reste élevé en moyenne annuelle (93,17 $/baril) avant la chute de fin d'année ; l'électricité industrielle américaine recule légèrement (7,10 ¢/kWh). | F.CLD.H3.001, F.CLD.H3.005 |
| 2015 | banalisation | 3 | État final : effondrement du pétrole (48,66 $/baril), gaz au plus bas de la fenêtre (2,52 $/MBtu), électricité industrielle américaine en léger recul (6,91 ¢/kWh), et coût du solaire déjà en forte baisse depuis fin 2009, confirmée à -73 % sur 2010-2017. | F.CLD.H3.001, F.CLD.H3.003, F.CLD.H3.005, J.CLD.2015.07, F.CLD.H3.007 |

### Narratif
<!-- Lines 217-234 -->

Le contexte énergétique macro de la fenêtre cloud est marqué par trois grands mouvements exogènes,
sans lien causal avec le choc lui-même [co:X.CLD.11] : la flambée puis l'effondrement du pétrole
autour de 2008 [J.CLD.2008.08][F.CLD.H3.001][F.CLD.H3.002], la révolution du gaz de schiste
américain qui fait chuter le prix du gaz et de l'électricité industrielle américaine à partir de
2013 [J.CLD.2013.07][F.CLD.H3.004][F.CLD.H3.008], et la chute du coût du solaire photovoltaïque
amorcée fin 2009, confirmée à -73 % entre 2010 et 2017 pour le coût actualisé moyen mondial
[J.CLD.2015.07][F.CLD.H3.007]. Le gaz Henry Hub recule presque
sans interruption après son pic de 2008, divisé par plus de trois d'ici 2015
[F.CLD.H3.003][F.CLD.H3.004]. Le prix de l'électricité industrielle américaine, seule série
vérifiée sur des années précises de cette collecte, recule légèrement entre 2014 et 2015
[F.CLD.H3.005]. Ces mouvements dessinent un environnement énergétique en repli de coût sur
l'essentiel de la fenêtre, ponctué d'un pic en son milieu, cohérent avec un contexte exogène qui ne
peut pas, à lui seul, expliquer les changements observés dans les autres sous-dimensions H
[F.CLD.H3.006][F.CLD.H3.009].

---

## H4 Effets du choc sur l'énergie du reste de l'économie
<!-- Lines 237-239 -->

**Question :** Le choc réduit-il ou déplace-t-il la consommation d'énergie des autres activités ?

### Faits
<!-- Lines 242-250 -->

| id | année | bloc | énoncé | valeur | acteurs | attribution | source | statut |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| F.CLD.H4.001 | 2014-2015 | US, EU | Des études d'analyse de cycle de vie comparant la vidéo en flux hébergée dans des centres de données et les supports physiques (disque, envoi postal) donnent des résultats contrastés selon le terminal, le réseau d'accès et le mode de visionnage. | résultats non convergents, statut disputé | P3, O2, O7 | co:X.CLD.04 | [S17] | D |
| F.CLD.H4.002 | 2010-2015 | US, EU | Le télétravail rendu possible par des services hébergés (courriel, documents, visioconférence) est documenté en tendance croissante sur la période, sans série annuelle continue et sourcée retrouvée dans cette collecte pour son effet énergétique net (déplacements évités contre chauffage et équipement à domicile). | tendance qualitative, non chiffrée | M1, M4, O4 | co:X.CLD.04 | [S18] | K |
| F.CLD.H4.003 | 2012-2015 | MONDE | La dématérialisation des documents et des supports (photo, musique, vidéo, correspondance administrative) vers des services hébergés est documentée comme tendance de fond de la fenêtre, sans mesure agrégée de son bilan énergétique net retrouvée dans cette collecte. | tendance qualitative, non chiffrée | P2, P3, O4 | co:X.CLD.04 | [S18] | K |
| F.CLD.H4.004 | 2008-2015 | MONDE | L'essor du commerce en ligne, rendu possible en partie par des plateformes hébergées, déplace une part de la consommation énergétique du commerce de détail physique (magasin, déplacement client) vers la logistique de livraison, avec un bilan net disputé selon les études et les hypothèses de dernier kilomètre. | bilan net non tranché dans la littérature identifiée ici | O2, O4, P3 | co:X.CLD.08 | [S17] | D |
| F.CLD.H4.005 | 2005-2015 | MONDE | L'effet rebond — la baisse du coût de l'informatique et de la bande passante entraînant une augmentation du volume total de services consommés — est évoqué dans la littérature de la période comme facteur limitant les gains énergétiques nets attendus de la dématérialisation, sans quantification agrégée retrouvée dans cette collecte. | non chiffré, effet qualitatif documenté dans la littérature | MONDE | co:X.CLD.04 | [S17] | K |

### Jalons cités
<!-- Lines 253-256 -->

`J.CLD.2015.08` (bascule principale, seule à ce jour : premières études comparant l'énergie de la
vidéo en flux aux supports physiques, résultats contrastés).

### Trajectoire `T.CLD.H4`
<!-- Lines 259-274 -->

| année | phase | intensité | ce qui change | faits et jalons |
| --- | --- | --- | --- | --- |
| avant t0 | latent | 0 | La distribution de contenu et les échanges reposent sur des supports physiques et des déplacements ; aucune substitution hébergée à grande échelle. | |
| 2005 | latent | 0 | Pas de fait ni de jalon propre à H4 pour cette année. | |
| 2006 | latent | 0 | Pas de fait ni de jalon propre à H4 pour cette année. | |
| 2007 | latent | 0 | Le terminal mobile connecté en permanence (produit dérivé) crée une nouvelle habitude de consultation, sans effet énergétique documenté dans cette collecte. | |
| 2008 | émergence | 1 | L'économie à la demande hébergée commence à déplacer une part de la consommation et de la logistique physiques. | F.CLD.H4.004 |
| 2009 | émergence | 1 | Pas de fait propre à cette année ; l'économie à la demande hébergée, documentée sur 2008-2015, continue de déplacer une part de la consommation physique. | F.CLD.H4.004 |
| 2010 | émergence | 1 | Le télétravail et la dématérialisation documentaire commencent à être documentés comme tendances portées par les services hébergés. | F.CLD.H4.002 |
| 2011 | émergence | 1 | Pas de fait propre à cette année ; l'économie à la demande hébergée, documentée sur 2008-2015, continue de déplacer une part de la consommation physique. | F.CLD.H4.004 |
| 2012 | accélération | 1 | La synchronisation grand public de documents et de photos dans des centres de données distants (E3) accompagne la dématérialisation de supports physiques. | F.CLD.H4.003 |
| 2013 | accélération | 1 | Pas de fait propre à cette année ; le télétravail (2010-2015) et la dématérialisation documentaire (2012-2015) restent en tendance croissante. | F.CLD.H4.002, F.CLD.H4.003 |
| 2014 | accélération | 2 | Le télétravail et la dématérialisation restent en tendance croissante, sans mesure énergétique agrégée disponible dans cette collecte. | F.CLD.H4.002, F.CLD.H4.003 |
| 2015 | consolidation | 2 | État final : premières études comparant l'énergie de la vidéo en flux aux supports physiques, résultats contrastés et non conclusifs ; l'effet rebond est identifié dans la littérature comme facteur limitant les gains nets. | J.CLD.2015.08, F.CLD.H4.001, F.CLD.H4.005 |

### Narratif
<!-- Lines 277-292 -->

Le domaine H4 est pauvre en faits datés pour la fenêtre cloud, ce qui est cohérent avec la
couverture attendue de ce domaine : la dématérialisation, le télétravail et l'effet rebond sont
documentés en tendance plutôt qu'en bascules précises [F.CLD.H4.002][F.CLD.H4.003]. Le seul jalon
propre à H4 dans la chronologie arrive en toute fin de fenêtre, avec des premières études
comparant l'énergie de la vidéo en flux aux supports physiques et à leur distribution, dont les
résultats sont contrastés selon le terminal et le réseau [J.CLD.2015.08][F.CLD.H4.001]. Le
commerce en ligne déplace une part de la consommation du commerce physique vers la logistique de
livraison, avec un bilan net non tranché par la littérature identifiée dans cette collecte
[F.CLD.H4.004]. L'effet rebond — plus de service consommé à mesure que son coût baisse — est
mentionné comme facteur limitant les économies nettes, sans quantification agrégée trouvée pour la
fenêtre [F.CLD.H4.005]. Deux faits de cette sous-dimension portent le statut `D`, disputé, faute de
convergence entre les études disponibles [F.CLD.H4.001][F.CLD.H4.004].

---

## Sources
<!-- Lines 295-315 -->

| clé | type | référence | note |
| --- | --- | --- | --- |
| [S1] | off | U.S. Environmental Protection Agency, ENERGY STAR Program, *Report to Congress on Server and Data Center Energy Efficiency, Public Law 109-431*, 2 août 2007 | Identique à [S51] de `par_annee/cloud_2005_2015.md`. Vérifié sur le document lui-même : 61 TWh en 2006, 1,5 % de l'électricité américaine, doublement depuis 2000. |
| [S2] | acad | Koomey, J., *Growth in Data Center Electricity Use 2005 to 2010*, Analytics Press, complété à la demande du New York Times, 1er août 2011 | Identique à [S30]/[S58] de `par_annee/`. Ouvert et lu le 2026-09-22 : PDF complet (alejandrobarros.com/wp-content/uploads/old/4363/Growth_in_Data_Center_Electricity_use_2005_to_2010.pdf), pages de garde à conclusion. Résultat central (p.9, Conclusions) : électricité des centres de données US et monde a doublé 2000-2005 ; croissance 2005-2010 ralentit à +36 % (US) et +56 % (monde), estimation médiane entre bornes basse et haute ; 2010 : 1,3 % de l'électricité mondiale, 2 % de l'électricité US ; Google <1 % de l'électricité mondiale des centres de données. Corrige l'ancienne valeur de mémoire « +24 % 2005-2010 / +90 % 2000-2005 », qui était erronée. |
| [S3] | acad | Shehabi, A. et al. (Lawrence Berkeley National Laboratory), *United States Data Center Energy Usage Report*, juin 2016, couvrant 2000-2014 | Admissible car postérieure à la fenêtre mais mesurant la fenêtre. Ouvert et lu le 2026-09-22 : webinaire de présentation du rapport complet, 6 décembre 2016 (datacenters.lbl.gov/sites/default/files/EnergyUsageWebinar12062016.pdf), slides 6, 20-23. Consommation US : ~61 Md kWh (2006, cohérent avec [S1]) → plateau ~67-70 Md kWh sur 2008-2014 → ~70 Md kWh en 2014 (~1,8 % de l'électricité américaine) ; PUE moyen hyperscale 1,2 en 2014 (slide 20). Le rapport lui-même (texte intégral, hors webinaire) n'a pas été ouvert ; hôte eta-publications.lbl.gov non testé séparément. |
| [S4] | off | The Green Grid, documents fondateurs et définition de l'indicateur PUE, 2007-2008 | Identique à [S52] de `par_annee/`. Consortium et métrique confirmés par plusieurs sources secondaires ; date de fondation à vérifier. |
| [S5] | off | Google Inc., publications annuelles sur l'efficacité énergétique de sa flotte de centres de données (indicateur PUE), 2008-2015 | Identique à [S53] de `par_annee/`. Ouvert et lu le 2026-09-22 : datacenters.google/efficiency/, tableau historique du PUE trimestriel (trailing twelve-month, flotte). Valeurs lues : T4 2008 = 1,20 ; T4 2009 = 1,19 ; T4 2010 = 1,16 ; T4 2011 = 1,14 ; T4 2012 = 1,12 ; T4 2013 = 1,12 ; T4 2014 = 1,12 (constant sur l'année). Corrige l'ancienne valeur de mémoire « 1,21 en 2008 » (lue : 1,20). |
| [S6] | presse | Communications d'exploitants de centres de données contestant les estimations externes de consommation, 2009-2011 | Généralité qualitative ; épisode et acteur précis à identifier lors d'une collecte ultérieure. |
| [S7] | presse | Presse technique et communiqués contemporains des implantations de centres de données près de sources hydroélectriques dans le nord-ouest des États-Unis, 2006-2008 | À vérifier ; sites et dates précises non confirmés dans cette collecte. |
| [S8] | presse | Communiqués et presse contemporaine des implantations de centres de données en Finlande, Suède et Islande, 2010-2013 | Identique à [S59] de `par_annee/`. |
| [S9] | off | Communiqués d'exploitants de centres de données sur leurs premiers contrats d'achat d'électricité renouvelable de longue durée, 2010-2015 | Identique à [S56] de `par_annee/` pour le premier contrat (2010) ; le décompte cumulé annuel 2011-2015 n'a pas été retrouvé dans cette collecte. |
| [S10] | stat | U.S. Energy Information Administration, séries de prix de l'électricité industrielle ; Eurostat, séries de prix de l'électricité aux entreprises | Identique à [S60] de `par_annee/` pour la partie gaz. Série complète 2005-2013 non extraite ; seuls 2014-2015 sont vérifiés directement ([S14]). |
| [S11] | presse | Greenpeace International, rapports de la série *How Clean is Your Cloud* / *Make IT Green*, 2010-2014 | Identique à [S57] de `par_annee/`. Artefact militant, utilisé pour dater l'entrée du sujet dans le débat public, pas pour ses chiffres. |
| [S12] | stat | U.S. Energy Information Administration, série de prix au comptant du pétrole brut WTI (Cushing, OK), dnav/pet/hist | Vérifié directement via l'outil de récupération web le 2026-09-21 : valeurs annuelles 2004-2015 confirmées (41,51 $ en 2004, 99,67 $ en 2008, 48,66 $ en 2015). |
| [S13] | stat | U.S. Energy Information Administration, série de prix au comptant du gaz naturel Henry Hub, dnav/ng/hist | Vérifié directement via l'outil de récupération web le 2026-09-21 : valeurs annuelles 2005-2015 confirmées (8,69 $/MBtu en 2005, 8,86 $/MBtu pic en 2008, 2,52 $/MBtu en 2015). |
| [S14] | stat | U.S. Energy Information Administration, *Electric Power Annual*, prix moyen de l'électricité au secteur industriel, table epa_02_04 | Vérifié directement via l'outil de récupération web le 2026-09-21, mais la table consultée ne couvre que 2014-2025 : 7,10 ¢/kWh (2014), 6,91 ¢/kWh (2015). Série 2005-2013 non retrouvée dans cette table ; une autre table ou l'Electricity Data Browser serait nécessaire. |
| [S15] | stat | IRENA, *Renewable Power Generation Costs in 2017*, Key Findings and Executive Summary, Figure ES.1 (série 2010-2017) ; Lazard, *Levelized Cost of Energy* | Identique à [S61] de `par_annee/`. Ouvert et lu le 2026-09-22 : irena.org/-/media/Files/IRENA/Agency/Publication/2018/Jan/IRENA_2017_Power_Costs_2018_summary.pdf, pages 4-5 (Executive Summary et Figure ES.1). Valeurs lues : LCOE solaire PV utility-scale, moyenne mondiale pondérée, 0,36 $/kWh (2010) → 0,10 $/kWh (2017), soit -73 % ; prix des modules solaires -81 % depuis fin 2009 (mesuré jusqu'en 2017). La fenêtre exacte 2009-2015 n'est pas publiée telle quelle dans ce document (la série disponible est 2010-2017) ; valeur retenue par la borne la plus proche disponible, écart signalé dans l'énoncé du fait. |
| [S16] | stat | Agence internationale de l'énergie, Banque mondiale, séries d'intensité énergétique du PIB mondial | Généralité qualitative issue de la mémoire de l'agent ; série non consultée. |
| [S17] | acad | Travaux d'analyse de cycle de vie comparant la distribution vidéo en flux et les supports physiques ; travaux sur le bilan énergétique du commerce en ligne contre le commerce physique, 2012-2016 | Identique à [S62] de `par_annee/` pour la partie vidéo. Littérature contrastée, non consultée directement ; statut `D` retenu par prudence. |
| [S18] | acad | Travaux sur le télétravail, la dématérialisation documentaire et l'effet rebond informatique, 2010-2015 | Généralité qualitative issue de la mémoire de l'agent ; aucune série chiffrée retrouvée dans cette collecte. |
