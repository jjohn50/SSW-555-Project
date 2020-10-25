import unittest
from datetime import datetime
from parse_gedcom.parser import Individual, Family
from parse_gedcom.sprint2_user_stories import US11_no_bigamy_anomaly

class Test(unittest.TestCase):

    def setUp(self):
        self.husband = Individual("I1")
        self.wife = Individual("I2")
        self.fam1 = Family("F1") 
        self.fam2 = Family("F2")
        self.fam3 = Family("F3") 
        self.fam1.marriageDateObject = datetime(2016, 5, 3)
        self.fam2.marriageDateObject = datetime(2018, 5, 3)
        self.fam3.marriageDateObject = datetime(2017, 5, 3)
        self.fam1.husbandObject = self.husband
        self.fam2.husbandObject = self.husband
        self.fam3.husbandObject = self.husband
        
    def test_overlapping_fam1_fam2_no_divorce_no_death(self):
        husband = self.husband
        fam1 = self.fam1
        fam2 = self.fam2
        husband.spouseFamilyObjects = [fam1, fam2]
        US11_no_bigamy_anomaly(husband)
        self.assertEqual(len(husband.anomalies), 1)
        self.assertEqual(husband.anomalies[0], "Bigamy")
    
    def test_overlapping_fam1_fam3_divorce_no_death(self):
        husband = self.husband
        fam1 = self.fam1
        fam3 = self.fam3
        fam3.divorced = True
        fam3.divorceDateObject = datetime(2018, 9, 7)
        husband.spouseFamilyObjects = [fam1, fam3]
        US11_no_bigamy_anomaly(husband)
        self.assertEqual(len(husband.anomalies), 1)
        self.assertEqual(husband.anomalies[0], "Bigamy")

    def test_overlapping_fam3_fam2_death_no_divorce(self):
        husband = self.husband
        fam2 = self.fam2
        fam3 = self.fam3
        spouse = self.wife
        spouse.alive = False
        spouse.deathDateObject = datetime(2019,5,3)
        husband.spouseFamilyObjects = [fam3, fam2]
        US11_no_bigamy_anomaly(husband)
        self.assertEqual(len(husband.anomalies), 1)
        self.assertEqual(husband.anomalies[0], "Bigamy")

    def test_not_overlapping_divorce(self):
        husband = self.husband
        fam1 = self.fam1
        fam3 = self.fam3
        fam1.divorced = True
        fam1.divorceDateObject = datetime(2016, 12, 7)
        husband.spouseFamilyObjects = [fam1, fam3]
        US11_no_bigamy_anomaly(husband)
        self.assertEqual(len(husband.anomalies), 0)
        self.assertEqual(husband.anomalies,[])
   
    # def test_not_overlapping_death(self):
    #     husband = self.husband
    #     fam1 = self.fam1
    #     fam3 = self.fam3
    #     wife = self.wife
    #     wife.alive = False
    #     wife.deathDateObject = datetime(2016,12,3)
    #     fam1.wifeObject = wife
    #     husband.spouseFamilyObjects = [fam1, fam3]
    #     US11_no_bigamy_anomaly(husband)
    #     self.assertEqual(len(husband.anomalies), 0)
    #     self.assertEqual(husband.anomalies,[])

    def test_no_marriages(self):
        husband = self.husband
        US11_no_bigamy_anomaly(husband)
        self.assertEqual(len(husband.anomalies), 0)
        self.assertEqual(husband.anomalies,[])

    def test_one_marriage(self):
        husband = self.husband
        fam1 = self.fam1
        husband.spouseFamilyObjects = [fam1]
        US11_no_bigamy_anomaly(husband)
        self.assertEqual(len(husband.anomalies), 0)
        self.assertEqual(husband.anomalies,[])

    def test_three_marriages_not_overlapping(self):
        husband = self.husband
        fam1 = self.fam1
        fam2 = self.fam2
        fam3 = self.fam3
        fam1.divorced = True
        fam1.divorceDateObject = datetime(2016, 12, 7)
        fam3.divorced = True
        fam3.divorceDateObject = datetime(2017, 12, 7)
        husband.spouseFamilyObjects = [fam1, fam2, fam3]
        US11_no_bigamy_anomaly(husband)
        self.assertEqual(len(husband.anomalies), 0)
        self.assertEqual(husband.anomalies,[])

    def test_three_marriages_fam2_fam3_overlapping(self):
        husband = self.husband
        fam1 = self.fam1
        fam2 = self.fam2
        fam3 = self.fam3
        fam1.divorced = True
        fam1.divorceDateObject = datetime(2016, 12, 7)
        husband.spouseFamilyObjects = [fam1, fam2, fam3]
        US11_no_bigamy_anomaly(husband)
        self.assertEqual(len(husband.anomalies), 1)
        self.assertEqual(husband.anomalies[0], "Bigamy")

if __name__ == "__main__":
    unittest.main()