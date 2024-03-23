import unittest
import Plateau
import Joueur
import Ia

class TestPlateau(unittest.TestCase):

    def test_coups_possibles(self):
        plateau = Plateau.Plateau()
        plateau.plateau = [
            ['_', '_', '_'],
            ['_', '_', '_'],
            ['_', '_', '_']
        ]
        self.assertEqual(plateau.coups_possibles(),[[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]])

    def test_case_vide(self):
        plateau = Plateau.Plateau()
        self.assertTrue(plateau.est_case_vide(1,1))

    def test_verif_win_ligne(self):
        plateau = Plateau.Plateau()
        joueur = Joueur.Joueur('X')
        plateau.plateau = [
            ['X', 'X', 'X'],
            ['_', '_', '_'],
            ['_', '_', '_']
        ]
        self.assertTrue(plateau.verif_win(joueur))


    def test_verif_win_colonne(self):
        plateau = Plateau.Plateau()
        joueur = Joueur.Joueur('X')

        plateau.plateau = [
            ['X', '_', '_'],
            ['X', '_', '_'],
            ['X', '_', '_']
        ]
        self.assertTrue(plateau.verif_win(joueur))

    def test_verif_win_diagonale(self):
        plateau = Plateau.Plateau()
        joueur = Joueur.Joueur('X')
        plateau.plateau = [
            ['X', '_', '_'],
            ['_', 'X', '_'],
            ['_', '_', 'X']
        ]
        self.assertTrue(plateau.verif_win(joueur))

        plateau.plateau = [
            ['_', '_', 'X'],
            ['_', 'X', '_'],
            ['X', '_', '_']
        ]
        self.assertTrue(plateau.verif_win(joueur))

    def test_est_full(self):
        plateau = Plateau.Plateau()
        plateau.plateau = [
            ['O', 'O', 'X'],
            ['X', 'X', 'O'],
            ['O', 'O', 'X']
        ]
        self.assertTrue(plateau.est_full())

        plateau.plateau = [
            ['O', 'O', '_'],
            ['X', 'X', 'O'],
            ['O', 'O', 'X']
        ]
        self.assertFalse(plateau.est_full())



class TestJoueur(unittest.TestCase):
    pass

class TestIA(unittest.TestCase):
    def setUp(self):
        self.ia = Ia.IA('X')
        self.plateau = Plateau.Plateau()

    def test_choisir_coup_gagnant(self):
        self.plateau.plateau = [
            ['O', 'X', '_'],
            ['_', 'X', '_'],
            ['O', '_', 'O']
        ]
        coup = self.ia.choisir_coup(self.plateau)
        self.assertEqual(coup, [2, 1])  # L'IA doit choisir [2, 1] pour gagner



    def test_choisir_coup_bloquant(self):
        pass

    def test_choisir_coup_egalite(self):
        pass



if __name__ == '__main__':
    unittest.main()
