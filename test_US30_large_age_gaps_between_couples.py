import unittest
from parse_gedcom.parser import Individual, Family
from parse_gedcom.sprint3_user_stories import US30_large_age_gaps_between_couples_anomalies

class Test(unittest.TestCase):

    def setUp(self):
        self.husband = Individual("I1")
        self.wife = Individual("I2")
        self.testFam1 = Family("F1")
        self.testFam1.husbandObject = self.husband
        self.testFam1.wifeObject = self.wife
    
    def test_less_than_double_wife_older(self):
        husband = self.husband
        wife = self.wife
        testFam1 = self.testFam1
        husband.age = 25
        wife.age = 26
        US30_large_age_gaps_between_couples_anomalies(testFam1)
        self.assertEqual(len(testFam1.anomalies), 0)
        self.assertEqual(testFam1.anomalies, [])

    def test_less_than_double_husband_older(self):
        husband = self.husband
        wife = self.wife
        testFam1 = self.testFam1
        husband.age = 35
        wife.age = 26
        US30_large_age_gaps_between_couples_anomalies(testFam1)
        self.assertEqual(len(testFam1.anomalies), 0)
        self.assertEqual(testFam1.anomalies, [])

    def test_exactly_double_wife_older(self):
        husband = self.husband
        wife = self.wife
        testFam1 = self.testFam1
        husband.age = 25
        wife.age = 50
        US30_large_age_gaps_between_couples_anomalies(testFam1)
        self.assertEqual(len(testFam1.anomalies), 0)
        self.assertEqual(testFam1.anomalies, [])

    def test_exactly_double_husband_older(self):
        husband = self.husband
        wife = self.wife
        testFam1 = self.testFam1
        husband.age = 40
        wife.age = 20
        US30_large_age_gaps_between_couples_anomalies(testFam1)
        self.assertEqual(len(testFam1.anomalies), 0)
        self.assertEqual(testFam1.anomalies, [])

    def test_more_than_double_wife_older(self):
        husband = self.husband
        wife = self.wife
        testFam1 = self.testFam1
        husband.age = 30
        wife.age = 65
        US30_large_age_gaps_between_couples_anomalies(testFam1)
        self.assertEqual(len(testFam1.anomalies), 1)
        self.assertEqual(testFam1.anomalies[0], "Wife is more than twice the age of the Husband")
        
    def test_more_than_double_husband_older(self):
        husband = self.husband
        wife = self.wife
        testFam1 = self.testFam1
        husband.age = 50
        wife.age = 20
        US30_large_age_gaps_between_couples_anomalies(testFam1)
        self.assertEqual(len(testFam1.anomalies), 1)
        self.assertEqual(testFam1.anomalies[0], "Husband is more than twice the age of the Wife")

if __name__ == "__main__":
    unittest.main()
