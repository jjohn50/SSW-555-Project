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
        self.husband.birthDateObject = datetime(1990, 5, 3)
        self.husband.deathDateObject = datetime(2019, 5, 3) #husband died on date
        self.fam.childrenObjects.append(self.child) #added child

    def test_fatherdiedbefore9months(self):
        husband = self.husband
        child = self.child   
        fam = self.fam
        child.birthDateObject = datetime(2020,2,3)
        US13_fatherdeath_before_child_birth(fam)
        self.assertEqual(len(fam.anomalies), 1)
        self.assertEqual(fam.anomalies, ["Child was born after 9 months after death of father"])  

    def test_fatheralive(self):
        husband = self.husband
        child = self.child
        fam = self.fam
        fam.husbandObject = husband
        fam.childObject = child
        husband.birthDateObject = datetime(1992,9,14)
        child.birthDateObject = datetime(2013, 9 ,14)
        US13_fatherdeath_before_child_birth(fam)
        self.assertEqual(len(fam.anomalies), 1)
        self.assertEqual(fam.anomalies, ["Child was born after 9 months after death of father"]) 
 
if __name__ == "__main__": 
    unittest.main()