import unittest
from datetime import datetime
from parse_gedcom.parser import Individual, Family
from parse_gedcom.sprint4_user_stories import US36_recent_births

class Test(unittest.TestCase):

    def setUp(self): 
        self.indiv = Individual("I1")
        self.individuals = [self.indiv]
   
    def test_less_than_30_days_old(self):
        indiv = self.indiv
        indiv.birthDateObject = datetime(2020, 11, 30)
        individuals = self.individuals
        self.assertEqual(US36_recent_births(individuals), [indiv])

    def test_exactly_30_days_old(self): #this test is based on today 11/29/20 date if test doesn't work fix date
        indiv = self.indiv 
        indiv.birthDateObject = datetime(2020, 10, 31)
        individuals = self.individuals
        self.assertEqual(US36_recent_births(individuals), [indiv])
            
    def test_over_30_days_old(self): 
        indiv = self.indiv
        indiv.birthDateObject = datetime(2019, 11, 30)
        individuals = self.individuals
        self.assertEqual(US36_recent_births(individuals), [])

if __name__ == "__main__":
    unittest.main()
