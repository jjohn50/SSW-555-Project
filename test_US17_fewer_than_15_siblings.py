import unittest
from parse_gedcom.parser import Individual, Family
from parse_gedcom.sprint2_user_stories import US17_fewer_than_15_siblings_anomaly

class Test(unittest.TestCase):  
    
    def setUp(self):
        self.testFam = Family("F1")
        self.testFam.childrenObjects.append(Individual("C1"))
        self.testFam.childrenObjects.append(Individual("C2"))
        self.testFam.childrenObjects.append(Individual("C3"))
        self.testFam.childrenObjects.append(Individual("C4"))
        self.testFam.childrenObjects.append(Individual("C5"))
        self.testFam.childrenObjects.append(Individual("C6"))
        self.testFam.childrenObjects.append(Individual("C7"))
        self.testFam.childrenObjects.append(Individual("C8"))
        self.testFam.childrenObjects.append(Individual("C9"))
        self.testFam.childrenObjects.append(Individual("C10"))
        self.testFam.childrenObjects.append(Individual("C11"))
        self.testFam.childrenObjects.append(Individual("C12"))
        self.testFam.childrenObjects.append(Individual("C13"))
        self.testFam.childrenObjects.append(Individual("C14"))
        
    def test_fewer_than_15_siblings(self):
        US17_fewer_than_15_siblings_anomaly(self.testFam)
        self.assertEqual(len(self.testFam.anomalies), 0)

    def test_15_siblings(self):
        testFam = self.testFam
        testFam.childrenObjects.append(Individual("C15"))
        US17_fewer_than_15_siblings_anomaly(testFam)
        self.assertEqual(len(testFam.anomalies), 1)
        self.assertEqual(testFam.anomalies[0], "There should be fewer than 15 siblings in a family")

    def test_more_than_15_siblings(self):
        testFam = self.testFam
        testFam.childrenObjects.append(Individual("C15"))
        testFam.childrenObjects.append(Individual("C16"))
        US17_fewer_than_15_siblings_anomaly(testFam)
        self.assertEqual(len(testFam.anomalies), 1)
        self.assertEqual(testFam.anomalies[0], "There should be fewer than 15 siblings in a family")

    def test_no_children(self):
        testFam2 = Family("F2")
        self.assertEqual(len(testFam2.anomalies), 0)

    def test_no_siblings(self):
        testFam3 = Family("F3")
        testFam3.childrenObjects.append(Individual("C1"))
        self.assertEqual(len(testFam3.anomalies), 0)

if __name__ == "__main__":
    unittest.main()