================
Manuel de Pythot
================

Présentation
============

Le logiciel **Pythot** est un programme de calcul littéral traitant des équations du
premier degré à une inconnue (classe de quatrième du collège), son objectif est d'aider à
la compréhension des techniques de résolution : en se chargeant de l'aspect purement
calculatoire, il permet à l'utilisateur de se focaliser sur la démarche de résolution de
l'équation.

La méthode classique ici retenue est celle basée sur l'image de la balance à l'équilibre :
à partir d'une équation donnée, il est possible de réaliser sur celle-ci un ensemble
d'opérations qui laissent les solutions inchangées.

Le nom du programme est celui du dieu égyptien **Thot** en charge des Mathématiques qui
était également le garant de la justesse de la balance lors de la pesée des âmes.

Types d'erreurs
===============

Les erreurs fréquentes sont les suivantes :

**Le bouton Valider d'une fenêtre est inactif**
    L'équation ou l'opération proposée est incorrecte (le coefficient n'est pas un nombre
    valide, on tente une division par zéro…), on peut obtenir des renseignements sur le
    type d'erreur en déplaçant le curseur sur le bouton.

**L'affichage des nombres ne fonctionne pas**
    Le programme affiche des nombres avec cinq chiffres maximum, si le nombre de chiffres
    est supérieur à cinq il affiche trois points de suspension. Dans le cas d'un
    dépassement des capacités de calcul, le programme affiche le signe tilde.

**L'ouverture d'un fichier équation échoue**
    Le fichier n'est pas du type équation ou il a été modifié manuellement de manière
    incorrecte, dans ce dernier cas le programme indique la ligne à laquelle la première
    erreur est rencontrée.

Version du programme
====================

La **version 1.0.3** du programme **Pythot** est écrite en Python 3 et utilise PyQt.

Elle est basée sur le logiciel Thot d'Emmanuel Morand : http://www.emmanuelmorand.net

Le code source est disponible sur GitHub : https://github.com/christophe-riolo/pythot/

Zone de travail
===============

La **zone de travail** affiche les différentes étapes de résolution de l'équation, y
compris les opérations effectuées.  Les lignes sous forme résolue sont signalées par la
présence sur leur droite de l'icône du programme, le type de l'ensemble des solutions est
signalé lorsque l'on déplace le curseur de la souris sur celle-ci.

L'affichage comporte deux modes possibles : le **mode fraction** ou le **mode décimal**,
le mode en cours est affiché dans la barre d'état.

La taille d'affichage peut être modifiée à l'aide des boutons *Agrandir* et *Réduire* de
la première barre d'outils horizontale, elle est affichée dans la barre d'état.

Fichiers équation
=================

Le programme Thot permet de sauvegarder le travail en cours sous la forme d'un **fichier
équation** dont l'extension associée est **.tht**. Les fichiers de ce type doivent être
ouverts à partir du programme.

Barre d'état
============

La **barre d'état** indique le **mode d'affichage** (mode fraction ou mode décimal) et la
**taille d'affichage**.

Première barre d'outils horizontale
===================================

Les commandes respectives de la première barre d'outils horizontale (et les touches de
raccourci associées) sont les suivantes :

Le bouton **Ouvrir (Ctrl O)**
    Il permet d'ouvrir un fichier équation.

Le bouton **Sauvegarder (Ctrl S)**
    Il permet de sauvegarder un fichier équation.

Le bouton **Nouvelle équation (Ctrl N)**
    Il permet d'ouvrir la boîte de dialogue « Saisie de l'équation ».

Le bouton **Equation au hasard (Ctrl H)**
    Il permet d'afficher une nouvelle équation générée de manière aléatoire (elle est à
    coefficients entiers et admet une solution unique).

Le bouton **Effacer l'équation (Ctrl E)**
    Il permet d'effacer l'équation en cours.

Le bouton **Mode fraction (Ctrl Q)**
    Il permet d'imposer un affichage numérique de type fraction dans la zone de travail,
    c'est le mode par défaut.

Le bouton **Mode décimal (Ctrl D)**
    Il permet d'imposer un affichage numérique de type décimal (quand le nombre considéré
    est décimal !).

Le bouton **Agrandir (Ctrl +)**
    Il permet d'augmenter la taille d'affichage dans la zone de travail.

Le bouton **Réduire (Ctrl -)**
    Il permet de réduire la taille d'affichage dans la zone de travail.

Le bouton **Aide (F1)**
    Il permet d'activer le fichier d'aide du programme.

Le bouton **A propos** 
    Il permet d'ouvrir la boîte de dialogue « À propos … » du programme.

Deuxième barre d'outils horizontale
===================================

Les commandes respectives de la deuxième barre d'outils horizontale (et les touches de
raccourci associées) sont les suivantes :

Le bouton **Ajouter un nombre (+)**
    Il permet d'ajouter un même nombre dans les deux membres de la ligne courante, sa
    valeur doit être saisie dans la boîte de dialogue « Choix d'une opération ».

Le bouton **Soustraire un nombre (-)**
    Il permet de soustraire un même nombre dans les deux membres de la ligne courante, sa
    valeur doit être saisie dans la boîte de dialogue « Choix d'une opération ».

Le bouton **Ajouter un terme en x (P)**
    Il permet d'ajouter un même terme en x dans les deux membres de la ligne courante, sa
    valeur doit être saisie dans la boîte de dialogue « Choix d'une opération ».

Le bouton **Soustraire un terme en x (M)**
    Il permet de soustraire un même terme en x dans les deux membres de la ligne courante,
    sa valeur doit être saisie dans la boîte de dialogue « Choix d'une opération ».

Le bouton **Multiplier (*)**
    Il permet de multiplier par un même nombre les deux membres de la ligne courante, sa
    valeur doit être saisie dans la boîte de dialogue « Choix d'une opération ».

Le bouton **Diviser (/)**
    Il permet de diviser par un même nombre les deux membres de la ligne courante, sa
    valeur doit être saisie dans la boîte de dialogue « Choix d'une opération ».

Le bouton **Intervertir les deux membres (I)**
    Il permet d'intervertir les deux membres de la ligne courante.

Le bouton **Prendre l'opposé (O)**
    Il permet de prendre l'opposé de la ligne courante.

Le bouton **Annuler (Suppr)**
    Il permet d'annuler la dernière opération réalisée.

Utilisation au moyen de la souris
=================================

Le logiciel peut être utilisé entièrement au moyen de la souris (ce qui permet son
utilisation facile sur un tableau interactif), les différents boutons s'actionnent au
moyen d'un clic gauche, les boîtes de saisie s'activent par un clic gauche et leur contenu
peut être modifié à l'aide du pavé numérique virtuel.

Utilisation au moyen du clavier
===============================

Le logiciel peut être utilisé au moyen du clavier, les flèches directionnelles permettent
de passer d'un contrôle (bouton, boîte de saisie…) à un autre à l'intérieur d'une fenêtre,
le contrôle focalisé apparaît encadré en marron, on actionne celui-ci en appuyant sur la
touche entrée. Le contenu des boîtes de saisie peut être modifié à l'aide du pavé
numérique, des touches Suppr et Tab ainsi que des flèches directionnelles.

Les touches début et fin de paragraphe permettent d'actionner la barre de défilement
associée à la zone de travail (équivalent de la molette de la souris).

Les touches de raccourci sont détaillées dans les rubriques **Première et Deuxième barres
d'outils horizontales**.
