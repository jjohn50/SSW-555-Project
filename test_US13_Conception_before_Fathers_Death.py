import unittest
# import parser
from datetime import datetime
from parse_gedcom.parser import Individual, Family
from parse_gedcom.sprint2_user_stories import US13_fatherdeath_before_child_birth 

class Test(unittest.TestCase):

    def setUp(self):
        self.husband = Individual("I1")  
        self.child = Individual("I2")          
        self.fam = Family("F1") 
        self.fam.husbandObject = self.husband
        self.fam.childrenObjects.append(self.child) #added child

    def test_fatherdiedbefore12months(self):
        child = self.child   
        husband = self.husband
        fam = self.fam   
        husband.deathDateObject = datetime(2019, 1, 3)
        husband.alive = False 
        child.birthDateObject = datetime(2020,1,3)
        US13_fatherdeath_before_child_birth(fam)
        self.assertEqual(len(fam.errors), 1)
        self.assertEqual(fam.errors, ["Child was born after 9 months after death of father"])  

    def test_fatheralive(self):
        #create a new family objects here 
        child = self.child   
        husband = self.husband
        fam = self.fam
        husband.alive = True
        child.birthDateObject = datetime(2013, 9 ,14)
        US13_fatherdeath_before_child_birth(fam)
        self.assertEqual(len(fam.errors), 0)
        self.assertEqual(fam.errors, []) 
 
    def test_fatherdiedlessthan9months(self):
        child = self.child   
        husband = self.husband
        fam = self.fam   
        husband.deathDateObject = datetime(2019, 1, 3)
        husband.alive = False 
        child.birthDateObject = datetime(2019,9,3)
        US13_fatherdeath_before_child_birth(fam)
        self.assertEqual(len(fam.errors), 0)
        self.assertEqual(fam.errors, [])  

if __name__ == "__main__": 
    unittest.main()
