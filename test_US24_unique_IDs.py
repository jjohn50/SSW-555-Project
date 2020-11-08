import unittest
from parse_gedcom.parser import Individual, Family
from parse_gedcom.sprint3_user_stories import US24_Unique_IDs

class Test(unittest.TestCase):
    
    def setUp(self):
        self.husband = Individual("I1")
        self.wife = Individual("I2")
        self.testFam1 = Family("F1")
        self.testFam1.husbandObject = self.husband
        self.testFam1.wifeObject = self.wife

    def test_uniqueid_for_spouses(self):
        testFam1 = self.testFam1
        individuals= [testFam1.husbandObject, testFam1.wifeObject]
        US24_Unique_IDs(individuals, "individuals")  
        self.assertEqual(len(testFam1.wifeObject.errors), 0)   
        self.assertEqual(testFam1.wifeObject.errors, []) 

    def test_not_uniqueid_for_spouses(self):
        testFam1 = self.testFam1
        child1 = Individual("I1")
        testFam1.childrenObjects.append(child1)
        errorMsg = "There are 2 individuals with id I1"
        individuals= [testFam1.husbandObject, testFam1.wifeObject, child1]
        US24_Unique_IDs(individuals,"individuals") 
        self.assertEqual(len(testFam1.husbandObject.errors), 1)    
        self.assertEqual(testFam1.husbandObject.errors, [errorMsg])

    def test_not_uniqueid_for_family(self):
        testFam1 = self.testFam1 
        testFam2 = self.testFam1
        testFam3 = self.testFam1
        families = [testFam1, testFam2, testFam3]
        errorMsg = "There are 3 families with id F1" 
        US24_Unique_IDs(families,"families")  
        self.assertEqual(len(testFam1.errors), 3)   
        self.assertEqual(testFam1.errors[0], errorMsg)
    
    def test_unique_for_families(self):
        testFam1 = self.testFam1
        testFam2 = Family("F2")
        testFam3 = Family("F3")
        families = [testFam1, testFam2, testFam3]
        US24_Unique_IDs(families,"families")  
        self.assertEqual(len(testFam1.errors), 0)     
        self.assertEqual(testFam1.errors, [])   
        
if __name__ == "__main__": 
    unittest.main()    