import unittest
from parse_gedcom.parser import Individual, Family
from parse_gedcom.sprint4_user_stories import US31_list_fam_with_no_errors_or_anomalies

class Test(unittest.TestCase):

    def setUp(self):
        self.husband = Individual("I1")
        self.wife = Individual("I2")
        self.testFam = Family("F1")
        self.families = [self.testFam]
        # self.testFam.husbandObject = self.husband
        # self.testFam.wifeObject = self.wife
      
    
    def test_no_errors_or_anomalies(self):
        husband = self.husband
        wife = self.wife
        testFam = self.testFam
        self.assertEqual(US31_list_fam_with_no_errors_or_anomalies(self.families), [testFam])

    def test_error(self):
        husband = self.husband
        wife = self.wife
        testFam = self.testFam
        testFam.errors.append("here's an error to test")
        self.assertEqual(US31_list_fam_with_no_errors_or_anomalies(self.families), [])

    def test_anomaly(self):
        husband = self.husband
        wife = self.wife
        testFam = self.testFam
        testFam.anomalies.append("here's an anomaly to test") 
        self.assertEqual(US31_list_fam_with_no_errors_or_anomalies(self.families), [])

    def test_anomaly_and_error(self):
        husband = self.husband
        wife = self.wife
        testFam = self.testFam
        testFam.anomalies.append("here's an anomaly to test") 
        testFam.errors.append("here's an error to test")
        self.assertEqual(US31_list_fam_with_no_errors_or_anomalies(self.families), [])


if __name__ == "__main__":
    unittest.main()
