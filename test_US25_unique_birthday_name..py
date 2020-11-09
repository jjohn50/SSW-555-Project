import unittest
from parse_gedcom.parser import Individual, Family
from parse_gedcom.sprint3_user_stories import US25_unique_birthday_and_name
import datetime

class Test(unittest.TestCase):
    
    def setUp(self):
        self.husband = Individual("I1")
        self.wife = Individual("I2")
        self.testFam1 = Family("F1")
        self.testFam1.husbandObject = self.husband
        self.testFam1.wifeObject = self.wife

    def test_same_name_and_birthday(self):
        husband = self.husband
        husband1 = Individual("I3")
        husband.name = "Mark Ass Colins"
        husband1.name = "Mark Ass Colins"
        husband.birthDateString = "1990,10,23"
        husband1.birthDateString = "1990,10,23"
        individuals= [husband, husband1]
        errorMsg = "There are 2 people with the same name and birthday"   
        US25_unique_birthday_and_name(individuals)  
        self.assertEqual(len(husband.errors), 1)   
        self.assertEqual(husband.errors, [errorMsg]) 

    def test_same_birth_different_name(self):
        husband = self.husband
        husband1 = Individual("I3")
        husband.name = "Marvin Mconners"
        husband1.name = "Mark Ass Colins"
        husband.birthDateString = "1990,10,23"
        husband1.birthDateString = "1990,10,23"
        individuals= [husband, husband1]
        US25_unique_birthday_and_name(individuals) 
        self.assertEqual(len(husband.errors), 0)    
        self.assertEqual(husband.errors, [])

    def test_samename_different_birthday(self):
        husband = self.husband
        husband1 = Individual("I3")
        husband.name = "Mark Ass Colins"
        husband1.name = "Mark Ass Colins"
        husband.birthDateString = "1991,10,23"
        husband1.birthDateString = "1990,10,24"
        individuals= [husband, husband1]
        US25_unique_birthday_and_name(individuals)  
        self.assertEqual(len(husband1.errors), 0)     
        self.assertEqual(husband1.errors, [])   
        
if __name__ == "__main__": 
    unittest.main()    
