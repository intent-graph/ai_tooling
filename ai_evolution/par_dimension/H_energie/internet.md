# H. Énergie — Internet 1995-2005

Ce que le domaine énergie a connu pendant la fenêtre Internet, sous-dimension par sous-dimension :
faits sourcés, jalons cités, trajectoire année par année, narratif court. Ligne de base : état des
deux années précédant t0 (1993-1994). Le réseau est ici traité comme ce qu'il est au sens propre,
un convertisseur d'électricité en distribution ; cette cellule porte, avec C1, la matière du test
de l'hypothèse H5 (00_these_et_methode.md). La comparaison avec l'autre choc est réservée au
`README.md` du domaine.

## Table of Contents

1. [H1 Consommation et efficacité de l'appareil numérique](#h1-consommation-et-efficacit-de-l-appareil-num-rique) _(Lines 39-42)_
   1. [Faits](#faits) _(Lines 45-57)_
   1. [Jalons cités](#jalons-cit-s) _(Lines 60-63)_
   1. [Trajectoire `T.INT.H1`](#trajectoire-t-int-h1) _(Lines 66-81)_
   1. [Narratif](#narratif) _(Lines 84-97)_
1. [H2 Énergie comme contrainte et facteur de localisation](#h2-nergie-comme-contrainte-et-facteur-de-localisation) _(Lines 100-103)_
   1. [Faits](#faits-1) _(Lines 106-115)_
   1. [Jalons cités](#jalons-cit-s-1) _(Lines 118-121)_
   1. [Trajectoire `T.INT.H2`](#trajectoire-t-int-h2) _(Lines 124-139)_
   1. [Narratif](#narratif-1) _(Lines 142-155)_
1. [H3 Contexte énergétique macro : prix, mix, abondance](#h3-contexte-nerg-tique-macro-prix-mix-abondance) _(Lines 158-161)_
   1. [Faits](#faits-2) _(Lines 164-176)_
   1. [Jalons cités](#jalons-cit-s-2) _(Lines 179-182)_
   1. [Trajectoire `T.INT.H3`](#trajectoire-t-int-h3) _(Lines 185-200)_
   1. [Narratif](#narratif-2) _(Lines 203-220)_
1. [H4 Effets du choc sur l'énergie du reste de l'économie](#h4-effets-du-choc-sur-l-nergie-du-reste-de-l-conomie) _(Lines 223-225)_
   1. [Faits](#faits-3) _(Lines 228-238)_
   1. [Jalons cités](#jalons-cit-s-3) _(Lines 241-244)_
   1. [Trajectoire `T.INT.H4`](#trajectoire-t-int-h4) _(Lines 247-262)_
   1. [Narratif](#narratif-3) _(Lines 265-281)_
1. [Sources](#sources) _(Lines 284-303)_


---

## H1 Consommation et efficacité de l'appareil numérique
<!-- Lines 39-42 -->

**Question :** Combien d'énergie consomment réseaux, terminaux et centres de données, et à quel
rythme l'efficacité par unité de service progresse-t-elle ?

### Faits
<!-- Lines 45-57 -->

| id | année | bloc | énoncé | valeur | acteurs | attribution | source | statut |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| F.INT.H1.001 | 1999 | US | Une tribune très reprise affirme que les nœuds du réseau Internet consomment déjà 8 % de la demande électrique américaine, et que l'ensemble de l'électronique et de l'informatique en consomme 13 %. | 8 % (réseau seul), 13 % (ensemble informatique) de l'électricité américaine (affirmation) | O6, M9, P3 | choc | [S1] | V |
| F.INT.H1.002 | 1999-2001 | US | L'affirmation de 1999 est reprise par son auteur dans une audition devant une sous-commission de la Chambre des représentants en février 2000, avant toute mesure indépendante publiée. | qualitatif | O6 | choc | [S2] | V |
| F.INT.H1.003 | 1999-2000 | US | Des travaux de mesure d'un laboratoire national américain (LBNL), portant sur la situation fin 1999, situent la consommation directe des équipements de bureau et de réseau à environ 2 % de l'électricité du pays, et à environ 3 % en ajoutant les télécommunications et la fabrication électronique ; le LBNL chiffre l'affirmation de 1999 à un facteur 4 à 8 au-dessus de cette mesure. | 2 % (équipements directs), 3 % (avec télécoms et fabrication) de l'électricité américaine (mesure) | O7 | choc | [S2], [S15] | V |
| F.INT.H1.004 | 2000-2005 | MONDE | La consommation électrique mondiale des centres de données double sur la période (70,8 → 152,5 milliards de kWh/an), portée aux trois quarts par la multiplication des serveurs d'entrée de gamme. | 70,8 → 152,5 milliards de kWh/an, ×2,15 (2000→2005) | O3, O1, M1 | choc | [S3] | V |
| F.INT.H1.005 | 2000 | MONDE | L'électricité directement utilisée par les équipements informatiques des centres de données représente environ 0,5 % de la consommation électrique mondiale totale. | 0,5 % de l'électricité mondiale | O3 | choc | [S3] | V |
| F.INT.H1.006 | 2005 | MONDE | En incluant le refroidissement et la distribution électrique, les centres de données représentent environ 1 % de l'électricité mondiale ; les seuls États-Unis (56,0 milliards de kWh/an) en représentent environ 0,4 point. | 1 % mondial (infrastructure incluse), ~0,4 % du total mondial pour les États-Unis seuls | O3 | choc | [S3] | V |
| F.INT.H1.007 | 2000-2006 | US | L'énergie consommée par les serveurs et les centres de données américains, infrastructure de refroidissement comprise, double sur la période, selon l'estimation reprise dans le rapport remis au Congrès en 2007. | doublement 2000→2006 | O3, O6 | choc | [S4] | K |
| F.INT.H1.008 | 1995-2004 | US | La généralisation du micro-ordinateur de bureau, puis de l'écran, se fait sans gain d'efficacité énergétique documenté par unité comparable sur la fenêtre : le sujet n'entre dans l'agenda de normalisation qu'après 2005. | qualitatif | P3, M4, O2 | co:X.INT.01 | [S1] | K |
| F.INT.H1.009 | 2004 | US, EU | Le passage du foyer connecté majoritairement au haut débit permanent supprime la déconnexion entre deux sessions et laisse modem et routeur sous tension en continu, sans qu'aucune mesure d'ampleur nationale de cet effet ne soit documentée pendant la fenêtre. | qualitatif | P3, P5, O3 | choc | [S1] | K |

### Jalons cités
<!-- Lines 60-63 -->

`J.INT.1999.07` (affirmation de 1999), `J.INT.2000.07` (mesure de 2000, bascule principale),
`J.INT.2004.04` (haut débit majoritaire, connexion permanente).

### Trajectoire `T.INT.H1`
<!-- Lines 66-81 -->

| année | phase | intensité | ce qui change | faits et jalons |
| --- | --- | --- | --- | --- |
| avant t0 | latent | 0 | Le parc de micro-ordinateurs et de serveurs existe mais sa consommation n'est pas un sujet public ; aucune mesure agrégée n'est cherchée. | |
| 1995 | latent | 0 | Le réseau commercial démarre ; sa consommation reste hors de vue. | |
| 1996 | latent | 0 | Diffusion continue des micro-ordinateurs de bureau sans suivi énergétique dédié. | co:X.INT.01 |
| 1997 | latent | 0 | Aucun signal de rupture identifié. | |
| 1998 | latent | 0 | Le pétrole bon marché déplace l'attention loin du coût de l'énergie électrique. | |
| 1999 | émergence | 1 | Une affirmation non mesurée fixe le sujet dans le débat public. | F.INT.H1.001, F.INT.H1.002, J.INT.1999.07 |
| 2000 | crise | 2 | Une mesure de laboratoire corrige l'affirmation d'un ordre de grandeur ; bascule de l'année. | F.INT.H1.003, J.INT.2000.07 |
| 2001 | consolidation | 0 | Le sujet énergétique des équipements se lit surtout par la contrainte de localisation (H2), pas par de nouvelles mesures nationales : aucun fait propre à H1 pour cette année. | |
| 2002 | consolidation | 1 | Pas de nouvelle mesure d'ampleur identifiée ; la croissance des centres de données, doublement mesuré sur 2000-2005, se poursuit sous le radar public. | F.INT.H1.004 |
| 2003 | consolidation | 1 | Idem : croissance continue, pas de nouvelle affirmation ni de nouvelle mesure publique majeure. | F.INT.H1.004 |
| 2004 | accélération | 2 | La connexion permanente du foyer généralise l'équipement sous tension continue. | F.INT.H1.009, J.INT.2004.04 |
| 2005 | banalisation | 1 | Fin de fenêtre : la consommation des centres de données a doublé depuis 2000, sans alarme publique comparable à celle de 1999. | F.INT.H1.006 |

### Narratif
<!-- Lines 84-97 -->

Le sujet énergétique de l'appareil numérique s'ouvre par une affirmation non mesurée en 1999
[F.INT.H1.001], reprise jusqu'au Congrès [F.INT.H1.002], avant qu'une mesure de laboratoire ne la
corrige d'un ordre de grandeur en 2000 [F.INT.H1.003, J.INT.2000.07]. La consommation réelle des
centres de données croît fortement sur la décennie, doublant entre 2000 et 2005 dans le monde
[F.INT.H1.004] et aux États-Unis entre 2000 et 2006 [F.INT.H1.007], mais reste une part minoritaire
de l'électricité nationale [F.INT.H1.006]. Le passage à la connexion permanente en 2004 change la
nature de la consommation domestique, de la session à l'état continu, sans qu'une mesure d'ampleur
en documente le volume pendant la fenêtre [F.INT.H1.009, J.INT.2004.04]. La forme du signal est
donc un écart entre discours et mesure en 1999-2000 [F.INT.H1.001, F.INT.H1.003], suivi d'une
croissance réelle mais discrète de la consommation jusqu'en 2005 [F.INT.H1.004, F.INT.H1.006].

---

## H2 Énergie comme contrainte et facteur de localisation
<!-- Lines 100-103 -->

**Question :** Où et pourquoi les usines s'installent-elles ; l'accès à l'électricité borne-t-il
la croissance ?

### Faits
<!-- Lines 106-115 -->

| id | année | bloc | énoncé | valeur | acteurs | attribution | source | statut |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| F.INT.H2.001 | 2000-2001 | US | La Californie connaît des coupures tournantes et un état d'urgence électrique, dans l'État qui héberge la plus forte densité d'entreprises du réseau et de centres d'hébergement du pays. | qualitatif | O3, O6, O1 | co:X.INT.10 | [S5] | K |
| F.INT.H2.002 | 2000-2001 | US | La croissance de la demande électrique californienne des années 1990, portée par l'essor de la Silicon Valley, est citée par des acteurs du secteur électrique comme un facteur du resserrement de l'offre, sans être identifiée comme cause principale par les analyses officielles de la crise. | croissance de la demande +15 % 1990-2000 (Californie) | O3, O6 | co:X.INT.10 | [S6] | K |
| F.INT.H2.003 | 2001 | US | Une analyse de presse spécialisée conclut que l'informatique n'est pas la cause de la pénurie électrique californienne, en s'appuyant sur des représentants du secteur électrique et de la recherche du secteur. | qualitatif | O3, O6 | co:X.INT.10 | [S7] | K |
| F.INT.H2.004 | 2001 | US | Une synthèse d'une institution monétaire internationale attribue la crise californienne au décalage entre offre et demande, aux défauts de conception du marché de gros et à la contrainte réglementaire sur les prix de détail, sans mentionner l'informatique ou les centres d'hébergement parmi les causes. | qualitatif | O6 | exo | [S8] | K |
| F.INT.H2.005 | 2001 | US | Des grands consommateurs industriels de la Silicon Valley, dont un fabricant de semi-conducteurs, réduisent volontairement une part de leur charge lors des premières coupures tournantes, en échange d'une protection de leurs circuits critiques. | réduction volontaire ≥10 % de charge | M9, O4 | co:X.INT.10 | [S7] | K |
| F.INT.H2.006 | 1995-2005 | US | Les premiers grands centres d'hébergement s'implantent près des points d'échange réseau et des marchés urbains denses de la côte Ouest et du nord-est américain, avant que le prix ou la disponibilité de l'électricité ne deviennent un critère de localisation documenté pour la fenêtre. | qualitatif | O1, O3 | choc | [S5] | K |

### Jalons cités
<!-- Lines 118-121 -->

`J.INT.2001.07` (crise électrique californienne, bascule principale), `J.INT.1998.07`
(pétrole bon marché, contexte).

### Trajectoire `T.INT.H2`
<!-- Lines 124-139 -->

| année | phase | intensité | ce qui change | faits et jalons |
| --- | --- | --- | --- | --- |
| avant t0 | latent | 0 | Aucune installation du réseau n'est documentée comme contrainte par l'électricité. | |
| 1995 | latent | 0 | Premiers centres d'hébergement, sans contrainte énergétique visible. | F.INT.H2.006 |
| 1996 | latent | 0 | Pas de signal identifié. | |
| 1997 | latent | 0 | Pas de signal identifié. | |
| 1998 | latent | 0 | Énergie bon marché ; aucune contrainte de localisation rapportée. | J.INT.1998.07 |
| 1999 | émergence | 1 | Croissance de la demande électrique californienne, portée en partie par la Silicon Valley. | F.INT.H2.002 |
| 2000 | crise | 3 | Début des coupures tournantes en Californie ; rupture de ligne de base. | F.INT.H2.001, J.INT.2001.07 |
| 2001 | crise | 3 | État d'urgence, réduction volontaire de charge des industriels, débat sur la part réelle des centres d'hébergement dans la crise. | F.INT.H2.003, F.INT.H2.004, F.INT.H2.005 |
| 2002 | consolidation | 0 | Sortie de crise ; pas de nouvelle contrainte documentée. | |
| 2003 | consolidation | 0 | Pas de signal identifié. | |
| 2004 | consolidation | 0 | Pas de signal identifié. | |
| 2005 | banalisation | 0 | Fin de fenêtre : aucune autre contrainte énergétique de localisation documentée que l'épisode californien. | |

### Narratif
<!-- Lines 142-155 -->

La crise électrique californienne de 2000-2001 est l'unique épisode de contrainte énergétique
documenté sur la fenêtre pour l'appareil du réseau [F.INT.H2.001, J.INT.2001.07]. Le lien avec les
centres d'hébergement, souvent avancé par association géographique, n'est pas confirmé comme cause
principale par les analyses spécialisées consultées : une synthèse de presse technique et une
synthèse d'une institution monétaire internationale l'attribuent au décalage offre-demande et aux
défauts du marché de gros [F.INT.H2.003, F.INT.H2.004]. La croissance de la demande liée à la
Silicon Valley est un facteur cité par le secteur électrique lui-même, mais secondaire dans les
analyses officielles [F.INT.H2.002]. Faute d'une contrainte identifiée avant 2005, les premières
implantations de centres d'hébergement de la fenêtre semblent guidées par la proximité réseau et
les marchés urbains, non par l'électricité [F.INT.H2.006].

---

## H3 Contexte énergétique macro : prix, mix, abondance
<!-- Lines 158-161 -->

**Question :** Dans quel environnement énergétique le choc se déploie-t-il, et cet environnement
change-t-il pendant la fenêtre ?

### Faits
<!-- Lines 164-176 -->

| id | année | bloc | énoncé | valeur | acteurs | attribution | source | statut |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| F.INT.H3.001 | 1993-1997 | US | Le prix moyen annuel du brut américain (WTI) reste dans une fourchette basse et stable avant de refluer. | 18,43 (1993) · 17,20 (1994) · 20,61 (1997) $/baril nominal | O4, O3 | exo | [S9] | V |
| F.INT.H3.002 | 1998 | US | Le prix moyen annuel du brut américain touche son point bas nominal de la fenêtre. | 14,42 $/baril nominal | O4, O3 | exo | [S9] | V |
| F.INT.H3.003 | 1998 | US | Déflaté par l'indice des prix à la consommation américain (1998 = 163,0 contre 2005 = 195,3, base 1982-84=100), le point bas nominal de 1998 vaut environ 17,3 dollars en pouvoir d'achat de 2005, soit un point bas réel proche du point bas nominal lui-même car l'inflation cumulée sur la période reste modérée. | ≈17,3 $/baril en dollars de 2005 (calcul) | O4 | exo | [S9], [S10] | V |
| F.INT.H3.004 | 1999-2002 | US | Le prix moyen annuel du brut américain remonte puis oscille sans dépasser le niveau d'avant 1998 pendant trois ans. | 19,34 (1999) · 30,38 (2000) · 25,98 (2001) · 26,18 (2002) $/baril nominal | O4, O3 | exo | [S9] | V |
| F.INT.H3.005 | 2003-2005 | US | Le prix moyen annuel du brut américain enchaîne trois hausses consécutives jusqu'à la fin de la fenêtre, atteignant près de quatre fois le point bas de 1998. | 31,08 (2003) · 41,51 (2004) · 56,64 (2005) $/baril nominal | O4, O3 | exo | [S9] | V |
| F.INT.H3.006 | 1993-1999 | US | Le prix du gaz naturel livré au secteur électrique reste bas et étroitement borné sur toute la première moitié de la fenêtre, sans tendance nette. | 2,54 (1993) · 2,22 (1994) · 1,97 (1995) · 2,62 (1996) · 2,71 (1997) · 2,32 (1998) · 2,55 (1999) $/million de Btu | O3, O4 | exo | [S16] | V |
| F.INT.H3.007 | 2000-2005 | US | Le prix du gaz naturel livré au secteur électrique bascule en 2000, double par rapport à la moyenne des années 1990, marque un creux relatif en 2002 puis grimpe jusqu'à un sommet de fenêtre en 2005, à plus de trois fois son niveau de 1999. | 4,27 (2000) · 4,48 (2001) · 3,59 (2002) · 5,41 (2003) · 5,96 (2004) · 8,24 (2005) $/million de Btu | O3, O4 | exo | [S16] | V |
| F.INT.H3.008 | 1995-2005 | US | L'intensité énergétique de l'économie américaine, énergie consommée par dollar de PIB, poursuit sa baisse tendancielle entamée dans les années 1970 sur toute la fenêtre. | 8,6 (1995) → 6,7 (2005) quadrillions de Btu par milliard de dollars chaînés 2012 de PIB, soit -22 % | O6 | exo | [S17] | V |
| F.INT.H3.009 | 1995-2005 | US | Le mix de production électrique américain reste dominé par le charbon et le nucléaire, avec une montée continue mais encore minoritaire du gaz naturel, sans rupture documentée sur la fenêtre. | qualitatif | O3, O6 | exo | [S12] | K |

### Jalons cités
<!-- Lines 179-182 -->

`J.INT.1998.07` (point bas nominal du pétrole, bascule principale), `J.INT.2005.07`
(remontée du pétrole en fin de fenêtre).

### Trajectoire `T.INT.H3`
<!-- Lines 185-200 -->

| année | phase | intensité | ce qui change | faits et jalons |
| --- | --- | --- | --- | --- |
| avant t0 | consolidation | 0 | Prix du pétrole bas et stable depuis le contre-choc des années 1980 ; pas de tension identifiée. | |
| 1995 | consolidation | 0 | Continuité du contexte d'énergie bon marché. | F.INT.H3.001 |
| 1996 | consolidation | 0 | Continuité. | |
| 1997 | consolidation | 0 | Prix du brut encore en léger repli. | F.INT.H3.001 |
| 1998 | crise (pour les producteurs) | 2 | Point bas nominal du pétrole de toute la fenêtre ; gaz naturel encore bas, sans tendance. | F.INT.H3.002, F.INT.H3.003, F.INT.H3.006, J.INT.1998.07 |
| 1999 | émergence | 1 | Remontée amorcée du pétrole ; gaz naturel toujours dans sa fourchette basse. | F.INT.H3.004, F.INT.H3.006 |
| 2000 | accélération | 2 | Prix du brut au-dessus du niveau d'avant 1998 ; gaz naturel double par rapport à sa moyenne des années 1990. | F.INT.H3.004, F.INT.H3.007 |
| 2001 | consolidation | 1 | Repli partiel du brut sous l'effet de la récession ; gaz naturel encore élevé. | F.INT.H3.004, F.INT.H3.007 |
| 2002 | consolidation | 1 | Creux relatif du prix du gaz naturel après 2001, sans revenir au niveau des années 1990. | F.INT.H3.007 |
| 2003 | accélération | 2 | Reprise de la hausse du brut et du gaz. | F.INT.H3.005, F.INT.H3.007 |
| 2004 | accélération | 2 | Poursuite de la hausse du brut et du gaz. | F.INT.H3.005, F.INT.H3.007 |
| 2005 | rupture | 3 | Prix du brut à près de quatre fois le point bas de 1998 ; sommet de fenêtre aussi pour le gaz naturel ; fin de la fenêtre sur un contexte énergétique inversé par rapport au début. | F.INT.H3.005, F.INT.H3.007, J.INT.2005.07 |

### Narratif
<!-- Lines 203-220 -->

Le choc Internet démarre dans une énergie exceptionnellement bon marché, le prix du pétrole
touchant son point bas nominal de la fenêtre en 1998 [F.INT.H3.002, J.INT.1998.07], un point bas
dont le calcul en monnaie constante ne change pas l'ordre de grandeur compte tenu d'une inflation
américaine modérée sur la période [F.INT.H3.003]. Le gaz naturel reste dans une fourchette basse
sans tendance nette jusqu'en 1999, double dès 2000, puis, après un creux relatif en 2002, culmine
à son tour en 2005 [F.INT.H3.006, F.INT.H3.007]. La seconde moitié de la fenêtre inverse le
contexte pour les deux combustibles : le pétrole enchaîne les hausses jusqu'à quadrupler son point
bas en 2005 [F.INT.H3.005, J.INT.2005.07], et le gaz naturel clôt la fenêtre à plus de trois fois
son niveau de 1999 [F.INT.H3.007]. L'intensité énergétique de l'économie américaine continue de
baisser sur toute la période, tendance de fond antérieure au choc et non spécifique à lui
[F.INT.H3.008]. Le choc Internet n'a donc pas connu un climat énergétique stable sur ses dix ans :
il commence dans l'abondance sur le pétrole comme sur le gaz et se referme sur une remontée durable
des deux prix [F.INT.H3.005, F.INT.H3.007], ce qui borne toute lecture de la productivité de la
période (C1) sans qu'on tranche ici le sens de causalité.

---

## H4 Effets du choc sur l'énergie du reste de l'économie
<!-- Lines 223-225 -->

**Question :** Le choc réduit-il ou déplace-t-il la consommation d'énergie des autres activités ?

### Faits
<!-- Lines 228-238 -->

| id | année | bloc | énoncé | valeur | acteurs | attribution | source | statut |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| F.INT.H4.001 | 2002 | US, EU | Des premières évaluations publiques comparent le bilan matière et énergie du commerce en ligne à celui du commerce physique : papier économisé et supports physiques évités d'un côté, déplacements de livraison ajoutés de l'autre. | qualitatif | O7, O6, O4 | choc | [S13] | K |
| F.INT.H4.002 | début 2000s | US, EU | Les travaux contemporains de la fenêtre sur le bilan énergétique du commerce en ligne ne convergent pas vers un signe unique net ; aucune évaluation ne s'impose comme référence pendant la période étudiée. | qualitatif | O7 | choc | [S13] | K |
| F.INT.H4.003 | 1995-2000 | US | Le nombre de télétravailleurs américains, au sens large de la définition professionnelle du secteur (au moins un jour par mois hors du lieu de travail habituel), progresse fortement sur la seconde moitié des années 1990. | 19,6 millions (1999) → 23,6 millions (2000) | P3, M1, M4 | choc | [S14] | V |
| F.INT.H4.004 | 2001-2004 | US | Le nombre de télétravailleurs américains, même définition professionnelle, culmine en 2001 puis reflue d'environ un sixième, tout en représentant encore près d'un cinquième de la population active occupée en 2004. | 28,8 millions (2001) → 24,1 millions, soit 18,3 % des actifs occupés (2004) | P3, M1, M4 | choc | [S14] | V |
| F.INT.H4.005 | 1995-2005 | US | Contrairement au chiffrage professionnel de H4.003-004, la seule mesure officielle agrégée du travail à domicile (Current Population Survey du Bureau of Labor Statistics) ne couvre que mai 2001 et mai 2004 pendant la fenêtre, avec une définition plus étroite (au moins une fois par semaine) : aucun bilan net déplacements évités contre déplacements induits, par le télétravail ou le commerce en ligne, n'est publié par les administrations de transport pendant la fenêtre. | 19,8 millions, 15 % de l'emploi total (mai 2001) → 20,7 millions, 15 % de l'emploi non agricole (mai 2004) | O6 | choc | [S16] | V |
| F.INT.H4.006 | 1995-2005 | US, EU | La numérisation des contenus (musique, texte, image) réduit la production de supports physiques dans les industries culturelles concernées, effet documenté qualitativement en A5 et F1 sans chiffrage énergétique dédié dans la fenêtre. | qualitatif | M2, O4 | co:X.INT.08 | [S13] | K |
| F.INT.H4.007 | 1995-2005 | US | Le débat contemporain sur l'effet rebond, une consommation induite par le gain d'efficacité compensant tout ou partie de l'économie visée, reste ouvert dans les publications techniques de la période sans qu'une mesure agrégée américaine ne le tranche pour l'économie numérique. | qualitatif | O7 | choc | [S13] | D |

### Jalons cités
<!-- Lines 241-244 -->

`J.INT.2002.07` (dématérialisation, bascule principale, jalon générique à requalifier), `J.INT.2004.04`
(connexion permanente, contexte du télétravail et du commerce en ligne).

### Trajectoire `T.INT.H4`
<!-- Lines 247-262 -->

| année | phase | intensité | ce qui change | faits et jalons |
| --- | --- | --- | --- | --- |
| avant t0 | latent | 0 | Commerce et travail restent très majoritairement physiques ; pas de substitution documentée. | |
| 1995 | latent | 0 | Premiers commerces en ligne, volume négligeable sur le bilan énergétique global. | |
| 1996 | latent | 0 | Pas de signal identifié. | |
| 1997 | émergence | 1 | Croissance du télétravail déjà amorcée depuis le milieu des années 1990. | F.INT.H4.003 |
| 1998 | émergence | 1 | Continuité de la croissance du télétravail. | F.INT.H4.003 |
| 1999 | émergence | 1 | Le télétravail dépasse les vingt millions de personnes aux États-Unis. | F.INT.H4.003 |
| 2000 | accélération | 1 | Poursuite de la croissance du commerce en ligne et du télétravail. | F.INT.H4.003 |
| 2001 | accélération | 1 | Le télétravail continue de croître pendant la récession. | F.INT.H4.004 |
| 2002 | émergence | 1 | Premières évaluations publiques, non conclusives, du bilan matière-énergie du commerce en ligne. | F.INT.H4.001, F.INT.H4.002, J.INT.2002.07 |
| 2003 | consolidation | 1 | Pas de nouvelle évaluation identifiée ; le débat reste ouvert. | F.INT.H4.007 |
| 2004 | consolidation | 1 | Le télétravail atteint près d'un cinquième des actifs occupés américains. | F.INT.H4.004, J.INT.2004.04 |
| 2005 | banalisation | 1 | Fin de fenêtre : substitution partielle documentée par le télétravail, bilan net du commerce en ligne toujours disputé. | F.INT.H4.007 |

### Narratif
<!-- Lines 265-281 -->

Le télétravail est le signal le plus solide de cette sous-dimension : au sens large, il progresse
fortement jusqu'en 2001 puis reflue, tout en couvrant encore près d'un cinquième des actifs occupés
américains en 2004 [F.INT.H4.003, F.INT.H4.004] ; la mesure officielle, plus étroite, reste stable
à 15 % de l'emploi entre 2001 et 2004 [F.INT.H4.005]. Le bilan énergétique du commerce en ligne, en
revanche, reste disputé pendant toute la fenêtre : les premières évaluations publiques de 2002 ne
concluent pas dans un sens net entre papier et supports évités d'un côté, déplacements de livraison
de l'autre [F.INT.H4.001, F.INT.H4.002, J.INT.2002.07]. Aucune mesure agrégée américaine ne tranche
le débat contemporain sur l'effet rebond pour l'économie numérique naissante [F.INT.H4.007]. La
numérisation des contenus culturels réduit la production de supports physiques mais ce fait vit
principalement dans les domaines A5 et F1, cité ici seulement comme part du confondant prérequis
[F.INT.H4.006]. La forme de la trajectoire est donc une montée suivie d'un plateau sur le travail,
sans bascule identifiable [F.INT.H4.003, F.INT.H4.004, F.INT.H4.005], et une question ouverte plutôt qu'un résultat sur
le commerce [F.INT.H4.001, F.INT.H4.002, F.INT.H4.007].

---

## Sources
<!-- Lines 284-303 -->

| clé | type | référence | note |
| --- | --- | --- | --- |
| [S1] | presse | Forbes, Peter Huber et Mark Mills, « Dig more coal — the PCs are coming », 31 mai 1999 ; reprises et auditions consécutives | Historique : cette clé restait non revérifiée directement lors de la première collecte. Voir [S15] pour la lecture directe du texte original faite le 2026-09-22, qui remplace ce statut pour F.INT.H1.001. |
| [S2] | acad | Lawrence Berkeley National Laboratory, travaux de J. Koomey et al. sur la consommation électrique des équipements de bureau et de réseau, 1999-2000 | Historique : lbl.gov et osti.gov inaccessibles pendant la première collecte, ordre de grandeur non revérifié directement. Voir [S15] pour la lecture directe faite le 2026-09-22 (document LBNL-46509, qui contient aussi le texte intégral de l'audition Mills de février 2000), qui remplace ce statut pour F.INT.H1.002 et F.INT.H1.003. |
| [S3] | acad | J. Koomey, *Growth in Data Center Electricity Use 2005 to 2010* et travaux antérieurs (2007-2008) sur le doublement 2000-2005 de l'électricité des centres de données dans le monde | Historique : chiffres retrouvés par recherche web sans ouverture directe lors de la première collecte. Voir [S15] pour la lecture directe de l'article Koomey 2008 (Environ. Res. Lett.) faite le 2026-09-22, qui remplace ce statut pour F.INT.H1.004, F.INT.H1.005, F.INT.H1.006. |
| [S4] | off | US EPA, *Report to Congress on Server and Data Center Energy Efficiency*, août 2007 (en réponse à la Public Law 109-431), chiffre du doublement de l'énergie des serveurs et centres de données américains 2000-2006 | energystar.gov référencé par recherche web ; PDF non ouvert directement en rendu texte lisible pendant la rédaction. Chiffre à confirmer sur le rapport lui-même. Non revérifié le 2026-09-22 (hors priorité de cette passe) : F.INT.H1.007 reste `K`. |
| [S5] | off | California Energy Commission et California ISO, chronologie de la crise électrique de 2000-2001 ; proclamation d'état d'urgence, janvier 2001 (reprise de [S73] de la chronologie) | Page CEC déjà notée sans contenu historique lors de la rédaction de la chronologie ; non revérifiée ici. |
| [S6] | presse | VOA News, « Silicon Valley Copes With California Power Crisis », 7 août 2001 ; reprises de données sur la croissance de la demande électrique californienne des années 1990 (+15 % 1990-2000) | Chiffre de croissance retrouvé par recherche web ; article non ouvert en texte intégral (contenu agrégé par le moteur de recherche). Non revérifié le 2026-09-22 (hors priorité de cette passe). |
| [S7] | presse | CNN / IDG News Service, « IT cleared of blame in California energy crunch », 4 juillet 2001 | Page renvoyée en erreur 451 (indisponible pour raison légale) lors de la tentative de récupération directe ; contenu repris via le résumé du moteur de recherche uniquement, citant des représentants du secteur électrique (EPRI) et des grands consommateurs industriels (dont un fabricant de semi-conducteurs) disculpant l'informatique. Tentative renouvelée le 2026-09-22 : toujours indisponible (hors priorité, faits datés plutôt que chiffrés). |
| [S8] | off | Fonds monétaire international, *Finance & Development*, septembre 2001, article de Besant-Jones et Tenenbaum sur les causes de la crise électrique californienne | Page récupérée et lue directement (WebFetch) : l'article attribue la crise au décalage offre-demande, aux défauts du marché de gros et à la contrainte réglementaire sur les prix de détail ; ne mentionne ni les centres d'hébergement ni l'informatique parmi les causes. |
| [S9] | stat | U.S. Energy Information Administration, *Cushing, OK WTI Spot Price FOB*, série annuelle (dnav/pet/hist, série RWTC) | Récupérée directement (WebFetch, page LeafHandler) : valeurs confirmées identiques à celles déjà vérifiées dans la chronologie ([S70]) pour 1993 à 2005. |
| [S10] | stat | Federal Reserve Bank of Minneapolis, série de l'indice des prix à la consommation américain (CPI-U, base 1983=100), valeurs annuelles 1998 et 2005 | Ouvert et lu le 2026-09-22 : https://www.minneapolisfed.org/about-us/monetary-policy/inflation-calculator/consumer-price-index-1913- ; 1998 = 163,0 ; 2005 = 195,3, confirmés. Calcul de déflation du point bas pétrolier fait dans ce fichier (F.INT.H3.003), méthode : 14,42 × (195,3 / 163,0) ≈ 17,3. |
| [S11] | stat | U.S. Energy Information Administration, prix du gaz naturel livré au secteur électrique, série annuelle (dnav/ng/hist, série N3045US3) | Historique : valeurs 1993-2005 obtenues en une passe par un outil intermédiaire, non recroisées. Invalidées le 2026-09-22 : la série N3045US3 elle-même ne couvre que 1990-1992 puis 2000 et suivant, sans donnée 1993-1999 ; les valeurs alors retenues correspondaient en fait, décalées de 5 ans, à d'autres années de la vraie série (ex. la valeur notée pour 1998 était celle de 2004). Voir [S16] pour la série de remplacement, ouverte et lue directement, qui couvre toute la fenêtre. |
| [S12] | acad | U.S. Energy Information Administration, indicateurs d'intensité énergétique du PIB américain (quadrillions de Btu par milliard de dollars chaînés de PIB) ; valeurs approximatives 1995 ≈ 8,6 et 2005 ≈ 6,7 retrouvées par recherche web sans ouverture du tableau primaire | Historique : ordre de grandeur seulement, non revérifié sur table primaire. Voir [S17] pour la lecture directe faite le 2026-09-22, qui confirme exactement ces deux valeurs et remplace ce statut pour F.INT.H3.008. Le mix électrique (charbon, nucléaire, gaz) de F.INT.H3.009 reste un énoncé qualitatif de connaissance générale, non revérifié sur série eia.gov pendant cette collecte. |
| [S13] | acad | Travaux d'évaluation du cycle de vie du commerce en ligne et de la dématérialisation, début des années 2000 (laboratoires nationaux américains, EPA, équipes universitaires européennes), repris de [S74] de la chronologie ; débat contemporain sur l'effet rebond dans la littérature d'efficacité énergétique de la période | Jalon et littérature volontairement génériques : aucune publication unique ne fait bascule, conformément à la note déjà portée sur J.INT.2002.07. Non revérifié le 2026-09-22 (hors priorité de cette passe, faits qualitatifs sans chiffre à vérifier) ; F.INT.H4.001, F.INT.H4.002, F.INT.H4.006, F.INT.H4.007 restent `K`/`D`. |
| [S14] | stat | International Telework Association and Council puis Telework Coalition, séries de dénombrement des télétravailleurs américains, 1999-2004 ; chiffre de 2004 (24,1 millions, 18,3 % des actifs occupés) | Ouvert et lu le 2026-09-22 : https://www.telcoa.org/resources/references/telework-tools/telework-facts-stats/ ; confirme exactement 19,6 M (1999, ITAC), 23,6 M (2000, ITAC), 28,8 M (2001, ITAC) et 24,1 M (2004, Dieringer Research Group/ITAC). Source professionnelle du secteur du télétravail, à traiter avec la prudence méthodologique déjà notée ; voir [S16] pour la mesure officielle BLS de définition différente. |
| [S15] | acad | J. G. Koomey, « Worldwide electricity used in data centers », *Environmental Research Letters* 3, 034008, 2008 ; Kawamoto, Koomey et al., *Electricity Used by Office Equipment and Network Equipment in the U.S.: Detailed Report and Appendices*, LBNL-45917, février 2001 ; J. G. Koomey, *Rebuttal to Testimony on 'Kyoto and the Internet: The Energy Implications of the Digital Economy'*, LBNL-46509, août 2000 (inclut le texte intégral de la déposition de Mark Mills du 2 février 2000 devant la Chambre des représentants, et l'article Forbes original de mai 1999) | Ouverts et lus le 2026-09-22 : (1) datacenters.lbl.gov/sites/default/files/Koomey_2008.pdf — monde : 70,8 milliards kWh/an (2000) → 152,5 milliards kWh/an (2005), ×2,15 ; 0,5 % (2000) puis 1 % (2005, infrastructure incluse) de l'électricité mondiale ; États-Unis 2005 = 56,0 milliards kWh/an, soit 37 % du total mondial des centres de données et ≈0,4 % de l'électricité mondiale totale ; trois quarts de la croissance imputables aux serveurs volume. (2) escholarship.org/content/qt3c93475q/qt3c93475q.pdf (LBNL-45917) — abstract : 74 TWh/an, 2 % de l'électricité américaine pour les équipements directs, 3 % en ajoutant télécoms et fabrication électronique, données arrêtées fin 1999. (3) eta-publications.lbl.gov/sites/default/files/lbnl-46509.pdf (LBNL-46509) — cite la déposition Mills du 2 février 2000 : « something like 8% of the nation's electric supply... the total probably reaches 13% » ; réfutation Koomey : « electricity used for all office, telecommunications, and network equipment... is about 3%... a factor of four lower than the 13% claimed by Mills ». |
| [S16] | stat | U.S. Energy Information Administration, *Annual Energy Outlook Retrospective*, Table 8a, « Natural gas price, electric power sector, actual versus projected », ligne « Actual in nominal dollars » (série open data API TOTAL.NGEIUUS.A) ; U.S. Bureau of Labor Statistics, *Work at Home*, communiqués CPS de mars 2002 (homey_03012002) et septembre 2005 (homey_09222005) | Ouverts et lus le 2026-09-22 : (1) eia.gov/outlooks/aeo/retrospective/pdf/table_8a.pdf — prix du gaz naturel secteur électrique en $/million de Btu (unité différente de la série [S11] invalidée, en $/millier de pieds cubes) : 2,54 (1993) · 2,22 (1994) · 1,97 (1995) · 2,62 (1996) · 2,71 (1997) · 2,32 (1998) · 2,55 (1999) · 4,27 (2000) · 4,48 (2001) · 3,59 (2002) · 5,41 (2003) · 5,96 (2004) · 8,24 (2005). (2) bls.gov/news.release/history/homey_03012002.txt — mai 2001 : 19,8 millions de personnes ont travaillé à domicile au moins une fois par semaine, 15 % de l'emploi total. bls.gov/news.release/history/homey_09222005.txt — mai 2004 : 20,7 millions, 15 % de l'emploi non agricole. Ces deux communiqués établissent qu'une mesure officielle du travail à domicile existe pour deux points de la fenêtre, avec une définition plus étroite que celle d'ITAC/Telework Coalition ([S14]). |
| [S17] | off | U.S. Energy Information Administration, *Annual Energy Outlook Retrospective*, Table 29, « Energy intensity, projected versus actual », ligne « Actual », données BEA, quadrillion Btu par milliard de dollars chaînés 2012 de PIB | Ouvert et lu le 2026-09-22 : eia.gov/outlooks/aeo/retrospective/pdf/Table_29.pdf ; ligne Actual, source de données déclarée « U.S. Energy Information Administration open data API, série TOTAL.TETCBUS.A » et BEA (dollars chaînés 2012) : 1995 = 8,6, 2005 = 6,7, confirme exactement l'ordre de grandeur déjà retenu ([S12]). |
