from Plateau import *
from Joueur import *


class Partie:
    def __init__(self, ):
        self.joueur1 = Joueur("O")
        self.joueur2 = Joueur("X", True)
        self.joueur_actuel = self.joueur1
        self.plateau = Plateau()

    def demarrer(self):
        self.plateau.afficher()
        self.jouer()
    
    def jouer(self):
        nb_tour = 0

        while True:
            if nb_tour % 2 == 0:
                self.joueur_actuel = self.joueur1
            else:
                self.joueur_actuel = self.joueur2

            #########################
            print(self.plateau.coups_possibles())

            if not self.joueur_actuel.is_ia:
                ligne,colonne = self.joueur_actuel.choisir_coup(self.plateau)
                self.plateau = self.joueur_actuel.remplire_case(ligne, colonne, self.plateau)
            else:
                score, coup = self.joueur_actuel.minimax(self.plateau, self.joueur_actuel)
                print(f"L'IA choisit la case : {coup[0]}, {coup[1]} avec un score {score}")
                self.plateau = self.joueur_actuel.remplire_case(coup[0], coup[1], self.plateau)


            
            
            self.plateau.afficher()
            if self.plateau.verif_win(self.joueur_actuel):
                print(f"Le joueur {self.joueur_actuel.symbole} a WIn ! ")
                break
            elif self.plateau.est_full():
                print("Le plateau est full. Egalité")
                break
            nb_tour = nb_tour+1
            

        