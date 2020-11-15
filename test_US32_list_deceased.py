import unittest
from parse_gedcom.parser import Individual, Family
from parse_gedcom.sprint4_user_stories import US32_list_deceased

class Test(unittest.TestCase):
    
    def setUp(self):
        self.indiv = Individual("I1")
        self.individuals = [self.indiv]
    
    def test_alive(self):
        indiv = self.indiv
        indiv.alive = True
        self.assertEqual(US32_list_deceased(self.individuals), [indiv])

    def test_dead(self):
        indiv = self. indiv
        indiv.alive = False
        self.assertEqual(US32_list_deceased(self.individuals), [])

if __name__ == "__main__":
    unittest.main()
