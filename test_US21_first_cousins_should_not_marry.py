import unittest
from parse_gedcom.parser import Individual, Family
from parse_gedcom.sprint3_user_stories import US21_first_cousins_should_not_marry_anomaly

class Test(unittest.TestCase):

    def setUp(self):
        self.husband = Individual("I1")
        self.wife = Individual("I2")
        self.testFam1 = Family("F1")
        self.testFam1.husbandObject = self.husband
        self.testFam1.wifeObject = self.wife

        self.husbandMom = Individual("I3")
        self.husbandDad = Individual("I4")
        self.testFam2 = Family("F2")
        self.testFam2.husbandObject = self.husbandDad
        self.testFam2.wifeObject = self.husbandMom
        self.testFam2.childrenObjects.append(self.husband)
        self.testFam2.childrenIds.append(self.husband)
        self.husband.childFamilyObject = self.testFam2
        
        self.wifeMom = Individual("I5")
        self.wifeDad = Individual("I6")
        self.testFam3 = Family("F3")
        self.testFam3.husbandObject = self.wifeDad
        self.testFam3.wifeObject = self.wifeMom
        self.testFam3.childrenObjects.append(self.wife)
        self.testFam3.childrenIds.append(self.wife)
        self.wife.childFamilyObject = self.testFam3

    def test_first_cousins_are_not_married(self):
        husband = self.husband
        wife = self.wife
        testFam1 = self.testFam1
        testFam2 = self.testFam2
        testFam3 = self.testFam3
        US21_first_cousins_should_not_marry_anomaly(testFam1)
        self.assertEqual(len(testFam1.anomalies), 0)
        self.assertEqual(testFam1.anomalies, [])

    def test_first_cousins_are_married(self):
        husband = self.husband
        wife = self.wife
        testFam1 = self.testFam1
        testFam2 = self.testFam2
        testFam3 = self.testFam3
        testFam4 = Family("F4")
        testFam2.husbandObject.childFamilyObject = testFam4
        testFam3.wifeObject.childFamilyObject = testFam4
        US21_first_cousins_should_not_marry_anomaly(testFam1)
        self.assertEqual(len(testFam1.anomalies), 1)
        self.assertEqual(testFam1.anomalies[0], "First cousins should not marry")

    def test_first_cousins_are_married_null_parent(self):
        husband = self.husband
        wife = self.wife
        testFam1 = self.testFam1
        testFam2 = self.testFam2
        testFam3 = self.testFam3
        testFam4 = Family("F4")
        testFam2.husbandObject.childFamilyObject = testFam4
        testFam2.wifeObject = ""
        testFam3.wifeObject.childFamilyObject = testFam4
        testFam3.husbandObject = ""
        US21_first_cousins_should_not_marry_anomaly(testFam1)
        self.assertEqual(len(testFam1.anomalies), 1)
        self.assertEqual(testFam1.anomalies[0], "First cousins should not marry")

if __name__ == "__main__":
    unittest.main()
