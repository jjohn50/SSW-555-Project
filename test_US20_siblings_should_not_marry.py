import unittest
from parse_gedcom.parser import Individual, Family
from parse_gedcom.sprint2_user_stories import US20_siblings_should_not_marry_anomaly

class Test(unittest.TestCase):

    def setUp(self):
        self.husband = Individual("I1")
        self.wife = Individual("I2")
        self.testFam1 = Family("F1")
        self.testFam1.husbandObject = self.husband
        self.testFam1.wifeObject = self.wife
    
    def test_same_child_fam(self):
        husband = self.husband
        wife = self.wife
        testFam1 = self.testFam1
        testFam2 = Family("F2")
        husband.childFamilyObject = testFam2
        wife.childFamilyObject = testFam2
        US20_siblings_should_not_marry_anomaly(testFam1)
        self.assertEqual(len(testFam1.anomalies), 1)
        self.assertEqual(testFam1.anomalies[0], "Siblings should not marry")

    def test_different_child_fam(self):
        husband = self.husband
        wife = self.wife
        testFam1 = self.testFam1
        testFam2 = Family("F2")
        testFam3 = Family("F3")
        husband.childFamilyObject = testFam2
        wife.childFamilyObject = testFam3
        US20_siblings_should_not_marry_anomaly(testFam1)
        self.assertEqual(len(testFam1.anomalies), 0)
        self.assertEqual(testFam1.anomalies, [])

    def test_only_husband_child_fam_set(self):
        husband = self.husband
        wife = self.wife
        testFam1 = self.testFam1
        testFam2 = Family("F2")
        husband.childFamilyObject = testFam2
        US20_siblings_should_not_marry_anomaly(testFam1)
        self.assertEqual(len(testFam1.anomalies), 0)
        self.assertEqual(testFam1.anomalies, [])

    def test_only_wife_child_fam_set(self):
        husband = self.husband
        wife = self.wife
        testFam1 = self.testFam1
        testFam2 = Family("F2")
        wife.childFamilyObject = testFam2
        US20_siblings_should_not_marry_anomaly(testFam1)
        self.assertEqual(len(testFam1.anomalies), 0)
        self.assertEqual(testFam1.anomalies, [])
    
    def test_neither_child_fam_set(self):
        husband = self.husband
        wife = self.wife
        testFam1 = self.testFam1
        US20_siblings_should_not_marry_anomaly(testFam1)
        self.assertEqual(len(testFam1.anomalies), 0)
        self.assertEqual(testFam1.anomalies, [])

if __name__ == "__main__":
    unittest.main()
