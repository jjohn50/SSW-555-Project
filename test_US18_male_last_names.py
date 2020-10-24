import unittest
from parse_gedcom.parser import Individual, Family
from parse_gedcom.sprint2_user_stories import US18_male_last_names_anomaly

class Test(unittest.TestCase):

    def setUp(self):
        self.husband = Individual("I1")
        self.husband.name = "John /Doe/"
        self.testFam1 = Family("F1")
        self.testFam1.husbandObject = self.husband
    
    def test_no_children(self):
        testFam1 = self.testFam1
        US18_male_last_names_anomaly(testFam1)
        self.assertEqual(len(testFam1.anomalies), 0)

    def test_no_son(self):
        testFam1 = self.testFam1
        daughter = Individual("I2")
        daughter.gender = 'F'
        daughter.name = "Jane /Smith/"
        testFam1.childrenObjects.append(daughter)
        US18_male_last_names_anomaly(testFam1)
        self.assertEqual(len(testFam1.anomalies), 0)
        self.assertEqual(testFam1.anomalies, [])

    def test_son_different_name(self):
        testFam1 = self.testFam1
        son = Individual("I2")
        son.gender = 'M'
        son.name = "John /Smith/"
        testFam1.childrenObjects.append(son)
        US18_male_last_names_anomaly(testFam1)
        self.assertEqual(len(testFam1.anomalies), 1)
        self.assertEqual(testFam1.anomalies[0], "Males of the same family should have the same last name")

    def test_son_same_name(self):
        testFam1 = self.testFam1
        son = Individual("I2")
        son.gender = 'M'
        son.name = "Jake /Doe/"
        testFam1.childrenObjects.append(son)
        US18_male_last_names_anomaly(testFam1)
        self.assertEqual(len(testFam1.anomalies), 0)
        self.assertEqual(testFam1.anomalies, [])
    
    def test_sons_and_daughters(self):
        testFam1 = self.testFam1
        son1 = Individual("I2")
        son1.gender = 'M'
        son1.name = "Jake /Doe/"
        testFam1.childrenObjects.append(son1)
        son2 = Individual("I3")
        son2.gender = 'M'
        son2.name = "John /Smith/"
        testFam1.childrenObjects.append(son2)
        son3 = Individual("I4")
        son3.gender = 'M'
        son3.name = "Jim /Brown/"
        testFam1.childrenObjects.append(son3)
        daughter1 = Individual("I5")
        daughter1.gender = 'F'
        daughter1.name = "Jane /Smith/"
        testFam1.childrenObjects.append(daughter1)
        daughter2 = Individual("I6")
        daughter2.gender = 'F'
        daughter2.name = "Jodi /Doe/"
        testFam1.childrenObjects.append(daughter2)
        US18_male_last_names_anomaly(testFam1)
        self.assertEqual(len(testFam1.anomalies), 2)
        self.assertEqual(testFam1.anomalies[1], "Males of the same family should have the same last name")

if __name__ == "__main__":
    unittest.main()
