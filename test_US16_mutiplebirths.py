import unittest
from datetime import datetime
from parse_gedcom.parser import Individual, Family
from parse_gedcom.sprint2_user_stories import US16_Multiple_births

class Test(unittest.TestCase):

    def setUp(self):
        self.child = Individual("I1")
        self.child1 = Individual("I2")
        self.child2 = Individual("I3")
        self.child3 = Individual("I4")
        self.child4 = Individual("I5")
        self.child5 = Individual("I6")
        self.fam = Family("F1")
        self.fam.childrenObjects.append(self.child) #added child
        self.fam.childrenObjects.append(self.child1) #added child
        self.fam.childrenObjects.append(self.child2)#added child
        self.fam.childrenObjects.append(self.child3)#added child
        self.fam.childrenObjects.append(self.child4)#added child
        self.fam.childrenObjects.append(self.child5)#added child

    def test_5kidsBornSameBirthDate(self):
        child = self.child
        child1 = self.child1
        child2 = self.child2
        child3 = self.child3
        child4 = self.child4
        child5 = self.child5
        fam = self.fam
        child.birthDateObject = datetime(2013,4,14)
        child1.birthDateObject = datetime(2013,9,14)
        child2.birthDateObject = datetime(2013,9,14)
        child3.birthDateObject = datetime(2013,9,14)
        child4.birthDateObject = datetime(2013,9,14)
        child5.birthDateObject = datetime(2013,9,14)
        US16_Multiple_births(fam)
        self.assertEqual(len(fam.anomalies), 1)
        self.assertEqual(fam.anomalies, ["Too many births at one time"])  

    def test_SiblingsBornDiffYears(self):
        child = self.child
        child1 = self.child1
        child2 = self.child2
        child3 = self.child3
        child4 = self.child4
        child5 = self.child5
        fam = self.fam
        child.birthDateObject = datetime(2013,7,14)
        child1.birthDateObject = datetime(2014,9,14)
        child2.birthDateObject = datetime(2015,9,14)
        child3.birthDateObject = datetime(2016,9,14)
        child4.birthDateObject = datetime(2017,9,14)
        child5.birthDateObject = datetime(2018,9,14)
        US16_Multiple_births(fam)
        self.assertEqual(len(fam.anomalies), 0)
        self.assertEqual(fam.anomalies, [])  

    def test_SixSiblingsBornSameTime(self):   
        child = self.child
        child1 = self.child1
        child2 = self.child2
        child3 = self.child3
        child4 = self.child4
        child5 = self.child5
        child6 = Individual("I7")
        fam = self.fam
        fam.childrenObjects.append(child6)#added child
        child.birthDateObject = datetime(2013,9,14)
        child1.birthDateObject = datetime(2013,9,14)
        child2.birthDateObject = datetime(2013,9,14)
        child3.birthDateObject = datetime(2013,9,14)
        child4.birthDateObject = datetime(2013,9,14)
        child5.birthDateObject = datetime(2013,9,14)
        child6.birthDateObject = datetime(2010,10,23)
        US16_Multiple_births(fam)
        self.assertEqual(len(fam.anomalies), 1)
        self.assertEqual(fam.anomalies, ["Too many births at one time"])  

        
    def test_twoTriplets(self):
        child = self.child
        child1 = self.child1
        child2 = self.child2
        child3 = self.child3
        child4 = self.child4
        child5 = self.child5
        fam = self.fam
        child.birthDateObject = datetime(2013,9,14)
        child1.birthDateObject = datetime(2013,9,14)
        child2.birthDateObject = datetime(2013,9,14)
        child3.birthDateObject = datetime(2016,11,14)
        child4.birthDateObject = datetime(2016,11,14)
        child5.birthDateObject = datetime(2016,11,14)
        US16_Multiple_births(fam)
        self.assertEqual(len(fam.anomalies), 0)
        self.assertEqual(fam.anomalies, []) 
 
    
if __name__ == "__main__": 
    unittest.main()