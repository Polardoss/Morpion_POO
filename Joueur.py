import copy

class Joueur:
    def __init__(self, symbole, is_ia=False):
        self.symbole = symbole
        self.is_ia = is_ia

    def choisir_coup(self,plateau):
        while True:
            ligne = int(input("Choissisez la ligne: "))
            colonne = int(input("Choissisez la colonne: "))
            if 0 <= ligne < 3 and 0 <= colonne < 3 and plateau.est_case_vide(ligne,colonne):
                return ligne, colonne
            else:
                print("La Case est invalide ou occupée. Réessayez.")
        
    
    def remplire_case(self,ligne, colonne, plateau):
        plateau.modifier_plateau(ligne,colonne,self.symbole)
        return plateau
    
    def joueur_adverse(self):
        if self.symbole == 'X':
            if self.is_ia:
                return Joueur('O')
            else:
                return Joueur('O', True)
        else:
            if self.is_ia:
                return Joueur('X')
            else:
                return Joueur('X', True)
        

    def minimax(self, plateau, joueur):
        # Conditions de fin de récursivité
        if plateau.verif_win(joueur):
            return (1 if joueur.symbole == self.symbole else -1), None
        elif plateau.verif_win(joueur.joueur_adverse()):
            return (-1 if joueur.symbole == self.symbole else 1), None
        elif plateau.est_full():
            return 0, None

        scores = []
        listes_coup = []
        coups = plateau.coups_possibles()

        for coup in coups:
            copie_plateau = copy.deepcopy(plateau)
            copie_plateau.modifier_plateau(coup[0], coup[1], joueur.symbole)
            score, _ = self.minimax(copie_plateau, joueur.joueur_adverse())
            scores.append(score)
            listes_coup.append(coup)

        if joueur.symbole == self.symbole:
            meilleur_score = max(scores)
            meilleur_coup = listes_coup[scores.index(meilleur_score)]
        else:
            meilleur_score = min(scores)
            meilleur_coup = listes_coup[scores.index(meilleur_score)]

        return meilleur_score, meilleur_coup