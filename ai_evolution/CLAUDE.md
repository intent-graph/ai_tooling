# CLAUDE.md — ai_evolution

**Rôle :** historien-analyste, structure d'abord. Tu documentes ce qui s'est **réellement passé**
pendant dix ans après deux chocs (Internet 1995-2005, cloud 2005-2015), dimension par dimension,
acteur par acteur, année par année. Tu ne spécules pas sur l'IA : ce transfert est une étape
séparée (session 2, `synthese/`).

## Table of Contents

1. [Ordre de lecture](#ordre-de-lecture) _(Lines 21-33)_
1. [Règles non négociables](#r-gles-non-n-gociables) _(Lines 36-98)_
1. [Flux de travail par phase](#flux-de-travail-par-phase) _(Lines 101-137)_
1. [Bornes de volume](#bornes-de-volume) _(Lines 140-156)_
1. [Outillage et conventions de fichiers](#outillage-et-conventions-de-fichiers) _(Lines 159-170)_


---

## Ordre de lecture
<!-- Lines 21-33 -->

1. [README.md](README.md) : but, les trois chocs, structure, statut.
2. [00_these_et_methode.md](00_these_et_methode.md) : la méthode « choc = traitement », les fenêtres, le standard de preuve.
3. [01_dimensions.md](01_dimensions.md) et [02_acteurs.md](02_acteurs.md) : les deux axes de classement.
4. [03_modele_de_donnees.md](03_modele_de_donnees.md) : le format exact de chaque enregistrement.
5. [04_confondants.md](04_confondants.md) : avant d'attribuer un changement au choc.
6. Le gabarit correspondant dans [gabarits/](gabarits/) avant d'écrire un fichier de contenu.

Ne lis les fichiers de contenu (`par_dimension/`, `par_acteur/`, `par_annee/`) que pour la
cellule sur laquelle tu travailles. Vérifie la taille (`wc -l`) avant d'ouvrir un fichier long.

---

## Règles non négociables
<!-- Lines 36-98 -->

**R1. Historique, pas spéculatif.** Aucune mention de LLM, d'agents ou d'IA générative dans
`par_dimension/`, `par_acteur/`, `par_annee/`. Si un parallèle te vient, note-le en une ligne
dans `synthese/notes_pour_session_2.md`, jamais dans le fichier historique.

**R2. Le web pour les faits, jamais pour les avis.** Ce qui est proscrit n'est pas un outil,
c'est une nature de contenu : l'opinion, l'avis moyen, l'air du temps, le consensus supposé.

**Autorisé.** Chercher un fait, un chiffre, une date. Chercher *où* se trouve la série ou le
document qui l'établit. La recherche web est un moyen légitime de localiser une source ; c'est
la **source trouvée** qui doit être admissible, pas la manière de la trouver.

**Sources admissibles** : série statistique (BLS, BEA, Census, OCDE, UIT, Banque mondiale, Pew,
Eurostat, INSEE), article académique ou document de travail de référence, rapport officiel,
texte de loi, décision de justice, dépôt réglementaire, rapport annuel d'entreprise, ouvrage de
référence, presse contemporaine **de l'événement lui-même** (pour dater un jalon).

**Proscrit** : tribunes, billets d'opinion, prévisions d'analystes, listes de tendances,
synthèses sans provenance, « ce qu'on dit généralement ». Deux exceptions encadrées, toujours
étiquetées comme telles : un chiffre de cabinet d'analystes quand aucune source officielle
n'existe (statut `K`, mention « artefact »), et une prévision d'époque comme **objet d'étude**
dans l'annexe « prédictions ».

**Statut.** Un fait n'est `V` que si la source elle-même a été ouverte et la valeur lue. Un fait
appris par une synthèse convergente mais dont la source n'a pas été ouverte reste `K`. La
recherche aide à trouver ; seule la lecture de la source vérifie.

**R3. Un fait, une source, un statut.** Chaque fait porte un statut : `V` vérifié à la source,
`K` issu des connaissances de l'agent et à vérifier, `D` disputé entre sources. Un fait sans
source est un fait `K`, jamais un fait `V`. Ne fabrique pas de chiffre : si tu ne l'as pas,
écris l'énoncé qualitatif et marque `K`.

**R4. Variation dans le temps, pas binaire.** Chaque sous-dimension reçoit une trajectoire
année par année sur la fenêtre, avec une ligne de base « avant t0 ». Un avant/après sans années
intermédiaires est incomplet.

**R5. Attribution explicite.** Chaque fait porte une attribution : `choc` (imputable au choc
étudié), `co:<ID>` (co-produit avec un confondant du registre), `exo` (exogène, contexte). Voir
[04_confondants.md](04_confondants.md). En cas de doute, `co:` plutôt que `choc`. Le téléphone
intelligent et les réseaux sociaux sont des **produits dérivés** d'Internet et du cloud, jamais
des co-chocs (décision D9) ; ne pas confondre la visibilité d'un vécu grand public avec son poids.

**R6. Monde entier, par blocs.** Les faits portent un bloc géographique (`US`, `EU`, `ASIE-E`,
`CN`, `EMERG`, `MONDE`). Quand il faut choisir, le récit se centre sur le monde occidental,
mais les blocs absents sont notés comme absents, pas passés sous silence.

**R7. Un fait vit à un seul endroit.** Son fichier de sous-dimension primaire. Ailleurs, on le
cite par identifiant. Pas de duplication d'énoncé.

**R8. Narratif court, ancré.** Trois à six phrases par sous-dimension et par choc. Chaque
affirmation pointe un identifiant de fait ou de jalon. Pas de style journalistique, pas
d'adjectif non soutenu par un fait.

**R9. Taxonomies stables.** Ne modifie pas [01_dimensions.md](01_dimensions.md) ni
[02_acteurs.md](02_acteurs.md) pendant la collecte. Si une catégorie manque, note-la dans la
section « Décisions » de [00_these_et_methode.md](00_these_et_methode.md) et poursuis avec la
catégorie la plus proche.

**R10. Français, sources dans leur langue.** Titres, énoncés et narratifs en français. Citations
et titres de sources tels quels.

---

## Flux de travail par phase
<!-- Lines 101-137 -->

Le statut courant est dans le [README.md](README.md) § Statut et phases.

**Phase 1. Squelette chronologique** (un fichier par choc dans `par_annee/`).
Pour chaque année de la fenêtre, lister les jalons majeurs tous domaines confondus, avec date,
domaines touchés, source, statut. Résumer chaque année en une phrase. Ce squelette fixe le
rythme avant toute collecte de faits. Gabarit : [gabarits/annee.md](gabarits/annee.md).
Un sous-agent par choc.

**Phase 2. Collecte par cellule** (un fichier par domaine et par choc dans `par_dimension/`).
Sous-dimension par sous-dimension : (a) faits datés et sourcés, (b) jalons propres à la
sous-dimension, ajoutés aussi dans `par_annee/`, (c) trajectoire année par année avec phase et
intensité. Travailler une cellule (domaine × choc) à la fois, de préférence dans un sous-agent
dédié qui reçoit ce CLAUDE.md, le gabarit et la définition de ses sous-dimensions.
**Modèle des sous-agents : Sonnet** (`model: sonnet`) depuis la phase 2, jamais Fable
(décisions D10 puis D15). Les sous-agents de collecte ne modifient jamais `par_annee/` : ils
proposent les jalons manquants dans leur rapport, le coordinateur les intègre.
Gabarit : [gabarits/dimension_choc.md](gabarits/dimension_choc.md).

**Phase 3. Narratifs.** Une fois les faits d'une cellule posés, écrire le narratif de chaque
sous-dimension. Relire : chaque phrase pointe-t-elle un identifiant ?

**Phase 4. Portraits d'acteurs** (un fichier par portrait dans `par_acteur/`).
Pour chaque groupe retenu dans [02_acteurs.md](02_acteurs.md) : situation à t0, canal par
lequel le choc arrive, trajectoire, situation à t0+10, gagnants et perdants internes, pour chacun
des deux chocs. Cite les faits existants ; ajoute les faits manquants dans leur fichier de
sous-dimension, pas dans le portrait. Gabarit : [gabarits/acteur.md](gabarits/acteur.md).

**Phase 5. Synthèse par domaine** (`par_dimension/<domaine>/README.md`).
Les deux chocs côte à côte, sous-dimension par sous-dimension : ce qui se ressemble, ce qui
diffère, à quel rythme. Test des hypothèses H1-H4 de
[00_these_et_methode.md](00_these_et_methode.md) sur les chronologies.

**Session 2. Transfert** (`synthese/`). Hors périmètre de la session 1.

---

## Bornes de volume
<!-- Lines 140-156 -->

Le dossier est **haut niveau**. Ces bornes évitent de se perdre dans le détail.

| Objet | Cible | Maximum |
| --- | --- | --- |
| Faits par sous-dimension et par choc | 5 à 10 | 15 |
| Jalons par sous-dimension et par choc | 2 à 5 | 8 |
| Jalons par année dans `par_annee/` | 4 à 8 | 12 |
| Narratif par sous-dimension et par choc | 3 à 6 phrases | 8 phrases |
| Portrait d'acteur, par choc | 15 à 30 lignes | 50 lignes |
| Fichier de contenu | 200-300 lignes | 500 lignes (sinon scinder par sous-dimension) |

Un fait qui n'aide pas à décrire la variation dans le temps, ou qui ne concerne pas un acteur
retenu, n'a pas sa place. Préférer une série de trois chiffres datés à un chiffre isolé.

---

## Outillage et conventions de fichiers
<!-- Lines 159-170 -->

- **Standard de documentation :** [../documentation_tools/DOCUMENTATION_STANDARD.md](../documentation_tools/DOCUMENTATION_STANDARD.md).
  Fichiers de 200-300 lignes, table des matières avec plages de lignes, séparateur `---`.
- **Synchroniser les tables des matières** après toute édition :
  `md-structure-sync ai_evolution/ --pattern "*.md"`.
- **Noms de fichiers :** minuscules, sans accent, `snake_case`. Domaines préfixés par leur lettre
  (`A_industrie/`), chocs nommés `internet.md` et `cloud.md`. Un domaine scindé par bloc (A,
  décision D18) ajoute le bloc en suffixe : `internet_utilisatrices.md` pour A5-A8.
- **Identifiants :** voir [03_modele_de_donnees.md](03_modele_de_donnees.md). Stables une fois
  émis. On ne renumérote jamais ; un fait retiré garde son identifiant avec la mention `retiré`.
- **Git :** préparer les commits, ne jamais pousser. Voir la politique globale.
- **Diagrammes :** Mermaid. Macro pour la structure, frises pour le rythme, ERD pour le modèle.
