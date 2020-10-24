import unittest
# import parser
from datetime import datetime
from parse_gedcom.parser import Individual, Family
from parse_gedcom.sprint2_user_stories import US14_Parents_not_too_old 

class Test(unittest.TestCase):

    def setUp(self):
        self.wife = Individual("I1")  
        self.husband = Individual("I2")
        self.child = Individual("I3")
        self.fam = Family("F1")
        self.fam.divorceDateObject = datetime(2019, 5, 3) #divorce date
        self.fam.childrenObjects.append(self.child) #added child

        
    def test_motherIsOlderthan60(self):
        wife = self.wife
        child = self.child
        fam = self.fam
        wife.birthDateObject = datetime(1900,9,14)
        child.birthDateObject = datetime(2013, 9 ,14)
        US14_Parents_not_too_old(fam)
        self.assertEqual(len(fam.anomalies), 1)
        self.assertEqual(fam.anomalies, ["Mother is 60 years older than child/ren"])  

    def test_husbandIsOlderthan80(self):
        husband = self.husband
        child = self.child
        fam = self.fam
        fam.husbandObject = husband
        fam.childObject = child
        husband.birthDateObject = datetime(1992,9,14)
        child.birthDateObject = datetime(2013, 9 ,14)
        US14_Parents_not_too_old(fam)
        self.assertEqual(len(fam.anomalies), 1)
        self.assertEqual(fam.anomalies, ["Father is 80 years older than child/ren"]) 

    def test_bothWifeIs60AndHusbandis80(self):   
        husband = self.husband
        child = self.child
        wife = self.wife
        fam = self.fam
        wife.birthDateObject = datetime(1900,9,14)
        husband.birthDateObject = datetime(1900,9,14)
        child.birthDateObject = datetime(2013, 9 ,14)
        US14_Parents_not_too_old(fam)
        self.assertEqual(len(fam.anomalies), 2)
        self.assertEqual(fam.anomalies, ["Mother is 60 years older than child/ren", "Father is 80 years older than child/ren"])  
    
if __name__ == "__main__": 
    unittest.main()