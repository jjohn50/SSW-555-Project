import unittest
from parse_gedcom.parser import Individual, Family
from parse_gedcom.sprint3_user_stories import US23_Correct_gender_for_role

class Test(unittest.TestCase):
    def setUp(self):
        self.husband = Individual("I1")
        self.wife = Individual("I2")
        self.testFam1 = Family("F1")
        self.testFam1.husbandObject = self.husband
        self.testFam1.wifeObject = self.wife
    
    def test_Wife_is_male(self):
        husband = self.husband
        wife = self.wife
        wife.gender = 'M'
        testFam1 = self.testFam1
        US23_Correct_gender_for_role(testFam1)  
        self.assertEqual(len(testFam1.errors), 1)   
        self.assertEqual(testFam1.errors[0], "Wife is a male")
   
    def test_Wife_is_female(self): 
        husband = self.husband
        wife = self.wife
        wife.gender = 'F'
        testFam1 = self.testFam1
        US23_Correct_gender_for_role(testFam1)
        self.assertEqual(len(testFam1.errors), 0)
        self.assertEqual(testFam1.errors, [])

    def test_husband_is_male(self):
        husband = self.husband
        wife = self.wife
        husband.gender = 'M'
        testFam1 = self.testFam1
        US23_Correct_gender_for_role(testFam1)
        self.assertEqual(len(testFam1.errors), 0)
        self.assertEqual(testFam1.errors, [])

    def test_husband_is_female(self):
        husband = self.husband
        wife = self.wife
        husband.gender = 'F'
        testFam1 = self.testFam1
        US23_Correct_gender_for_role(testFam1)
        self.assertEqual(len(testFam1.errors), 1)
        self.assertEqual(testFam1.errors[0], "Husband is a female")

    def test_husband_is_female_and_wife_is_male(self):
        husband = self.husband
        wife = self.wife  
        husband.gender = 'F'
        wife.gender = 'M'
        testFam1 = self.testFam1   
        US23_Correct_gender_for_role(testFam1)
        self.assertEqual(len(testFam1.errors), 2)
        self.assertEqual(testFam1.errors[0], "Husband is a female", "Wife is a male")

if __name__ == "__main__":
    unittest.main()
