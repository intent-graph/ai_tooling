# H. Énergie — Cloud 2005-2015

Ce que le domaine énergie a connu pendant la fenêtre cloud, sous-dimension par sous-dimension :
faits sourcés, jalons cités, trajectoire année par année, narratif court. Le cloud est
l'industrialisation de l'informatique : ses usines — centres de données, plateformes — sont, au
sens propre, des convertisseurs d'électricité en service numérique. Cette cellule porte la
matière du test de l'hypothèse H5 (pas de choc de productivité sans changement énergétique) ; elle
documente, elle ne conclut pas. Ligne de base : état des deux années précédant t0 (2003-2004).

## Table of Contents

1. [H1 Consommation et efficacité de l'appareil numérique](#h1-consommation-et-efficacité-de-lappareil-numérique) _(Lines 41-44)_
   1. [Faits](#faits) _(Lines 47-59)_
   1. [Jalons cités](#jalons-cités) _(Lines 62-67)_
   1. [Trajectoire `T.CLD.H1`](#trajectoire-tcldh1) _(Lines 70-85)_
   1. [Narratif](#narratif) _(Lines 88-108)_
1. [H2 Énergie comme contrainte et facteur de localisation](#h2-énergie-comme-contrainte-et-facteur-de-localisation) _(Lines 111-114)_
   1. [Faits](#faits-1) _(Lines 117-127)_
   1. [Jalons cités](#jalons-cités-1) _(Lines 130-135)_
   1. [Trajectoire `T.CLD.H2`](#trajectoire-tcldh2) _(Lines 138-153)_
   1. [Narratif](#narratif-1) _(Lines 156-172)_
1. [H3 Contexte énergétique macro : prix, mix, abondance](#h3-contexte-énergétique-macro--prix-mix-abondance) _(Lines 175-178)_
   1. [Faits](#faits-2) _(Lines 181-193)_
   1. [Jalons cités](#jalons-cités-2) _(Lines 196-200)_
   1. [Trajectoire `T.CLD.H3`](#trajectoire-tcldh3) _(Lines 203-218)_
   1. [Narratif](#narratif-2) _(Lines 221-238)_
1. [H4 Effets du choc sur l'énergie du reste de l'économie](#h4-effets-du-choc-sur-lénergie-du-reste-de-léconomie) _(Lines 241-243)_
   1. [Faits](#faits-3) _(Lines 246-254)_
   1. [Jalons cités](#jalons-cités-3) _(Lines 257-260)_
   1. [Trajectoire `T.CLD.H4`](#trajectoire-tcldh4) _(Lines 263-278)_
   1. [Narratif](#narratif-3) _(Lines 281-297)_
1. [Sources](#sources) _(Lines 300-327)_




---

## H1 Consommation et efficacité de l'appareil numérique
<!-- Lines 41-44 -->

**Question :** Combien d'énergie consomment réseaux, terminaux et centres de données, et à quel
rythme l'efficacité par unité de service progresse-t-elle ?

### Faits
<!-- Lines 47-59 -->

| id | année | bloc | énoncé | valeur | acteurs | attribution | source | statut |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| F.CLD.H1.001 | 2000-2006 | US | La consommation électrique des serveurs et centres de données double aux États-Unis, avant de se stabiliser en croissance sur la décennie 2000. | 61 TWh en 2006, contre environ 30 TWh en 2000 ; 1,5 % de l'électricité nationale | O6, O2, M10 | choc | [S1] | V |
| F.CLD.H1.002 | 2000-2005 | MONDE, US | La consommation électrique des centres de données double au début de la fenêtre (installations et croissance de l'électricité par serveur), avant l'inflexion mesurée ensuite. | doublement 2000-2005, monde et US | O2, O7 | choc | [S2] | V |
| F.CLD.H1.003 | 2005-2010 | MONDE, US | La consommation électrique des centres de données continue de croître mais à un rythme nettement inférieur à celui de 2000-2005 (doublement), malgré la forte hausse du nombre de services hébergés. | +56 % monde, +36 % US sur 2005-2010 (estimation médiane entre bornes basse et haute) | O2, O7 | choc | [S2] | V |
| F.CLD.H1.004 | 2000-2014 | US | Une étude couvrant 2000-2014 confirme un découplage : le nombre de serveurs installés et le trafic de données croissent bien plus vite que la consommation électrique des centres de données sur la seconde moitié de la période. | consommation des centres de données américains ~70 milliards de kWh en 2014 (environ 1,8 % de l'électricité américaine), quasi stable depuis 2010 après un plateau amorcé en 2008 | O2, O7 | choc | [S3] | V |
| F.CLD.H1.005 | 2007 | MONDE | Un consortium industriel publie en 2007 une métrique d'efficacité des centres de données, rapportant l'énergie totale du site à celle des équipements informatiques, que l'industrie adopte ensuite à l'échelle mondiale. | indicateur PUE : énergie totale des installations / énergie des équipements informatiques, minimum 1,0 | O2, O3, M1 | choc | [S4] | V |
| F.CLD.H1.006 | 2008-2014 | US, MONDE | Le PUE moyen déclaré par un grand exploitant pour sa flotte de centres de données passe d'environ 1,20 en 2008 à environ 1,12 en 2014, contre une moyenne sectorielle alors estimée entre 1,8 et 2,0 pour les installations d'entreprise plus anciennes. | PUE flotte : ~1,20 (2008, T4) → 1,12 (2014, constant sur l'année) | O2 | choc | [S5] | V |
| F.CLD.H1.007 | 2009 | US | Un exploitant publie en janvier 2009 son estimation de l'énergie consommée par requête de recherche, travaux préalables compris, et indique que des estimations plus élevées publiées ailleurs sont de loin supérieures aux siennes. | 0,0003 kWh (1 kJ) par requête | O2 | choc | [S19] | V |
| F.CLD.H1.008 | 2011 | US, MONDE | Une étude indépendante conclut que la croissance de la consommation électrique des centres de données entre 2005 et 2010 (+56 % monde, +36 % US, estimation médiane) est très inférieure aux projections faites en 2007 sur la base de la tendance 2000-2005 (doublement), qui annonçaient elles-mêmes un nouveau doublement d'ici 2010-2011. | croissance réelle 2005-2010 : +56 % monde / +36 % US, contre un doublement projeté | O2, O7 | choc | [S2] | V |
| F.CLD.H1.009 | 2013-2014 | US | Les centres de données représentent une part stable de l'électricité consommée aux États-Unis malgré la croissance du nombre de services hébergés. | environ 1,8 % de l'électricité américaine en 2014 (70 milliards de kWh) | O2, O6 | choc | [S3] | V |

### Jalons cités
<!-- Lines 62-67 -->

`J.CLD.2007.06` (bascule principale : premier chiffrage officiel américain, 2007), `J.CLD.2007.07`
(métrique d'efficacité PUE), `J.CLD.2008.07` (premier exploitant publiant son PUE mesuré),
`J.CLD.2010.04` (les centres de données entrent dans les comptes énergétiques nationaux),
`J.CLD.2011.07` (étude indépendante sur le découplage 2005-2010).

### Trajectoire `T.CLD.H1`
<!-- Lines 70-85 -->

| année | phase | intensité | ce qui change | faits et jalons |
| --- | --- | --- | --- | --- |
| avant t0 | latent | 1 | La consommation des serveurs et centres de données double entre 2000 et 2004-2006 aux États-Unis, sans mesure officielle ni métrique d'efficacité partagée ; le sujet reste technique et interne. | F.CLD.H1.001, F.CLD.H1.002 |
| 2005 | émergence | 1 | Un opérateur commence à publier ses gains de densité et d'efficacité comme avantage industriel : l'énergie devient une variable de compétitivité affichée. | J.CLD.2005.03 |
| 2006 | émergence | 1 | Pas de rupture de mesure ; la croissance de la consommation se poursuit sur sa tendance de la première moitié de la décennie. | F.CLD.H1.002 |
| 2007 | accélération | 3 | Premier chiffrage officiel américain de la consommation des serveurs et centres de données (61 TWh, 1,5 % de l'électricité nationale) ; un consortium publie la métrique PUE. Le sujet entre dans la statistique publique et se dote d'un outil de mesure comparable. | F.CLD.H1.001, J.CLD.2007.06, J.CLD.2007.07, F.CLD.H1.005 |
| 2008 | accélération | 2 | Un grand exploitant publie pour la première fois son PUE mesuré, nettement meilleur que la moyenne du secteur ; l'efficacité devient un argument public. | J.CLD.2008.07, F.CLD.H1.006 |
| 2009 | consolidation | 1 | Un exploitant publie son estimation de l'énergie consommée par requête de recherche, inférieure aux estimations plus élevées publiées ailleurs ; pas de jalon propre à H1. | F.CLD.H1.007 |
| 2010 | consolidation | 2 | Le nombre et la consommation des très grands centres de données deviennent un objet de mesure publique et de politique énergétique. | J.CLD.2010.04 |
| 2011 | consolidation | 3 | Une étude indépendante établit le résultat central pour H5 : la consommation 2005-2010 a crû bien moins que projeté et bien moins que 2000-2005, malgré l'explosion du service rendu — découplage mesuré. | J.CLD.2011.07, F.CLD.H1.003, F.CLD.H1.008 |
| 2012 | banalisation | 0 | Pas de jalon propre ; la trajectoire d'efficacité se poursuit, moins commentée publiquement que la contrainte de localisation (H2). | |
| 2013 | banalisation | 1 | La part des centres de données dans l'électricité américaine reste stable en proportion malgré la croissance du service hébergé. | F.CLD.H1.009 |
| 2014 | banalisation | 2 | Une étude couvrant 2000-2014 confirme la quasi-stabilité de la consommation mondiale des centres de données sur 2010-2014, malgré la poursuite de la croissance du trafic et des serveurs. | F.CLD.H1.004 |
| 2015 | banalisation | 1 | État final : le PUE moyen des grands exploitants s'est rapproché de 1,1-1,2 ; la mesure de l'efficacité et le découplage consommation/service sont des faits établis pour l'épicentre du choc, moins documentés hors des très grands exploitants. | F.CLD.H1.006 |

### Narratif
<!-- Lines 88-108 -->

La consommation électrique des centres de données double aux États-Unis entre 2000 et 2006, avant
qu'un chiffrage officiel n'entre dans la statistique publique en 2007 [F.CLD.H1.001][J.CLD.2007.06].
La même année, un consortium industriel publie une métrique d'efficacité commune, que l'industrie adopte
ensuite à l'échelle mondiale [J.CLD.2007.07][F.CLD.H1.005]. Entre 2005 et 2010, la
consommation croît beaucoup moins vite qu'entre 2000 et 2005 (doublement) : +56 % au niveau
mondial et +36 % aux États-Unis, un résultat confirmé par une étude indépendante de 2011 qui
contredit les projections faites en 2007 sur la simple extrapolation de tendance, lesquelles
annonçaient un nouveau doublement [F.CLD.H1.002][F.CLD.H1.003][J.CLD.2011.07][F.CLD.H1.008]. Le
PUE moyen trimestriel du plus grand exploitant suivi passe de 1,20 fin 2008 à 1,12 en 2014, contre
une moyenne sectorielle alors estimée à près du double [F.CLD.H1.006]. Une étude couvrant
2000-2014 prolonge ce constat : la consommation des centres de données américains atteint un
plateau autour de 67-70 milliards de kWh entre 2008 et 2014 (environ 1,8 % de l'électricité
américaine en 2014), quasi stable depuis 2010 malgré la croissance continue du trafic et du
nombre de serveurs [F.CLD.H1.004]. Dès janvier 2009, un exploitant avait publié une estimation de
l'énergie par requête de recherche inférieure aux estimations plus élevées publiées ailleurs
[F.CLD.H1.007] ; en 2013-2014, la part des centres de données dans l'électricité américaine reste
stable [F.CLD.H1.009].

---

## H2 Énergie comme contrainte et facteur de localisation
<!-- Lines 111-114 -->

**Question :** Où et pourquoi les usines s'installent-elles ; l'accès à l'électricité borne-t-il
la croissance ?

### Faits
<!-- Lines 117-127 -->

| id | année | bloc | énoncé | valeur | acteurs | attribution | source | statut |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| F.CLD.H2.001 | 2006 | US | Des exploitants implantent de nouveaux centres de données dans la région du fleuve Columbia, dans le nord-ouest des États-Unis, attirés par l'électricité hydroélectrique abondante et bon marché. | non chiffré | O2 | choc | [S20] | A |
| F.CLD.H2.002 | 2011-2012 | EU | Des exploitants ouvrent des centres de données en Suède et en Finlande en 2011, puis en Islande en 2012, motivés par le refroidissement naturel que permet le climat froid et par le prix et la disponibilité de l'électricité locale ; en Islande, celle-ci est presque entièrement hydraulique et géothermique. | non chiffré | O2, T2 | choc | [S8] | A |
| F.CLD.H2.003 | 2010 | US | En juillet 2010, la filiale énergie d'un exploitant de centres de données signe avec un producteur un contrat d'achat de 114 MW d'électricité éolienne, sur 20 ans à prix fixé ; c'est le premier contrat de cette filiale. | 114 MW ; 20 ans ; livraisons à partir du 30 juillet 2010 | O2, O3 | choc | [S9] | A |
| F.CLD.H2.004 | 2014 | US | En 2014, des exploitants de centres de données signent des contrats d'achat d'électricité renouvelable de 15 à 20 ans ; d'autres grands exploitants en ont aussi signé, sans série annuelle disponible dans la source lue. | 175 MW éolien sur 20 ans (juillet 2014) pour un centre de données de Chicago ; 23 MW sur 15 ans pour un centre de données des grandes plaines | O2, O3 | choc | [S21] | A |
| F.CLD.H2.005 | 2013 | US, EU | En 2013, les prix de l'électricité pour les consommateurs industriels en Europe sont plus du double de ceux des États-Unis, selon l'analyse prospective publiée en novembre 2013 par l'Agence internationale de l'énergie. | plus du double (Europe contre États-Unis, 2013) | O2, O3, T1, T2 | co:X.CLD.11 | [S22] | A |
| F.CLD.H2.006 | 2010 | US | En mars 2010, une organisation environnementale publie un rapport qui compare des centres de données de grands exploitants selon la part du charbon, du nucléaire et des énergies renouvelables dans le réseau électrique local. | Chicago : 72,8 % de charbon et 1,1 % de renouvelable ; The Dalles : 34,4 % de charbon et 50,9 % de renouvelable (réseau local) | O8, O2 | choc | [S11] | V |
| F.CLD.H2.007 | 2006-2012 | US | En 2006, des exploitants de centres de données contractent des capacités électriques de 30 à 48 MW dans le nord-ouest des États-Unis, deux d'entre elles auprès de distributeurs publics de comté ; un article de 2012 rapporte qu'un exploitant reprochait à son distributeur la lenteur de la construction d'une sous-station de 48 MW. | 48 MW (Quincy, distributeur du comté de Grant) ; 42 MW (Wenatchee) ; 30 MW (distributeur du comté de Douglas) ; contrats rapportés en août 2006 | O2, O3 | choc | [S7] | A |

### Jalons cités
<!-- Lines 130-135 -->

`J.CLD.2010.07` (bascule principale : contrat d'achat de 114 MW d'électricité éolienne signé par la
filiale énergie d'un exploitant), `J.CLD.2011.08` (implantations Suède, Finlande et Islande,
refroidissement naturel et électricité locale), `J.CLD.2010.08` (rapport de Greenpeace comparant le
mix électrique local de centres de données).

### Trajectoire `T.CLD.H2`
<!-- Lines 138-153 -->

| année | phase | intensité | ce qui change | faits et jalons |
| --- | --- | --- | --- | --- |
| avant t0 | latent | 0 | Les centres de données sont dimensionnés pour la proximité des usagers et le coût immobilier ; l'électricité est un intrant de réseau standard, non un critère de site différenciant. | |
| 2005 | latent | 1 | Un opérateur commence à publier ses gains de densité et d'efficacité, signe que l'énergie devient un paramètre de conception d'usine. | J.CLD.2005.03 |
| 2006 | émergence | 2 | Des implantations près de sources hydroélectriques bon marché apparaissent dans le nord-ouest américain, où des exploitants contractent des capacités de 30 à 48 MW. | F.CLD.H2.001, F.CLD.H2.007 |
| 2007 | émergence | 0 | Pas de fait ni de jalon propre à H2 pour cette année. | |
| 2008 | émergence | 0 | Pas de jalon propre à H2 ; contexte de prix de l'énergie très volatil (voir H3). | |
| 2009 | émergence | 0 | Pas de jalon propre à H2. | |
| 2010 | accélération | 3 | Bascule : la filiale énergie d'un exploitant signe avec un producteur un contrat de 20 ans pour 114 MW d'électricité éolienne ; une organisation environnementale publie un rapport comparant le mix électrique local de centres de données. | J.CLD.2010.07, J.CLD.2010.08, F.CLD.H2.003, F.CLD.H2.006 |
| 2011 | accélération | 3 | Des centres de données ouvrent en Suède et en Finlande, motivés par le refroidissement naturel du climat froid et par l'électricité locale. | J.CLD.2011.08, F.CLD.H2.002 |
| 2012 | consolidation | 1 | Un centre de données ouvre en Islande, où l'électricité est presque entièrement hydraulique et géothermique ; pas de jalon propre à H2 identifié dans la chronologie. | F.CLD.H2.002 |
| 2013 | consolidation | 2 | Les prix de l'électricité pour les consommateurs industriels en Europe sont plus du double de ceux des États-Unis. | F.CLD.H2.005 |
| 2014 | consolidation | 1 | Des exploitants signent des contrats d'achat d'électricité renouvelable de 15 à 20 ans. | F.CLD.H2.004 |
| 2015 | banalisation | 2 | État final : des contrats d'achat d'électricité renouvelable de long terme sont signés par plusieurs exploitants (2014) ; la baisse du coût du solaire (H3) desserre la contrainte. | F.CLD.H2.004, J.CLD.2015.07 |

### Narratif
<!-- Lines 156-172 -->

Le facteur énergétique de localisation apparaît tôt dans la fenêtre : en 2006, des exploitants
implantent des centres de données près du fleuve Columbia, attirés par l'électricité
hydroélectrique abondante et bon marché [F.CLD.H2.001]. La bascule se produit en 2010 quand la
filiale énergie d'un exploitant signe avec un producteur un contrat de 20 ans pour 114 MW
d'électricité éolienne [J.CLD.2010.07][F.CLD.H2.003]. La même année, une organisation
environnementale publie un rapport comparant le mix électrique local de centres de données
[J.CLD.2010.08][F.CLD.H2.006]. En 2011-2012, des centres de données ouvrent en Suède, en Finlande
puis en Islande, où jouent le refroidissement naturel du climat froid et le prix et la
disponibilité de l'électricité locale [J.CLD.2011.08][F.CLD.H2.002]. En 2013, les prix de
l'électricité industrielle en Europe sont plus du double de ceux des États-Unis
[F.CLD.H2.005][co:X.CLD.11]. La collecte n'a pas retrouvé de série annuelle des contrats d'achat
d'électricité renouvelable des exploitants : seuls des exemples de 2014 sont sourcés
[F.CLD.H2.004].

---

## H3 Contexte énergétique macro : prix, mix, abondance
<!-- Lines 175-178 -->

**Question :** Dans quel environnement énergétique le choc se déploie-t-il, et cet environnement
change-t-il pendant la fenêtre ?

### Faits
<!-- Lines 181-193 -->

| id | année | bloc | énoncé | valeur | acteurs | attribution | source | statut |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| F.CLD.H3.001 | 2004, 2008, 2015 | US, MONDE | Le prix au comptant du pétrole brut WTI passe d'un niveau modéré en 2004 à un sommet en 2008 puis retombe à un creux en fin de fenêtre. | 41,51 $/baril (2004) ; 99,67 $/baril (2008) ; 48,66 $/baril (2015) | T1, T2 | exo | [S12] | V |
| F.CLD.H3.002 | 2008 | MONDE | Le prix du baril de WTI atteint son point le plus haut de la fenêtre avant de s'effondrer avec la crise financière et la récession. | pic annuel moyen 99,67 $/baril en 2008 | T1 | exo | [S12] | V |
| F.CLD.H3.003 | 2005, 2009, 2015 | US | Le prix au comptant du gaz naturel Henry Hub recule fortement entre le sommet du milieu de fenêtre et sa fin, sous l'effet de la production de gaz de schiste. | 8,69 $/MBtu (2005) ; 3,94 $/MBtu (2009) ; 2,52 $/MBtu (2015) | T1 | exo | [S13] | V |
| F.CLD.H3.004 | 2005-2015 | US | Le prix du gaz Henry Hub, après un sommet en 2008, entame une baisse quasi continue jusqu'à la fin de la fenêtre, portée par l'essor de l'extraction non conventionnelle. | 8,86 $/MBtu (2008) → 2,52 $/MBtu (2015), soit une division par environ 3,5 | T1 | exo | [S13] | V |
| F.CLD.H3.005 | 2014, 2015 | US | Le prix moyen de l'électricité au secteur industriel américain recule légèrement en fin de fenêtre. | 7,10 ¢/kWh (2014) ; 6,91 ¢/kWh (2015) | T1 | exo | [S14] | V |
| F.CLD.H3.006 | 2005, 2010-2014 | US, EU | Hors taxes, le prix de l'électricité industrielle aux États-Unis est inférieur à celui de chacun des pays de l'UE-15 dont la table de l'Agence internationale de l'énergie donne une valeur en 2010, 2012, 2013 et 2014 ; en 2005 il est inférieur à tous sauf à celui de la France. | États-Unis, hors taxes : 3,00 (2005), 4,19 (2010), 4,05 (2014) pence/kWh ; France 2005 : 2,43 ; UE-15, valeur la plus basse en 2010 : Finlande 5,92 ; en 2014 : Suède 4,92 | T1, T2 | exo | [S10] | A |
| F.CLD.H3.007 | 2009-2015 | MONDE | Le coût actualisé de l'électricité solaire photovoltaïque baisse fortement sur la période, portée par la chute du prix des modules amorcée fin 2009 ; la baisse se poursuit après la fenêtre jusqu'à dépasser les trois quarts. | LCOE moyen mondial utility-scale : 0,36 $/kWh (2010) → 0,10 $/kWh (2017), soit -73 % ; prix des modules -81 % depuis fin 2009 (mesuré jusqu'en 2017, au-delà de la fenêtre) | O2, O3 | exo | [S15] | V |
| F.CLD.H3.008 | 2012 | US | En 2012, la hausse de la production de gaz, notamment dans le bassin de schiste de Marcellus, contribue à la baisse du prix au comptant du gaz à Henry Hub ; avec un temps clément, la baisse du gaz contribue à celle des prix de gros de pointe de l'électricité. | Henry Hub : 4,02 $/MBtu (2011) → 2,77 $/MBtu (2012), plus bas annuel depuis 1999 | T1, T2 | exo | [S23] | A |
| F.CLD.H3.009 | 1970-2015 | MONDE | L'intensité énergétique du produit intérieur brut mondial, énergie primaire par unité de PIB, baisse en moyenne de 1,3 % par an de 1970 à 2010, puis de 1,5 % en 2014 et de 1,8 % en 2015, selon l'Agence internationale de l'énergie. | 1,3 %/an (1970-2010) ; 1,5 % (2014) ; 1,8 % (2015) | MONDE | exo | [S16] | A |

### Jalons cités
<!-- Lines 196-200 -->

`J.CLD.2008.08` (bascule principale : pic puis effondrement du pétrole en 2008), `J.CLD.2013.07`
(production américaine de gaz de schiste et baisse du prix du gaz, prix industriels de l'électricité européens plus du double des américains),
`J.CLD.2015.07` (chute du coût du solaire photovoltaïque depuis 2009).

### Trajectoire `T.CLD.H3`
<!-- Lines 203-218 -->

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
| 2012 | consolidation | 1 | Le pétrole reste stable et élevé (94,05 $/baril) ; le gaz atteint un creux (2,75 $/MBtu), la hausse de la production de gaz contribuant à la baisse. | F.CLD.H3.001, F.CLD.H3.003, F.CLD.H3.008 |
| 2013 | consolidation | 3 | Bascule exogène : la production américaine de gaz de schiste a contribué à la baisse du prix du gaz en 2012 ; en 2013, les prix de l'électricité pour les consommateurs industriels en Europe sont plus du double de ceux des États-Unis. | J.CLD.2013.07, F.CLD.H3.008, F.CLD.H2.005 |
| 2014 | consolidation | 2 | Le pétrole reste élevé en moyenne annuelle (93,17 $/baril) avant la chute de fin d'année ; l'électricité industrielle américaine recule légèrement (7,10 ¢/kWh). | F.CLD.H3.001, F.CLD.H3.005 |
| 2015 | banalisation | 3 | État final : effondrement du pétrole (48,66 $/baril), gaz au plus bas de la fenêtre (2,52 $/MBtu), électricité industrielle américaine en léger recul (6,91 ¢/kWh), et coût du solaire déjà en forte baisse depuis fin 2009, confirmée à -73 % sur 2010-2017. | F.CLD.H3.001, F.CLD.H3.003, F.CLD.H3.005, J.CLD.2015.07, F.CLD.H3.007 |

### Narratif
<!-- Lines 221-238 -->

Le contexte énergétique macro de la fenêtre cloud est marqué par trois grands mouvements exogènes,
sans lien causal avec le choc lui-même [co:X.CLD.11] : la flambée puis l'effondrement du pétrole
autour de 2008 [J.CLD.2008.08][F.CLD.H3.001][F.CLD.H3.002], la hausse de la production
américaine de gaz de schiste, qui contribue à la baisse du prix du gaz dès 2012
[J.CLD.2013.07][F.CLD.H3.004][F.CLD.H3.008], et la chute du coût du solaire photovoltaïque
amorcée fin 2009, confirmée à -73 % entre 2010 et 2017 pour le coût actualisé moyen mondial
[J.CLD.2015.07][F.CLD.H3.007]. Le gaz Henry Hub recule presque
sans interruption après son pic de 2008, divisé par plus de trois d'ici 2015
[F.CLD.H3.003][F.CLD.H3.004]. Le prix de l'électricité industrielle américaine recule
légèrement entre 2014 et 2015 [F.CLD.H3.005] et reste, hors taxes, inférieur à celui de
l'UE-15 en 2010-2014 [F.CLD.H3.006]. Ces mouvements dessinent un environnement énergétique en repli de coût sur
l'essentiel de la fenêtre, ponctué d'un pic en son milieu, cohérent avec un contexte exogène qui ne
peut pas, à lui seul, expliquer les changements observés dans les autres sous-dimensions H
[F.CLD.H3.006][F.CLD.H3.009].

---

## H4 Effets du choc sur l'énergie du reste de l'économie
<!-- Lines 241-243 -->

**Question :** Le choc réduit-il ou déplace-t-il la consommation d'énergie des autres activités ?

### Faits
<!-- Lines 246-254 -->

| id | année | bloc | énoncé | valeur | acteurs | attribution | source | statut |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| F.CLD.H4.001 | 2014-2015 | US, EU | Des études d'analyse de cycle de vie comparant la vidéo en flux hébergée dans des centres de données et les supports physiques (disque, envoi postal) donnent des résultats contrastés selon le terminal, le réseau d'accès et le mode de visionnage. | résultats non convergents, statut disputé | P3, O2, O7 | co:X.CLD.04 | [S17] | D |
| F.CLD.H4.002 | 2003-2015 | US | Aux États-Unis, la part des travailleurs qui travaillent à domicile la majeure partie de la semaine passe de 3,6 % en 2005 à 4,3 % en 2010 (American Community Survey), et la part des actifs occupés qui ont travaillé en partie ou en totalité à domicile les jours où ils ont travaillé passe de 19 % en 2003 à 24 % en 2015 (American Time Use Survey). | 3,6 % → 4,3 % (2005-2010) ; 19 % → 24 % (2003-2015) | M1, M4, O4 | co:X.CLD.04 | [S18] | V |
| F.CLD.H4.003 | 2014 | MONDE | En 2014, les ventes numériques et les ventes physiques de musique enregistrée représentent chacune environ 46 % des revenus mondiaux de l'industrie, et les revenus des abonnements à des services de musique en ligne progressent de 39 % pour atteindre 1,57 milliard de dollars. | 46 % numérique, 46 % physique ; abonnements : 1,57 milliard de dollars (+39 %) | P2, P3, O4 | co:X.CLD.04 | [S24] | A |
| F.CLD.H4.004 | 2008-2015 | MONDE | L'essor du commerce en ligne, rendu possible en partie par des plateformes hébergées, déplace une part de la consommation énergétique du commerce de détail physique (magasin, déplacement client) vers la logistique de livraison, avec un bilan net disputé selon les études et les hypothèses de dernier kilomètre. | bilan net non tranché dans la littérature identifiée ici | O2, O4, P3 | co:X.CLD.08 | [S17] | D |
| F.CLD.H4.005 | 2015 | MONDE | Une revue de la littérature publiée en 2015 conclut que les études existantes indiquent toutes que les technologies de l'information et de la communication sont soumises à des effets rebond importants (énergie, temps, savoir), que ces effets y restent peu étudiés, et que si ces effets sont élevés les gains visés sont absorbés ; elle cite une étude où l'enseignement à distance électronique ne réduit ni l'énergie ni les émissions de CO2 par rapport à l'enseignement à distance imprimé, du fait de l'usage d'ordinateurs et du chauffage à domicile. | non chiffré ici | MONDE | co:X.CLD.04 | [S25] | A |

### Jalons cités
<!-- Lines 257-260 -->

`J.CLD.2015.08` (bascule principale, seule à ce jour : premières études comparant l'énergie de la
vidéo en flux aux supports physiques, résultats contrastés).

### Trajectoire `T.CLD.H4`
<!-- Lines 263-278 -->

| année | phase | intensité | ce qui change | faits et jalons |
| --- | --- | --- | --- | --- |
| avant t0 | latent | 0 | La distribution de contenu et les échanges reposent sur des supports physiques et des déplacements ; aucune substitution hébergée à grande échelle. | |
| 2005 | latent | 0 | Pas de fait ni de jalon propre à H4 pour cette année. | |
| 2006 | latent | 0 | Pas de fait ni de jalon propre à H4 pour cette année. | |
| 2007 | latent | 0 | Le terminal mobile connecté en permanence (produit dérivé) crée une nouvelle habitude de consultation, sans effet énergétique documenté dans cette collecte. | |
| 2008 | émergence | 1 | L'économie à la demande hébergée commence à déplacer une part de la consommation et de la logistique physiques. | F.CLD.H4.004 |
| 2009 | émergence | 1 | Pas de fait propre à cette année ; l'économie à la demande hébergée, documentée sur 2008-2015, continue de déplacer une part de la consommation physique. | F.CLD.H4.004 |
| 2010 | émergence | 1 | Le travail à domicile progresse aux États-Unis : 3,6 % des travailleurs le pratiquent la majeure partie de la semaine en 2005, 4,3 % en 2010. | F.CLD.H4.002 |
| 2011 | émergence | 1 | Pas de fait propre à cette année ; l'économie à la demande hébergée, documentée sur 2008-2015, continue de déplacer une part de la consommation physique. | F.CLD.H4.004 |
| 2012 | accélération | 0 | Pas de fait ni de jalon propre à H4 pour cette année. | |
| 2013 | accélération | 1 | Pas de fait propre à cette année ; le travail à domicile reste en progression aux États-Unis (19 % des actifs occupés en 2003, 24 % en 2015). | F.CLD.H4.002 |
| 2014 | accélération | 2 | Les ventes numériques de musique enregistrée égalent les ventes physiques (46 % des revenus mondiaux chacune) ; le travail à domicile progresse aux États-Unis. | F.CLD.H4.002, F.CLD.H4.003 |
| 2015 | consolidation | 2 | État final : premières études comparant l'énergie de la vidéo en flux aux supports physiques, résultats contrastés et non conclusifs ; une revue de la littérature publiée en 2015 conclut que les technologies de l'information sont soumises à des effets rebond importants, peu étudiés. | J.CLD.2015.08, F.CLD.H4.001, F.CLD.H4.005 |

### Narratif
<!-- Lines 281-297 -->

Le domaine H4 est pauvre en faits datés pour la fenêtre cloud, ce qui est cohérent avec la
couverture attendue de ce domaine : le travail à domicile progresse aux États-Unis (3,6 % des
travailleurs en 2005, 4,3 % en 2010) [F.CLD.H4.002], et les ventes numériques de musique égalent
les ventes physiques en 2014 [F.CLD.H4.003], sans mesure de leur bilan énergétique. Le seul jalon
propre à H4 dans la chronologie arrive en toute fin de fenêtre, avec des premières études
comparant l'énergie de la vidéo en flux aux supports physiques et à leur distribution, dont les
résultats sont contrastés selon le terminal et le réseau [J.CLD.2015.08][F.CLD.H4.001]. Le
commerce en ligne déplace une part de la consommation du commerce physique vers la logistique de
livraison, avec un bilan net non tranché par la littérature identifiée dans cette collecte
[F.CLD.H4.004]. Une revue de la littérature publiée en 2015 conclut que les études
existantes indiquent toutes des effets rebond importants des technologies de l'information, encore
peu étudiés [F.CLD.H4.005]. Deux faits de cette sous-dimension portent le statut `D`, disputé, faute de
convergence entre les études disponibles [F.CLD.H4.001][F.CLD.H4.004].

---

## Sources
<!-- Lines 300-327 -->

| clé | type | référence | note |
| --- | --- | --- | --- |
| [S1] | off | U.S. Environmental Protection Agency, ENERGY STAR Program, *Report to Congress on Server and Data Center Energy Efficiency, Public Law 109-431*, 2 août 2007 | Identique à [S51] de `par_annee/cloud_2005_2015.md`. Vérifié sur le document lui-même : 61 TWh en 2006, 1,5 % de l'électricité américaine, doublement depuis 2000. |
| [S2] | acad | Koomey, J., *Growth in Data Center Electricity Use 2005 to 2010*, Analytics Press, complété à la demande du New York Times, 1er août 2011 | Identique à [S30]/[S58] de `par_annee/`. Ouvert et lu le 2026-09-22 : PDF complet (alejandrobarros.com/wp-content/uploads/old/4363/Growth_in_Data_Center_Electricity_use_2005_to_2010.pdf), pages de garde à conclusion. Résultat central (p.9, Conclusions) : électricité des centres de données US et monde a doublé 2000-2005 ; croissance 2005-2010 ralentit à +36 % (US) et +56 % (monde), estimation médiane entre bornes basse et haute ; 2010 : 1,3 % de l'électricité mondiale, 2 % de l'électricité US ; Google <1 % de l'électricité mondiale des centres de données. Corrige l'ancienne valeur de mémoire « +24 % 2005-2010 / +90 % 2000-2005 », qui était erronée. |
| [S3] | acad | Shehabi, A. et al. (Lawrence Berkeley National Laboratory), *United States Data Center Energy Usage Report*, juin 2016, couvrant 2000-2014 | Admissible car postérieure à la fenêtre mais mesurant la fenêtre. Ouvert et lu le 2026-09-22 : webinaire de présentation du rapport complet, 6 décembre 2016 (datacenters.lbl.gov/sites/default/files/EnergyUsageWebinar12062016.pdf), slides 6, 20-23. Consommation US : ~61 Md kWh (2006, cohérent avec [S1]) → plateau ~67-70 Md kWh sur 2008-2014 → ~70 Md kWh en 2014 (~1,8 % de l'électricité américaine) ; PUE moyen hyperscale 1,2 en 2014 (slide 20). Le rapport lui-même (texte intégral, hors webinaire) n'a pas été ouvert ; hôte eta-publications.lbl.gov non testé séparément. |
| [S4] | off | The Green Grid, *PUE: A Comprehensive Examination of the Metric*, White Paper #49, 2012 (copie : https://datacenters.lbl.gov/sites/default/files/WP49-PUE%20A%20Comprehensive%20Examination%20of%20the%20Metric_v6.pdf) | Ouvert et lu le 2026-11-22 : PDF complet, texte extrait. Résumé : « Since its original publication in 2007, PUE has been globally adopted by the industry » ; The Green Grid y est décrit comme « a non-profit, open industry consortium » ; « PUE is defined as the ratio of total facilities energy to IT equipment energy » ; « The minimum PUE is 1.0 ». Le document date de 2012 : il établit l'année 2007 de la première publication, pas son mois (février dans J.CLD.2007.07, non lu). Entrée réécrite ; [S52] de `par_annee/` reste à aligner. |
| [S5] | off | Google Inc., publications annuelles sur l'efficacité énergétique de sa flotte de centres de données (indicateur PUE), 2008-2015 | Identique à [S53] de `par_annee/`. Ouvert et lu le 2026-09-22 : datacenters.google/efficiency/, tableau historique du PUE trimestriel (trailing twelve-month, flotte). Valeurs lues : T4 2008 = 1,20 ; T4 2009 = 1,19 ; T4 2010 = 1,16 ; T4 2011 = 1,14 ; T4 2012 = 1,12 ; T4 2013 = 1,12 ; T4 2014 = 1,12 (constant sur l'année). Corrige l'ancienne valeur de mémoire « 1,21 en 2008 » (lue : 1,20). |
| [S6] | presse | Communications d'exploitants de centres de données contestant les estimations externes de consommation, 2009-2011 | Généralité qualitative ; épisode et acteur précis à identifier lors d'une collecte ultérieure. |
| [S7] | presse | Data Center Knowledge, « Huge Power Draws for Google, Yahoo, Sabey », 10 août 2006 (https://datacenterknowledge.com/hyperscalers/huge-power-draws-for-google-yahoo-sabey) ; Glanz, J., « In farm town, data barns gobble power », *The New York Times*, 24 septembre 2012, republié par NBC News (https://www.nbcnews.com/id/wbna49147152) | Ouverts et lus le 2026-11-22. *Data Center Knowledge* (10 août 2006) : « The Sabey Corp. has contracted with the Douglas County Public Utility District for 30 megawatts of electricity » ; « Microsoft's project in Quincy, Wash. has contracted for a maximum of 48 megawatts of power » (Grant County PUD) ; « Yahoo is building a data center in Wenatchee and has contracted for 42 megawatts of power » ; l'article ne dit ni dates de contrat, ni sous-station, ni ligne dédiée. *The New York Times* (2012) : Microsoft se plaignait que le distributeur tardait à construire « a substation to provide 48 million watts of electrical capacity » ; l'article ne date pas cette plainte. Aucune des deux pages ne dit que l'accès à la capacité électrique devient un critère de site ni ne chiffre les grands campus de fin de période : ces clauses de l'ancien énoncé sont retirées. Entrée réécrite. |
| [S8] | presse | Bradbury, D., « Power in a cold climate », *The Register*, 12 mai 2016 (https://www.theregister.com/2016/05/12/power_in_a_cold_climate) ; « Google Using Sea Water to Cool Finland Project », *Data Center Knowledge*, 15 septembre 2010 (https://www.datacenterknowledge.com/archives/2010/09/15/google-using-sea-water-to-cool-finland-project) | Ouverts et lus le 2026-11-22. *The Register* : « Facebook opened its data centre in Luleå, northern Sweden in 2011 », « Google rolled out its Hamina data centre in Finland the same year », « Verne Global, which opened its Icelandic data centre in 2012 » ; motifs : le refroidissement gratuit par air froid réduit les dépenses, et « the price and availability of local power sources is at least as important » ; Islande : « almost entirely generated by hydro and geothermal power ». *Data Center Knowledge* (2010) : le centre finlandais, en construction, doit entrer en service début 2011 et refroidir par eau de mer. Entrée réécrite ; [S59] de `par_annee/` reste à aligner. |
| [S9] | off | NextEra Energy Resources, communiqué « NextEra Energy Resources signs PPA with Google Energy to supply wind power », 20 juillet 2010 (https://newsroom.nexteraenergy.com/NextEra-Energy-Resources-signs-PPA-with-Google-Energy-to-supply-wind-power-July-2010-Resources) ; TechCrunch, « Google Energy's First Purchase: 20 Years of Wind Power », 20 juillet 2010 (https://techcrunch.com/2010/07/20/google-energy-windpower-jul20) | Ouverts et lus le 2026-11-22. Communiqué : « Google Energy will purchase 114 megawatts of clean, renewable energy » du parc Story II (Iowa), livraisons à partir du 30 juillet 2010 ; il ne donne ni la durée ni ne dit que le contrat est le premier du secteur. TechCrunch : « 114 megawatts of wind power capacity per year for 20 years at a set price » ; porte-parole : « This is the first contract for Google Energy » (premier contrat de la filiale, pas du secteur) ; la production ne va pas d'abord aux opérations de l'exploitant. Entrée réécrite ; [S56] de `par_annee/` reste à aligner. |
| [S10] | off | UK Department of Energy and Climate Change, *Quarterly Energy Prices*, décembre 2015, annexe des tableaux, tableau 5.3.1 « Industrial electricity prices in the IEA », dérivé de l'Agence internationale de l'énergie, *Energy Prices and Taxes* (https://assets.publishing.service.gov.uk/media/5a80becde5274a2e87dbb936/QEP_December_2015_Tables_Annex.pdf) | Ouvert et lu le 2026-11-22 : PDF complet, texte extrait. Tableau en pence par kWh (taux de change annuels moyens), hors taxes et taxes comprises, pour 2005, 2010, 2012, 2013, 2014. États-Unis hors taxes : 3,00 (2005), 4,19 (2010), 4,01 (2012), 4,17 (2013), 4,05 (2014) ; France 2,43 (2005), 6,18 (2010) ; Finlande 3,56 (2005), 5,92 (2010) ; Suède 5,58 (2012), 5,74 (2013), 4,92 (2014) ; Allemagne 4,62 (2005), 5,77 (2014). Taxes comprises, le même classement tient (États-Unis 3,15 en 2005 contre France 2,74 ; 4,26 en 2014 contre Suède 4,96). La table ne donne pas de valeur pour la Belgique, le Luxembourg, les Pays-Bas et la Suède en 2005, ni pour l'Espagne en 2012-2014 ; les prix américains hors taxes y sont estimés par l'éditeur. La table de l'agence elle-même, les séries Eurostat et celles de l'agence américaine de l'énergie n'ont pas été ouvertes ; 2006-2009 et 2011 ne figurent pas dans la table. Entrée réécrite. |
| [S11] | presse | Greenpeace International, *Make IT Green: Cloud Computing and its Contribution to Climate Change*, mars 2010 (https://www.greenpeace.org/static/planet4-international-stateless/2010/03/f2954209-make-it-green-cloud-computing.pdf) | Ouvert et lu le 2026-11-22 : PDF complet, texte extrait (mention « Published in March 2010 » ; la page de dépôt de Greenpeace USA affiche la date du 28 avril 2010). Le tableau « Comparison of significant cloud data centres » donne par site la surface, le PUE estimé et la part de charbon, de nucléaire et de renouvelable du réseau local (Chicago 72,8 % charbon, 1,1 % renouvelable ; The Dalles 34,4 % charbon, 50,9 % renouvelable). Le rapport compare des sites ; il ne classe pas les exploitants. Le classement des exploitants que décrit J.CLD.2010.08 n'a pas été ouvert. Artefact militant, utilisé pour ce que le rapport publie, non pour ses projections. Entrée réécrite ; [S57] de `par_annee/` reste à aligner. |
| [S12] | stat | U.S. Energy Information Administration, série de prix au comptant du pétrole brut WTI (Cushing, OK), dnav/pet/hist | Vérifié directement via l'outil de récupération web le 2026-09-21 : valeurs annuelles 2004-2015 confirmées (41,51 $ en 2004, 99,67 $ en 2008, 48,66 $ en 2015). |
| [S13] | stat | U.S. Energy Information Administration, série de prix au comptant du gaz naturel Henry Hub, dnav/ng/hist | Vérifié directement via l'outil de récupération web le 2026-09-21 : valeurs annuelles 2005-2015 confirmées (8,69 $/MBtu en 2005, 8,86 $/MBtu pic en 2008, 2,52 $/MBtu en 2015). |
| [S14] | stat | U.S. Energy Information Administration, *Electric Power Annual*, prix moyen de l'électricité au secteur industriel, table epa_02_04 | Vérifié directement via l'outil de récupération web le 2026-09-21, mais la table consultée ne couvre que 2014-2025 : 7,10 ¢/kWh (2014), 6,91 ¢/kWh (2015). Série 2005-2013 non retrouvée dans cette table ; une autre table ou l'Electricity Data Browser serait nécessaire. |
| [S15] | stat | IRENA, *Renewable Power Generation Costs in 2017*, Key Findings and Executive Summary, Figure ES.1 (série 2010-2017) ; Lazard, *Levelized Cost of Energy* | Identique à [S61] de `par_annee/`. Ouvert et lu le 2026-09-22 : irena.org/-/media/Files/IRENA/Agency/Publication/2018/Jan/IRENA_2017_Power_Costs_2018_summary.pdf, pages 4-5 (Executive Summary et Figure ES.1). Valeurs lues : LCOE solaire PV utility-scale, moyenne mondiale pondérée, 0,36 $/kWh (2010) → 0,10 $/kWh (2017), soit -73 % ; prix des modules solaires -81 % depuis fin 2009 (mesuré jusqu'en 2017). La fenêtre exacte 2009-2015 n'est pas publiée telle quelle dans ce document (la série disponible est 2010-2017) ; valeur retenue par la borne la plus proche disponible, écart signalé dans l'énoncé du fait. |
| [S16] | off | Agence internationale de l'énergie, *Energy Efficiency 2017* (https://www.iea.org/reports/energy-efficiency-2017) ; Agence internationale de l'énergie, « Energy efficiency gains ground despite lower energy prices, new IEA report says », 9 octobre 2016 (https://www.iea.org/news/energy-efficiency-gains-ground-despite-lower-energy-prices-new-iea-report-says) | Ouverts et lus le 2026-11-22 (pages de présentation des rapports, non les rapports complets). *Energy Efficiency 2017* : l'intensité énergétique mondiale, « measured as the amount of primary energy demand needed to produce one unit of gross domestic product », a baissé de 1,8 % en 2016 ; « Since 2010, intensity has declined at an average rate of 2.1% per year, which is a significant increase from the average rate of 1.3% between 1970 and 2010 ». Communiqué de 2016 : amélioration de 1,8 % en 2015, après 1,5 % en 2014, soit « triple the average rate seen over the past decade » (taux moyen non précisé, donc non repris). Le document sur 2005-2015 année par année n'a pas été ouvert. Entrée réécrite. |
| [S17] | acad | Travaux d'analyse de cycle de vie comparant la distribution vidéo en flux et les supports physiques ; travaux sur le bilan énergétique du commerce en ligne contre le commerce physique, 2012-2016 | Identique à [S62] de `par_annee/` pour la partie vidéo. Littérature contrastée, non consultée directement ; statut `D` retenu par prudence. |
| [S18] | off | U.S. Census Bureau, *Home-Based Workers in the United States: 2010*, Current Population Reports P70-132, octobre 2012 (https://www.census.gov/library/publications/2012/demo/p70-132.html) ; U.S. Bureau of Labor Statistics, « 24 percent of employed people did some or all of their work at home in 2015 », *The Economics Daily*, 2016 (https://www.bls.gov/OPUB/TED/2016/24-PERCENT-OF-EMPLOYED-PEOPLE-DID-SOME-OR-ALL-OF-THEIR-WORK-AT-HOME-IN-2015.HTM) | Ouverts et lus le 2026-11-22. Census (page de la publication) : la part des travailleurs qui ont travaillé la majeure partie de la semaine à domicile « increased from 3.6 percent to 4.3 percent » entre 2005 et 2010 (American Community Survey) ; la page ne chiffre pas les effectifs. BLS : « On the days they worked in 2015, 24 percent of employed people did some or all of their work at home » ; la part « grew from 19 percent in 2003 to 24 percent in 2015 » (American Time Use Survey) ; 23,6 % en 2010 et 23,1 % en 2014 dans le tableau du graphique. Les deux mesures n'ont ni la même définition ni la même population. Ni l'un ni l'autre ne traite l'énergie, les services hébergés ni l'Europe : ces clauses de l'ancien énoncé sont retirées. Entrée réécrite. |
| [S19] | off | Google, billet de blog « Powering a Google search », janvier 2009 (https://googleblog.blogspot.com/2009/01/powering-google-search.html ; version italienne lue : https://blog.google/intl/it-it/notizie-aziendali/iniziative/dare-energia-alle-ricerche-su-google/) | La page anglaise n'a pas rendu son texte au récupérateur (seules les métadonnées : 11 janvier 2009). Version italienne ouverte et lue le 2026-11-22 (page datée du 13 janvier 2009) : « si ottiene un valore di 0,0003 kWh per ricerca effettuata, pari a 1 kJ » ; le billet reconnaît que « alcune fonti hanno riportato delle stime più alte », chiffre « di gran lunga superiore alle nostre stime » ; calcul fondé sur le temps de calcul des serveurs plus des opérations préalables comme la génération de l'index. Citation anglaise recoupée par *eWeek*, 12 janvier 2009 (https://www.eweek.com/news/green-minded-google-gets-red-faced-over-search-energy-consumption-claims/) : « this amounts to 0.0003 kWh of energy per search, or 1 kJ ». Ni l'un ni l'autre ne dit que l'estimation vient de compteurs. |
| [S20] | presse | Harden, B., « Tech firms are rushing to the Quincy, Wash. area », *The Washington Post*, 9 juillet 2006, republié par NBC News (https://www.nbcnews.com/id/wbna13774178) | Ouvert et lu le 2026-11-22. Passages : « There is cheap electricity here and lots of it », « the Columbia, the premier hydroelectric river in North America, flows nearby » ; Microsoft construit à Quincy, Yahoo à Wenatchee (en service à l'automne), Google à The Dalles (Oregon, en service dans l'année). Seule l'année 2006 est établie : 2007-2008 non lu. |
| [S21] | off | Miller, J., Bird, L., Heeter, J., Gorham, B. (National Renewable Energy Laboratory), *Renewable Electricity Use by the U.S. Information and Communication Technology (ICT) Industry*, NREL/TP-6A20-64011, juillet 2015 (https://docs.nlr.gov/docs/fy15osti/64011.pdf) | Ouvert et lu le 2026-11-22 : PDF complet, texte extrait. Passages : « Recently, a number of ICT companies signed long-term PPAs for renewable energy. In July 2014, Microsoft announced it would purchase 175 MW from the Pilot Hill Wind Project in Illinois as part of a 20-year PPA to power its Chicago data center » ; Yahoo : 23 MW d'un parc de 48 MW au Kansas, PPA de 15 ans, pour son centre de données des grandes plaines ; « Additional companies such as Amazon Web Services, Apple, Facebook, and Google have also signed on to long-term PPAs ». Le rapport décrit un mouvement qui commence (« beginning to purchase ») ; il ne donne aucune série annuelle 2010-2015. |
| [S22] | presse | World Nuclear News, « IEA predicts price pinch », 12 novembre 2013 (https://www.world-nuclear-news.org/Articles/IEA-predicts-price-pinch), rendant compte du *World Energy Outlook 2013* de l'Agence internationale de l'énergie | Ouvert et lu le 2026-11-22. Passage : « Currently, electricity prices for industrial consumers in Europe and Japan are more than double those in the USA », écart « projected to be maintained through to 2035 ». Le rapport de l'agence n'a pas été ouvert ; la page ne donne pas de série année par année ni de lien avec la localisation des centres de données. Une page de l'EIA américaine consultée (18 novembre 2014) ne traite que les prix résidentiels. |
| [S23] | off | U.S. Energy Information Administration, *Today in Energy*, « 2012 Brief: Average wholesale natural gas prices fell 31% in 2012 », 8 janvier 2013 (https://www.eia.gov/todayinenergy/detail.php?id=9490) ; « 2012 Brief: Average wholesale electricity prices down compared to last year », 9 janvier 2013 (https://www.eia.gov/todayinenergy/detail.php?id=9510) | Ouverts et lus le 2026-11-22. Première page : Henry Hub à 4,02 $/MMBtu en 2011 et 2,77 $/MMBtu en 2012, « the lowest annual average since 1999 » ; la hausse de l'offre contribue à la baisse, « much of this increase can be attributed to increased production from the Pennsylvania portion of the Marcellus Shale Basin », avec aussi un hiver doux et des stocks élevés ; production du Lower 48 de 63,6 Bcf/j (+4 %). Seconde page : « Lower natural gas prices in 2012 and generally mild temperatures contributed to the 2012 declines in on-peak power prices » ; les prix de gros de l'électricité suivent souvent ceux du gaz. Les pages parlent de prix de gros, non de prix industriels. Le chiffre annuel de la série [S13] pour 2012 est 2,75 : l'écart de 0,02 avec cette page n'est pas expliqué (définitions de moyenne différentes, non vérifié). |
| [S24] | presse | Tandon, S. (AFP), « For first time, digital music matches physical sales », 14 avril 2015, rendant compte du rapport 2015 de l'IFPI (https://phys.org/news/2015-04-digital-music-physical-sales.pdf) | Ouvert et lu le 2026-11-22 (PDF de la dépêche, texte extrait). Passages : « digital and physical music sales were roughly even with each representing 46 percent of revenue for the industry, with rights for performances, films and advertisements making up the rest » ; abonnements : « revenue shot up 39 percent last year to $1.57 billion, according to the IFPI » ; 41 millions d'abonnés payants dans le monde (estimation de l'IFPI). Le rapport de l'IFPI lui-même n'a pas été ouvert (deux pages de relais refusées ou vides). La musique n'est qu'un des supports de l'ancien énoncé (photo, vidéo, documents, correspondance) : les autres clauses sont retirées. |
| [S25] | acad | Gossart, C., « Rebound Effects and ICT: A Review of the Literature », in Hilty, L.M., Aebischer, B. (dir.), *ICT Innovations for Sustainability*, Springer, 2015, p. 435 et suivantes, DOI 10.1007/978-3-319-09228-7_26 (copie lue : https://files.ifi.uzh.ch/hilty/t/Literature_by_RQs/RQ%20301/2015_Gossart_Rebound_Effects_and_ICT_A_Review_of_the_Literature.pdf) | Ouvert et lu le 2026-11-22 : texte complet extrait, sections 3.3 et 4 relues. Conclusion : « existing papers all point out that ICT are subject to important rebound effects of all kinds (energy, time, and knowledge-related) » et « the ICT sector remains underinvestigated » ; section 3.3 : Herring et Roy concluent que « electronic delivery does not result in a reduction in energy or CO2 emissions compared to print-based distance learning, due to rebound effects, e.g. in use of computers and home heating » ; pour le commerce en ligne, la revue note que les auteurs qui mentionnent l'effet rebond n'en donnent aucune évaluation. Revue publiée en 2015, qui ne couvre pas la fenêtre année par année. La page du chapitre sur le site de l'éditeur n'a pas été ouverte. |
