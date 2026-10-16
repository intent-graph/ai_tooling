# Arbre des effets en quatre ordres — construction descendante

Statut : cadre posé par l'auteur ; arbres Internet et cloud en première génération. Vue
expérimentale, à côté des arbres précédents ([../internet/](../internet/README.md),
[../cloud.md](../cloud.md)), qu'elle ne modifie pas.

## Table of Contents

1. [Racine](#racine)
1. [Les quatre ordres](#les-quatre-ordres)
1. [Règles de construction](#r-gles-de-construction)
1. [Pratique du niveau de détail](#pratique-du-niveau-de-d-tail)
1. [Fichiers](#fichiers)

---

## Racine
<!-- Lines 19-27 -->

Posée par l'auteur : **les deux sont des chocs nets, qui agissent sur l'information,
l'industrie, les affaires et la gouvernance.**

C'est un cadre, pas encore une affirmation. L'énoncé de la racine de chaque arbre s'écrit en
dernier, comme ce que ses quatre branches additionnent.

---

## Les quatre ordres
<!-- Lines 30-46 -->

Le niveau 1 de chaque arbre compte exactement quatre boîtes. Chacune répond à une question sur
**ce qui change**.

| Boîte | Ordre | Question | Couvre, entre autres |
| --- | --- | --- | --- |
| .1 | **Information** | Ce que les gens peuvent savoir et dire | accès, s'écrire, publier, trouver, se divertir, le substrat partagé (tête et traîne) |
| .2 | **Industrie** | Comment on produit | infrastructure, outils et organisation de la production, travail, productivité, énergie |
| .3 | **Affaires** | Où va la valeur | capital et son cycle, rentes, marchés, modèles d'affaires, captation par les plateformes, surplus des usagers |
| .4 | **Gouvernance** | Qui fixe les règles | droit, régulation, souveraineté, rapports entre États, contrôle de l'entrée |

Ces quatre ordres regroupent à peu près les huit domaines du dossier (E et F ; A, D et H ; B
et C ; G). Ce n'est donc pas la couverture qui prouve le cadre : ce sont les énoncés de
niveau 2 et les flèches entre ordres.

---

## Règles de construction
<!-- Lines 49-73 -->

1. **Partition par ce qui change.** Un changement va dans l'ordre qui répond à sa question, pas
   dans celui de sa cause.
2. **Un événement se découpe en changements.** Un événement qui touche plusieurs ordres
   devient plusieurs feuilles, une par ordre, reliées par des flèches causales. Exemple :
   l'échange de musique entre pairs, c'est copier librement (Information), des revenus perdus
   par les maisons de disques (Affaires) et une réponse du droit (Gouvernance).
3. **Sous le niveau 1, la coupe est libre**, choisie par branche : par qui vit le changement
   par défaut, par mécanisme quand c'est plus net. Deux à six enfants par boîte.
4. **Les leviers du choc sont des changements comme les autres.** Ils se placent dans l'ordre
   qui leur répond : par exemple, « transmettre ne coûte presque plus rien » en Industrie (une
   infrastructure nouvelle), « personne ne filtre l'entrée » en Gouvernance. Les autres boîtes
   pointent vers eux par leurs flèches.
5. **Ce que le choc n'a pas causé reste dans l'arbre**, en feuille marquée : sa cause principale
   est un confondant du registre ([../../04_confondants.md](../../04_confondants.md)).
6. **Flèches et poids** : conventions de l'arbre précédent ([../README.md](../README.md)). Le
   poids dit ce qui disparaît sans la cause ; les poids d'une même boîte ne s'additionnent pas.
7. **Produits dérivés** (téléphone intelligent, réseaux sociaux, partage de vidéo, applications) :
   des effets du choc cloud (décisions D9 et D16), à placer dans l'arbre, souvent attribués avec
   le haut débit mobile (X.CLD.04).
8. **Couverture** : chaque fait actif du choc est cité par une feuille ou élagué avec une raison.
9. **Aucune mention de l'IA** (règle R1). Le transfert au choc IA viendra en session 2.

---

## Pratique du niveau de détail
<!-- Lines 76-86 -->

L'arbre est un exercice de niveau de détail
([../../../level_of_detail/LOD_CORE.md](../../../level_of_detail/LOD_CORE.md)) :

- chaque boîte énonce ce que ses enfants additionnent, avec sa propre certitude ;
- remonter d'un niveau est une compression avec perte, pas une coupe ;
- les hauteurs varient : une feuille à un fait peut côtoyer une boîte qui en roule vingt ;
- descendre n'invente jamais : un changement sans fait est noté ouvert, hors de l'arbre.

---

## Fichiers
<!-- Lines 89-96 -->

| dossier | contenu |
| --- | --- |
| [internet/](internet/README.md) | Internet 1995-2005 : racine et vue d'ensemble, puis un fichier par ordre |
| [cloud/](cloud/README.md) | Cloud 2005-2015 : même structure |

Vérification : `python3 verifier_arbre.py quatre_ordres/internet --check` (et `cloud`), lancé
depuis `arbre_des_effets/`.
