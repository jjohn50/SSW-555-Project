import unittest
from parse_gedcom.parser import Individual, Family
from parse_gedcom.sprint3_user_stories import US24_Unique_IDs

class Test(unittest.TestCase):

    def setUp(self):
        self.husband = Individual("I1")
        self.wife = Individual("I2")
        self.husband1 = Individual("I3")
        self.wife1 = Individual("I4")
        self.testFam1 = Family("F1")
        self.testFam2 = Family("F2")
        self.testFam2 = self.testFam2

        self.testFam1.husbandObject = self.husband
        self.testFam1.wifeObject = self.wife

    def test_uniqueid_for_spouses(self):
        testFam1 = self.testFam1
        families= [testFam1]
        US24_Unique_IDs(families)  
        self.assertEqual(len(testFam1.errors), 0)   
        self.assertEqual(testFam1.errors, []) 

    def test_not_uniqueid_for_spouses(self):
        husband = self.husband
        wife = self.wife
        husband1 = self.husband
        wife1 = self.wife
        testFam1 = self.testFam1
        testFam2 = self.testFam1
        errorMsg = "There are 2 same with id "
        errorMsg1 = "There are 2 same with id "
        families= [testFam1, testFam2]
        US24_Unique_IDs(families) 
        self.assertEqual(len(testFam1.errors), 2)    
        self.assertEqual(testFam1.errors, [errorMsg, errorMsg1])

    def test_not_uniqueid_for_family(self):
        testFam1 = self.testFam1 
        testFam2 = self.testFam1
        testFam3 = self.testFam1
        families = [testFam1, testFam2, testFam3]
        errorMsg = "There are 3 same with id "
        US24_Unique_IDs(families)  
        self.assertEqual(len(testFam1.errors), 3)   
        self.assertEqual(testFam1.errors[0], errorMsg)
     
if __name__ == "__main__": 
    unittest.main()    