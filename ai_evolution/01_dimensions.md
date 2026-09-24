# Dimensions — axe 1

Taxonomie des aspects de la société dont on suit la variation après chaque choc. Huit domaines
(niveau 1) : sept domaines de réponse ordonnés par retard attendu, A à G, et un domaine
d'énergie, H, facteur de production au même titre que le travail. Chacun est décomposé en
sous-dimensions (niveau 2). Chaque sous-dimension a une question,
des types d'indicateurs et des frontières avec ses voisines. Ce fichier est **stable pendant la
collecte** (règle R9 du [CLAUDE.md](CLAUDE.md)).

## Table of Contents

1. [Principes de construction](#principes-de-construction) _(Lines 33-63)_
1. [Niveau 1 : les huit domaines](#niveau-1-les-huit-domaines) _(Lines 66-85)_
1. [Niveau 2 : sous-dimensions par domaine](#niveau-2-sous-dimensions-par-domaine) _(Lines 88-88)_
   1. [A. Industrie et infrastructure](#a-industrie-et-infrastructure) _(Lines 91-105)_
   1. [B. Finance](#b-finance) _(Lines 108-119)_
   1. [C. Économie](#c-conomie) _(Lines 122-131)_
   1. [D. Travail et emploi](#d-travail-et-emploi) _(Lines 134-141)_
   1. [E. Vie quotidienne](#e-vie-quotidienne) _(Lines 144-152)_
   1. [F. Culture et société](#f-culture-et-soci-t) _(Lines 155-163)_
   1. [G. Politique et gouvernance](#g-politique-et-gouvernance) _(Lines 166-178)_
   1. [H. Énergie](#h-nergie) _(Lines 181-190)_
1. [Frontières entre domaines voisins](#fronti-res-entre-domaines-voisins) _(Lines 193-218)_
1. [Couverture attendue par choc](#couverture-attendue-par-choc) _(Lines 221-234)_




---

## Principes de construction
<!-- Lines 33-63 -->

**P1. Partition par niveau d'organisation sociale.** Chaque domaine correspond à un niveau où
le changement s'observe avec ses propres acteurs et ses propres indicateurs : l'appareil
productif, le capital, les agrégats et marchés, les travailleurs, la personne dans sa journée,
le sens collectif, la puissance publique, et l'énergie qui alimente l'appareil productif. Cela
évite les listes thématiques qui mélangent niveaux et effets.

**P2. Ordre par retard attendu.** Les domaines sont numérotés A à G du plus proche au plus
éloigné de l'épicentre technologique, ce qui correspond à l'hypothèse H1 de
[00_these_et_methode.md](00_these_et_methode.md) : l'industrie bouge en premier, la politique
en dernier. Cet ordre est une hypothèse à tester, pas un résultat. Le domaine H, énergie, est
hors de cet ordre : c'est un facteur de production, à la fois précondition et conséquence du
choc, avec sa propre horloge (cycles de prix, infrastructures à l'échelle de la décennie). Sa
lettre H garde les codes A à G stables.

**P3. Une sous-dimension = une question + des indicateurs.** Une sous-dimension qu'on ne sait
pas mesurer, même qualitativement, n'en est pas une. Les indicateurs listés sont des *types* de
séries à chercher, pas des obligations.

**P4. Identiques pour les deux chocs.** Les mêmes sous-dimensions servent pour Internet et pour
le cloud, pour rendre la comparaison possible. Une sous-dimension vide pour un choc est notée
vide, avec une ligne d'explication.

**P5. Frontières explicites.** Là où deux sous-dimensions se recouvrent, une règle dit où va le
fait. Un fait a une sous-dimension primaire et peut en lister une secondaire.

**P6. Codes courts.** Un code lettre-chiffre par sous-dimension (`A1`, `C4`), utilisé dans les
identifiants de faits et de trajectoires.

---

## Niveau 1 : les huit domaines
<!-- Lines 66-85 -->

| Code | Domaine | Question du domaine | Ce qu'il n'est pas |
| --- | --- | --- | --- |
| **A** | Industrie et infrastructure | Deux blocs : comment et par qui les services numériques sont-ils produits (**bâtisseurs**, A1-A4) ; comment les autres industries s'en servent-elles (**utilisatrices**, A5-A8) ? | Pas les résultats de marché (C), pas le capital (B). |
| **B** | Finance | Comment le capital finance-t-il le choc, selon trois composantes (privé domestique, étranger, public et régulation), et comment se redistribue-t-il ? | Pas le secteur financier comme industrie (A5, A8). |
| **C** | Économie | Quels résultats agrégés et quels mécanismes de marché ? | Pas les salaires et l'emploi (D). |
| **D** | Travail et emploi | Qu'arrive-t-il à ceux qui travaillent ? | Pas la vie hors travail (E). |
| **E** | Vie quotidienne | Qu'est-ce qui change dans la journée d'une personne ordinaire ? | Pas le sens collectif ni les normes (F). |
| **F** | Culture et société | Qu'est-ce qui change dans le sens collectif, le savoir, les normes ? | Pas le droit ni la puissance publique (G). |
| **G** | Politique et gouvernance | Comment la puissance publique et les rapports de force internationaux répondent-ils ? | Pas les normes sociales informelles (F3). |
| **H** | Énergie | Combien d'énergie l'appareil du choc consomme-t-il, sous quelle contrainte, dans quel contexte énergétique, et avec quel effet sur la consommation du reste de l'économie ? | Pas l'infrastructure construite et son capex (A1), pas les prix des TIC (C2). |

**Axiome porté par H :** la production est humain + énergie. Le travail a son domaine (D),
l'énergie a le sien (H). Les usines du cloud sont, au sens propre, des convertisseurs
d'électricité en service numérique ; le réseau Internet est un convertisseur d'électricité en
distribution. On regarde donc, pour chaque choc, ce qui a bougé du côté de l'énergie, en
consommation, en contrainte, en contexte de prix et de mix, et en effet sur le reste de l'économie.

---

## Niveau 2 : sous-dimensions par domaine
<!-- Lines 88-88 -->

### A. Industrie et infrastructure
<!-- Lines 91-105 -->

Bloc **bâtisseurs** : A1 à A4. Bloc **utilisatrices** : A5 à A8 (décision D18).
<!-- Lines 91-99 -->

| Code | Sous-dimension | Question | Types d'indicateurs |
| --- | --- | --- | --- |
| A1 | Infrastructure physique et capacité | Qu'est-ce qui a été construit, à quel rythme, avec quelles surcapacités ? | Kilomètres de fibre, abonnés haut débit, nombre et taille des centres de données, capex des opérateurs et des plateformes, prix unitaire du transit, du stockage, du calcul, consommation d'énergie. |
| A2 | Pile technique, standards et plateformes | Quelles briques logicielles et quels standards se sont imposés, ouverts ou propriétaires, et qui les a fixés ? | Parts de marché des navigateurs, systèmes, serveurs ; jalons des standards ; jalons de l'open source ; interfaces devenues standards de fait. |
| A3 | Structure du secteur technologique | Qui produit la technologie : anciens, nouveaux, intégrés, concentrés ? | Entrées et sorties d'acteurs, acquisitions, parts de marché des fournisseurs, intégration verticale, naissance de géants. |
| A4 | Mode de production du logiciel et des services | Comment fabrique-t-on et exploite-t-on un service numérique, à quel coût, avec quelle organisation ? | Coût de lancement d'un service, délai de mise en production, part des dépenses informatiques externalisées, dépenses en capital contre dépenses de fonctionnement, pratiques d'ingénierie, organisation des directions informatiques. |
| A5 | Reconfiguration des chaînes de valeur des autres secteurs | Comment les chaînes de valeur des autres industries se réorganisent-elles : intermédiaires supprimés ou créés, secteurs en déclin mesurable ? | Revenus des acteurs établis, faillites et sorties, nouveaux intermédiaires, emploi des secteurs court-circuités. Secteurs suivis : médias, commerce, voyage, services financiers, télécoms, éducation, santé, agriculture, logiciel. |
| A6 | Canaux de vente électroniques, entre entreprises et par secteur | Quelle part des ventes des autres industries passe par un canal électronique, par quelle technologie (échange de données informatisé préexistant ou Internet), et dans quels secteurs le canal en ligne devient-il important ? | Part des expéditions et des ventes de gros réalisées en ligne, part de l'échange de données informatisé contre Internet, part des réservations et des ordres en ligne par secteur, places de marché entre entreprises. |
| A7 | Adoption et usage interne dans les entreprises utilisatrices | À quel rythme les entreprises hors secteur numérique se connectent-elles et intègrent-elles le réseau à leurs opérations, selon leur taille ? | Part des entreprises connectées, dotées d'un site, achetant ou vendant en ligne, par taille ; usage dans les achats, la chaîne d'approvisionnement, la relation client. |
| A8 | Services rendus possibles | Quels services nouveaux les secteurs non technologiques offrent-ils grâce au réseau ? | Banques dotées d'un site transactionnel, comptes de courtage en ligne, suivi et information des clients, services en ligne des assureurs, transporteurs et distributeurs. |

### B. Finance
<!-- Lines 108-119 -->

Composantes du capital : B1 privé domestique, B4 étranger, B5 public et régulation. B2 et B3 sont des vues transversales aux trois composantes (décision D18).
<!-- Lines 102-108 -->

| Code | Sous-dimension | Question | Types d'indicateurs |
| --- | --- | --- | --- |
| B1 | Capital privé domestique | Quel capital privé du pays d'origine a financé les entreprises et l'infrastructure, en fonds propres et en dette ? | Capital-risque, introductions en bourse, participation des ménages à la bourse, dette bancaire et obligataire des opérateurs, marchés nationaux de valeurs de croissance. |
| B2 | Cycle spéculatif et valorisations | Y a-t-il eu emballement, pic, correction ; de quelle ampleur ; avec quels effets de richesse ? | Indices sectoriels, multiples de valorisation, pertes de capitalisation, chronologie du cycle. |
| B3 | Redistribution de la valeur | Où la valeur boursière et les rendements ont-ils atterri : anciens, nouveaux, investisseurs, fondateurs ? | Classements de capitalisation avant et après, fusions et acquisitions emblématiques, faillites emblématiques, concentration des rendements. |
| B4 | Capital étranger | Quelle part du financement vient de l'étranger, par quels canaux, et avec quel rôle dans le cycle ? | Achats nets de titres par des non-résidents, investissement direct étranger, fusions et acquisitions transfrontalières, financement du déficit courant. |
| B5 | Capital public et régulation financière | Comment la puissance publique finance, amplifie ou corrige le cycle ? | Financement public de la recherche et du réseau, politique monétaire, privatisations d'opérateurs, recettes d'enchères de licences, lois et règles des marchés financiers. |

### C. Économie
<!-- Lines 122-131 -->

| Code | Sous-dimension | Question | Types d'indicateurs |
| --- | --- | --- | --- |
| C1 | Productivité et croissance | Le choc se voit-il dans les agrégats, avec quel délai, et que mesure-t-on mal ? | Productivité du travail et multifactorielle, contribution des TIC à la croissance, débats de mesure, surplus non compté. |
| C2 | Investissement, prix et inflation | Comment l'investissement se déplace-t-il et quels prix baissent ? | Part de l'investissement TIC, indices de prix ajustés de la qualité, désinflation importée, déplacement des dépenses en capital vers les dépenses de fonctionnement. |
| C3 | Commerce international et mondialisation | Quels services deviennent échangeables et où se déplace la production ? | Commerce de services, délocalisation, chaînes de valeur mondiales, commerce numérique. |
| C4 | Modèles d'affaires et création de valeur | Comment gagne-t-on de l'argent avec la nouvelle technologie ? | Gratuit financé par la publicité, place de marché, abonnement, longue traîne, effets de réseau, paiement à l'usage, part de chaque modèle dans les revenus. |
| C5 | Concurrence, concentration et pouvoir de marché | Les marchés se concentrent-ils, et comment la concurrence réagit-elle ? | Parts de marché, indices de concentration, procédures antitrust, dynamique gagnant-rafle-tout. |
| C6 | Répartition des gains et inégalités | Qui capte les gains : quelles firmes, quels territoires, quels ménages ? | Écart entre firmes de tête et les autres, concentration géographique, revenus et patrimoines par décile hors salaires (les salaires sont en D4). |

### D. Travail et emploi
<!-- Lines 134-141 -->

| Code | Sous-dimension | Question | Types d'indicateurs |
| --- | --- | --- | --- |
| D1 | Volume et structure de l'emploi | Combien d'emplois créés, détruits, déplacés, dans quels secteurs, à quel rythme ? | Emploi par secteur et par profession, emploi du secteur technologique, vagues de licenciements, taux de chômage par groupe. |
| D2 | Métiers, compétences et formation | Quels métiers apparaissent, disparaissent, se transforment ; quelles compétences sont demandées ; comment on se forme ? | Nomenclatures de professions, offres d'emploi par compétence, inscriptions dans les filières, certifications, formations nouvelles. |
| D3 | Organisation du travail et outils en réseau | Où, quand, avec quels outils en réseau et sous quel statut travaille-t-on, dans tous les métiers et toutes les tailles d'entreprise ? | Part des actifs utilisant ordinateur, Internet et courriel au travail par profession et niveau d'études, télétravail, externalisation et délocalisation des tâches de bureau, travail à la tâche et plateformes, statuts d'emploi, substitution du courrier et de la télécopie. |
| D4 | Salaires, polarisation et rapport de force | Qui gagne plus, qui gagne moins, et comment le rapport de force évolue-t-il ? | Primes de qualification, polarisation par tâche, part du travail dans la valeur ajoutée, syndicalisation, négociation collective. |

### E. Vie quotidienne
<!-- Lines 144-152 -->

| Code | Sous-dimension | Question | Types d'indicateurs |
| --- | --- | --- | --- |
| E1 | Adoption et équipement | Qui est équipé et connecté, quand, et qui reste à l'écart ? | Pénétration des ménages, terminaux, type de connexion, fracture interne par âge, revenu, territoire. |
| E2 | Communication et liens | Comment les gens se parlent-ils et se rencontrent-ils ? | Usage du courriel, de la messagerie, du téléphone, des réseaux, rencontres en ligne, fréquence de contact. |
| E3 | Consommation et démarches | Comment achète-t-on, se déplace-t-on, se soigne-t-on, fait-on ses démarches ? | Commerce en ligne par catégorie, banque en ligne, réservation de voyage, démarches administratives, information de santé, mobilité. |
| E4 | Information, loisirs et divertissement | Comment s'informe-t-on et se divertit-on ? | Recherche d'information, actualité en ligne, musique, vidéo, jeux, lecture, temps par média. |
| E5 | Temps, espace et attention | Comment le budget-temps, la frontière domicile-travail et la disponibilité changent-ils ? | Enquêtes emploi du temps, temps d'écran, joignabilité permanente, mobilité quotidienne. |

### F. Culture et société
<!-- Lines 155-163 -->

| Code | Sous-dimension | Question | Types d'indicateurs |
| --- | --- | --- | --- |
| F1 | Médias, information et création | Comment l'écosystème de l'information et des œuvres se réorganise-t-il ? | Économie de la presse, désintermédiation, contenus amateurs, industries culturelles, conflits sur le droit d'auteur, confiance dans les médias. |
| F2 | Savoir, science et éducation | Comment l'accès au savoir, la pratique scientifique et l'enseignement changent-ils ? | Encyclopédies et accès libre, pratiques de publication, enseignement en ligne, données ouvertes, science computationnelle. |
| F3 | Imaginaires, normes et valeurs | Quels récits, quelles utopies et dystopies, quelles normes de vie privée, de partage, de propriété ? | Discours publics, cycles d'enthousiasme et de désillusion, enquêtes de valeurs, normes de vie privée déclarées et pratiquées. |
| F4 | Lien social, communautés et identités | Quelles communautés, identités et fractures se forment ? | Communautés en ligne, anonymat, sous-cultures, langue dominante et localisation, fossé générationnel, globalisation culturelle. |
| F5 | Concentration et diversité des consommations et de l'attention | Les consommations culturelles et l'attention se concentrent-elles sur quelques titres et sites, la traîne s'allonge-t-elle, et quelle forme prend la distribution ? | Part du trafic des premiers sites, lois de puissance du trafic et des liens, concentration des ventes en tête, part des titres peu ou pas vendus, variété offerte. Test de l'hypothèse H7. |

### G. Politique et gouvernance
<!-- Lines 166-178 -->

G1 à G3 sont **gelées** : pas de nouvelle collecte, narratifs roulés en une ligne. L'effort porte sur la géopolitique, G4 à G6 (décision D18).
<!-- Lines 154-161 -->

| Code | Sous-dimension | Question | Types d'indicateurs |
| --- | --- | --- | --- |
| G1 | Droit et régulation (gelée, D18) | Quelles lois, décisions et régulateurs apparaissent, avec quel retard sur les usages ? | Textes de loi, jurisprudence, création de régulateurs, fiscalité, responsabilité des intermédiaires, protection des données, concurrence. |
| G2 | Gouvernance de la technologie (gelée, D18) | Qui gouverne les standards et les ressources communes : États, instances multi-acteurs, entreprises ? | Instances de normalisation, gouvernance des ressources partagées, standards de fait contre standards négociés, fondations. |
| G3 | État, services publics et vie démocratique (gelée, D18) | Comment l'État se sert de la technologie et comment la vie démocratique en est-elle changée ? | Administration en ligne, marchés publics, campagnes et communication politique, mobilisations, transparence, sphère publique. |
| G4 | Géopolitique, souveraineté et sécurité | Comment les rapports entre puissances, la souveraineté et la sécurité sont-ils modifiés ? | Domination et dépendances, réponses des blocs, fracture entre pays, cybersécurité, surveillance, localisation des données, stratégies nationales. |
| G5 | Domination d'infrastructure et ressources critiques | Quelle puissance contrôle l'infrastructure et les ressources critiques du réseau, et quelles dépendances en résultent ? | Localisation des serveurs racine, tutelle des ressources de nommage, propriété des câbles, routes du trafic international, origine des grands services utilisés par bloc. |
| G6 | Fracture entre pays et diplomatie du développement | Comment l'écart d'accès entre pays évolue-t-il, et quelles initiatives multilatérales y répondent ? | Internautes par région et par niveau de revenu, sommets et chartes multilatéraux, programmes d'aide à l'équipement. |

### H. Énergie
<!-- Lines 181-190 -->

| Code | Sous-dimension | Question | Types d'indicateurs |
| --- | --- | --- | --- |
| H1 | Consommation et efficacité de l'appareil numérique | Combien d'énergie consomment réseaux, terminaux et centres de données, et à quel rythme l'efficacité par unité de service progresse-t-elle ? | Térawattheures et part de l'électricité nationale, consommation des centres de données, efficacité énergétique des installations, énergie par unité de calcul ou de trafic, écart entre affirmations publiques et mesures. |
| H2 | Énergie comme contrainte et facteur de localisation | Où et pourquoi les usines s'installent-elles ; l'accès à l'électricité borne-t-il la croissance ? | Implantations et leurs motifs (hydroélectricité, climat, prix), raccordements, contrats d'achat d'électricité, prix de l'électricité par région, épisodes de pénurie. |
| H3 | Contexte énergétique macro : prix, mix, abondance | Dans quel environnement énergétique le choc se déploie-t-il, et cet environnement change-t-il pendant la fenêtre ? | Prix du pétrole, du gaz, de l'électricité ; mix de production ; coût des renouvelables ; intensité énergétique du PIB ; chocs et contre-chocs énergétiques. |
| H4 | Effets du choc sur l'énergie du reste de l'économie | Le choc réduit-il ou déplace-t-il la consommation d'énergie des autres activités ? | Dématérialisation (papier, supports physiques), déplacements évités ou induits, commerce en ligne contre commerce physique, efficacité permise par l'informatique, effets rebond. |

---

## Frontières entre domaines voisins
<!-- Lines 193-218 -->

| Frontière | Règle | Exemple |
| --- | --- | --- |
| A3 / C5 | A3 décrit **qui existe** dans le secteur technologique et comment il s'intègre ; C5 mesure la **concentration comme résultat de marché** et la réponse antitrust. | La naissance d'une offre de calcul à la demande est A3 ; la part de marché de son fournisseur dix ans plus tard et l'enquête qu'elle déclenche sont C5. |
| A4 / C4 | A4 est le **coût et la manière de produire** ; C4 est la **manière de facturer et de capter la valeur**. | Le passage à la location de capacité est A4 ; le paiement à l'usage comme modèle de revenu est C4. |
| A5 / E3, F1 | A5 est le **côté producteur** d'un secteur (revenus, structure, intermédiaires) ; E3 et F1 sont le **côté usager et culturel**. | La chute des revenus de la presse est A5 ; le passage des lecteurs à l'actualité en ligne est E4 ; la crise de confiance dans les médias est F1. |
| B / C | B est le **capital et son allocation** ; C est l'**économie réelle**. | Une vague d'introductions en bourse est B1 ; la productivité qu'elle finance ou non est C1. |
| B / A5, A8 | Le **secteur financier comme industrie** est A5 (structure) et A8 (services offerts, banque et courtage en ligne) ; B ne traite que du capital finançant le choc. | |
| A6 / C4 | C4 garde la **mesure agrégée du commerce de détail** et les modèles de revenu ; A6 mesure le **canal de vente par secteur et entre entreprises**. | La part du détail en ligne dans les ventes au détail est C4 ; la part des expéditions manufacturières en ligne est A6. |
| A8 / E3 | A8 = le service **offert** par le producteur ; E3 = son **adoption** par les ménages. | Les banques dotées d'un site transactionnel sont A8 ; la part des internautes qui font de la banque en ligne est E3. |
| B5 / G1 | B5 = **régulation des marchés financiers** et du cycle du capital ; G1 = droit du réseau (intermédiaires, données, droit d'auteur). | La loi Sarbanes-Oxley est B5 ; la responsabilité des hébergeurs est G1. |
| C6 / D4 | D4 = **salaires et part du travail** ; C6 = **répartition entre firmes, territoires et ménages**, revenus du capital inclus. | |
| D / E | D = la personne **au travail** ; E = la personne **hors travail**. La frontière domicile-travail elle-même est E5 avec D3 en secondaire. | |
| E / F | E = **individuel, pratique, mesurable en usage et en temps** ; F = **collectif, symbolique, normatif**. | Le temps passé en ligne est E5 ; ce qu'on pense que la vie privée devrait être est F3. |
| F3 / G1 | F3 = **normes sociales** ; G1 = **normes juridiques**. Une norme sociale qui devient loi produit deux faits liés. | |
| G2 / A2 | A2 = **quels standards** se sont imposés ; G2 = **qui décide** et par quel processus. | |
| G2 / G5 | G2 = le **processus de décision** sur les standards et ressources communes ; G5 = la **dépendance entre puissances** qui en résulte. | La constitution de l'entité de nommage est G2 ; la part des serveurs racine situés dans un seul pays est G5. |
| G4 / G5, G6 | G4 = **souveraineté, sécurité, conflits** ; G5 = **contrôle de l'infrastructure** ; G6 = **écart d'accès entre pays**. Les faits G4 antérieurs à D18 gardent leur identifiant et sont cités depuis G5 ou G6 quand leur objet y appartient. | |
| F4 / F5 | F4 = communautés, identités, langues, globalisation culturelle **par bloc** ; F5 = **forme de la distribution** des consommations et de l'attention. | |
| H1 / A1 | A1 = **ce qui est construit** et son capex ; H1 = **ce que cela consomme** et l'efficacité par unité de service. | L'ouverture d'un centre de données est A1 ; sa consommation et son efficacité sont H1. |
| H2 / A1, G4 | H2 = l'énergie comme **motif d'implantation et contrainte** ; A1 = la capacité ; G4 = la souveraineté. | Une implantation choisie pour l'hydroélectricité est H2 ; choisie pour la localisation des données, G4. |
| H3 / C2 | C2 = **prix et investissement des TIC** ; H3 = **prix et mix de l'énergie** comme contexte. | La baisse du prix du calcul est C2 (avec X.CLD.10) ; la baisse du prix du gaz est H3. |
| H4 / E3, E5 | E = **l'usage** ; H4 = **la conséquence énergétique** de l'usage. | L'achat en ligne est E3 ; le bilan énergétique de la livraison contre le déplacement en magasin est H4. |

---

## Couverture attendue par choc
<!-- Lines 221-234 -->

Rappel : les mêmes sous-dimensions servent pour les deux chocs. On s'attend à des cellules
riches et des cellules pauvres ; les cellules pauvres sont documentées comme telles.

| Domaine | Internet 1995-2005 | Cloud 2005-2015 |
| --- | --- | --- |
| A Industrie | Riche (réseaux, navigateurs, secteur naissant, désintermédiation) | **Très riche**, analogue primaire |
| B Finance | **Très riche** (bulle, krach, refinancement) | Moyenne (crise exogène de 2008, puis abondance de capital) |
| C Économie | **Riche**, analogue primaire | Moyenne à riche (déflation du calcul, modèles à l'usage) |
| D Travail | Riche | Moyenne (métiers de l'informatique très touchés, reste diffus) |
| E Vie quotidienne | **Très riche**, analogue primaire | Moyenne ; le grand public vit le cloud à travers ses produits dérivés (mobile, services en ligne), voir X.CLD.01 ; poids limité dans le choc |
| F Culture | **Très riche**, analogue primaire | Pauvre à moyenne ; la pauvreté est un résultat |
| G Politique | Riche | Moyenne à riche (données, surveillance, souveraineté) |
| H Énergie | Moyenne : ère de l'énergie bon marché, affirmations publiques sur la consommation du réseau contre mesures, crise électrique locale | **Riche** : les usines sont des convertisseurs d'électricité ; l'énergie devient contrainte d'implantation, métrique d'efficacité et sujet politique |
