# Exiercice 00 — Lecture de code et prédictions (15 min) :
#  avant exécution, écrire les sorties des deux boucles.

# Exercice 01 — Billets (15 min) : demander une quantité entre 1 et 20 ;
# afficher une ligne par billet. Faire une vérification avec if.
# Demander la quantité de billets
# quantite = int(input("Entrez le nombre de billets (1 à 20) : "))

# # Vérifier la quantité avec if
# if 1 <= quantite and quantite <= 20:

#     # Afficher une ligne par billet

#     for i in range(1, quantite + 1):
#         print("Billet numéro", i)

# else:
#     print("Erreur : la quantité doit être entre 1 et 20.")

# Explication du jeux de données
# Premier jeu de données : quantité valide
# Entrée:
# Entrez le nombre de billets (1 à 20) : 4
# Sortie attendue:
# Billet numéro 1
# Billet numéro 2
# Billet numéro 3
# Billet numéro 4

# Deuxième jeu de données : quantité invalide
# Entrée:
# Entrez le nombre de billets (1 à 20) : 25
# Sortie attendue:
# Erreur : quantité invalide


#Exercice 02 — Panier (25 min) : demander le nombre d’articles puis leur prix,
# ignorer les prix négatifs, 
# afficher le total après remise de 10 % dès 100 $.

# Demander le nombre d'articles
# n = int(input("Entrez le nombre d'articles : "))
# Initialiser le total
# total = float(0)

# for i in range(n):
#     prix = float(input(f"Entrez le prix de l'article {i+1} : "))
# Saisir le prix de chaque article
#     if prix < 0:
#         print("Prix négatif ignoré")
#     else:
     
#      total += prix

# print("Total avant remise :", round(total, 2), "$")

# if total >= 100:
#     remise = total * 0.10
#     total = total - remise

#     print("Remise de 10 % :", round(remise, 2), "$")
# else:
#     print("Aucune remise appliquée")

# print("Total à payer :", round(total, 2), "$")

# Demander à l'utilisateur combien d'articles il souhaite acheter
# int() permet de convertir la saisie en nombre entier
# n = int(input("Entrez le nombre d'articles : "))

# Initialiser le total à 0
# float(0) représente un nombre décimal
# total = float(0)

# Répéter la saisie des prix selon le nombre d'articles
# range(n) permet de répéter la boucle n fois
# for i in range(n):

#     Demander le prix de chaque article
#     float() permet de saisir un prix décimal
#     i+1 permet de commencer la numérotation des articles à 1
#     prix = float(input(f"Entrez le prix de l'article {i+1} : "))

#     Vérifier si le prix est négatif
#     if prix < 0:
#         Si le prix est négatif, afficher un message
#         Le prix négatif ne sera pas ajouté au total
#         print("Prix négatif ignoré")
#     else:
#         Si le prix est positif ou égal à zéro, l'ajouter au total
#         total += prix signifie total = total + prix
#         total += prix

# Afficher le total des articles avant la remise
# round(total, 2) permet d'arrondir à deux décimales
# print("Total avant remise :", round(total, 2), "$")

# Vérifier si le total est supérieur ou égal à 100 $
# if total >= 100:

#     Calculer une remise de 10 % sur le total
#     0.10 représente 10 %
#     remise = total * 0.10

#     Soustraire le montant de la remise du total
#     total = total - remise

#     Afficher le montant de la remise
#     print("Remise de 10 % :", round(remise, 2), "$")

# else:
#     Si le total est inférieur à 100 $, aucune remise
#     print("Aucune remise")

# Afficher le montant final à payer après la remise éventuelle
# print("Total à payer après remise :", round(total, 2), "$")

# Deux jeux de données à exécuter

# Test 1 : Avec remise et prix négatif

# Entrez le nombre d'articles : 3
# Entrez le prix de l'article 1 : 50
# Entrez le prix de l'article 2 : -10
# Prix négatif ignoré
# Entrez le prix de l'article 3 : 70

# Total avant remise : 120.0 $
# Remise de 10 % : 12.0 $
# Total à payer : 108.0 $

# 03 — Cinq températures (25 min) : lire 5 valeurs sans les stocker ; 
# calculer moyenne, minimum et maximum via variables, compteur et conditions.

# Initialiser les variables
# moyenne = 0
# compteur = 0
# # Répéter la saisie 5 fois
# for i in range(5):
#     # Demander une température à l'utilisateur
#     temperature = float(input(f"Entrez la température {i+1} : "))
#     # Ajouter la température saisie à la moyenne
#     moyenne = moyenne + temperature
#     # Augmenter le compteur de 1
#     compteur = compteur + 1
#     # Pour la première température, initialiser le minimum et le maximum
#     if compteur == 1:
#         minimum = temperature
#         maximum = temperature
#     # Pour les températures suivantes, comparer les valeurs
#     else:
#         # Si la température est inférieure au minimum actuel
#         if temperature < minimum:
#             minimum = temperature
#         # Si la température est supérieure au maximum actuel
#         if temperature > maximum:
#             maximum = temperature

# # Calculer la moyenne des 5 températures
# moyenne = moyenne / compteur
# # Afficher les résultats
# print("Moyenne :", round(moyenne, 2), "°C")
# print("Minimum :", minimum, "°C")
# print("Maximum :", maximum, "°C")

# Test 1 : Températures positives
# Valeurs saisies : 10, 15, 20, 25, 30
# Moyenne : 20.0 °C
# Minimum : 10.0 °C
# Maximum : 30.0 °C

# Test 2 : Températures négatives et positives
# Valeurs saisies : -5, 0, 10, -2, 7
# Moyenne : 2.0 °C
# Minimum : -5.0 °C
# Maximum : 10.0 °C


# 04 — Code PIN (20 min) : utiliser while avec un maximum de 3 essais, 
# indiquer le nombre d’essais restants.

# Définir le code PIN correct
#code_pin = "1234"
# Initialiser le nombre de tentatives autorisées
#essai_restants = 3
# Répéter la saisie tant qu'il reste des tentatives
# while essais_restants > 0:
#     # Demander à l'utilisateur de saisir son code PIN
#     pin_saisi = input("Entrez le code PIN : ")
#     # Vérifier si le code saisi correspond au code PIN correct
#     if pin_saisi == code_pin:
#         # Afficher un message si le code est correct
#         print("Code PIN correct")
#         # Arrêter la boucle si le code PIN est correct
#         break
#     else:
#         # Diminuer le nombre de tentatives de 1
#         essais_restants = essais_restants - 1
#         # Afficher le nombre de tentatives restantes
#         print("Code PIN incorrect. Essais restants :", essais_restants)
# # Vérifier si toutes les tentatives sont épuisées
# if essais_restants == 0:
#     # Bloquer l'accès après 3 tentatives incorrectes
#     print("Accès bloqué.")

# Test 1 : Code PIN correct
# Entrez le code PIN : 1234
# Code PIN correct
# Le programme s'arrête immédiatement.

# Test 2 : Trois codes incorrects
# Entrez le code PIN : 1111
# Code PIN incorrect. Essais restants : 2
# Entrez le code PIN : 2222
# Code PIN incorrect. Essais restants : 1
# Entrez le code PIN : 3333
# Code PIN incorrect. Essais restants : 0

# Accès bloqué.

# 05 — Épargne (20 min) : calculer le nombre de mois nécessaires
#    à l’atteinte d’un objectif avec versement constant ;
#   valider les entrées.

# Demander les montants
# objectif = float(input("Entrez votre objectif d'épargne ($) : "))
# versement = float(input("Entrez votre versement mensuel ($) : "))
# # Initialiser les variables
# mois = 0
# total = 0
# # Vérifier que les montants sont positifs
# if objectif > 0 and versement > 0:
#     # Calculer le nombre de mois
#     while total < objectif:
#         total = total + versement
#         mois = mois + 1
#     # Afficher le résultat
#     print("Nombre de mois nécessaires :", mois)
#     print("Montant total épargné :", total, "$")
# else:
#     print("Erreur : les montants doivent être positifs.")
#Entrez votre objectif d'épargne ($) : 1000
# Entrez votre versement mensuel ($) : 300
# Nombre de mois nécessaires : 4
# Montant total épargné : 1000.0 $

#06 — Débogage (25 min) : corriger six erreurs : indentation, 
# borne de range, conversion, boucle infinie, confusion = / ==, test logique.

# 1. Erreur d'indentation
# age = int(input("Entrez votre âge : "))
# if age >= 18:
# print("Majeur")
# #=>
# if age >= 18:
#  age
#  print("Majeur")

#  2. Erreur de borne de range(): Pour afficher les nombres de 1 à 5 
#  for i in range(1, 5):
#     print(i)
#=>La dernière valeur de range() est exclue

# for i in range(1,6):
#     print(i)

# 3. Erreur de conversion

# age = input("Entrez votre âge : ")
# print(age + 5)
#=>input() retourne une chaîne de caractères. int() permet de la convertir en entier.
# age = int(input("Entrez votre âge : "))
# print(age + 5)

# 4. Erreur de boucle infinie
# compteur = 0

# while compteur < 5:
#     print(compteur)

#=>Il faut modifier le compteur pour que la condition devienne fausse.
# compteur = 0
# while compteur < 5:
#     print(compteur)
#     compteur = compteur + 1

# 5:Confusion entre = et ==
# age = 18
# if age = 18:
#     print("Vous avez 18 ans")
# => = sert à affecter une valeur.
# => == sert à comparer deux valeurs
# age = 18
# if age ==18:
#     print("Vous avez 18 ans")

#6:Erreur de test logique
# note = 15
# if note >= 10 or note <= 20:
#     print("Note valide")

#=>Cette condition accepte également certaines notes invalides, comme 25.
# note = 15
# if note >= 10 and note <= 20:
#     print("Note valide")

#07 — Caisse automat
# ique (35 min) : saisir les prix jusqu’à n ;
# refuser un prix négatif ; appliquer une remise de 10 % si au moins 3 articles ET total >= 60 $,
#  sinon 5 % si total >= 100 $.

# Demander le nombre d'articles
# n = int(input("Entrez le nombre d'articles : "))
# Initialiser les variables
# total = 0
# compteur = 0
# Vérifier le nombre d'articles
# if n > 0:
#     # Saisir les prix des articles
#     while compteur < n:
#         prix = float(input(f"Entrez le prix de l'article {compteur + 1} : "))
#         # Vérifier si le prix est positif ou nul
#         if prix >= 0:
#             total = total + prix
#             compteur = compteur + 1
#         else:
#             print("Erreur : le prix ne peut pas être négatif.")
#     # Appliquer une remise de 10 %
#     if n >= 3 and total >= 60:
#         remise = total * 0.10
#     # Sinon, appliquer une remise de 5 %
#     elif total >= 100:
#         remise = total * 0.05
#     # Sinon, aucune remise
#     else:
#         remise = 0
#     # Calculer le montant final
#     total_final = total - remise
#     # Afficher les résultats
#     print("Total avant remise :", total, "$")
#     print("Montant de la remise :", remise, "$")
#     print("Total à payer :", total_final, "$")
# else:
#     print("Erreur : le nombre d'articles doit être positif.")


# Sortie 1 : Remise de 10 %
# Le client achète 3 articles et le total est supérieur à 60 $.
# Entrez le nombre d'articles : 3
# Entrez le prix de l'article : 20
# Entrez le prix de l'article : 30
# Entrez le prix de l'article : 40
# Total avant remise : 90.0 $
# Montant de la remise : 9.0 $
# Total à payer : 81.0 $

# Nombre d'articles = 3
# Total = 90 $
# Remise = 90 × 0,10 = 9 $
# Total final = 81 $

# Sortie 2 : Remise de 5 %
# Le client achète 2 articles et le total est supérieur à 100 $.
# Entrez le nombre d'articles : 2
# Entrez le prix de l'article : 70
# Entrez le prix de l'article : 50
# Total avant remise : 120.0 $
# Montant de la remise : 6.0 $
# Total à payer : 114.0 $

# Sortie 3 : Aucune remise
# Entrez le nombre d'articles : 2
# Entrez le prix de l'article : 20
# Entrez le prix de l'article : 30
# Total avant remise : 50.0 $
# Montant de la remise : 0 $
# Total à payer : 50.0 $

# Sortie 4 : Prix négatif refusé
# Entrez le nombre d'articles : 3
# Entrez le prix de l'article : 20
# Entrez le prix de l'article : -10
# Erreur : le prix ne peut pas être négatif.
# Entrez le prix de l'article : 30
# Entrez le prix de l'article : 40
# Total avant remise : 90.0 $
# Montant de la remise : 9.0 $
# Total à payer : 81.0 $

# Remarque : Le prix négatif est refusé.
# Le programme redemande un prix jusqu'à obtenir 3 prix valides.

# Sortie 5 : Nombre d'articles invalide
# Entrez le nombre d'articles : 0
# Erreur : le nombre d'articles doit être positif.