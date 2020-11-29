import unittest
from parse_gedcom.parser import Individual, Family
from parse_gedcom.sprint4_user_stories import US34_list_singles

class Test(unittest.TestCase):

    def setUp(self):
        self.indiv1 = Individual("I1")
        self.indiv2 = Individual("I2")  
        self.indiv1.spouseFamilyObjects = []
        self.indiv2.spouseFamilyObjects = []
        self.individuals = [self.indiv1, self.indiv2]

    def test_people_over_30_not_married(self):
        indiv1 = self.indiv1
        indiv2 = self.indiv2
        indiv1.age = 35
        indiv2.age = 45
        individuals = self.individuals
        self.assertEqual(US34_list_singles(individuals), [indiv1, indiv2]) 

    def test_people_under_30_not_married(self):
        indiv1 = self.indiv1
        indiv2 = self.indiv2
        indiv1.age = 20
        indiv2.age = 21 
        individuals = self.individuals
        self.assertEqual(US34_list_singles(individuals), []) 
        
    def test_people_under_30_one_married(self):
        indiv1 = self.indiv1
        indiv2 = self.indiv2
        indiv3 = Individual("I3")
        indiv1.age = 26
        indiv2.age = 27
        indiv3.age = 28
        individuals = self.individuals
        individuals.append(indiv3)
        fam = Family("F1")
        fam.husbandObject = indiv1
        fam.wifeObjecet = indiv3
        indiv1.spouseFamilyObjects.append(fam)
        indiv3.spouseFamilyObjects.append(fam)
        self.assertEqual(US34_list_singles(individuals), [])
        
    def test_people_over_30_one_married(self):
        indiv1 = self.indiv1
        indiv2 = self.indiv2
        indiv3 = Individual("I3")
        indiv1.age = 45
        indiv2.age = 34 
        indiv3.age = 36
        individuals = self.individuals
        individuals.append(indiv3)
        fam = Family("F1")
        fam.husbandObject = indiv1
        fam.wifeObjecet = indiv3
        indiv1.spouseFamilyObjects.append(fam)
        indiv3.spouseFamilyObjects.append(fam)
        self.assertEqual(US34_list_singles(individuals), [indiv2])

if __name__ == "__main__":
    unittest.main()
