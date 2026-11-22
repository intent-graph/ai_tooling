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

1. [G1 Droit et régulation](#g1-droit-et-régulation) _(Lines 42-44)_
   1. [Faits](#faits) _(Lines 47-67)_
   1. [Jalons cités](#jalons-cités) _(Lines 70-73)_
   1. [Trajectoire `T.CLD.G1`](#trajectoire-tcldg1) _(Lines 76-91)_
   1. [Narratif](#narratif) _(Lines 94-111)_
1. [G2 Gouvernance de la technologie](#g2-gouvernance-de-la-technologie) _(Lines 114-117)_
   1. [Faits](#faits-1) _(Lines 120-130)_
   1. [Jalons cités](#jalons-cités-1) _(Lines 133-135)_
   1. [Trajectoire `T.CLD.G2`](#trajectoire-tcldg2) _(Lines 138-153)_
   1. [Narratif](#narratif-1) _(Lines 156-170)_
1. [G3 État, services publics et vie démocratique](#g3-état-services-publics-et-vie-démocratique) _(Lines 173-177)_
   1. [Faits](#faits-2) _(Lines 180-194)_
   1. [Jalons cités](#jalons-cités-2) _(Lines 197-199)_
   1. [Trajectoire `T.CLD.G3`](#trajectoire-tcldg3) _(Lines 202-217)_
   1. [Narratif](#narratif-2) _(Lines 220-235)_
1. [G4 Géopolitique, souveraineté et sécurité](#g4-géopolitique-souveraineté-et-sécurité) _(Lines 238-242)_
   1. [Faits](#faits-3) _(Lines 245-258)_
   1. [Jalons cités](#jalons-cités-3) _(Lines 261-264)_
   1. [Trajectoire `T.CLD.G4`](#trajectoire-tcldg4) _(Lines 267-282)_
   1. [Narratif](#narratif-3) _(Lines 285-304)_
1. [Sources](#sources) _(Lines 307-343)_



---

## G1 Droit et régulation
<!-- Lines 42-44 -->

**Question :** Quelles lois, décisions et régulateurs apparaissent, avec quel retard sur les usages ?

### Faits
<!-- Lines 47-67 -->

| id | année | bloc | énoncé | valeur | acteurs | attribution | source | statut |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| F.CLD.G1.001 | 2003-2004 | US, EU | Avant t0 : le cadre juridique en place repose sur une loi antiterroriste américaine de 2001 élargissant l'accès des autorités aux données détenues par des tiers, et sur une directive européenne de 1995 encadrant le transfert des données personnelles hors de l'Union, deux textes antérieurs au choc et non conçus pour des données hébergées à l'étranger. | Public Law 107-56 (2001-10-26) ; directive 95/46/CE | O6, T1, T2 | exo | [S1] | V |
| F.CLD.G1.002 | 2008-07-10 | US | Les États-Unis adoptent une loi élargissant les pouvoirs de surveillance des communications électroniques, autorisant le renseignement à cibler des personnes situées hors du territoire américain sans mandat individualisé, avec effet sur les données hébergées par des fournisseurs américains où qu'elles se trouvent. | Public Law 110-261, FISA Amendments Act of 2008, 10 juillet 2008 | O6, M10 | exo | [S2] | V |
| F.CLD.G1.003 | 2011-12-08 | US | Un mémorandum de l'Office of Management and Budget crée un programme fédéral unique d'homologation de sécurité des services en nuage, applicable à toutes les agences ; une homologation vaut pour l'ensemble du gouvernement fédéral. | Mémorandum « Security Authorization of Information Systems in Cloud Computing Environments », signé Steven VanRoekel, 8 décembre 2011 | O6, M10 | choc | [S3] | V |
| F.CLD.G1.004 | 2012-01-25 | EU | La Commission européenne propose une refonte du cadre de protection des données personnelles, qui prévoit l'application des règles de l'Union aux traitements opérés à l'étranger par des entreprises actives sur le marché de l'Union, et l'obligation de notifier les violations graves de données à l'autorité nationale, si possible sous 24 heures. | proposition de règlement, 25 janvier 2012 | T2, O6 | choc | [S4] | A |
| F.CLD.G1.005 | 2012-07-01 | EU | Le groupe de travail réunissant les autorités nationales de protection des données de l'Union adopte un avis dédié à l'informatique en nuage, qui demande que le client connaisse les sous-traitants et les lieux de traitement des données, recommande un contrat couvrant notamment la liste de ces lieux et la notification des violations, et estime que la seule auto-certification « sphère de sécurité » du destinataire américain peut ne pas suffire. | avis WP196, adopté le 1er juillet 2012 | T2, O6 | choc | [S5] | V |
| F.CLD.G1.006 | 2013 | EU | À la suite des révélations sur la surveillance de masse, les autorités allemandes de protection des données annoncent le 24 juillet 2013 qu'elles n'accorderont plus de nouvelle autorisation de transfert vers des pays tiers et examineront la suspension des transferts fondés sur la sphère de sécurité, et le groupe des autorités européennes écrit à la Commission le 13 août 2013 qu'il doute que la surveillance à grande échelle puisse relever de l'exception de sécurité nationale de la sphère de sécurité. | communiqué du 24 juillet 2013 ; lettre du 13 août 2013 | T2, O6, O4 | co:X.CLD.07 | [S28] | V |
| F.CLD.G1.007 | 2015-06-02 | US | Les États-Unis adoptent une loi qui met fin à la collecte en masse de métadonnées téléphoniques par le renseignement et transfère la conservation de ces données aux opérateurs, avec obligation de demande individualisée pour y accéder. | Public Law 114-23, USA FREEDOM Act, 2 juin 2015 | O6, M10 | co:X.CLD.07 | [S6] | V |
| F.CLD.G1.008 | 2015-10-06 | EU | La Cour de justice de l'Union européenne invalide la décision de la Commission qui reconnaissait le cadre américain « sphère de sécurité » comme offrant un niveau de protection adéquat pour les transferts de données personnelles vers les États-Unis. | affaire C-362/14, arrêt du 6 octobre 2015 | T2, O6, O4, O2 | co:X.CLD.07 | [S7] | A |
| F.CLD.G1.009 | 2015 | EU | En février 2015, l'agence française de sécurité des systèmes d'information crée le dispositif Secure Cloud, destiné à la sécurité des services en nuage et devenu SecNumCloud en 2016. | dispositif Secure Cloud, février 2015 | T2, O6, O2 | choc | [S29] | A |
| F.CLD.G1.010 | 2013-2015 | US | Au Sénat, deux projets de loi portés par les sénateurs Leahy et Lee, S. 607 en mars 2013 et S. 356 en février 2015, prévoient d'exiger un mandat pour obtenir le contenu des courriers électroniques détenus par des fournisseurs et de supprimer la règle des 180 jours ; aucune loi en ce sens n'est adoptée pendant la fenêtre. | S. 607 (2013) et S. 356 (2015), non adoptés | O6 | co:X.CLD.07 | [S9] | A |
| F.CLD.G1.011 | 2011-2013 | MONDE | Plusieurs pays adoptent des obligations de localisation des données sur leur territoire pour certains secteurs : en 2011 la banque centrale chinoise interdit aux banques de stocker ou de traiter hors de Chine les informations financières personnelles collectées en Chine, en 2012 l'Australie interdit, sauf exceptions, le transfert hors du pays des dossiers de santé électroniques de son système national, en 2013 le Nigeria impose d'héberger localement les données publiques. | Chine 2011 (banques), Australie 2012 (santé), Nigeria 2013 (administration) | O6, T2, T4 | choc | [S10] | A |

**Note sur les sources juridiques européennes.** Le portail du droit de l'Union (EUR-Lex) et le
site de la Cour de justice (CURIA) sont inaccessibles depuis cet environnement de recherche. La
directive 95/46/CE et l'arrêt *Schrems* (C-362/14) sont documentés par leur référence exacte
(numéro, date, juridiction) plutôt que par un accès direct au texte ; statut `V` réservé au seul
fait où un relais officiel accessible (govinfo.gov, whitehouse.gov) a pu être ouvert et lu.

### Jalons cités
<!-- Lines 70-73 -->

`J.CLD.2011.03`, `J.CLD.2013.01`, `J.CLD.2013.04`, `J.CLD.2015.02`, `J.CLD.2015.03`,
`J.CLD.2015.04`.

### Trajectoire `T.CLD.G1`
<!-- Lines 76-91 -->

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
| 2012 | accélération | 2 | Proposition de refonte du cadre européen de protection des données ; avis européen dédié au cloud. | F.CLD.G1.004, F.CLD.G1.005 |
| 2013 | crise | 3 | Après les révélations sur la surveillance de masse, les autorités allemandes cessent d'accorder de nouvelles autorisations de transfert vers des pays tiers et le groupe des autorités européennes met en doute l'exception de sécurité nationale de la sphère de sécurité. | F.CLD.G1.006, J.CLD.2013.01, J.CLD.2013.04 |
| 2014 | crise | 0 | Poursuite du contentieux et du débat sans texte nouveau documenté cette année pour G1. | — |
| 2015 | crise | 3 | Invalidation du cadre de transfert transatlantique ; loi américaine mettant fin à la collecte en masse ; création en France du dispositif Secure Cloud de sécurité des services en nuage. | F.CLD.G1.007, F.CLD.G1.008, F.CLD.G1.009, J.CLD.2015.02, J.CLD.2015.03, J.CLD.2015.04 |

### Narratif
<!-- Lines 94-111 -->

Le droit part d'un cadre antérieur au choc et non conçu pour lui : une loi antiterroriste
américaine de 2001 et une directive européenne de 1995 [F.CLD.G1.001]. La première réponse
propre au cloud est américaine et sécuritaire, avec l'élargissement des pouvoirs de surveillance
en 2008 [F.CLD.G1.002], suivie trois ans plus tard par la création d'un programme unique
d'homologation qui rend l'achat public de cloud possible [F.CLD.G1.003]. Les révélations sur la
surveillance de masse en 2013 font basculer le registre : les autorités européennes de
protection des données réagissent sur les transferts hors de l'Union, par l'arrêt des nouvelles
autorisations en Allemagne et par les doutes du groupe européen sur la sphère de sécurité
[F.CLD.G1.006], et la crise se referme en 2015 par deux textes
symétriques, l'invalidation judiciaire européenne du cadre transatlantique et une loi américaine
qui met fin à la collecte en masse de métadonnées [F.CLD.G1.007, F.CLD.G1.008]. Le droit répond
au choc avec retard mais de façon endogène : chaque texte cité est une réponse à une pratique déjà
installée, jamais une anticipation [F.CLD.G1.001][F.CLD.G1.002][F.CLD.G1.003][F.CLD.G1.006]
[F.CLD.G1.007][F.CLD.G1.008].

---

## G2 Gouvernance de la technologie
<!-- Lines 114-117 -->

**Question :** Qui fixe les normes du cloud, organismes de normalisation nationaux et
internationaux, fondations de l'open source comme gouvernance privée, certifications et audits ?

### Faits
<!-- Lines 120-130 -->

| id | année | bloc | énoncé | valeur | acteurs | attribution | source | statut |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| F.CLD.G2.001 | 2007 | US | Un consortium industriel ouvert à but non lucratif, réunissant des utilisateurs finaux, des fournisseurs de technologie et d'autres acteurs des centres de données, publie en 2007 une métrique partagée d'efficacité énergétique des centres de données, le PUE. | livre blanc The Green Grid n° 6, 2007 | O2, O3, M1 | choc | [S11] | A |
| F.CLD.G2.002 | 2011-09-28 | US | L'institut américain de normalisation publie la définition officielle de l'informatique en nuage, acte de gouvernance qui fixe le vocabulaire opposable pour tout marché ou audit : cinq caractéristiques, trois modèles de service, quatre modèles de déploiement. | NIST Special Publication 800-145, Mell et Grance, 28 septembre 2011 | O6, M1 | choc | [S12] | V |
| F.CLD.G2.003 | 2012-09 | US | En septembre 2012, le projet ouvert de logiciel d'infrastructure en nuage OpenStack, annoncé en juillet 2010 à partir de code de Rackspace et de code Nova développé pour la NASA, est confié à une fondation indépendante dont le conseil de 24 membres compte des représentants de plusieurs entreprises. | projet annoncé en juillet 2010 ; fondation lancée en septembre 2012 | O6, O2, M1 | choc | [S13] | A |
| F.CLD.G2.004 | 2015-07 | US | En juillet 2015, une fondation rattachée à la Linux Foundation est créée et reçoit de Google, comme technologie de départ, le système d'orchestration de conteneurs Kubernetes, dont le code a été publié en logiciel libre en juin 2014 ; la fondation est chargée de l'intendance des projets, avec un comité de supervision technique. | fondation annoncée le 21 juillet 2015 ; premier commit public du projet le 6 juin 2014 | M1, O2, O1 | choc | [S14] | A |
| F.CLD.G2.005 | 2012-07 | EU | Le groupe des autorités européennes de protection des données retient, dans son avis sur le cloud, que la certification par un tiers reconnu peut être un moyen crédible pour un fournisseur de démontrer sa conformité, et qu'un audit par un tiers choisi par le responsable de traitement peut tenir lieu de son droit d'audit individuel. | avis WP196 | T2, O6 | choc | [S5] | V |
| F.CLD.G2.006 | 2011-12 | US | Le programme fédéral d'homologation de sécurité des services en nuage crée un comité d'autorisation conjoint réunissant trois agences, qui devient l'autorité de fait pour juger de la conformité des fournisseurs vis-à-vis du secteur public fédéral. | comité conjoint DHS, DOD, GSA | O6, M10 | choc | [S3] | V |
| F.CLD.G2.007 | 2014 | MONDE | L'UIT-T publie la Recommandation Y.3500 sur la vue d'ensemble et le vocabulaire de l'informatique en nuage, en vigueur dans sa version 08/14 ; l'UIT indique que ses Recommandations ont un statut non obligatoire tant qu'elles ne sont pas adoptées dans les lois nationales. | Y.3500 (08/14), en vigueur ; statut non obligatoire des Recommandations | O6, O2 | choc | [S30] | A |

### Jalons cités
<!-- Lines 133-135 -->

`J.CLD.2007.07`, `J.CLD.2010.01`, `J.CLD.2011.01`, `J.CLD.2011.03`, `J.CLD.2014.03`.

### Trajectoire `T.CLD.G2`
<!-- Lines 138-153 -->

| année | phase | intensité | ce qui change | faits et jalons |
| --- | --- | --- | --- | --- |
| avant t0 | latent | 0 | Aucune gouvernance dédiée au cloud ; les standards de virtualisation et de la pile ouverte relèvent d'A2, pas encore d'une instance de gouvernance propre. | — |
| 2005 | latent | 0 | Aucune instance de gouvernance dédiée documentée cette année. | — |
| 2006 | latent | 0 | Aucune instance de gouvernance dédiée documentée cette année. | — |
| 2007 | émergence | 2 | Publication par un consortium industriel d'une métrique partagée d'efficacité énergétique des centres de données. | F.CLD.G2.001, J.CLD.2007.07 |
| 2008 | émergence | 0 | Aucune bascule de gouvernance nouvelle documentée cette année. | — |
| 2009 | émergence | 0 | Aucune bascule de gouvernance nouvelle documentée cette année. | — |
| 2010 | accélération | 2 | Annonce d'un projet ouvert de logiciel d'infrastructure en nuage, à partir de code de Rackspace et de la NASA. | J.CLD.2010.01 |
| 2011 | rupture | 3 | Définition normative officielle américaine ; création du comité d'autorisation conjoint fédéral. | F.CLD.G2.002, F.CLD.G2.006, J.CLD.2011.01, J.CLD.2011.03 |
| 2012 | consolidation | 2 | Avis européen retenant la certification et l'audit par un tiers comme moyens de démontrer la conformité des fournisseurs ; le projet ouvert de 2010 est confié à une fondation indépendante. | F.CLD.G2.005, F.CLD.G2.003 |
| 2013 | consolidation | 0 | Aucune bascule de gouvernance nouvelle documentée cette année. | — |
| 2014 | consolidation | 2 | Publication en logiciel libre du système d'orchestration de conteneurs Kubernetes ; recommandation internationale de l'UIT-T sur le vocabulaire de l'informatique en nuage, de statut non obligatoire tant que les lois nationales ne l'adoptent pas. | J.CLD.2014.03, F.CLD.G2.007 |
| 2015 | banalisation | 0 | Une fondation rattachée à la Linux Foundation reçoit ce système d'orchestration de conteneurs. | F.CLD.G2.004 |

### Narratif
<!-- Lines 156-170 -->

La gouvernance du cloud commence par un consortium industriel qui publie en 2007 une métrique
partagée d'efficacité énergétique des centres de données [F.CLD.G2.001]. Elle se
structure ensuite par trois voies distinctes qui ne se recouvrent pas : la normalisation
publique américaine, avec la définition officielle de 2011 [F.CLD.G2.002], la gouvernance
privée des fondations ouvertes, qui reçoivent des projets de logiciel ouvert en 2012 et en 2015
[F.CLD.G2.003, F.CLD.G2.004], et l'avis des autorités européennes de protection des données, qui
retient la certification et l'audit par un tiers comme moyens de démontrer la conformité
sans produire elles-mêmes de norme technique [F.CLD.G2.005]. À l'échelle internationale, la
recommandation de l'UIT-T de 2014 sur le vocabulaire du cloud n'est obligatoire que si les lois
nationales l'adoptent [F.CLD.G2.007] ; aux États-Unis, définition et homologation
[F.CLD.G2.006] ; en Europe, avis et certification.

---

## G3 État, services publics et vie démocratique
<!-- Lines 173-177 -->

**Question :** Comment l'État se sert de la technologie et comment la vie démocratique en
est-elle changée : politiques d'achat public, stratégies nationales, migration des
administrations, marchés publics emblématiques ?

### Faits
<!-- Lines 180-194 -->

| id | année | bloc | énoncé | valeur | acteurs | attribution | source | statut |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| F.CLD.G3.001 | 2009-09 | US | Le 15 septembre 2009, la Maison-Blanche annonce le lancement d'Apps.gov, vitrine en ligne où les agences fédérales américaines parcourent et achètent des services informatiques en nuage. | portail Apps.gov, lancé le 15 septembre 2009 | O6, M10 | choc | [S15] | V |
| F.CLD.G3.002 | 2011-02-08 | US | Le directeur informatique fédéral des États-Unis publie une stratégie donnant la priorité aux services en nuage dans les achats informatiques de l'administration, dite politique « Cloud First ». | *Federal Cloud Computing Strategy*, Vivek Kundra, U.S. Chief Information Officer, 8 février 2011 | O6, M10 | choc | [S16] | V |
| F.CLD.G3.003 | 2011-07-26 | US | L'organe d'audit du Congrès constate que la quasi-totalité des agences fédérales n'a pas complété son inventaire de centres de données ni son plan de consolidation, malgré un objectif annoncé de fermeture de 137 centres d'ici fin 2011. | GAO-11-565, 26 juillet 2011 ; objectif de 137 fermetures annoncé en avril 2011 | O6, M10 | choc | [S17] | V |
| F.CLD.G3.004 | 2012-12 | US | Les agences fédérales avaient fermé 420 centres de données à fin décembre 2012, sur un objectif de 1 253 fermetures d'ici fin 2015 (40 % des 3 133 centres) ; l'organe d'audit du Congrès constate en avril 2013 que l'administration budgétaire n'a pas mesuré les progrès par rapport à son autre objectif, 3 milliards de dollars d'économies d'ici fin 2015. | 420 fermetures à fin 2012 sur 1 253 visées ; objectif 3 Md$ ; GAO-13-378, 23 avril 2013 | O6, M10 | choc | [S18] | V |
| F.CLD.G3.005 | 2012-02 | EU | Le 19 février 2012, le gouvernement britannique annonce l'ouverture de CloudStore, boutique en ligne du cadre G-Cloud pour les services informatiques en nuage, destinée aux organisations du secteur public ; le cadre a reçu de près de 300 fournisseurs des offres portant sur environ 1 700 services. | CloudStore, cadre G-Cloud, 19 février 2012 ; environ 1 700 services, près de 300 offres de fournisseurs | T2, O6 | choc | [S19] | V |
| F.CLD.G3.006 | 2011-09 | EU | En septembre 2011, le Premier ministre français présente un projet de cloud public national, Andromède, doté de 285 millions d'euros dont 135 millions de la Caisse des dépôts, financé en partie par le grand emprunt et destiné à offrir une alternative aux fournisseurs nord-américains qui dominent le marché. | projet « Andromède » : 285 M€, dont 135 M€ de la Caisse des dépôts, septembre 2011 | T2, O6 | choc | [S31] | A |
| F.CLD.G3.007 | 2012-09 | EU | Le projet français de plateforme nationale se scinde en deux sociétés, Cloudwatt et Numergy, lancées en septembre 2012 avec chacune 225 millions d'euros d'investissement total, dont 75 millions d'euros de la Caisse des dépôts et consignations pour chacune, après un désaccord entre industriels. | deux sociétés ; 225 M€ d'investissement chacune ; 75 M€ de la Caisse des dépôts chacune, 150 M€ au total | T2, O6, O4 | choc | [S32] | A |
| F.CLD.G3.008 | 2015-03 | EU | Le 20 mars 2015, l'État annonce qu'Orange, qui détenait 44,4 % de Cloudwatt, a racheté l'intégralité des participations de l'État (33,3 %) et de Thales (22,2 %), et confirme son soutien à Numergy. | reprise de Cloudwatt par Orange, 20 mars 2015 : Orange de 44,4 % à 100 % | T2, O4, O6 | choc | [S33] | V |
| F.CLD.G3.009 | 2013 | US | En janvier 2013, une agence de renseignement américaine attribue à un fournisseur américain de services en nuage un contrat d'une valeur pouvant atteindre 600 millions de dollars ; un concurrent saisit l'organe d'audit du Congrès, qui lui donne en partie raison, puis le fournisseur saisit la juridiction fédérale des réclamations, qui tranche en sa faveur en octobre 2013. | contrat jusqu'à 600 M$, attribué en janvier 2013 ; décision de la juridiction en octobre 2013 | O6, O2, O4 | choc | [S34] | A |
| F.CLD.G3.010 | 2014-09 | US | En septembre 2014, l'organe d'audit du Congrès relève que les agences fédérales déclarent environ 1,1 milliard de dollars d'économies et d'évitements de coûts pour 2011-2013 et en prévoient environ 3,3 milliards au total jusqu'en 2015, soit environ 300 millions de plus que l'objectif initial de 3 milliards, et que 11 des 21 agences concernées sous-déclarent leurs prévisions à l'administration budgétaire, d'environ 2,2 milliards. | GAO-14-713, 25 septembre 2014 ; 1,1 Md$ déclarés (2011-2013), 3,3 Md$ prévus (jusqu'en 2015), sous-déclaration d'environ 2,2 Md$ | O6, M10 | choc | [S22] | V |
| F.CLD.G3.011 | 2014-2015 | EU | En 2014 et 2015, plusieurs États membres de l'Union disposent de référentiels nationaux de sécurité des services en nuage à l'usage de leurs administrations : le Royaume-Uni a publié en 2014 les Cloud Security Principles, l'Espagne a diffusé en avril 2014 un projet de guide de sécurité en environnement cloud, et la France a créé en février 2015 le dispositif Secure Cloud. | Royaume-Uni 2014 ; Espagne avril 2014 (projet) ; France février 2015 | T2, O6 | choc | [S8], [S29] | A |

### Jalons cités
<!-- Lines 197-199 -->

`J.CLD.2009.02`, `J.CLD.2010.02`, `J.CLD.2011.03`, `J.CLD.2012.03`, `J.CLD.2013.02`.

### Trajectoire `T.CLD.G3`
<!-- Lines 202-217 -->

| année | phase | intensité | ce qui change | faits et jalons |
| --- | --- | --- | --- | --- |
| avant t0 | latent | 0 | Aucune politique d'achat public dédiée au cloud ; l'informatique publique reste possédée, comme le reste du secteur. | F.CLD.A1.010 (cité en secondaire) |
| 2005 | latent | 0 | Aucune politique publique dédiée documentée cette année. | — |
| 2006 | latent | 0 | Aucune politique publique dédiée documentée cette année. | — |
| 2007 | latent | 0 | Aucune politique publique dédiée documentée cette année. | — |
| 2008 | latent | 0 | Aucune politique publique dédiée documentée cette année. | — |
| 2009 | émergence | 2 | Lancement du portail d'achat fédéral américain de services en nuage Apps.gov. | F.CLD.G3.001, J.CLD.2009.02 |
| 2010 | émergence | 1 | Aucune bascule nouvelle documentée cette année pour G3 au-delà de la préparation de la stratégie fédérale. | J.CLD.2010.02 |
| 2011 | accélération | 3 | Politique fédérale « Cloud First » ; homologation de sécurité unique ; premier audit critique de la consolidation ; projet français de cloud public national présenté en septembre. | F.CLD.G3.002, F.CLD.G3.003, F.CLD.G3.006, J.CLD.2011.03 |
| 2012 | accélération | 3 | Ouverture de la boutique en ligne publique britannique CloudStore ; scission du projet français en deux sociétés, Cloudwatt et Numergy ; 420 fermetures de centres fédéraux américains à fin décembre. | F.CLD.G3.004, F.CLD.G3.005, F.CLD.G3.007, J.CLD.2012.03 |
| 2013 | consolidation | 2 | Contrat de renseignement américain attribué à un fournisseur de services en nuage, contesté par un concurrent puis confirmé par la juridiction fédérale en octobre. | F.CLD.G3.009, J.CLD.2013.02 |
| 2014 | consolidation | 1 | Audit du Congrès américain : économies déclarées inférieures aux économies prévues, prévisions sous-déclarées à l'administration budgétaire. | F.CLD.G3.010 |
| 2015 | consolidation | 2 | Rachat par Orange des parts de l'État dans l'une des deux sociétés ; création en France du dispositif Secure Cloud, après des référentiels nationaux de sécurité publiés en 2014 au Royaume-Uni et en Espagne. | F.CLD.G3.008, F.CLD.G3.011 |

### Narratif
<!-- Lines 220-235 -->

L'État américain ouvre la marche avec un portail d'achat dédié dès 2009 [F.CLD.G3.001], suivi
en 2011 d'une politique d'achat par défaut qui fait du cloud la norme d'exemplarité fédérale
[F.CLD.G3.002], mais l'audit du Congrès montre la même année que la mise en œuvre reste très en
retard sur l'annonce [F.CLD.G3.003] ; un audit de 2014 relève des économies déclarées de 1,1 milliard
de dollars et des prévisions sous-déclarées [F.CLD.G3.010]. Le Royaume-Uni
suit une voie comparable avec une boutique en ligne publique dès 2012 [F.CLD.G3.005]. La France
choisit une réponse industrielle plutôt qu'un cadre d'achat, finançant sur fonds publics un
projet de cloud public national présenté en 2011 [F.CLD.G3.006], scindé en deux sociétés en 2012
après un désaccord entre industriels [F.CLD.G3.007], et dont l'une est rachetée en 2015 par Orange,
qui reprend les parts de l'État et de Thales [F.CLD.G3.008]. En 2013, une agence de renseignement américaine
attribue à un fournisseur de services en nuage un contrat pouvant atteindre 600 millions de dollars,
confirmé en octobre par la juridiction fédérale après une contestation [F.CLD.G3.009].

---

## G4 Géopolitique, souveraineté et sécurité
<!-- Lines 238-242 -->

**Question :** Comment les rapports entre puissances, la souveraineté et la sécurité sont-ils
modifiés : concentration des usines, écosystème chinois séparé, révélations sur la surveillance,
localisation des données comme instrument ?

### Faits
<!-- Lines 245-258 -->

| id | année | bloc | énoncé | valeur | acteurs | attribution | source | statut |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| F.CLD.G4.001 | 2010-01-18 | EU | Le 18 janvier 2010, le Premier ministre français déclare que les Nord-Américains dominent le marché de l'informatique en nuage, qu'il présente comme un enjeu pour la compétitivité, le développement durable et la souveraineté, et appelle à développer une alternative française et européenne. | discours du 18 janvier 2010, Vélizy | T2, O6, O2 | choc | [S20] | V |
| F.CLD.G4.002 | 2009 | CN | Un groupe chinois de commerce en ligne lance en 2009 son activité de services de calcul en nuage, qui se présente comme le premier fournisseur de cloud en Chine. | 2009 | T4, O2 | choc | [S23] | A |
| F.CLD.G4.003 | 2013-06 | MONDE | En juin 2013, la presse révèle que le renseignement américain obtient, au titre du programme PRISM, des données de communications électroniques auprès de grands fournisseurs américains de services en ligne ; en juillet 2013, le comité de contrôle du renseignement du Parlement britannique indique que le service britannique GCHQ a produit des rapports à partir de renseignement sollicité auprès des États-Unis. | révélations à partir du 6 juin 2013 ; déclaration du comité du 17 juillet 2013 | O6, O2, T1, T2 | co:X.CLD.07 | [S24] | A |
| F.CLD.G4.004 | 2013 | US | En 2013, une agence de renseignement américaine attribue à un fournisseur américain de services en nuage un contrat pouvant atteindre 600 millions de dollars pour un nuage appelé à traiter des informations classifiées, notamment cloisonnées, et à être homologué selon les normes de la communauté du renseignement. | contrat jusqu'à 600 M$ sur 10 ans, 2013 | O6, O2 | choc | [S21] | A |
| F.CLD.G4.005 | 2013 | US | En 2013, deux grands fournisseurs américains de services en ligne annoncent chiffrer les échanges entre leurs centres de données, dans le contexte des révélations de presse sur la surveillance : Google, dont un programme existant a été accéléré en juin 2013, et Microsoft, qui annonce le 4 décembre 2013 un chiffrement du contenu des clients entre ses centres de données, prévu en totalité d'ici fin 2014. | Google, septembre 2013 ; Microsoft, 4 décembre 2013, échéance fin 2014 | O2, M1 | co:X.CLD.07 | [S25] | A |
| F.CLD.G4.006 | 2014 | EU | En octobre 2014, un grand fournisseur américain de services en nuage ouvre à Francfort une région de centres de données, sa deuxième région européenne, que la presse spécialisée relie à la demande de localisation des données en Allemagne, certaines entreprises allemandes ayant pour règle interne que leurs données ne quittent pas le pays. | région de Francfort, 23 octobre 2014 | T2, O2, O6 | choc | [S26] | A |
| F.CLD.G4.007 | 2015-10-06 | EU | La Cour de justice de l'Union européenne invalide la décision de la Commission qui reconnaissait le cadre américain « sphère de sécurité » comme assurant un niveau de protection adéquat des données personnelles transférées vers les États-Unis. | affaire C-362/14, 6 octobre 2015 | T2, O6, O4, O2 | co:X.CLD.07 | [S7] | A |
| F.CLD.G4.008 | 2015-06-02 | US | L'industrie américaine du cloud fait campagne publiquement en faveur d'une loi limitant la collecte en masse de métadonnées, afin de rassurer sa clientèle étrangère inquiète depuis 2013 ; la loi est promulguée le 2 juin 2015. | Public Law 114-23, 2 juin 2015 | O2, O6, M10 | co:X.CLD.07 | [S6] | V |
| F.CLD.G4.009 | 2012-09 | EU | En septembre 2012, l'État français, par la Caisse des dépôts, investit dans deux sociétés de cloud, Cloudwatt et Numergy, issues d'un projet que le Premier ministre avait appelé en janvier 2010 à mener comme alternative française et européenne à la domination nord-américaine du marché. | 75 M€ de la Caisse des dépôts par société ; discours du 18 janvier 2010 | T2, O6, O2 | choc | [S20], [S32] | A |
| F.CLD.G4.010 | 2015-03 | ASIE-E | La Corée du Sud promulgue la première loi au monde spécifiquement dédiée au cloud computing, qui organise le soutien public au secteur et la protection des utilisateurs plutôt qu'une politique de repli souverain, trajectoire distincte de la réponse sécuritaire américaine et européenne de la même période. | loi n° 13234, promulguée le 27 mars 2015, entrée en vigueur le 27 septembre 2015 | T3, O6 | choc | [S27] | V |

### Jalons cités
<!-- Lines 261-264 -->

`J.CLD.2013.01`, `J.CLD.2013.02`, `J.CLD.2013.03`, `J.CLD.2014.04`, `J.CLD.2015.02`,
`J.CLD.2015.03`.

### Trajectoire `T.CLD.G4`
<!-- Lines 267-282 -->

| année | phase | intensité | ce qui change | faits et jalons |
| --- | --- | --- | --- | --- |
| avant t0 | latent | 0 | Aucune usine de cloud à l'échelle mondiale hors des États-Unis ; la question de la souveraineté ne se pose pas encore. | — |
| 2005 | latent | 0 | Aucune bascule géopolitique documentée cette année. | — |
| 2006 | latent | 0 | Aucune bascule géopolitique documentée cette année. | — |
| 2007 | émergence | 1 | Les fournisseurs chinois engagent la construction de leurs propres centres de données, hors des fournisseurs américains (cité en A3 ; jalon fondateur de la trajectoire séparée chinoise). | J.CLD.2007.05 (A3) |
| 2008 | émergence | 0 | Aucune bascule géopolitique nouvelle documentée cette année. | — |
| 2009 | émergence | 2 | Un groupe chinois de commerce en ligne lance son activité de services en nuage. | F.CLD.G4.002 |
| 2010 | consolidation | 0 | Le Premier ministre français déclare que les Nord-Américains dominent le marché du cloud et appelle à une alternative française et européenne. | F.CLD.G4.001 |
| 2011 | consolidation | 0 | Aucune bascule géopolitique nouvelle documentée cette année pour G4. | — |
| 2012 | consolidation | 1 | Création en France, avec financement public, de deux sociétés de cloud, suite à l'appel de janvier 2010 à une alternative française et européenne. | F.CLD.G4.009 |
| 2013 | crise | 3 | Révélations sur la surveillance de masse ; contrat de cloud pour informations classifiées passé par un service de renseignement américain ; annonces de chiffrement des échanges entre centres de données. | F.CLD.G4.003, F.CLD.G4.004, F.CLD.G4.005, J.CLD.2013.01, J.CLD.2013.02, J.CLD.2013.03 |
| 2014 | crise | 2 | Ouverture à Francfort d'une région de centres de données par un grand fournisseur américain, en réponse à la demande de localisation des données en Allemagne. | F.CLD.G4.006, J.CLD.2014.04 |
| 2015 | crise | 3 | Invalidation judiciaire du cadre de transfert transatlantique ; loi américaine mettant fin à la collecte en masse, portée par l'industrie elle-même ; la Corée du Sud promulgue la première loi au monde dédiée au cloud, trajectoire de développement plutôt que de repli. | F.CLD.G4.007, F.CLD.G4.008, F.CLD.G4.010, J.CLD.2015.02, J.CLD.2015.03 |

### Narratif
<!-- Lines 285-304 -->

La géopolitique du cloud se noue autour d'une asymétrie : un groupe chinois lance son propre
service en 2009 [F.CLD.G4.002], et le Premier ministre français déclare en janvier 2010 que les
Nord-Américains dominent le marché [F.CLD.G4.001], avant que l'État français investisse en 2012
dans deux sociétés de cloud comme alternative [F.CLD.G4.009]. La crise de
confiance de 2013 est le pivot de la sous-dimension : les révélations sur la surveillance de
masse [F.CLD.G4.003] surviennent la même année où une agence de renseignement américaine confie
à un fournisseur de cloud un contrat pour des informations classifiées [F.CLD.G4.004] ; des
fournisseurs annoncent le chiffrement des échanges entre leurs centres de données [F.CLD.G4.005],
puis l'un d'eux ouvre en 2014 une région à Francfort, que la presse relie à la demande de
localisation des données en Allemagne [F.CLD.G4.006]. La fenêtre se referme en 2015 sur
deux textes qui répondent à la même crise par des voies opposées, l'un judiciaire et européen,
l'autre législatif et américain porté par l'industrie elle-même [F.CLD.G4.007, F.CLD.G4.008].
L'Asie de l'Est développée hors Chine suit une trajectoire distincte des deux précédentes : la
Corée du Sud clôt la fenêtre en promulguant la première loi au monde spécifiquement dédiée au
cloud, orientée vers le développement du secteur et la protection des utilisateurs plutôt que
vers la sécurité ou la souveraineté défensive [F.CLD.G4.010].

---

## Sources
<!-- Lines 307-343 -->

| clé | type | référence | note |
| --- | --- | --- | --- |
| [S1] | off | *USA PATRIOT Act*, Public Law 107-56, 26 octobre 2001, section 215 ; directive 95/46/CE du Parlement européen et du Conseil, 24 octobre 1995 | Public Law 107-56 vérifiée directement sur govinfo.gov (titre exact, numéro, date, texte de la section 215). La directive 95/46/CE est citée par sa référence exacte ; EUR-Lex étant inaccessible depuis cet environnement, son texte n'a pas été ouvert (statut `V` porté par la seule partie américaine du fait). |
| [S2] | off | *FISA Amendments Act of 2008*, Public Law 110-261, 10 juillet 2008 | Vérifiée directement sur govinfo.gov : titre exact (« Foreign Intelligence Surveillance Act of 1978 Amendments Act of 2008 »), numéro de loi publique et date d'enactment confirmés ; texte de la section 702 lu. |
| [S3] | off | Office of Management and Budget, mémorandum *Security Authorization of Information Systems in Cloud Computing Environments*, Steven VanRoekel, Federal Chief Information Officer, 8 décembre 2011 | Vérifié directement sur le PDF ouvert (archive whitehouse.gov) : date, auteur, objet et création du FedRAMP confirmés à la lecture du document. |
| [S4] | off | Commission européenne, communiqué de presse IP/12/46, « Commission proposes a comprehensive reform of data protection rules to increase users' control of their data and to cut costs for businesses », Bruxelles, 25 janvier 2012, https://dataskydd.net/files/utredningar-eu/IP_12_46_EN.pdf (copie du communiqué) | Communiqué ouvert et lu en PDF (le texte de la proposition COM(2012) 11 sur EUR-Lex est revenu vide à trois essais, il n'a pas été lu). Passages lus : « EU rules must apply if personal data is handled abroad by companies that are active in the EU market and offer their services to EU citizens » ; « companies and organisations must notify the national supervisory authority of serious data breaches as soon as possible (if feasible within 24 hours) ». |
| [S5] | off | Groupe de travail « Article 29 », *Opinion 05/2012 on Cloud Computing*, WP196, 1er juillet 2012, https://ec.europa.eu/justice/article-29/documentation/opinion-recommendation/files/2012/wp196_en.pdf | Document ouvert et lu en entier (PDF, `pdftotext`) : « Adopted July 1st 2012 ». § 3.4.1.1 : le client doit connaître « all subcontractors » et « the locations of all data centres personal data may be processed at » ; liste des clauses du contrat, dont « Obligation of the cloud provider to provide a list of locations in which the data may be processed » et la notification des violations ; § 3.5.1 : « sole self-certification with Safe Harbor may not be deemed sufficient » ; § 4.2 : la certification par un tiers « can be a credible means for cloud providers to demonstrate their compliance », un audit tiers choisi par le responsable « may be deemed to satisfy in lieu of an individual controller's right to audit ». |
| [S6] | off | *USA FREEDOM Act of 2015*, Public Law 114-23, approuvée le 2 juin 2015 (H.R. 2048, 114e Congrès) | Reprise de [S50] de `par_annee/cloud_2005_2015.md`, déjà vérifiée sur govinfo.gov : titre, numéro de loi publique et date d'approbation confirmés. |
| [S7] | off | Cour de justice de l'Union européenne, communiqué de presse n° 117/15 sur l'arrêt du 6 octobre 2015, *Maximillian Schrems c. Data Protection Commissioner*, affaire C-362/14, Luxembourg, 6 octobre 2015, https://curia.europa.eu/jcms/upload/docs/application/pdf/2015-10/cp150117en.pdf | Communiqué de la Cour ouvert et lu en PDF ; le texte de l'arrêt (CURIA et EUR-Lex) est revenu vide à trois essais, il n'a pas été lu, d'où le statut `A`. Passages lus : « the Court declares the Safe Harbour Decision invalid » ; la décision du 26 juillet 2000 (2000/520/CE) par laquelle la Commission avait jugé que les États-Unis assurent, au titre de la sphère de sécurité, un niveau de protection adéquat. |
| [S8] | off | Agence de l'Union européenne pour la cybersécurité (ENISA), *Security Framework for Governmental Clouds*, février 2015, https://www.enisa.europa.eu/publications/security-framework-for-governmental-clouds (PDF : https://www.enisa.europa.eu/sites/default/files/publications/Security%20Framework%20for%20Governmental%20Clouds.pdf) | Page de publication lue (date : 26 février 2015) et PDF lu (`pdftotext`). Le rapport s'appuie sur quatre modèles nationaux de cloud gouvernemental (Estonie, Grèce, Espagne, Royaume-Uni) ; sa bibliographie cite « CESG, Cabinet Office (2014). Cloud Security Principles » et « Centro Criptológico Nacional, Ministerio de Defensa de España, Guía/Norma de Seguridad de las TIC (CCN-STIC-823), Seguridad en Entornos Cloud (Borrador), Abril, 2014 » ; il décrit aussi, pour le Royaume-Uni, une adhésion à G-Cloud fondée sur « an accreditation process » imposant un socle de contrôles. Les deux textes cités n'ont pas été ouverts eux-mêmes : leur existence et leur date viennent de la bibliographie d'ENISA. Pour la France (Secure Cloud, février 2015), voir [S29] (source de grade faible). Le rapport ne dit pas que ces référentiels aient été publiés en 2015 ni qu'un cadre européen unique d'achat public fait défaut : l'année de l'énoncé est ramenée à 2014-2015, le terme « certification » remplacé par « sécurité » et la clause sur l'absence de cadre européen retirée. Rapport d'agence de l'Union, mais Espagne et Royaume-Uni ne sont lus que par leurs références. |
| [S9] | off | *Congressional Record* : Leahy, présentation de S. 607 (*Electronic Communications Privacy Act Amendments Act of 2013*), 19 mars 2013, https://irp.fas.org/congress/2013_cr/s607.html ; Lee, présentation de S. 356 (*Electronic Communications Privacy Act Amendments Act of 2015*), 4 février 2015, https://www.govinfo.gov/content/pkg/CREC-2015-02-04/html/CREC-2015-02-04-pt1-PgS773-2.htm ; IAPP, « The Email Privacy Act: What happened and where are we now », https://iapp.org/news/a/the-email-privacy-act-what-happened-and-where-we-are-now | Deux extraits du Congressional Record ouverts et lus : S. 607 exige un mandat fondé sur la cause probable pour le contenu des courriels (« obtain a search warrant based on probable cause to obtain the content of Americans' email »), section 3 « Elimination of 180-day rule » ; S. 356 « eliminates the ambiguous and outdated 180-day rule ». Article IAPP lu : le texte équivalent de la Chambre (H.R. 699) adopté par la Chambre en 2016 (419-0), bloqué au Sénat pendant la 114e législature, réintroduit en janvier 2017 ; la non-adoption de S. 607 et S. 356 est déduite de là (la page ProPublica sur S. 1011 de 2011 n'était plus disponible : cette proposition est écartée de l'énoncé). |
| [S10] | acad | Chander, A. et Lê, U. P., « Data Nationalism », *Emory Law Journal*, vol. 64, n° 3, 2015, p. 677, https://www.chander.org/s/data-nationalism.pdf | Article ouvert et lu (PDF, `pdftotext`), sections par pays : Chine, avis de la banque centrale de janvier 2011 qui « prohibits Banks from storing, processing or analysing outside China any PFI which has been collected in China » ; Australie, loi de 2012 sur les dossiers de santé électroniques, section 77 « prohibits the transfer of health records outside of Australia, with certain exceptions » ; Nigeria, lignes directrices de 2013 : les entreprises doivent « host government data locally within the country ». |
| [S11] | off | The Green Grid, *PUE: A Comprehensive Examination of the Metric*, livre blanc n° 49, 2012, https://datacenters.lbl.gov/sites/default/files/WP49-PUE%20A%20Comprehensive%20Examination%20of%20the%20Metric_v6.pdf (copie hébergée par le Lawrence Berkeley National Laboratory) | Document ouvert et lu en PDF (`pdftotext`) : la métrique PUE « was developed by The Green Grid Association, a non-profit, open industry consortium of end users, policy makers, technology providers, facility architects, and utility companies » ; « Since its original publication in 2007, PUE has been globally adopted by the industry » ; bibliographie : White Paper n° 6, 2007, *The Green Grid Data Center Power Efficiency Metrics: PUE and DCiE*. Le livre blanc de 2007 lui-même n'a pas été ouvert ; la date de fondation du consortium n'a été lue nulle part (la mention « février 2007 » est retirée). |
| [S12] | off | Mell, P. et Grance, T., *The NIST Definition of Cloud Computing*, NIST Special Publication 800-145, 28 septembre 2011 | Vérifiée directement sur nist.gov : date de publication (28 septembre 2011), auteurs (Peter Mell, Timothy Grance) et numéro de publication confirmés. |
| [S13] | off | OpenStack, *Introduction: A Bit of OpenStack History*, project team guide, https://docs.openstack.org/project-team-guide/introduction.html ; The Next Web, « OpenStack launches independent foundation, raising $10M », 19 septembre 2012, https://thenextweb.com/news/openstack-launches-independent-foundation-raising-10m | Pages ouvertes et lues. Guide OpenStack : le projet est né de deux efforts (réécriture du code d'infrastructure de Rackspace ; code Nova publié par Anso Labs, sous-traitant de la NASA), « officially announced at OSCON in Portland, OR, on July 21, 2010 » ; la fondation « launched in September 2012 as an independent body ». The Next Web : « new, independent foundation », conseil de 24 membres avec des représentants de SUSE, Rackspace, HP et Cisco. Aucune des pages lues ne dit que la fondation a été créée pour empêcher le contrôle par deux ou trois fournisseurs : clause retirée. |
| [S14] | off | Cloud Native Computing Foundation / Linux Foundation, « New Cloud Native Computing Foundation to drive alignment among container technologies », San Francisco, 21 juillet 2015, https://www.cncf.io/announcements/2015/06/21/new-cloud-native-computing-foundation-to-drive-alignment-among-container-technologies/ ; Kubernetes, « 10 Years of Kubernetes », 6 juin 2024, https://kubernetes.io/blog/2024/06/06/10-Years-of-Kubernetes/ | Communiqué ouvert et lu : la Linux Foundation annonce la CNCF, « a Linux Foundation Collaborative Project » ; Google est « pleased to contribute Kubernetes, the open source cluster scheduler, to the foundation as a seed technology » ; comité de supervision technique ; la fondation sera « responsible for stewardship of the projects » ; dateline du 21 juillet 2015 (l'URL porte 2015/06/21, incohérence relevée). Billet kubernetes.io (début de page seulement lu) : « on June 6th, 2014, the first commit of Kubernetes was pushed to GitHub ». Le rôle de Google comme concepteur et la séparation entre maintenance du projet et entreprise ne sont pas énoncés dans ce qui a été lu : clauses retirées. |
| [S28] | off | Conférence des commissaires allemands à la protection des données, communiqué du 24 juillet 2013, https://www.datenschutz.bremen.de/aktuelles/press-release-24-july-2013-9285 ; Groupe de travail « Article 29 », lettre de son président à la vice-présidente Reding, Bruxelles, 13 août 2013 (Ares(2013)2872799), https://ec.europa.eu/justice/article-29/documentation/other-document/files/2013/20130813_letter_to_vp_reding_final_en.pdf | Deux documents ouverts et lus. Communiqué : les autorités « will not issue any new permission for data transfer to non-EU countries (for example also for the use of certain cloud services) » et « will examine whether such data transfers should be suspended on the basis of the Safe Harbour framework ». Lettre (PDF, `pdftotext`) : « the WP29 has doubts whether the seemingly large-scale and structural surveillance of personal data that has now emerged can still be considered an exception strictly limited to the extent necessary » ; rappel de la possibilité, pour les autorités nationales, de suspendre les flux. |
| [S29] | livre | Wikipédia, article « SecNumCloud », https://fr.wikipedia.org/wiki/SecNumCloud | Page lue : l'ANSSI a créé « Secure Cloud » en février 2015 ; « Secure Cloud devient SecNumCloud en 2016 » ; version 3.0 définie en 2016. Source de référence de grade faible, retenue faute de mieux : les documents de l'ANSSI (cyber.gouv.fr) sont revenus en 404 ou vides, et aucun autre pays européen n'a pu être sourcé pour 2015 (clause « plusieurs pays » retirée). |
| [S15] | off | Maison-Blanche, blog officiel, billet du 15 septembre 2009 annonçant le lancement d'Apps.gov, https://obamawhitehouse.archives.gov/blog/2009/09/15/streaming-100-cloud | Page ouverte et lue : billet daté du 15 septembre 2009, « Today, I am excited to announce that we have launched Apps.gov » ; Apps.gov est « an online storefront for federal agencies to quickly browse and purchase cloud-based IT services ». Le titre exact du billet et son auteur n'ont pas été relevés. La clause « première reconnaissance par un État que la capacité informatique s'achète sur catalogue comme une fourniture » est retirée : le billet ne l'énonce pas. |
| [S16] | off | Kundra, V., U.S. Chief Information Officer, *Federal Cloud Computing Strategy*, Executive Office of the President, Office of Management and Budget, 8 février 2011 | Vérifiée directement : PDF ouvert (archive whitehouse.gov), page de titre lue (auteur, fonction, adresse whitehouse.gov) ; la date du 8 février 2011 est corroborée par une seconde archive indépendante portant la même mention en en-tête. |
| [S17] | off | U.S. Government Accountability Office, *Data Center Consolidation: Agencies Need to Complete Inventories and Plans to Achieve Expected Savings*, GAO-11-565, 26 juillet 2011 | Vérifié directement sur gao.gov : titre, numéro de rapport, date de publication et principales constatations confirmés. |
| [S18] | off | U.S. Government Accountability Office, *Data Center Consolidation: Strengthened Oversight Needed to Achieve Cost Savings Goal*, GAO-13-378, 23 avril 2013, https://www.gao.gov/products/gao-13-378 | Page du rapport (points saillants) ouverte et lue : « Agencies closed 420 data centers by the end of December 2012 » ; objectif de l'administration budgétaire : « close 40 percent, or 1,253 of the 3,133 total federal data centers, by the end of 2015 » ; « OMB has not measured agencies' progress against its other goal of $3 billion in cost savings by the end of 2015 ». Le PDF complet n'a pas été ouvert. |
| [S19] | off | Cabinet Office (gouvernement britannique), communiqué « CloudStore opens for business », 19 février 2012, https://www.gov.uk/government/news/cloudstore-opens-for-business | Communiqué ouvert et lu, daté du 19 février 2012 : « CloudStore, the online appstore of the government G-Cloud framework for cloud-based ICT services, is open for business » ; « The G-Cloud received nearly 300 bids from suppliers, for a total of some 1,700 services » ; « Public sector organisations will be able to purchase ». Le chiffre « plus de 250 fournisseurs » de l'énoncé d'origine n'y figure pas : remplacé par « près de 300 offres de fournisseurs ». Le communiqué parle des offres reçues par le cadre, pas du nombre de services déjà listés le jour de l'ouverture. |
| [S20] | off | Premier ministre François Fillon, *Discours sur le thème du très haut débit et l'économie numérique*, Vélizy, 18 janvier 2010, service de presse de Matignon, https://www.arcep.fr/fileadmin/reprise/communiques/communiques/2010/disc-1er-ministre-thdebit-180110.pdf ; Noro, P., « Le cloud souverain est de retour : généalogie d'une ambition emblématique de la souveraineté numérique en France », Sciences Po, 20 juillet 2020, https://www.sciencespo.fr/public/chaire-numerique/2020/07/20/cloud-souverain-genealogie-ambition-emblematique-souverainete-numerique/ | Discours ouvert et lu en entier pour son passage sur le cloud (PDF, `pdftotext`) : « Aujourd'hui force est de constater que les Nord-américains dominent ce marché, qui constitue pourtant un enjeu absolument majeur pour la compétitivité de nos économies, pour le développement durable et même, j'ose le dire, pour la souveraineté de nos pays » ; « Il faut absolument que nous soyons capables de développer une alternative française et européenne dans ce domaine » ; souhait d'un partenariat public-privé grâce aux fonds du programme pour les investissements d'avenir. Le discours date le constat de janvier 2010, non de 2009, et ne dit ni que les groupes européens du numérique l'ont fait, ni qu'aucun fournisseur mondial n'est européen : seule la domination nord-américaine est énoncée (clauses de l'énoncé d'origine ramenées à cela). Sciences Po (Noro), page rouverte : l'idée d'un cloud souverain « a germé au sein de l'État », le projet Andromède est esquissé deux ans après 2009 et l'État prend 33 % de chacune des deux sociétés de 2012 par deux investissements de 75 M€ gérés par la Caisse des dépôts. Pour la création de Cloudwatt et Numergy en septembre 2012, voir [S32]. Document primaire pour F.CLD.G4.001 ; pour F.CLD.G4.009 le lien entre le discours et le projet de 2012 repose sur Noro (secondaire), d'où `A`. |
| [S21] | presse | Nextgov, « Daring Deal », 9 juillet 2014, https://www.nextgov.com/modernization/2014/07/daring-deal/100872/ ; voir aussi [S34] pour le contrat et la décision de la juridiction fédérale | Article ouvert et lu : la CIA a attribué à AWS un contrat « worth up to $600 million over a period of up to 10 years » ; le nuage « will, for example, be able to handle Sensitive Compartmented Information, a type of classified information » ; un haut responsable de la CIA dit qu'il « will be accredited and compliant with IC standards » ; c'est « a public cloud built on private premises ». Le texte est au futur : l'article ne dit pas que l'homologation était obtenue en 2013, d'où la correction de l'énoncé d'origine (« obtient l'homologation »). La clause « fait tomber l'argument selon lequel certaines données seraient trop sensibles » est retirée : l'article ne l'énonce pas ; seul un ancien chercheur de la CIA, cité, dit que la décision « removes the clouded judgment that cloud isn't secure » (opinion). Auteur de l'article non relevé. |
| [S22] | off | U.S. Government Accountability Office, *Data Center Consolidation: Reporting Can Be Improved to Reflect Substantial Planned Savings*, GAO-14-713, 25 septembre 2014, https://www.gao.gov/products/gao-14-713 ; texte intégral https://www.gao.gov/assets/670/666125.txt | Page du rapport lue ; texte intégral lu pour ses 100 000 premiers caractères sur 191 536. Passages : environ 1,1 Md$ « in savings and avoidances for fiscal years 2011 through 2013 » ; prévisions d'environ 3,3 Md$ jusqu'en fin d'exercice 2015, « about $300 million higher than the Office of Management and Budget's (OMB) original $3 billion goal » ; « 11 of the 21 agencies with planned cost savings are underreporting » leurs chiffres 2012-2015 d'environ 2,2 Md$ ; « the $5.3 billion in total savings will be understated ». Le rapport ne parle pas d'un objectif fixé en 2010 dans la partie lue : cette clause de l'énoncé d'origine est retirée, ainsi que le constat d'un suivi « insuffisant pour vérifier l'atteinte de l'objectif », que le rapport contredit (prévisions supérieures à l'objectif). |
| [S23] | presse | Alibaba Cloud Community, « 10 Years of Cloud Intelligence: How Will Alibaba Change the Future of Cloud Computing? », 27 août 2019, https://www.alibabacloud.com/blog/10-years-of-cloud-intelligence-how-will-alibaba-change-the-future-of-cloud-computing_595298 ; Yicai (第一财经), article sur Alibaba Cloud, https://www.yicai.com/news/100273576.html | Billet de l'entreprise ouvert et lu : le groupe est « the first cloud provider in China, officially opening for business in 2009 » ; avant 2009 aucune autre entreprise chinoise n'avait fait du cloud son activité principale. Article de Yicai ouvert et lu : « 自2009年成立以来，经过10年的技术沉淀 » (depuis sa création en 2009). Le jour et le mois (10 septembre 2009) n'ont été lus dans aucune source ouverte (billet : année seule ; Yicai : année seule ; Wikipédia anglais : « September 2009 » sans référence ; un billet de blog donne le 10 septembre, non retenu) : la date du jour est retirée. Les clauses « pour le marché intérieur » et « séparant durablement l'écosystème chinois des fournisseurs américains » sont retirées : aucune source lue ne les énonce. « Premier fournisseur de cloud de Chine » est l'affirmation de l'entreprise, rapportée comme telle. Le jalon J.CLD.2010.05 de la chronologie date la création de 2010 : écart relevé. Sources de grade moyen (page d'entreprise, presse chinoise). |
| [S24] | presse | Gregory Ferenstein, TechCrunch, « Report: NSA Collects Data Directly From Servers Of Google, Apple, Microsoft, Facebook And More », 6 juin 2013, https://techcrunch.com/2013/06/06/report-nsa-collects-data-directly-from-servers-of-google-apple-microsoft-facebook-and-more ; Intelligence and Security Committee of Parliament, *Statement on GCHQ's Alleged Interception of Communications under the US PRISM Programme*, 17 juillet 2013, https://assets.publishing.service.gov.uk/media/5a7c9cfbed915d6969f461df/ISC-Statement-on-GCHQ.pdf | Article TechCrunch ouvert et lu (presse de l'événement) : le Washington Post a rapporté que la NSA et le FBI « tapping directly into the central servers of nine leading U.S. Internet companies » (programme PRISM) ; données : audio, vidéo, photos, courriels, documents, journaux de connexion ; entreprises citées : Microsoft, Yahoo, Google, Facebook, PalTalk, YouTube, Skype, AOL, Apple, qui nient toutes un accès direct. Déclaration du comité parlementaire britannique ouverte et lue (PDF, `pdftotext`) : « PRISM is a programme through which the US Government obtains intelligence material (such as communications) from Internet Service Providers » ; des fuites ont paru « over the last month » ; le comité a examiné « the reports that GCHQ produced on the basis of intelligence sought from the US » et conclut que l'allégation de contournement du droit britannique par PRISM est « unfounded ». Les articles du Guardian et du Washington Post eux-mêmes n'ont pas été ouverts (le Guardian est refusé par l'outil de lecture ; le Post n'a pas été tenté directement) : le contenu des révélations est lu par TechCrunch. La clause « avec coopération de services alliés » est remplacée par ce que le comité britannique dit ; le terme « révélations documentées » ramené à « la presse révèle ». Le comité ne dit pas que GCHQ a eu accès à PRISM. |
| [S25] | off | Microsoft, Brad Smith (General Counsel), « Protecting customer data from government snooping », 4 décembre 2013, https://blogs.microsoft.com/blog/2013/12/04/protecting-customer-data-from-government-snooping/ ; Data Center Knowledge, « Google Boosting Encryption Between Data Centers », 9 septembre 2013, https://www.datacenterknowledge.com/archives/2013/09/09/google-boosts-encryption-between-data-centers/ | Billet de Microsoft ouvert et lu (ce que le fournisseur a annoncé) : « Key services will encrypt customer content as it moves between our data centers » ; « We also will encrypt customer content that we store » ; « All of this will be in place by the end of 2014, and much of it is effective immediately » ; motif : « recent allegations in the press of a broader and concerted effort by some governments » ; le billet ne nomme ni Google ni Yahoo. Article de la presse spécialisée ouvert et lu : Google chiffre les données entre ses centres de données, serveurs et liaisons en fibre, « amid ongoing revelations about the code-breaking capabilities of the NSA » ; un programme existant a été accéléré en juin 2013 « as Google sought to reassure consumers ». Un billet IEEE Spectrum lu cite le directeur juridique de Google : « continued to extend encryption across more and more Google services and links ». Retiré faute de source lue : Yahoo (IEEE Spectrum ne rapporte pas de chiffrement par Yahoo), le caractère « systématique » et « généralisé » du chiffrement, « les grands fournisseurs » (deux seulement lus), « réponse technique directe à la perte de confiance » (Microsoft et la presse parlent d'allégations et de rassurer, pas de perte de confiance). Le chiffrement de Google avait commencé avant les révélations de l'automne 2013 : l'énoncé d'origine, qui en faisait une réaction, est nuancé. |
| [S26] | off | Amazon Web Services, « Announcing the AWS EU (Frankfurt) Region », 23 octobre 2014, https://aws.amazon.com/about-aws/whats-new/2014/10/23/announcing-the-aws-eu-frankfurt-region ; TechCrunch, « AWS expands its European footprint with Frankfurt data center », 23 octobre 2014, https://techcrunch.com/2014/10/23/aws-expands-its-european-footprint-with-frankfurt-data-center ; Data Center Knowledge, « AWS Adds Second European Cloud Region in Germany », 23 octobre 2014, https://www.datacenterknowledge.com/archives/2014/10/23/aws-launches-cloud-data-center-in-germany/ | Trois pages ouvertes et lues. Annonce du fournisseur (ce qu'il a fait) : billet du 23 octobre 2014, « immediate availability of the new EU (Frankfurt) infrastructure region » ; avec l'Irlande, deux régions uniquement européennes ; « customers choose where their data is processed and stored ». TechCrunch : « the second data center for its AWS cloud computing service in Europe » ; les développeurs peuvent « ensure that their data never leaves the European Union » ; certaines entreprises allemandes ont des règles internes selon lesquelles les données « isn't allowed to leave the country » et pourront choisir la plateforme. Data Center Knowledge : forte demande d'une région en Allemagne « in big part due to data sovereignty concerns ». Seul un fournisseur et une région (Francfort) sont établis : « les grands fournisseurs américains » et « dans d'autres pays européens » sont retirés, aucune ouverture d'un autre fournisseur en 2014 n'ayant été lue (Data Center Knowledge ne mentionne que des « reports » sur Microsoft). La clause « exigence de localisation » est reformulée en règle interne d'entreprises et en demande de localisation rapportée par la presse ; « plutôt que par un changement d'actionnariat » est retirée, aucune source lue ne l'énonce. |
| [S27] | off | République de Corée, *Act on the Development of Cloud Computing and Protection of Its Users*, loi n° 13234, promulguée le 27 mars 2015 (Korea Legislation Research Institute, elaw.klri.re.kr, traduction officielle anglaise) | Ouvert et lu le 2026-09-22 : elaw.klri.re.kr ; titre exact, numéro de loi, date de promulgation (27 mars 2015) et entrée en vigueur (27 septembre 2015) confirmés, ainsi que l'objet de la loi (développement du secteur, protection des utilisateurs). |
| [S30] | off | Union internationale des télécommunications, secteur de la normalisation (UIT-T), Recommandation Y.3500 « Information technology – Cloud computing – Overview and vocabulary » (08/14), https://www.itu.int/rec/T-REC-Y.3500 ; UIT-T, page « ITU-T Recommendations », https://www.itu.int/en/ITU-T/publications/Pages/recs.aspx | Deux pages ouvertes et lues. Notice de la Recommandation : « Y.3500 (08/14) », statut « In force » ; le texte de la Recommandation n'a pas été ouvert, et la notice ne cite pas ISO/IEC 17788. Page de l'UIT-T : « ITU-T Recs have non-mandatory status until they are adopted in national laws ». Aucune source lue ne traite de l'absence d'autres instances intergouvernementales : la clause « aucune instance intergouvernementale ne fixe de norme contraignante unique » de l'énoncé d'origine est retirée. Source de grade moyen pour le sens du fait (notice et page de présentation, pas le texte). |
| [S31] | presse | Le Monde Informatique, « 285 millions d'euros pour Andromède, le cloud souverain français », 21 septembre 2011, https://www.lemondeinformatique.fr/actualites/lire-285-millions-d-euros-pour-andromede-le-cloud-souverain-francais-41990.html ; Assemblée nationale, question écrite de Jean-Christophe Lagarde, JO du 4 octobre 2011, https://questions.assemblee-nationale.fr/q13/13-119124QE.htm | Article ouvert et lu : « son cloud public national : un projet baptisé Andromède », « En partie financé par le grand emprunt », « La Caisse des Dépôts investira 135 millions d'euros », 285 millions d'euros au total, objectif de concurrencer les grands fournisseurs américains (les Nord-Américains « dominent ce marché »). Question écrite lue : « L'État injectera 135 millions d'euros dans la structure par l'intermédiaire de la Caisse des dépôts », les 150 millions restants venant de partenaires privés. Date d'origine du projet : l'article dit « lancé en 2009 par François Fillon » ; Sciences Po (Noro, 2020) dit que l'idée naît en 2009 et que le projet émerge « deux ans plus tard » ; Acteurs publics écrit « À l'origine, en 2010 » : l'énoncé ne retient que septembre 2011. La clause « motivé par l'absence de fournisseur français à l'échelle » est retirée, aucune source lue ne l'énonce. Presse spécialisée, grade moyen. |
| [S32] | presse | IDG News Service (PCWorld), « French sovereign wealth funds invests in two local cloud computing providers », 6 septembre 2012, https://www.pcworld.com/article/461135/french_sovereign_wealth_funds_invests_in_two_local_cloud_computing_providers.html ; OPECST, rapport n° 271 (2014-2015), tome II, audition d'un responsable de Cloudwatt du 26 février 2014, https://www.senat.fr/rap/r14-271-2/r14-271-27.html ; Noro, P., « Le cloud souverain est de retour : généalogie d'une ambition emblématique de la souveraineté numérique en France », Chaire Digital, Gouvernance et Souveraineté, Sciences Po, 20 juillet 2020, https://www.sciencespo.fr/public/chaire-numerique/2020/07/20/cloud-souverain-genealogie-ambition-emblematique-souverainete-numerique/ ; Rude Baguette, « Cloudwatt : vie et mort du premier cloud souverain de la France », août 2019, https://www.rudebaguette.com/2019/08/cloudwatt-orange-cloud-souverain-fin/ | Quatre pages ouvertes et lues. IDG : Numergy et Cloudwatt lancés la même semaine de septembre 2012, la Caisse détient 33,33 % d'un investissement total de 225 M€ dans Cloudwatt, Numergy avec « the same » total. OPECST : Cloudwatt « Créé le 6 septembre 2012 », capital de « 225 millions d'euros, dont 100 millions d'euros ont été apportés par Orange, 50 millions d'euros par Thales », 75 M€ de la Caisse des dépôts. Sciences Po : l'État prend 33 % de chacune des deux sociétés par « deux investissements de 75 millions d'euros », scission après un « désaccord entre Dassault Système et Orange ». Rude Baguette : les groupes « ne parviennent pas à s'entendre », Orange et SFR refusent de coopérer, 150 M€ d'aide en tout. Les sources divergent sur les industriels en désaccord : l'énoncé ne les nomme pas. Le montant de 75 M€ pour Numergy repose sur Sciences Po seul ; le total de 150 M€ est la somme des deux. |
| [S33] | off | Direction générale des entreprises et Commissariat général à l'investissement, communiqué de presse « Cloud computing : L'Etat annonce l'acquisition par Orange de sa participation dans Cloudwatt et confirme son soutien à Numergy », Paris, 20 mars 2015, https://www.info.gouv.fr/upload/media/organization/0001/01/sites_default_files_contenu_piece-jointe_2015_03_cp_numergy.pdf | Communiqué ouvert et lu en PDF (`pdftotext`) : « Orange, qui détenait 44,4% de Cloudwatt, a racheté l'intégralité des participations de l'État (33,3%) et de Thalès (22,2%) » ; « l'Etat continue par ailleurs à investir dans Numergy ». Le mot « souverain » de l'énoncé d'origine n'y figure pas : retiré. |
| [S34] | presse | Nextgov, « Amazon CIA contract protested », 31 mai 2013, https://www.nextgov.com/cybersecurity/2013/05/amazon-cia-contract-protested/211559/ ; IDG News Service (PCWorld), « Amazon wins CIA cloud deal in court battle with IBM », 8 octobre 2013, https://www.pcworld.com/article/448013/amazon-wins-cia-cloud-deal-in-court-battle-with-ibm.html | Deux articles ouverts et lus. Nextgov : contrat de la CIA « awarded to AWS in January », « 10-year, $600 million cloud computing contract », « IBM filed a bid protest on Feb. 26 » devant le GAO. IDG : contrat « worth up to $600 million », IBM s'est plaint au GAO, le GAO a donné en partie raison à IBM et recommandé de rouvrir la mise en concurrence, AWS a saisi la Court of Federal Claims, qui a tranché pour Amazon, IBM prévoyant de faire appel. La durée du contrat n'est pas reprise (dix ans selon Nextgov, non indiquée par IDG) ; la décision de la juridiction elle-même n'a pas été ouverte, sa date (octobre 2013) vient de l'article du 8 octobre. |
