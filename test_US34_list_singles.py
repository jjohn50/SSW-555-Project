import unittest
from parse_gedcom.parser import Individual, Family
from parse_gedcom.sprint4_user_stories import US34_list_singles

class Test(unittest.TestCase):

    def setUp(self):
        indiv = Individual("I1")
        indiv1 = Individual("I2")
        indiv2 = Individual("I3")
        indiv3 = Individual("I4")
        indiv4 = Individual("I5")
        indiv.age = 30
        indiv1.age = 40
        indiv2.age = 20
        indiv3.age = 25       
        indiv4.age = 35  
        indiv.spouseFamilyObjects = []
        indiv1.spouseFamilyObjects = []
        indiv2.spouseFamilyObjects = [] 
        indiv3.spouseFamilyObjects = [] 
        indiv4.spouseFamilyObjects = [] 

    def test_people_over_30_not_married(self):
        indiv = Individual("I1")
        indiv1 = Individual("I2")
        indiv2 = Individual("I3")
        US34_list_singles(indiv)
        US34_list_singles(indiv1)
        US34_list_singles(indiv2)
        self.assertEqual(US34_list_singles(indiv.errors), []) 

    def test_people_under_30_not_married(self):
      indiv = Individual("I3")
      invid = Individual("I4")
       US34_list_singles(indiv)
       US34_list_singles(indiv1)
       US34_list_singles(indiv2)
      self.assertEqual(US34_list_singles(self.families), [])

if __name__ == "__main__":
    unittest.main()
