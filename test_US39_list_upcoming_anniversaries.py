from datetime import datetime
import unittest
from parse_gedcom.parser import Family, Individual
from parse_gedcom.sprint4_user_stories import US39_list_upcoming_anniversaries

class Test(unittest.TestCase):

    def setUp(self):
        self.fam1 = Family("F1")
        self.wife = Individual("I1")
        self.wife.name = "Jane Doe"
        self.husband = Individual("I2")
        self.husband.name = "John  Doe"
        self.fam1.wife = self.wife
        self.fam1.husband = self.husband
        self.families = [self.fam1]

    def test_upcoming_anniv_married(self):
        fam1 = self.fam1
        fam1.divorced = False
        fam1.marriageDateObject = datetime(1999, 12, 25)
        self.assertEqual(US39_list_upcoming_anniversaries(self.families), [fam1])

    def test_upcoming_anniv_divorced(self):
        fam1 = self.fam1
        fam1.divorced = True
        fam1.marriageDateObject = datetime(1999, 12, 25)
        self.assertEqual(US39_list_upcoming_anniversaries(self.families), [])
    
    def test_not_upcoming_anniv_married(self):
        fam1 = self.fam1
        fam1.divorced = False
        fam1.marriageDateObject = datetime(1999, 8, 25)
        self.assertEqual(US39_list_upcoming_anniversaries(self.families), [])

if __name__ == "__main__":
    unittest.main()
    print(datetime.now())
