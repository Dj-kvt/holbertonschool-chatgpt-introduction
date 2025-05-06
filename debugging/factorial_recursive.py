#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calcule le factoriel d'un entier n de manière récursive.

    Paramètres:
        n (int): Un entier naturel dont on veut calculer le factoriel.
                 Le factoriel de 0 est défini comme 1.

    Retourne:
        int: Le résultat de n! (n factoriel)
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Récupère le premier argument en ligne de commande, le convertit en entier
f = factorial(int(sys.argv[1]))

# Affiche le résultat du factoriel
print(f)
