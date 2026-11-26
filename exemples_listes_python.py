# -*- coding: utf-8 -*-
"""Cours : LES LISTES EN PYTHON

Fichier compagnon du PowerPoint « Les listes en Python ».
Chaque démonstration correspond aux diapositives indiquées.

Exécution : python exemples_listes_python.py
Puis choisir le numéro de la démonstration.
Pour exécuter tout le cours, choisir 0.
"""


def demo_01_creation():
    """Diapos 2–3 — Définir et créer une liste."""
    note1, note2, note3 = 12, 15, 18
    notes = [12, 15, 18]
    nombres = [10, 20, 30, 40]
    noms = ["Ali", "Sara", "Lina"]
    temperatures = [18.5, 21.3, 19.8]
    melange = [10, "Python", True, 3.5]
    liste_vide = []
    print("Variables :", note1, note2, note3)
    print("Liste notes :", notes)
    print("Nombres :", nombres)
    print("Noms :", noms)
    print("Températures :", temperatures)
    print("Types mélangés :", melange)
    print("Liste vide :", liste_vide)


def demo_02_indices():
    """Diapos 4–5 — Indices positifs et négatifs."""
    notes = [12, 15, 18, 20]
    print("Liste :", notes)
    print("Premier notes[0] :", notes[0])
    print("Troisième notes[2] :", notes[2])
    print("Dernier notes[-1] :", notes[-1])
    print("Avant-dernier notes[-2] :", notes[-2])
    print("Indices valides de 0 à", len(notes) - 1)


def demo_03_modification():
    """Diapo 6 — Modifier une valeur."""
    notes = [12, 15, 18, 20]
    print("Avant :", notes)
    notes[1] = 17
    print("Après notes[1] = 17 :", notes)


def demo_04_ajout():
    """Diapos 7–8 — append, insert, extend."""
    notes = [12, 15, 18]
    notes.append(20)
    print("append(20) :", notes)
    notes.insert(1, 14)
    print("insert(1, 14) :", notes)
    notes.extend([16, 19])
    print("extend([16, 19]) :", notes)
    # append([16, 19]) aurait ajouté UNE liste imbriquée.


def demo_05_suppression():
    """Diapos 9–10 — remove, pop, del, clear."""
    notes = [12, 15, 18, 15, 20]
    print("Départ :", notes)
    notes.remove(15)  # première occurrence seulement
    print("remove(15) :", notes)
    valeur_retiree = notes.pop(1)  # retire l'indice 1 et retourne sa valeur
    print("pop(1) :", notes, "| Valeur retirée :", valeur_retiree)
    valeur_retiree = notes.pop()  # dernier élément
    print("pop() :", notes, "| Valeur retirée :", valeur_retiree)
    del notes[0]
    print("del notes[0] :", notes)
    notes.clear()
    print("clear() :", notes)


def demo_06_tri():
    """Diapos 11–12 — sort, reverse, sorted."""
    nombres = [8, 2, 15, 4, 10]
    print("Départ :", nombres)
    nombres.sort()
    print("sort() croissant :", nombres)
    nombres.sort(reverse=True)
    print("sort(reverse=True) décroissant :", nombres)
    nombres.reverse()
    print("reverse() inverse l'ordre actuel :", nombres)
    originaux = [8, 2, 15]
    tries = sorted(originaux)
    print("sorted() -> original :", originaux, "; nouvelle liste :", tries)


def demo_07_fonctions():
    """Diapo 13 — Fonctions natives et méthodes de recherche."""
    notes = [10, 15, 20, 5, 15]
    print("Notes :", notes)
    print("len :", len(notes))
    print("sum :", sum(notes))
    print("min :", min(notes))
    print("max :", max(notes))
    print("count(15) :", notes.count(15))
    print("index(15) :", notes.index(15))
    print("Moyenne :", sum(notes) / len(notes))


def demo_08_extraction():
    """Diapo 14 — Tranches [début:fin:pas]."""
    liste = [10, 20, 30, 40, 50, 60]
    print("Liste :", liste)
    print("L[1:4] :", liste[1:4])
    print("L[:3] :", liste[:3])
    print("L[3:] :", liste[3:])
    print("L[::2] :", liste[::2])
    print("L[::-1] :", liste[::-1])


def demo_09_copie():
    """Diapo 15 — Copie indépendante et alias."""
    original = [10, 20, 30]
    alias = original         # même objet liste
    copie = original[:]      # copie superficielle indépendante (liste simple)
    original[0] = 99
    print("Original modifié :", original)
    print("Alias (modifié aussi) :", alias)
    print("Copie (inchangée) :", copie)


def demo_10_boucles():
    """Diapos 16–17 — Parcours par valeurs et par indices."""
    notes = [12, 15, 18]
    print("Par valeur :")
    for note in notes:
        print(note)
    print("Par indice :")
    for i in range(len(notes)):
        print("Indice :", i, "Valeur :", notes[i])


def demo_11_conditions():
    """Diapo 18 — Boucle for et if/else."""
    notes = [8, 12, 16, 9, 18]
    for note in notes:
        if note >= 10:
            print(note, ": Réussite")
        else:
            print(note, ": Échec")


def demo_12_statistiques():
    """Diapos 19–20 — Programme de synthèse : analyse de notes."""
    notes = [12, 8, 15, 18, 9, 14]
    moyenne = sum(notes) / len(notes)
    reussites = 0
    for note in notes:
        if note >= 10:
            reussites += 1
    print("Liste des notes :", notes)
    print("Moyenne :", moyenne)
    print("Note maximale :", max(notes))
    print("Note minimale :", min(notes))
    print("Nombre de réussites :", reussites)
    print("Nombre d'échecs :", len(notes) - reussites)


def demo_13_erreurs():
    """Diapo 21 — Analyse de messages d'erreur (exceptions interceptées)."""
    notes = [12, 15, 18]
    exemples = [
        ("IndexError", lambda: notes[5]),
        ("ValueError avec remove", lambda: notes.remove(99)),
        ("ValueError avec index", lambda: notes.index(99)),
        ("TypeError", lambda: notes + 10),
        ("AttributeError", lambda: notes.ajouter(20)),
    ]
    for etiquette, operation in exemples:
        try:
            operation()
        except (IndexError, ValueError, TypeError, AttributeError) as erreur:
            print(f"{etiquette} -> {type(erreur).__name__}: {erreur}")
    retour = notes.append(20)
    print("append(20) renvoie :", retour)
    print("La liste a été modifiée :", notes)


def exercice_01():
    """Diapo 22 — Correction : création + insertions."""
    nombres = [4, 8, 16, 20, 30]
    nombres.append(25)
    nombres.insert(2, 12)
    print(nombres)


def exercice_02():
    """Diapo 22 — Correction : suppression."""
    notes = [10, 14, 8, 14, 19]
    notes.remove(14)
    notes.pop()
    print(notes)  # [10, 8, 14]


def exercice_03():
    """Diapo 22 — Correction : températures et condition."""
    temperatures = [22, 27, 24, 30, 26]
    print("Moyenne :", sum(temperatures) / len(temperatures))
    compteur = 0
    for temperature in temperatures:
        if temperature > 25:
            compteur += 1
    print("Nombre de températures > 25 °C :", compteur)


def demo_14_exercices():
    print("Exercice 1 :")
    exercice_01()
    print("Exercice 2 :")
    exercice_02()
    print("Exercice 3 :")
    exercice_03()


DEMOS = {
    1: ("Création des listes", demo_01_creation),
    2: ("Indices positifs et négatifs", demo_02_indices),
    3: ("Modification", demo_03_modification),
    4: ("Ajout : append, insert, extend", demo_04_ajout),
    5: ("Suppression", demo_05_suppression),
    6: ("Tri et inversion", demo_06_tri),
    7: ("Fonctions natives", demo_07_fonctions),
    8: ("Extraction (slicing)", demo_08_extraction),
    9: ("Copie et alias", demo_09_copie),
    10: ("Boucles for", demo_10_boucles),
    11: ("Conditions", demo_11_conditions),
    12: ("Mini-programme de statistiques", demo_12_statistiques),
    13: ("Erreurs fréquentes", demo_13_erreurs),
    14: ("Corrections des exercices", demo_14_exercices),
}


def executer(numero):
    nom, fonction = DEMOS[numero]
    print("\n" + "=" * 65)
    print(f"DÉMONSTRATION {numero:02d} — {nom}")
    print("=" * 65)
    fonction()


if __name__ == "__main__":
    print("COURS : LES LISTES EN PYTHON")
    print("Sélectionner un exemple à exécuter :")
    print("0. Exécuter toutes les démonstrations")
    for numero, (nom, _) in DEMOS.items():
        print(f"{numero:2d}. {nom}")
    print("q. Quitter")
    while True:
        choix = input("\nVotre choix (0–14 ou q) : ").strip().lower()
        if choix == "q":
            break
        if choix == "0":
            for numero in DEMOS:
                executer(numero)
        elif choix.isdigit() and int(choix) in DEMOS:
            executer(int(choix))
        else:
            print("Choix non valide. Entrez 0 à 14 ou q.")
