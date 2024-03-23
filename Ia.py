import Joueur

class IA:
    def __init__(self, symbole):
        self.symbole = symbole

    def joueur_adverse(self):
        if self.symbole == 'X':
            return Joueur.Joueur('O')
        else:
            return Joueur.Joueur('X')

    def choisir_coup(self, plateau):
        _, meilleur_coup = self.minimax(plateau, self)
        return meilleur_coup
    
    def minimax(self, plateau, joueur):
        # Condition de fin de récursivité
        if plateau.verif_win(joueur):
            print(f"Gagné pour {joueur.symbole}")
            return 1, None
        elif plateau.verif_win(joueur.joueur_adverse()):
            print(f"Perdu pour {joueur.symbole}")
            return -1, None
        elif plateau.est_full():
            print("Match nul")
            return 0, None
        
        meilleur_score = -float('inf') if joueur.symbole == self.symbole else float('inf')
        meilleur_coup = None

        coups = plateau.coups_possibles()
        print(f"Les coups possibles sont: ",coups)
        for coup in coups:
            plateau.modifier_plateau(coup[0], coup[1], joueur)
            score, _ = self.minimax(plateau, joueur.joueur_adverse())
            plateau.modifier_plateau(coup[0], coup[1], '_')
            

            if joueur.symbole == self.symbole:
                if score > meilleur_score:
                    meilleur_score = score
                    meilleur_coup = coup
            else:
                if score < meilleur_score:
                    meilleur_score = score
                    meilleur_coup = coup

        return meilleur_score, meilleur_coup
