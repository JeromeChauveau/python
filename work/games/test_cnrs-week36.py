#!/usr/bin/python
# coding: utf8

import unittest
import logging as log
from cnrs-week36 import main

'''
Test de la fonction qui renvoie le nombre X de nombres à n chiffres dont tels que la somme deux à deux 
des chiffres les composant (1+n, 2+ n-1...) soit égal à un nombre Y
 On pourrait aussi introduire une notion d''ordre
  (par exemple, la somme des nombres qui se suivent : pour un nombre abc, on somme : a+b, b+c, c+a -->
  à faire dans un deuxième remps
'''
# Test des paramètres
class TestMainInputs(unittest.TestCase):
    def test_invalid_number_of_digits(self):
        self.assertRaises(InvalidNumberException, main, 8, 7)
        self.assertRaises(InvalidNumberException, main, 8, 0)

    def test_invalid_number_to_find(self):
        # La somme de deux chiffres ne peut être supérieure à 18
        self.assertRaises(InvalidNumberException, main, 19, 8)

    def test_not_numbers(self):
        self.assertRaises(InvalideNumberException, main, 'a', 'b')

    def test_not_whole_numbers(self):
        self.assertRaises(NotWholeNumberException, main, -1, 8)
        self.assertRaises(NotWholeNumberException, main, 10, -1)
        self.assertRaises(NotWholeNumberException, main, 0.5, 8)
        self.assertRaises(NotWholeNumberException, main, 9, 0.5)

# Test généraux sur les résultats - implicites
class TestMainOutput(unittest.TestCase):
    def test_not_whole_number(self):
        res = main(8,8)
        self.assertIsInstance(res, int)

    def test_output_expected_properties(self):
        # Le nombre de nombres à n chiffres ayant la propriété attendue 
        # ne peut être supérieur ou égal au nombre total de nombres à n chiffres
        # Intéressant à chercher : combien de nombres à n chiffres y'a-t-il? --> fonction!
        self.assertGreater(9000, main(2, 4))

        # Deux appels avec les mêmes paramètres renvoient les mêmes valeurs
        self.assertEqual(main(2,4), main(2, 4))

        # S'il y a plus de couples (a, b) tels que a+b = n que de couples (a, b) tels que a+b = m,
        # alors forcément main (n, i) > main (m, i)
        self.assetGreater (main (5, 10), main (6, 10))
        
        # Plus il y a de chiffres dans le nombre, plus il y a de combinaisons possible pour un même nombre cible
        self.assertGreater (main(2, 6), main (2, 8))

# Tests principaux - explicites
class TestMainResult(unittest.TestCase):
    def test_known_return_values(self):
        self.assertEqual(main(0,2), 0)
        self.assertEqual(main(1,2), 2)
        self.assertEqual(main(2,2), 3)





    
    
if __name__ == '__main__':
    unittest.main()