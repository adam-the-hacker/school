# Création des variables principales
joueur = 1
IA = 1
matrice = [[0 for i in range(3)]for j in range(3)]
ia_first = False
# Demande si l'on veut jouer contre une IA
if input("Voulez vous jouer contre une IA ? Y or N") == "Y":
  IA = -joueur
  # Demande qui joue en premier
  if input("L'IA joue-t-elle en premier? Y or N") == "Y":
    ia_first = True


# La fonction d'affichage
def affichage():
    print("######     TIC TAC TOE     ######")
    b = 0
    for ligne in matrice:
        a = 0
        for n in ligne:

            if n == 0:
                print(' ', end='\t')
                a += 1
                # print une pipe seulement entre les "X" ou les "O"
                if a != 3: print("|", end='\t')

            if n == -1:
                print('O', end='\t')
                a += 1
                if a != 3: print("|", end='\t')

            if n == 1:
                print('X', end='\t')
                a += 1
                if a != 3: print("|", end='\t')

        print()
        # print une séparation seulement entre les lignes
        if b != 2:
            print("──────────────────────────────────")
            b += 1


def saisie():
    extra = ''
    while True:
        coup = input(f"Saisissez le nombre représentatif de votre {extra} case choisie : \n0/1/2\n3/4/5\n6/7/8\n: ")

        if coup in [str(j) for j in range(9)]:
            coup = int(coup)

            if matrice[coup // 3][coup % 3] != 0:
                print('Saisie invalide, case déja prise.', end=' ')
                # texte adaptatif en fonction des situations
                extra = 'nouvelle'

            else:
                return coup

        else:
            print('Saisie invalide, veuillez entrer un nombre entre 0 et 9.', end=' ')
            extra = 'nouvelle'


def victoire():
    if matrice[0][0]+matrice[0][1]+matrice[0][2] in [-3,3] :
        return matrice[0][0]
    if matrice[1][0]+matrice[1][1]+matrice[1][2] in [-3,3] :
        return matrice[1][0]
    if matrice[2][0]+matrice[2][1]+matrice[2][2] in [-3,3] :
        return matrice[2][0]
    if matrice[0][0]+matrice[1][0]+matrice[2][0] in [-3,3] :
        return matrice[0][0]
    if matrice[0][1]+matrice[1][1]+matrice[2][1] in [-3,3] :
        return matrice[0][1]
    if matrice[0][2]+matrice[1][2]+matrice[2][2] in [-3,3] :
        return matrice[0][2]
    if matrice[0][0]+matrice[1][1]+matrice[2][2] in [-3,3] :
        return matrice[0][0]
    if matrice[2][0]+matrice[1][1]+matrice[0][2] in [-3,3] :
        return matrice[1][1]
    for ligne in matrice:
        for elt in ligne:
            if elt != 0:
              pass
            else:
              return 0
    return 2


def ia_joue():

  # Check si un des coups permet la victoire
    for coup in range(9):
        if matrice[coup//3][coup%3] == 0:
            matrice[coup//3][coup%3] = IA
            if victoire() == IA:
                return coup
            matrice[coup//3][coup%3] = 0
  # Check quel coup de l'adversaire est gagnant
    for coup in range(9):
        if matrice[coup//3][coup%3] == 0:
            matrice[coup//3][coup%3] = -IA
            if victoire() == -IA:
                return coup
            matrice[coup//3][coup%3] = 0
  # Liste de coups prédéfinis si aucun coup n'est gagnant
    coup_defaut = [4, 0, 2, 6, 8, 1, 3, 4, 5]
    for coup in coup_defaut:
        if matrice[coup//3][coup%3] == 0:
            return coup


# Code principal

if ia_first is True:
    while True:

        coup = ia_joue()
        matrice[coup // 3][coup % 3] = IA
        # Affichage après le coup de l'IA pour permettre au joueur de savoir où est-ce que l'IA a joué
        affichage()

        # Détermination de la victoire avant le coup du joueur permet d'éviter les bugs en cas de match nul,
        # où le joueur est obligé de jouer un coup malgré une matrice complète

        if victoire() != 0:
            if victoire() == 2:
                print('Match nul')
                affichage()
                break
            if victoire() == 1:
                print('Partie finie, joueur 1 a gagné !')
                affichage()
                break
            if victoire() == -1:
                if IA == -1:
                    print('Partie finie, IA a gagné !')
                else:
                    print('Partie finie, joueur 2 a gagné !')
                affichage()
                break

        coup = saisie()
        matrice[coup // 3][coup % 3] = joueur
else:
    while True:

        affichage()

        coup = saisie()
        matrice[coup // 3][coup % 3] = joueur

        # Détermination de la victoire avant le coup de l'ia ou du deuxième joueur permet d'éviter les bugs en cas de match nul,
        # où l'IA est obligée de jouer un coup malgré une matrice complète

        if victoire() != 0:
            if victoire() == 2:
                print('Match nul')
                affichage()
                break
            if victoire() == 1:
                print('Partie finie, joueur 1 a gagné !')
                affichage()
                break
            if victoire() == -1:
                if IA == -1:
                    print('Partie finie, IA a gagné !')
                else:
                    print('Partie finie, joueur 2 a gagné !')
                affichage()
                break

        if IA == -1:
            coup = ia_joue()
            matrice[coup // 3][coup % 3] = IA
        else:
            joueur = -joueur
