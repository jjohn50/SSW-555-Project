import unittest
from parse_gedcom.parser import Individual, Family
from parse_gedcom.sprint4_user_stories import US33_list_living_married

class Test(unittest.TestCase):

    def setUp(self):
        self.husband = Individual("I1")
        self.wife = Individual("I2")
        self.testFam = Family("F1")
        self.families = [self.testFam]
        self.testFam.husbandObject = self.husband
        self.testFam.wifeObject = self.wife
        self.husband.name = "John"
        self.wife.name = "Jane"
    
    def test_divorced(self):
        husband = self.husband
        wife = self.wife
        testFam = self.testFam
        testFam.divorced = True
        husband.alive = True
        wife.alive = True
        self.assertEqual(US33_list_living_married(self.families), [])

    def test_wife_is_dead(self):
        husband = self.husband
        wife = self.wife
        testFam = self.testFam
        testFam.divorced = False
        husband.alive = True
        wife.alive = False
        self.assertEqual(US33_list_living_married(self.families), [])

    def test_husband_is_dead(self):
        husband = self.husband
        wife = self.wife
        testFam = self.testFam
        testFam.divorced = True
        husband.alive = False
        wife.alive = True
        self.assertEqual(US33_list_living_married(self.families), [])

    def test_married_and_both_alive(self):
        husband = self.husband
        wife = self.wife
        testFam = self.testFam
        testFam.divorced = False
        husband.alive = True
        wife.alive = True
        self.assertEqual(US33_list_living_married(self.families), [testFam])

if __name__ == "__main__":
    unittest.main()
