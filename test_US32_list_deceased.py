import unittest
from parse_gedcom.parser import Individual
from parse_gedcom.sprint4_user_stories import US32_list_deceased

class Test(unittest.TestCase):
    
    def setUp(self):
        self.indiv = Individual("I1")
    
    def test_alive(self):
        indiv = self.indiv
        indiv.alive = True
        self.assertEqual(US32_list_deceased(self.indiv), [Individual])

    def test_dead(self):
        indiv = self. indiv
        indiv.alive = False
        self.assertEqual(US32_list_deceased(self.indiv), [])

if __name__ == "__main__":
    unittest.main()
