# G. Politique et gouvernance — Cloud 2005-2015

Ce que la puissance publique et les rapports de force internationaux ont connu pendant la
fenêtre du choc cloud, sous-dimension par sous-dimension : faits sourcés, jalons cités,
trajectoire année par année, narratif court. Le cloud est un choc **industriel** ; sa dimension
politique est le deuxième domaine le mieux doté de la chronologie (`par_annee/cloud_2005_2015.md`),
parce que le droit produit des événements datés. C'est la cellule où se joue la **souveraineté** :
des organisations publiques et privées de tous les pays confient leurs données à des usines
situées ailleurs et soumises à un droit étranger. Ligne de base : état des deux années précédant
2005. La comparaison avec l'autre choc est dans le `README.md` du domaine, pas ici.

## Table of Contents

1. [G1 Droit et régulation](#g1-droit-et-r-gulation) _(Lines 41-43)_
   1. [Faits](#faits) _(Lines 46-66)_
   1. [Jalons cités](#jalons-cit-s) _(Lines 69-72)_
   1. [Trajectoire `T.CLD.G1`](#trajectoire-t-cld-g1) _(Lines 75-90)_
   1. [Narratif](#narratif) _(Lines 93-108)_
1. [G2 Gouvernance de la technologie](#g2-gouvernance-de-la-technologie) _(Lines 111-114)_
   1. [Faits](#faits-1) _(Lines 117-127)_
   1. [Jalons cités](#jalons-cit-s-1) _(Lines 130-132)_
   1. [Trajectoire `T.CLD.G2`](#trajectoire-t-cld-g2) _(Lines 135-150)_
   1. [Narratif](#narratif-1) _(Lines 153-166)_
1. [G3 État, services publics et vie démocratique](#g3-tat-services-publics-et-vie-d-mocratique) _(Lines 169-173)_
   1. [Faits](#faits-2) _(Lines 176-190)_
   1. [Jalons cités](#jalons-cit-s-2) _(Lines 193-195)_
   1. [Trajectoire `T.CLD.G3`](#trajectoire-t-cld-g3) _(Lines 198-213)_
   1. [Narratif](#narratif-2) _(Lines 216-230)_
1. [G4 Géopolitique, souveraineté et sécurité](#g4-g-opolitique-souverainet-et-s-curit) _(Lines 233-237)_
   1. [Faits](#faits-3) _(Lines 240-253)_
   1. [Jalons cités](#jalons-cit-s-3) _(Lines 256-259)_
   1. [Trajectoire `T.CLD.G4`](#trajectoire-t-cld-g4) _(Lines 262-277)_
   1. [Narratif](#narratif-3) _(Lines 280-298)_
1. [Sources](#sources) _(Lines 301-330)_


---

## G1 Droit et régulation
<!-- Lines 41-43 -->

**Question :** Quelles lois, décisions et régulateurs apparaissent, avec quel retard sur les usages ?

### Faits
<!-- Lines 46-66 -->

| id | année | bloc | énoncé | valeur | acteurs | attribution | source | statut |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| F.CLD.G1.001 | 2003-2004 | US, EU | Avant t0 : le cadre juridique en place repose sur une loi antiterroriste américaine de 2001 élargissant l'accès des autorités aux données détenues par des tiers, et sur une directive européenne de 1995 encadrant le transfert des données personnelles hors de l'Union, deux textes antérieurs au choc et non conçus pour des données hébergées à l'étranger. | Public Law 107-56 (2001-10-26) ; directive 95/46/CE | O6, T1, T2 | exo | [S1] | V |
| F.CLD.G1.002 | 2008-07-10 | US | Les États-Unis adoptent une loi élargissant les pouvoirs de surveillance des communications électroniques, autorisant le renseignement à cibler des personnes situées hors du territoire américain sans mandat individualisé, avec effet sur les données hébergées par des fournisseurs américains où qu'elles se trouvent. | Public Law 110-261, FISA Amendments Act of 2008, 10 juillet 2008 | O6, M10 | exo | [S2] | V |
| F.CLD.G1.003 | 2011-12-08 | US | Un mémorandum de l'Office of Management and Budget crée un programme fédéral unique d'homologation de sécurité des services en nuage, applicable à toutes les agences ; une homologation vaut pour l'ensemble du gouvernement fédéral. | Mémorandum « Security Authorization of Information Systems in Cloud Computing Environments », signé Steven VanRoekel, 8 décembre 2011 | O6, M10 | choc | [S3] | V |
| F.CLD.G1.004 | 2012-01 | EU | La Commission européenne propose une refonte du cadre de protection des données personnelles, incluant des règles applicables aux traitements hors de l'Union et une obligation de notification des violations de données. | proposition de règlement, janvier 2012 | T2, O6 | choc | [S4] | K |
| F.CLD.G1.005 | 2012-07 | EU | Le groupe de travail réunissant les autorités nationales de protection des données de l'Union publie un avis dédié à l'informatique en nuage, posant des exigences de transparence contractuelle et de localisation pour les responsables de traitement qui recourent à des fournisseurs de cloud. | avis WP196, juillet 2012 | T2, O6 | choc | [S5] | K |
| F.CLD.G1.006 | 2013 | EU | À la suite des révélations sur la surveillance de masse, les autorités européennes de protection des données durcissent leur doctrine sur les transferts de données vers les États-Unis, sans attendre l'issue de la révision du cadre général. | durcissement de doctrine | T2, O6, O4 | co:X.CLD.07 | [S5] | K |
| F.CLD.G1.007 | 2015-06-02 | US | Les États-Unis adoptent une loi qui met fin à la collecte en masse de métadonnées téléphoniques par le renseignement et transfère la conservation de ces données aux opérateurs, avec obligation de demande individualisée pour y accéder. | Public Law 114-23, USA FREEDOM Act, 2 juin 2015 | O6, M10 | co:X.CLD.07 | [S6] | V |
| F.CLD.G1.008 | 2015-10-06 | EU | La Cour de justice de l'Union européenne invalide la décision de la Commission qui reconnaissait le cadre américain « sphère de sécurité » comme offrant un niveau de protection adéquat pour les transferts de données personnelles vers les États-Unis. | affaire C-362/14, arrêt du 6 octobre 2015 | T2, O6, O4, O2 | co:X.CLD.07 | [S7] | K |
| F.CLD.G1.009 | 2015 | EU | Plusieurs pays européens publient des référentiels nationaux de certification pour les services en nuage utilisés par les administrations et les organisations réglementées, en l'absence d'un cadre européen unifié. | référentiels nationaux | T2, O6, O2 | choc | [S8] | K |
| F.CLD.G1.010 | 2011-2015 | US | Le Congrès examine plusieurs propositions de loi visant à limiter l'accès des autorités américaines aux courriers électroniques hébergés de plus de six mois sans mandat, sans qu'aucune n'aboutisse pendant la fenêtre. | propositions non abouties | O6 | co:X.CLD.07 | [S9] | K |
| F.CLD.G1.011 | 2009-2015 | MONDE | Plusieurs pays imposent ou envisagent des obligations de localisation des données sur leur territoire pour certains secteurs (santé, finance, administration), instrument juridique distinct de la protection des données personnelles. | obligations sectorielles | O6, T2, T4 | choc | [S10] | K |

**Note sur les sources juridiques européennes.** Le portail du droit de l'Union (EUR-Lex) et le
site de la Cour de justice (CURIA) sont inaccessibles depuis cet environnement de recherche. La
directive 95/46/CE et l'arrêt *Schrems* (C-362/14) sont documentés par leur référence exacte
(numéro, date, juridiction) plutôt que par un accès direct au texte ; statut `V` réservé au seul
fait où un relais officiel accessible (govinfo.gov, whitehouse.gov) a pu être ouvert et lu.

### Jalons cités
<!-- Lines 69-72 -->

`J.CLD.2011.03`, `J.CLD.2013.01`, `J.CLD.2013.04`, `J.CLD.2015.02`, `J.CLD.2015.03`,
`J.CLD.2015.04`.

### Trajectoire `T.CLD.G1`
<!-- Lines 75-90 -->

| année | phase | intensité | ce qui change | faits et jalons |
| --- | --- | --- | --- | --- |
| avant t0 | latent | 1 | Cadre juridique antérieur au choc, non conçu pour l'hébergement à distance : loi antiterroriste américaine de 2001, directive européenne de 1995. | F.CLD.G1.001 |
| 2005 | latent | 0 | Aucun texte spécifique au cloud documenté cette année pour G1. | — |
| 2006 | latent | 0 | Aucun texte spécifique au cloud documenté cette année pour G1. | — |
| 2007 | latent | 0 | Aucun texte spécifique au cloud documenté cette année pour G1 ; le droit reste en retard sur l'usage déjà engagé en A. | — |
| 2008 | émergence | 2 | Élargissement des pouvoirs de surveillance des communications électroniques, avec portée extraterritoriale de fait sur les données hébergées par des fournisseurs américains. | F.CLD.G1.002 |
| 2009 | émergence | 0 | Aucun texte nouveau documenté cette année pour G1. | — |
| 2010 | émergence | 0 | Aucun texte nouveau documenté cette année pour G1. | — |
| 2011 | accélération | 3 | Création d'un programme fédéral unique d'homologation de sécurité pour les achats publics de cloud. | F.CLD.G1.003, J.CLD.2011.03 |
| 2012 | accélération | 2 | Proposition de refonte du cadre européen de protection des données ; premier avis européen dédié au cloud. | F.CLD.G1.004, F.CLD.G1.005 |
| 2013 | crise | 3 | Durcissement de la doctrine européenne sur les transferts transatlantiques après les révélations sur la surveillance de masse. | F.CLD.G1.006, J.CLD.2013.01, J.CLD.2013.04 |
| 2014 | crise | 0 | Poursuite du contentieux et du débat sans texte nouveau documenté cette année pour G1. | — |
| 2015 | crise | 3 | Invalidation du cadre de transfert transatlantique ; loi américaine mettant fin à la collecte en masse ; premiers référentiels nationaux de certification. | F.CLD.G1.007, F.CLD.G1.008, F.CLD.G1.009, J.CLD.2015.02, J.CLD.2015.03, J.CLD.2015.04 |

### Narratif
<!-- Lines 93-108 -->

Le droit part d'un cadre antérieur au choc et non conçu pour lui : une loi antiterroriste
américaine de 2001 et une directive européenne de 1995 [F.CLD.G1.001]. La première réponse
propre au cloud est américaine et sécuritaire, avec l'élargissement des pouvoirs de surveillance
en 2008 [F.CLD.G1.002], suivie trois ans plus tard par la création d'un programme unique
d'homologation qui rend l'achat public de cloud possible [F.CLD.G1.003]. Les révélations sur la
surveillance de masse en 2013 font basculer le registre : l'Europe durcit sa doctrine sur les
transferts hors de l'Union [F.CLD.G1.006], et la crise se referme en 2015 par deux textes
symétriques, l'invalidation judiciaire européenne du cadre transatlantique et une loi américaine
qui met fin à la collecte en masse de métadonnées [F.CLD.G1.007, F.CLD.G1.008]. Le droit répond
au choc avec retard mais de façon endogène : chaque texte cité est une réponse à une pratique déjà
installée, jamais une anticipation [F.CLD.G1.001][F.CLD.G1.002][F.CLD.G1.003][F.CLD.G1.006]
[F.CLD.G1.007][F.CLD.G1.008].

---

## G2 Gouvernance de la technologie
<!-- Lines 111-114 -->

**Question :** Qui fixe les normes du cloud, organismes de normalisation nationaux et
internationaux, fondations de l'open source comme gouvernance privée, certifications et audits ?

### Faits
<!-- Lines 117-127 -->

| id | année | bloc | énoncé | valeur | acteurs | attribution | source | statut |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| F.CLD.G2.001 | 2007-02 | US | Un consortium industriel d'exploitants et de constructeurs de centres de données publie une métrique partagée d'efficacité énergétique des installations ; première gouvernance privée d'une norme technique du secteur, hors de toute autorité publique. | consortium fondé février 2007 | O2, O3, M1 | choc | [S11] | K |
| F.CLD.G2.002 | 2011-09-28 | US | L'institut américain de normalisation publie la définition officielle de l'informatique en nuage, acte de gouvernance qui fixe le vocabulaire opposable pour tout marché ou audit : cinq caractéristiques, trois modèles de service, quatre modèles de déploiement. | NIST Special Publication 800-145, Mell et Grance, 28 septembre 2011 | O6, M1 | choc | [S12] | V |
| F.CLD.G2.003 | 2010-07 | US | Une fondation à but non lucratif est créée pour gouverner un projet ouvert de logiciel d'infrastructure, avec gouvernance partagée entre plusieurs entreprises et une organisation publique, explicitement pour empêcher que la pile d'infrastructure du cloud soit contrôlée par deux ou trois fournisseurs propriétaires. | lancement juillet 2010 | O6, O2, M1 | choc | [S13] | K |
| F.CLD.G2.004 | 2014-06 | US | Un système d'orchestration de conteneurs conçu par un grand exploitant est transféré en gouvernance ouverte par la création d'une fondation dédiée, séparant la maintenance du projet de l'entreprise qui l'a conçu. | fondation créée en 2015 sur la base du projet publié en juin 2014 | M1, O2, O1 | choc | [S14] | K |
| F.CLD.G2.005 | 2012-07 | EU | Le groupe des autorités européennes de protection des données pose, dans son avis sur le cloud, des critères d'audit et de certification des fournisseurs comme condition de conformité pour leurs clients organisationnels. | avis WP196 | T2, O6 | choc | [S5] | K |
| F.CLD.G2.006 | 2011-12 | US | Le programme fédéral d'homologation de sécurité des services en nuage crée un comité d'autorisation conjoint réunissant trois agences, qui devient l'autorité de fait pour juger de la conformité des fournisseurs vis-à-vis du secteur public fédéral. | comité conjoint DHS, DOD, GSA | O6, M10 | choc | [S3] | V |
| F.CLD.G2.007 | 2005-2015 | MONDE | Aucune instance intergouvernementale ne fixe de norme contraignante unique pour l'informatique en nuage pendant la fenêtre : la gouvernance se répartit entre normalisation nationale (États-Unis), avis d'autorités de protection des données (Europe) et fondations privées (projets ouverts). | absence de norme intergouvernementale contraignante | O6, O2 | choc | [S12] | K |

### Jalons cités
<!-- Lines 130-132 -->

`J.CLD.2007.07`, `J.CLD.2010.01`, `J.CLD.2011.01`, `J.CLD.2011.03`, `J.CLD.2014.03`.

### Trajectoire `T.CLD.G2`
<!-- Lines 135-150 -->

| année | phase | intensité | ce qui change | faits et jalons |
| --- | --- | --- | --- | --- |
| avant t0 | latent | 0 | Aucune gouvernance dédiée au cloud ; les standards de virtualisation et de la pile ouverte relèvent d'A2, pas encore d'une instance de gouvernance propre. | — |
| 2005 | latent | 0 | Aucune instance de gouvernance dédiée documentée cette année. | — |
| 2006 | latent | 0 | Aucune instance de gouvernance dédiée documentée cette année. | — |
| 2007 | émergence | 2 | Première gouvernance privée d'une norme technique du secteur par un consortium industriel. | F.CLD.G2.001, J.CLD.2007.07 |
| 2008 | émergence | 0 | Aucune bascule de gouvernance nouvelle documentée cette année. | — |
| 2009 | émergence | 0 | Aucune bascule de gouvernance nouvelle documentée cette année. | — |
| 2010 | accélération | 2 | Création d'une fondation ouverte pour empêcher le contrôle de la pile d'infrastructure par deux ou trois fournisseurs. | F.CLD.G2.003, J.CLD.2010.01 |
| 2011 | rupture | 3 | Définition normative officielle américaine ; création du comité d'autorisation conjoint fédéral. | F.CLD.G2.002, F.CLD.G2.006, J.CLD.2011.01, J.CLD.2011.03 |
| 2012 | consolidation | 2 | Premier avis européen posant des critères d'audit et de certification des fournisseurs. | F.CLD.G2.005 |
| 2013 | consolidation | 0 | Aucune bascule de gouvernance nouvelle documentée cette année. | — |
| 2014 | consolidation | 2 | Transfert d'un projet d'orchestration de conteneurs vers une gouvernance de fondation ouverte. | F.CLD.G2.004, J.CLD.2014.03 |
| 2015 | banalisation | 0 | La gouvernance reste répartie entre normalisation nationale, avis européens et fondations privées, sans instance intergouvernementale contraignante. | F.CLD.G2.007 |

### Narratif
<!-- Lines 153-166 -->

La gouvernance du cloud naît hors de toute autorité publique, par un consortium industriel qui
fixe en 2007 la première métrique d'efficacité partagée du secteur [F.CLD.G2.001]. Elle se
structure ensuite par trois voies distinctes qui ne se recouvrent pas : la normalisation
publique américaine, avec la définition officielle de 2011 [F.CLD.G2.002], la gouvernance
privée des fondations ouvertes, créées explicitement pour éviter qu'un standard technique soit
contrôlé par deux ou trois fournisseurs propriétaires [F.CLD.G2.003, F.CLD.G2.004], et l'avis
des autorités européennes de protection des données, qui pose des exigences de certification
sans produire elles-mêmes de norme technique [F.CLD.G2.005]. Faute d'instance intergouvernementale
contraignante, chaque bloc gouverne le cloud avec les instruments dont il dispose [F.CLD.G2.007] :
définition et homologation aux États-Unis [F.CLD.G2.006], avis et certification en Europe.

---

## G3 État, services publics et vie démocratique
<!-- Lines 169-173 -->

**Question :** Comment l'État se sert de la technologie et comment la vie démocratique en
est-elle changée : politiques d'achat public, stratégies nationales, migration des
administrations, marchés publics emblématiques ?

### Faits
<!-- Lines 176-190 -->

| id | année | bloc | énoncé | valeur | acteurs | attribution | source | statut |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| F.CLD.G3.001 | 2009-09 | US | Les États-Unis ouvrent un portail d'achat de services informatiques à la demande réservé aux administrations fédérales, première reconnaissance par un État que la capacité informatique s'achète sur catalogue comme une fourniture. | portail Apps.gov, septembre 2009 | O6, M10 | choc | [S15] | K |
| F.CLD.G3.002 | 2011-02-08 | US | Le directeur informatique fédéral des États-Unis publie une stratégie donnant la priorité aux services en nuage dans les achats informatiques de l'administration, dite politique « Cloud First ». | *Federal Cloud Computing Strategy*, Vivek Kundra, U.S. Chief Information Officer, 8 février 2011 | O6, M10 | choc | [S16] | V |
| F.CLD.G3.003 | 2011-07-26 | US | L'organe d'audit du Congrès constate que la quasi-totalité des agences fédérales n'a pas complété son inventaire de centres de données ni son plan de consolidation, malgré un objectif annoncé de fermeture de 137 centres d'ici fin 2011. | GAO-11-565, 26 juillet 2011 ; objectif de 137 fermetures annoncé en avril 2011 | O6, M10 | choc | [S17] | V |
| F.CLD.G3.004 | 2012-12 | US | Les agences fédérales ont fermé 420 centres de données sur un objectif de 1 253 fermetures d'ici 2015, pour un objectif d'économies de 3 milliards de dollars ; les économies réalisées ne sont pas encore mesurées à cette date. | 420 fermetures sur 1 253 visées, objectif 3 Md$ | O6, M10 | choc | [S18] | K |
| F.CLD.G3.005 | 2012-02 | EU | Le gouvernement britannique ouvre une place de marché en ligne référençant plus de 1 700 services en nuage de plus de 250 fournisseurs pour les achats publics, dans le cadre d'une politique d'achat dédiée. | CloudStore, cadre G-Cloud, février 2012 | T2, O6 | choc | [S19] | K |
| F.CLD.G3.006 | 2009 | EU | Le gouvernement français annonce un projet de plateforme nationale de cloud computing financée sur fonds publics, motivé par l'absence de fournisseur français à l'échelle. | projet « Andromède » annoncé en 2009 | T2, O6 | choc | [S20] | K |
| F.CLD.G3.007 | 2012 | EU | Le projet français de plateforme nationale se scinde en deux coentreprises distinctes, financées à hauteur de 75 millions d'euros chacune par la Caisse des dépôts et consignations, faute d'accord entre les industriels sur un projet unique. | 150 M€ au total, deux coentreprises | T2, O6, O4 | choc | [S20] | K |
| F.CLD.G3.008 | 2015-03 | EU | L'une des deux coentreprises françaises de cloud souverain est reprise intégralement par son actionnaire industriel télécoms, l'État se retirant de fait de sa participation directe au capital de cette structure. | reprise de Cloudwatt par Orange, mars 2015 | T2, O4, O6 | choc | [S20] | K |
| F.CLD.G3.009 | 2013 | US | Un fournisseur américain de services en nuage remporte un contrat pluriannuel de plusieurs centaines de millions de dollars auprès d'une agence de renseignement américaine, contesté devant la juridiction fédérale des marchés publics par un concurrent historique. | contrat contesté, 2013 | O6, O2, O4 | choc | [S21] | K |
| F.CLD.G3.010 | 2014-07 | US | L'audit du Congrès constate que la consolidation des centres de données fédéraux se poursuit mais que le suivi des économies réalisées reste insuffisant pour vérifier l'atteinte de l'objectif fixé en 2010. | GAO-14-713, 2014 | O6, M10 | choc | [S22] | K |
| F.CLD.G3.011 | 2015 | EU | Plusieurs États membres publient des référentiels nationaux de certification des services en nuage à l'usage des administrations et des secteurs réglementés, en l'absence de cadre européen unique d'achat public. | référentiels nationaux, 2015 | T2, O6 | choc | [S8] | K |

### Jalons cités
<!-- Lines 193-195 -->

`J.CLD.2009.02`, `J.CLD.2010.02`, `J.CLD.2011.03`, `J.CLD.2012.03`, `J.CLD.2013.02`.

### Trajectoire `T.CLD.G3`
<!-- Lines 198-213 -->

| année | phase | intensité | ce qui change | faits et jalons |
| --- | --- | --- | --- | --- |
| avant t0 | latent | 0 | Aucune politique d'achat public dédiée au cloud ; l'informatique publique reste possédée, comme le reste du secteur. | F.CLD.A1.010 (cité en secondaire) |
| 2005 | latent | 0 | Aucune politique publique dédiée documentée cette année. | — |
| 2006 | latent | 0 | Aucune politique publique dédiée documentée cette année. | — |
| 2007 | latent | 0 | Aucune politique publique dédiée documentée cette année. | — |
| 2008 | latent | 0 | Aucune politique publique dédiée documentée cette année. | — |
| 2009 | émergence | 2 | Premier portail d'achat fédéral américain de capacité à la demande ; premier projet français de plateforme nationale annoncé. | F.CLD.G3.001, F.CLD.G3.006, J.CLD.2009.02 |
| 2010 | émergence | 1 | Aucune bascule nouvelle documentée cette année pour G3 au-delà de la préparation de la stratégie fédérale. | J.CLD.2010.02 |
| 2011 | accélération | 3 | Politique fédérale « Cloud First » ; homologation de sécurité unique ; premier audit critique de la consolidation. | F.CLD.G3.002, F.CLD.G3.003, J.CLD.2011.03 |
| 2012 | accélération | 3 | Place de marché publique britannique ; scission du projet français en deux coentreprises publiques-privées ; 420 fermetures de centres fédéraux américains. | F.CLD.G3.004, F.CLD.G3.005, F.CLD.G3.007, J.CLD.2012.03 |
| 2013 | consolidation | 2 | Contrat public américain contesté validant l'achat de cloud par le secteur le plus sensible à la sécurité. | F.CLD.G3.009, J.CLD.2013.02 |
| 2014 | consolidation | 1 | Deuxième audit du Congrès américain, suivi encore jugé insuffisant. | F.CLD.G3.010 |
| 2015 | consolidation | 2 | Retrait de l'État français d'une des deux coentreprises ; référentiels nationaux de certification publiés en Europe. | F.CLD.G3.008, F.CLD.G3.011 |

### Narratif
<!-- Lines 216-230 -->

L'État américain ouvre la marche avec un portail d'achat dédié dès 2009 [F.CLD.G3.001], suivi
en 2011 d'une politique d'achat par défaut qui fait du cloud la norme d'exemplarité fédérale
[F.CLD.G3.002], mais l'audit du Congrès montre la même année que la mise en œuvre reste très en
retard sur l'annonce [F.CLD.G3.003], constat renouvelé en 2014 [F.CLD.G3.010]. Le Royaume-Uni
suit une voie comparable avec une place de marché publique dès 2012 [F.CLD.G3.005]. La France
choisit une réponse industrielle plutôt qu'un cadre d'achat, finançant sur fonds publics un
projet de plateforme nationale dès 2009 [F.CLD.G3.006], scindé en deux sociétés en 2012 faute
d'accord entre industriels [F.CLD.G3.007], et dont l'État se retire de fait en 2015 quand l'une
des deux est reprise par son actionnaire télécoms [F.CLD.G3.008]. Le secteur public le plus
exigeant en sécurité valide néanmoins l'achat de cloud dès 2013, y compris pour des données
sensibles [F.CLD.G3.009].

---

## G4 Géopolitique, souveraineté et sécurité
<!-- Lines 233-237 -->

**Question :** Comment les rapports entre puissances, la souveraineté et la sécurité sont-ils
modifiés : concentration des usines, écosystème chinois séparé, révélations sur la surveillance,
localisation des données comme instrument ?

### Faits
<!-- Lines 240-253 -->

| id | année | bloc | énoncé | valeur | acteurs | attribution | source | statut |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| F.CLD.G4.001 | 2009 | EU | Les groupes européens du numérique et les pouvoirs publics constatent qu'aucun fournisseur de capacité de cloud à l'échelle mondiale n'est européen, faisant de l'Europe une cliente d'une industrie qu'elle ne possède pas. | absence constatée | T2, O6, O2 | choc | [S20] | K |
| F.CLD.G4.002 | 2009-09-10 | CN | Un opérateur chinois de commerce en ligne crée une filiale dédiée aux services de calcul en nuage pour le marché intérieur, séparant durablement l'écosystème chinois des fournisseurs américains. | filiale créée le 10 septembre 2009 | T4, O2 | choc | [S23] | K |
| F.CLD.G4.003 | 2013-06 | MONDE | Des révélations documentées font connaître l'existence de programmes de collecte de données de communications électroniques opérés par des agences de renseignement américaines auprès de grands fournisseurs de services en ligne, avec coopération de services alliés. | révélations à partir de juin 2013 | O6, O2, T1, T2 | co:X.CLD.07 | [S24] | K |
| F.CLD.G4.004 | 2013 | US | Un fournisseur américain de services en nuage obtient l'homologation de sécurité nécessaire pour héberger des données classifiées d'une agence de renseignement, épisode qui fait tomber l'argument selon lequel certaines données seraient trop sensibles pour le cloud. | homologation et contrat 2013 | O6, O2 | choc | [S21] | K |
| F.CLD.G4.005 | 2013-2014 | US | Les grands fournisseurs de services en nuage annoncent le chiffrement systématique des liaisons entre leurs centres de données, réponse technique directe à la perte de confiance consécutive aux révélations de 2013. | chiffrement généralisé annoncé | O2, M1 | co:X.CLD.07 | [S25] | K |
| F.CLD.G4.006 | 2014 | EU | Les grands fournisseurs américains ouvrent des régions de centres de données en Allemagne et dans d'autres pays européens pour répondre à l'exigence de localisation des données, traitant la souveraineté par la géographie physique des usines plutôt que par un changement d'actionnariat. | ouvertures de régions européennes, 2014 | T2, O2, O6 | choc | [S26] | K |
| F.CLD.G4.007 | 2015-10-06 | EU | La Cour de justice de l'Union européenne invalide le cadre juridique qui autorisait par défaut le transfert des données personnelles vers les États-Unis, rendant incertaine l'architecture par défaut de milliers d'organisations européennes clientes d'usines américaines. | affaire C-362/14, 6 octobre 2015 | T2, O6, O4, O2 | co:X.CLD.07 | [S7] | K |
| F.CLD.G4.008 | 2015-06-02 | US | L'industrie américaine du cloud fait campagne publiquement en faveur d'une loi limitant la collecte en masse de métadonnées, afin de rassurer sa clientèle étrangère inquiète depuis 2013 ; la loi est promulguée le 2 juin 2015. | Public Law 114-23, 2 juin 2015 | O2, O6, M10 | co:X.CLD.07 | [S6] | V |
| F.CLD.G4.009 | 2012 | EU | Une administration nationale européenne engage un projet de plateforme de cloud financée sur fonds publics comme réponse de souveraineté au constat de 2009, plutôt que comme simple politique d'achat. | projet public de souveraineté | T2, O6, O2 | choc | [S20] | K |
| F.CLD.G4.010 | 2015-03 | ASIE-E | La Corée du Sud promulgue la première loi au monde spécifiquement dédiée au cloud computing, qui organise le soutien public au secteur et la protection des utilisateurs plutôt qu'une politique de repli souverain, trajectoire distincte de la réponse sécuritaire américaine et européenne de la même période. | loi n° 13234, promulguée le 27 mars 2015, entrée en vigueur le 27 septembre 2015 | T3, O6 | choc | [S27] | V |

### Jalons cités
<!-- Lines 256-259 -->

`J.CLD.2013.01`, `J.CLD.2013.02`, `J.CLD.2013.03`, `J.CLD.2014.04`, `J.CLD.2015.02`,
`J.CLD.2015.03`.

### Trajectoire `T.CLD.G4`
<!-- Lines 262-277 -->

| année | phase | intensité | ce qui change | faits et jalons |
| --- | --- | --- | --- | --- |
| avant t0 | latent | 0 | Aucune usine de cloud à l'échelle mondiale hors des États-Unis ; la question de la souveraineté ne se pose pas encore. | — |
| 2005 | latent | 0 | Aucune bascule géopolitique documentée cette année. | — |
| 2006 | latent | 0 | Aucune bascule géopolitique documentée cette année. | — |
| 2007 | émergence | 1 | Les fournisseurs chinois engagent la construction de leurs propres centres de données, hors des fournisseurs américains (cité en A3 ; jalon fondateur de la trajectoire séparée chinoise). | J.CLD.2007.05 (A3) |
| 2008 | émergence | 0 | Aucune bascule géopolitique nouvelle documentée cette année. | — |
| 2009 | émergence | 2 | La Chine se dote d'un fournisseur national dédié ; l'Europe constate l'absence d'un fournisseur à son échelle. | F.CLD.G4.001, F.CLD.G4.002 |
| 2010 | consolidation | 0 | Aucune bascule géopolitique nouvelle documentée cette année pour G4. | — |
| 2011 | consolidation | 0 | Aucune bascule géopolitique nouvelle documentée cette année pour G4. | — |
| 2012 | consolidation | 1 | Réponse de souveraineté publique européenne au constat de 2009. | F.CLD.G4.009 |
| 2013 | crise | 3 | Révélations sur la surveillance de masse ; validation sécuritaire du cloud par le renseignement américain ; chiffrement généralisé des liaisons en réponse. | F.CLD.G4.003, F.CLD.G4.004, F.CLD.G4.005, J.CLD.2013.01, J.CLD.2013.02, J.CLD.2013.03 |
| 2014 | crise | 2 | Ouverture de régions européennes par les fournisseurs américains pour répondre à l'exigence de localisation. | F.CLD.G4.006, J.CLD.2014.04 |
| 2015 | crise | 3 | Invalidation judiciaire du cadre de transfert transatlantique ; loi américaine mettant fin à la collecte en masse, portée par l'industrie elle-même ; la Corée du Sud promulgue la première loi au monde dédiée au cloud, trajectoire de développement plutôt que de repli. | F.CLD.G4.007, F.CLD.G4.008, F.CLD.G4.010, J.CLD.2015.02, J.CLD.2015.03 |

### Narratif
<!-- Lines 280-298 -->

La géopolitique du cloud se noue autour d'une asymétrie constatée dès 2009 : la Chine se dote
d'un fournisseur national séparé [F.CLD.G4.002] pendant que l'Europe constate l'absence de tout
fournisseur à son échelle [F.CLD.G4.001], asymétrie à laquelle une administration nationale
européenne répond en 2012 par un projet public de souveraineté [F.CLD.G4.009]. La crise de
confiance de 2013 est le pivot de la sous-dimension : les révélations sur la surveillance de
masse [F.CLD.G4.003] surviennent la même année où le secteur public le plus sensible valide
l'usine louée pour ses propres données [F.CLD.G4.004], contradiction que les fournisseurs
tentent de résoudre par le chiffrement généralisé des liaisons [F.CLD.G4.005] puis par
l'ouverture de régions localisées en Europe [F.CLD.G4.006]. La fenêtre se referme en 2015 sur
deux textes qui répondent à la même crise par des voies opposées, l'un judiciaire et européen,
l'autre législatif et américain porté par l'industrie elle-même [F.CLD.G4.007, F.CLD.G4.008].
L'Asie de l'Est développée hors Chine suit une trajectoire distincte des deux précédentes : la
Corée du Sud clôt la fenêtre en promulguant la première loi au monde spécifiquement dédiée au
cloud, orientée vers le développement du secteur et la protection des utilisateurs plutôt que
vers la sécurité ou la souveraineté défensive [F.CLD.G4.010].

---

## Sources
<!-- Lines 301-330 -->

| clé | type | référence | note |
| --- | --- | --- | --- |
| [S1] | off | *USA PATRIOT Act*, Public Law 107-56, 26 octobre 2001, section 215 ; directive 95/46/CE du Parlement européen et du Conseil, 24 octobre 1995 | Public Law 107-56 vérifiée directement sur govinfo.gov (titre exact, numéro, date, texte de la section 215). La directive 95/46/CE est citée par sa référence exacte ; EUR-Lex étant inaccessible depuis cet environnement, son texte n'a pas été ouvert (statut `V` porté par la seule partie américaine du fait). |
| [S2] | off | *FISA Amendments Act of 2008*, Public Law 110-261, 10 juillet 2008 | Vérifiée directement sur govinfo.gov : titre exact (« Foreign Intelligence Surveillance Act of 1978 Amendments Act of 2008 »), numéro de loi publique et date d'enactment confirmés ; texte de la section 702 lu. |
| [S3] | off | Office of Management and Budget, mémorandum *Security Authorization of Information Systems in Cloud Computing Environments*, Steven VanRoekel, Federal Chief Information Officer, 8 décembre 2011 | Vérifié directement sur le PDF ouvert (archive whitehouse.gov) : date, auteur, objet et création du FedRAMP confirmés à la lecture du document. |
| [S4] | off | Commission européenne, proposition de règlement général sur la protection des données, COM(2012) 11 final, 25 janvier 2012 | Référence de la proposition telle que documentée dans la littérature secondaire ; EUR-Lex inaccessible depuis cet environnement, le texte lui-même n'a pas été ouvert. À vérifier via un relais officiel accessible. |
| [S5] | off | Groupe de travail « Article 29 », *Opinion 05/2012 on Cloud Computing*, WP196, 1er juillet 2012 | Document du groupe de travail européen des autorités de protection des données ; référencé par son identifiant exact (WP196) mais non ouvert directement, portail européen des groupes de travail inaccessible depuis cet environnement. |
| [S6] | off | *USA FREEDOM Act of 2015*, Public Law 114-23, approuvée le 2 juin 2015 (H.R. 2048, 114e Congrès) | Reprise de [S50] de `par_annee/cloud_2005_2015.md`, déjà vérifiée sur govinfo.gov : titre, numéro de loi publique et date d'approbation confirmés. |
| [S7] | off | Cour de justice de l'Union européenne, arrêt du 6 octobre 2015, *Maximillian Schrems c. Data Protection Commissioner*, affaire C-362/14 | Reprise de [S49] de la chronologie. CURIA (portail de la Cour de justice) est inaccessible depuis cet environnement de recherche ; la référence exacte (numéro d'affaire, date, parties) est documentée sans lecture directe du texte de l'arrêt. Statut `K`. |
| [S8] | off | Référentiels nationaux de certification de services en nuage publiés par plusieurs administrations européennes, 2015 (par exemple le référentiel SecNumCloud en France, première version) | Reprise partielle de [S36] de la chronologie ; cas nommés non identifiés individuellement dans cette cellule, à vérifier référentiel par référentiel. |
| [S9] | off | Propositions de réforme de l'*Electronic Communications Privacy Act* de 1986 déposées au Congrès américain, 2011-2015 (non abouties dans la fenêtre) | congress.gov inaccessible depuis cet environnement ; propositions documentées par leur existence et leur objet via littérature secondaire, non par le texte des projets eux-mêmes. |
| [S10] | off | Lois et projets de loi sectoriels de localisation des données (santé, finance, administration) dans plusieurs pays, 2009-2015 | Généralité qualitative rassemblant plusieurs juridictions ; aucun texte unique cité, à décomposer pays par pays si la cellule est approfondie. |
| [S11] | off | The Green Grid, documents fondateurs et définition de l'indicateur d'efficacité PUE, 2007-2008 | Reprise de [S52] de la chronologie. |
| [S12] | off | Mell, P. et Grance, T., *The NIST Definition of Cloud Computing*, NIST Special Publication 800-145, 28 septembre 2011 | Vérifiée directement sur nist.gov : date de publication (28 septembre 2011), auteurs (Peter Mell, Timothy Grance) et numéro de publication confirmés. |
| [S13] | off | OpenStack Foundation, annonce de lancement du projet par la NASA et Rackspace, juillet 2010 | Reprise de [S28] de la chronologie. |
| [S14] | off | Google Inc. et Cloud Native Computing Foundation, publication initiale de Kubernetes en logiciel libre, juin 2014, et création de la fondation associée | Reprise de [S46] de la chronologie ; date de création de la fondation (2015) à vérifier séparément de la publication du projet (2014). |
| [S15] | off | *Apps.gov*, portail fédéral américain d'achat de services informatiques à la demande, lancé en septembre 2009 | Reprise de [S25] de la chronologie. |
| [S16] | off | Kundra, V., U.S. Chief Information Officer, *Federal Cloud Computing Strategy*, Executive Office of the President, Office of Management and Budget, 8 février 2011 | Vérifiée directement : PDF ouvert (archive whitehouse.gov), page de titre lue (auteur, fonction, adresse whitehouse.gov) ; la date du 8 février 2011 est corroborée par une seconde archive indépendante portant la même mention en en-tête. |
| [S17] | off | U.S. Government Accountability Office, *Data Center Consolidation: Agencies Need to Complete Inventories and Plans to Achieve Expected Savings*, GAO-11-565, 26 juillet 2011 | Vérifié directement sur gao.gov : titre, numéro de rapport, date de publication et principales constatations confirmés. |
| [S18] | off | U.S. Government Accountability Office, données citées dans les auditions et rapports de suivi de l'initiative fédérale de consolidation des centres de données, situation à décembre 2012 | Chiffres (420 fermetures sur 1 253 visées, objectif de 3 Md$) issus de littérature secondaire s'appuyant sur les rapports GAO ; le rapport source précis (probablement GAO-13-378) n'a pas été ouvert directement dans cette session. |
| [S19] | off | Gouvernement britannique, cadre d'achat public *G-Cloud* et place de marché *CloudStore*, lancée en février 2012 | Date et volumétrie (plus de 1 700 services, plus de 250 fournisseurs) issues de presse spécialisée contemporaine ; gov.uk non ouvert directement dans cette session. |
| [S20] | off, presse | Documents et presse contemporaine du projet français « Andromède » (annoncé 2009), de sa scission en Cloudwatt et Numergy (2012, 150 M€ financés par la Caisse des dépôts et consignations) et de la reprise de Cloudwatt par Orange (mars 2015) | Reconstitué à partir de sources secondaires convergentes (presse spécialisée, encyclopédies en ligne) ; aucun document officiel français primaire ouvert directement dans cette session. Statut `K` pour l'ensemble de la séquence. |
| [S21] | off | U.S. Government Accountability Office et Court of Federal Claims, décisions relatives au contrat de services en nuage d'une agence de renseignement américaine, 2013 | Reprise de [S42] de la chronologie ; document de décision non ouvert directement dans cette session. |
| [S22] | off | U.S. Government Accountability Office, *Data Center Consolidation: Reporting Can Be Improved to Reflect Substantial Planned Savings*, GAO-14-713, 2014 | Référence identifiée par recherche ; rapport non ouvert directement dans cette session. |
| [S23] | off | Alibaba Group Holding Ltd., annonce de création de la filiale de services en nuage (Alibaba Cloud / Aliyun), 10 septembre 2009 ; prospectus d'introduction en bourse (Form F-1, SEC, 2014) | Date de création (10 septembre 2009) issue de sources secondaires convergentes ; le prospectus SEC lui-même n'a pas été rouvert dans cette session pour ce fait précis. |
| [S24] | presse | The Guardian et The Washington Post, articles de juin 2013 sur les programmes de collecte de données par le renseignement américain | Reprise de [S41] de la chronologie. Presse contemporaine de l'événement, admissible pour dater le jalon. |
| [S25] | presse | Communiqués de Google, Microsoft et Yahoo sur le chiffrement des liaisons inter-centres de données, 2013-2014 | Reprise de [S43] de la chronologie. |
| [S26] | off | Annonces des fournisseurs américains sur l'ouverture de régions de centres de données en Allemagne et dans d'autres pays européens, 2014 | Reprise du contexte de [S27] de la chronologie ; annonces individuelles non ouvertes une à une dans cette session. |
| [S27] | off | République de Corée, *Act on the Development of Cloud Computing and Protection of Its Users*, loi n° 13234, promulguée le 27 mars 2015 (Korea Legislation Research Institute, elaw.klri.re.kr, traduction officielle anglaise) | Ouvert et lu le 2026-09-22 : elaw.klri.re.kr ; titre exact, numéro de loi, date de promulgation (27 mars 2015) et entrée en vigueur (27 septembre 2015) confirmés, ainsi que l'objet de la loi (développement du secteur, protection des utilisateurs). |
