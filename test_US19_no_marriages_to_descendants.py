import unittest
from datetime import datetime
from parse_gedcom.parser import Individual, Family
from parse_gedcom.sprint2_user_stories import US19_no_marriages_to_descendants_anomaly

class Test(unittest.TestCase):

    def setUp(self):
        self.husband = Individual("I1")
        self.wife = Individual("I2")
        self.testFam1 = Family("F1")
        self.testFam1.husbandObject = self.husband
        self.testFam1.wifeObject = self.wife
    
    def test_wife_is_mother_of_husband(self):
        husband = self.husband
        wife = self.wife
        testFam1 = self.testFam1
        testFam2 = Family("F2")
        wife.spouseFamilyObjects.append(testFam2)
        husband.childFamilyObject = testFam2
        US19_no_marriages_to_descendants_anomaly(testFam1)
        self.assertEqual(len(testFam1.anomalies), 1)
        self.assertEqual(testFam1.anomalies[0], "Parents should not marry their children")

    def test_husband_is_father_of_wife(self):
        husband = self.husband
        wife = self.wife
        testFam1 = self.testFam1
        testFam2 = Family("F2")
        testFam3 = Family("F3")
        husband.spouseFamilyObjects.append(testFam2)
        husband.spouseFamilyObjects.append(testFam3)
        wife.childFamilyObject = testFam3
        US19_no_marriages_to_descendants_anomaly(testFam1)
        self.assertEqual(len(testFam1.anomalies), 1)
        self.assertEqual(testFam1.anomalies[0], "Parents should not marry their children")

    def test_neither_spouse_is_parent_of_other(self):
        husband = self.husband
        wife = self.wife
        testFam1 = self.testFam1
        US19_no_marriages_to_descendants_anomaly(testFam1)
        self.assertEqual(len(testFam1.anomalies), 0)
        self.assertEqual(testFam1.anomalies, [])

if __name__ == "__main__":
    unittest.main()
