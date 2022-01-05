# Test Technique Serveurcom Telecom

## Préambule

L'objectif de ce test est de développer une application Django en respectant les objectifs suivants:
- Utiliser Django 2.1
- Coder en Python 3
- Utiliser les bonnes pratiques de Django et de DRF
- Coder le moins de lignes possible

Cela nous permettra d'évaluer ton degré de compréhension d'une spécification, ta capacité à lire et interpréter la documentation, et la rigueur et la qualité de ton code. Bien entendu, ton niveau d'expérience sur Django/DRF sera pris en compte !

Envoie nous un mail quand le projet te semble terminé ou prêt à être relu. Il n'existe pas de solution unique ou ni de *bonne* réponse, ta capacité à trouver des solutions et à interpréter les consignes fait partie de l'exercice.

L'utilisation de git est conseillée. Tu peux nous transmettre l'URL de ton repo Bitbucket/gitlab (repo privé), ou une archive du résultat. *Merci de respecter la confidentialité de ce test et ne pas le diffuser*.


## Consignes

L'objectif est de développer une suite de webservices utilisés par un bar au Mans.
Ce bar référence plusieurs types de bières. Il dispose de plusieurs comptoirs qui ont chacun leur propre stock de pintes disponibles.
Une carte permet de connaitre les références disponible sur tout le bar ou sur un comptoir en particulier.
Les clients (utilisateurs anonymes) peuvent commander et le personnel (utilisateurs authentifiés) peut gérer les références et le stock.


### Les references

L'endpoint `/api/references/` permet de lister les références de bières (qu'elles soient en stock ou non).

```
[
    {
        "ref": "leffeblonde",
        "name": "Leffe blonde",
        "description": "Une bière blonde d'abbaye brassée depuis 1240 et que l'on ne présente plus !"
    },
    {
        "ref": "brewdogipa",
        "name": "Brewdog Punk IPA",
        "description": "La Punk IPA est une bière écossaise s'inspirant des tendances américaines en matière de brassage et du choix des houblons."
    },
   {
        "ref": "fullerindiapale",
        "name": "Fuller's India Pale Ale",
        "description": "Brassée pour l'export, la Fuller's India Pale Ale est la vitrine du savoir faire bien « british » de cette brasserie historique. "
    },
]
```

Les utilisateurs non connectés ne peuvent pas accéder à cet endpoint.
Les utilisateurs connectés peuvent seulement le consulter.
Les utilisateurs `staff` peuvent modifier les références (toute suppression doit automatiquement supprimer les stocks décrits plus bas).

Attention, les primary keys des références ne doivent pas être exposées par l'API.

*Optionnel : Il faut pouvoir trier, filtrer et paginer les résultats.*


### Les comptoirs du bar

L'endpoint `/api/bars/` renvoie la liste des comptoirs présents dans le bar (minimum 2).

```
[
    {
        "pk" : 1,
        "name": "1er étage"

   },
   {
        "pk" : 2,
        "name": "2ème étage"
   }
]
```

Seuls les utilisateurs connectés ont le droit d'accéder à cet endpoint.
Seul un utilisateur staff peut ajouter, modifier ou supprimer des entrées via cet endpoint.

*Optionnel : Il faut pouvoir trier, filtrer et paginer les résultats.*

### Les stocks

Il convient donc de modéliser un *stock* qui permet de connaitre le nombre de référence disponibles pour chaque comptoir.

L'endpoint `/api/stock/{ID_COMPTOIR}/` permet de lister les références disponibles dans le stock d'un comptoir et leurs quantités.

```
[
    {
        "ref": "leffeblonde",
        "name": "Leffe blonde",
        "description": "Une bière blonde d'abbaye brassée depuis 1240 et que l'on ne présente plus !"
        "stock": 10,
    },
    {
        "ref": "brewdogipa",
        "name": "Brewdog Punk IPA",
        "description": "La Punk IPA est une bière écossaise s'inspirant des tendances américaines en matière de brassage et du choix des houblons."
        "stock": 5,
    },
    {
        "ref": "fullerindiapale",
        "name": "Fuller's India Pale Ale",
        "description": "Brassée pour l'export, la Fuller's India Pale Ale est la vitrine du savoir faire bien « british » de cette brasserie historique. "
        "stock": 0,
    }
]
```

Seuls les utilisateurs connectés ont le droit d'accéder à cet endpoint.

*Optionnel : Il faut pouvoir trier, filtrer et paginer les résultats.*

### Classer les comptoirs

Il est nécessaire de fournir au responsable du bar des informations sur les comptoirs. L'endpoint `/api/bars/ranking/` permet de lister les bars en fonction de leurs caractéristiques.

Les caractéristiques attendues sont :
- all_stocks
- miss_at_least_one


```
[
    {
        "name": "all_stocks",
        "description": "Liste des comptoirs qui ont toutes les références en stock",
        "bars": [1]

   },
   {
        "name" : "miss_at_least_one",
        "description": "Liste des comptoirs qui ont au moins une référence épuisée",
        "bars": [2]
   }
]
```

Seuls les utilisateurs connectés ont le droit d'accéder à cet endpoint.

### Le menu

L'endpoint `/api/menu/` doit renvoyer la liste de toutes les références de bières du Bar et préciser pour chaque référence si elle est en stock dans un des comptoirs ou si elle est épuisée.

```
[
    {
        "ref": "leffeblonde",
        "name": "Leffe blonde",
        "description": "Une bière blonde d'abbaye brassée depuis 1240 et que l'on ne présente plus !"
        "availability": "available"
    },
    {
        "ref": "brewdogipa",
        "name": "Brewdog Punk IPA",
        "description": "La Punk IPA est une bière écossaise s'inspirant des tendances américaines en matière de brassage et du choix des houblons."
        "availability": "available"
    },
   {
        "ref": "fullerindiapale",
        "name": "Fuller's India Pale Ale",
        "description": "Brassée pour l'export, la Fuller's India Pale Ale est la vitrine du savoir faire bien « british » de cette brasserie historique."
        "availability": "outofstock"
    }
]
```

Les utilisateurs peuvent y accéder de façon anonyme. Aucune modification n'est possible depuis cet endpoint.

*Optionnel : Il faut pouvoir trier, filtrer et paginer les résultats.*
*Optionnel : Ajouter des paramètres GET pour :*
- *préciser un comptoir et donc avoir des résultats de disponibilité différents puisque chaque bar a son propre stock*
- *préciser que l'on veut seulement voir les références qui sont en stock*


### Les commandes


L'endpoint `/api/order/{ID_COMPTOIR}/` permet de commander des bières à un comptoir donné en faisant un `POST` avec le payload suivant :

```
{
    "items": [
        {
            "ref": "brewdogipa"
        },
        {
            "ref": "brewdogipa"
        },
        {
            "ref": "fullerindiapale"
        },
        {
            "ref": "leffeblonde"
        }
    ]
}
```

Une entrée dans la table `Orders` doit être créé et `n` entrées dans la table `OrderItems` doivent être créées.
Chaque création dans la table `OrderItems` doit diminuer le comptage du stock du comptoir pour la référence.

Chaque mise à jour du compteur de stock doit déclencher un signal si le stock descend en dessous de 2 pour permettre un réapprovisionnement.

Seuls les utilisateurs anonymes peuvent commander.

Le résultat de cet appel doit être un order serializé sous la forme suivante :

```
{
    "pk": 1,
    "items": [
        {
            "ref": "brewdogipa",
            "name": "Brewdog Punk IPA",
            "description": "La Punk IPA est une bière écossaise s'inspirant des tendances américaines en matière de brassage et du choix des houblons."
        },
        {
            "ref": "brewdogipa",
            "name": "Brewdog Punk IPA",
            "description": "La Punk IPA est une bière écossaise s'inspirant des tendances américaines en matière de brassage et du choix des houblons."
        },
        {
            "ref": "fullerindiapale",
            "name": "Fuller's India Pale Ale",
            "description": "Brassée pour l'export, la Fuller's India Pale Ale est la vitrine du savoir faire bien « british » de cette brasserie historique. "
        },
        {
            "ref": "leffeblonde",
            "name": "Leffe blonde",
            "description": "Une bière blonde d'abbaye brassée depuis 1240 et que l'on ne présente plus !"
        }
    ]
}
```

Si l'utilisateur est connecté, un `GET` sur le endpoint `/api/orders/` permet de lister les commandes et un `GET` sur le endpoint `/api/order/{PK}/` permet de récupérer une commande en particulier.

### Le meilleur comptoir

Il faut ajouter une nouvelle caractéristique dans l'endpoint `/api/orders/bars/ranking/` permettant d'identifier le comptoir qui a vendu le plus de bières : 

```
[
   ...,
   {
        "name": "most_pints",
        "description": "Liste le comptoir avec le plus de pintes commandées",
        "bars": [1]
   }
]
```

## Pour finir

Pour permettre de se servir de cette application, il faut ajouter des fixtures que l'on peut charger pour bootstraper l'application (utilisateurs, bars, references, stocks).

*Optionnel : Gestion des permissions par utilisateur.*

Bien sûr, des tests utilisant les fixtures sont attendus pour valider le fonctionnement de l'application.

Bon test !
