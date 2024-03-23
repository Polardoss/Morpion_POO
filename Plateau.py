class Plateau:
    def __init__(self):
        self.plateau = [['_' for _ in range(3)] for _ in range(3)]

    def afficher(self):
        for ligne in self.plateau:
            print(ligne)
    
    def est_case_vide(self, ligne, colonne):
        return self.plateau[ligne][colonne] == '_'
    
    def modifier_plateau(self,ligne,colonne, signe):
        self.plateau[ligne][colonne] = signe
        return self.plateau
    
    def est_full(self):
        return all(case != '_' for ligne in self.plateau for case in ligne)
    
    def verif_win(self,joueur):
        for ligne in self.plateau: #Lignes
            if all(case == joueur.symbole for case in ligne):
                return True
        
        for colonne in range(len(self.plateau)): #Colonnes
            if all(self.plateau[ligne][colonne] == joueur.symbole for ligne in range(len(self.plateau))):
                return True

        if all(self.plateau[i][i] == joueur.symbole for i in range(len(self.plateau))):
            return True
        
        if all(self.plateau[i][len(self.plateau)-i-1] == joueur.symbole for i in range(len(self.plateau))):
            return True
        
        return False
    
    def coups_possibles(self):
        coups_possibles = []

        for i in range(len(self.plateau)):
            for j in range(len(self.plateau)):
                if self.plateau[i][j] == '_':
                    coups_possibles.append([i,j])

        return coups_possibles
    
