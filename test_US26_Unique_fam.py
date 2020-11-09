import unittest
from datetime import datetime
from parse_gedcom.parser import Individual, Family
from parse_gedcom.sprint3_user_stories import  US26_Unique_fam    

class Test(unittest.TestCase):

    def setUp(self):
        self.husband = Individual("I1")
        self.wife = Individual("I2")
        self.husband1 = Individual("I3")
        self.wife1 = Individual("I4")
        self.testFam1 = Family("F1")
        self.testFam2 = Family("F2")   
        self.testFam1.husbandObject = self.husband
        self.testFam1.wifeObject = self.wife
        self.testFam2.husbandObject = self.husband1
        self.testFam2.wifeObject = self.wife1
    
    def test_same_date_of_marriage_and_name(self):
        husband = self.husband
        wife = self.wife
        husband.name = "John"
        wife.name = "Darla"
        husband1 = self.husband1
        wife1 = self.wife1
        testFam1 = self.testFam1
        testFam2 = self.testFam2 
        testFam1.marriageDateObject = datetime(2010,10,2)
        testFam2.marriageDateObject = datetime(2010,10,2)
        husband1.name = "John"
        wife1.name = "Darla"
        families = [testFam1, testFam2]
        errorMsg = "There are 2 families with the same spouse and same marriage date"  
        US26_Unique_fam(families)
        self.assertEqual(len(testFam1.errors), 1)
        self.assertEqual(testFam1.errors[0], errorMsg)


    def test_same_date_of_marriage_different_name_husb(self):
        husband = self.husband
        wife = self.wife
        husband.name = "John"
        wife.name = "Darla"   
        husband1 = self.husband1
        wife1 = self.wife1
        testFam1 = self.testFam1
        testFam2 = self.testFam2 
        testFam1.marriageDateObject = datetime(2010,10,2)
        testFam2.marriageDateObject = datetime(2010,10,2)
        husband1.name = "Jack"
        wife1.name = "Darla"
        families = [testFam1, testFam2]
        US26_Unique_fam(families)
        self.assertEqual(len(testFam1.errors), 0)
        self.assertEqual(testFam1.errors, [])

    def test_same_date_of_marriage_different_name_Wife(self):
        husband = self.husband
        wife = self.wife
        husband.name = "John"
        wife.name = "Darla"
        husband1 = self.husband1
        wife1 = self.wife1
        testFam1 = self.testFam1
        testFam2 = self.testFam2 
        testFam1.marriageDateObject = datetime(2010,10,2)
        testFam2.marriageDateObject = datetime(2010,10,2)
        husband1.name = "John"
        wife1.name = "Carla"
        families = [testFam1, testFam2]
        US26_Unique_fam(families)
        self.assertEqual(len(testFam1.errors), 0)
        self.assertEqual(testFam1.errors, [])

        
    def test_same_name_different_marriage_date(self):
        husband = self.husband
        wife = self.wife
        husband.name = "John"
        wife.name = "Darla"
        husband1 = self.husband1
        wife1 = self.wife1
        testFam1 = self.testFam1
        testFam2 = self.testFam2 
        testFam1.marriageDateObject = datetime(2010,10,2)
        testFam2.marriageDateObject = datetime(2011,10,2)
        husband1.name = "John"
        wife1.name = "Darla"
        families = [testFam1, testFam2]  
        US26_Unique_fam(families)
        self.assertEqual(len(testFam1.errors), 0)
        self.assertEqual(testFam1.errors, [])

if __name__ == "__main__":
    unittest.main()
