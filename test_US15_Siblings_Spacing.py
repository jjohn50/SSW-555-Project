import unittest
from datetime import datetime
from parse_gedcom.parser import Individual, Family
from parse_gedcom.sprint2_user_stories import US15_Siblings_Spacing


class Test(unittest.TestCase):

    def setUp(self):
        self.wife = Individual("I1")  
        self.husband = Individual("I2")
        self.child = Individual("I3")
        self.child1 = Individual("I4")
        self.fam = Family("F1")
        self.fam.childrenObjects.append(self.child) #added child
        self.fam.childrenObjects.append(self.child1) #added child


        
    def test_siblings_5_month_apart(self):
        wife = self.wife
        husband = self.husband
        child = self.child
        child1 = self.child1
        fam = self.fam
        child.birthDateObject = datetime(2013,4,14)
        child1.birthDateObject = datetime(2013, 9 ,14)
        US15_Siblings_Spacing(fam)
        self.assertEqual(len(fam.anomalies), 2)
        self.assertEqual(fam.anomalies, ["Siblings were born too close together"])  

    def test_siblings_2_month_apart(self):
        wife = self.wife
        husband = self.husband
        child = self.child
        child1 = self.child1
        fam = self.fam
        child.birthDateObject = datetime(2013,7,14)
        child1.birthDateObject = datetime(2013, 9 ,14)
        US15_Siblings_Spacing(fam)
        self.assertEqual(len(fam.anomalies), 2)
        self.assertEqual(fam.anomalies, ["Siblings were born too close together"])  

    def test_sibling_8_month_apart(self):   
        wife = self.wife
        husband = self.husband
        child = self.child
        child1 = self.child1
        fam = self.fam
        child.birthDateObject = datetime(2013,1,14)
        child1.birthDateObject = datetime(2013, 9 ,14)
        US15_Siblings_Spacing(fam)
        self.assertEqual(len(fam.anomalies), 2)
        self.assertEqual(fam.anomalies, ["Siblings were born too close together"])  
 
    
if __name__ == "__main__": 
    unittest.main()