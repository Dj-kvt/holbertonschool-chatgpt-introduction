#!/usr/bin/python3
import sys

def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1  # Décrémenter n pour éviter une boucle infinie
    return result  # Retourner le résultat correctement

f = factorial(int(sys.argv[1]))  # Appeler la fonction factorial avec l'argument passé en ligne de commande
print(f)  # Afficher le résultat
