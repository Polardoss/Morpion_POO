class Joueur:
    def __init__(self, symbole):
        self.symbole = symbole

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
            return Joueur('O')
        else:
            return Joueur('X')
        