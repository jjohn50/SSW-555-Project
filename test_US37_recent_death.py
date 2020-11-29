import unittest
from parse_gedcom.parser import Individual
from datetime import datetime
from parse_gedcom.sprint4_user_stories import US37_recent_death

class Test(unittest.TestCase):

    def setUp(self):
        self.indiv = Individual("I1")
        self.indiv.alive = False 
        self.individuals = [self.indiv]
    
    def test_died_less_than_30_days(self):
        indiv = self.indiv
        indiv.deathDateObject = datetime.now()
        individuals = self.individuals
        self.assertEqual(US37_recent_death(individuals), [indiv])

    def test_died_after_30_days(self):
        indiv = self.indiv
        indiv.deathDateObject = datetime(2019, 11, 29)
        individuals = self.individuals
        self.assertEqual(US37_recent_death(individuals), [])
    
    def test_died_exactly_30_days(self): #this test only works today on 11/29/2020
        indiv = self.indiv
        indiv.deathDateObject = datetime(2020,10,31)
        individuals = self.individuals
        self.assertEqual(US37_recent_death(individuals), [indiv])

if __name__ == "__main__":
    unittest.main()
