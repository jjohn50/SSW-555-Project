import unittest
from datetime import datetime
from parse_gedcom.parser import Individual, Family
from parse_gedcom.sprint4_user_stories import US35_list_multiple_births

class Test(unittest.TestCase):

    def setUp(self):
        self.child1 = Individual("I1")
        self.child2 = Individual("I2")
        self.child3 = Individual("I3")
        self.child4 = Individual("I4")
        self.child5 = Individual("I5")
        self.child1.name = "Child 1"
        self.child2.name = "Child 2"
        self.child3.name = "Child 3"
        self.child4.name = "Child 4"
        self.child5.name = "Child 5"
        self.testFam = Family("F1")
        self.testFam.childrenObjects = [self.child1, self.child2, self.child3, self.child4, self.child5]
        self.families = [self.testFam]
    
    def test_quintuplets(self):
        self.child1.birthDateObject = datetime(2013,9,14)
        self.child2.birthDateObject = datetime(2013,9,14)
        self.child3.birthDateObject = datetime(2013,9,14)
        self.child4.birthDateObject = datetime(2013,9,15)
        self.child5.birthDateObject = datetime(2013,9,15)
        self.assertEqual(US35_list_multiple_births(self.families), ["F1: Child 1 (I1), Child 2 (I2), Child 3 (I3), Child 4 (I4), Child 5 (I5)"])

    def test_quadruplets(self):
        self.child1.birthDateObject = datetime(2013,9,14)
        self.child2.birthDateObject = datetime(2013,9,14)
        self.child3.birthDateObject = datetime(2013,9,15)
        self.child4.birthDateObject = datetime(2013,9,15)
        self.child5.birthDateObject = datetime(2014,9,1)
        self.assertEqual(US35_list_multiple_births(self.families), ["F1: Child 1 (I1), Child 2 (I2), Child 3 (I3), Child 4 (I4)"])

    def test_triplets_twins(self):
        self.child1.birthDateObject = datetime(2013,9,14)
        self.child2.birthDateObject = datetime(2013,9,14)
        self.child3.birthDateObject = datetime(2013,9,15)
        self.child4.birthDateObject = datetime(2014,9,5)
        self.child5.birthDateObject = datetime(2014,9,6)
        self.assertEqual(US35_list_multiple_births(self.families), ["F1: Child 1 (I1), Child 2 (I2), Child 3 (I3)", "F1: Child 4 (I4), Child 5 (I5)"])

    def test_two_sets_of_twins(self):
        self.child1.birthDateObject = datetime(2013,12,24)
        self.child2.birthDateObject = datetime(2013,12,25)
        self.child3.birthDateObject = datetime(2014,2,2)
        self.child4.birthDateObject = datetime(2016,9,5)
        self.child5.birthDateObject = datetime(2016,9,6)
        self.assertEqual(US35_list_multiple_births(self.families), ["F1: Child 1 (I1), Child 2 (I2)", "F1: Child 4 (I4), Child 5 (I5)"])

    def test_no_duplicates(self):
        self.child1.birthDateObject = datetime(2012,9,14)
        self.child2.birthDateObject = datetime(2013,12,24)
        self.child3.birthDateObject = datetime(2014,12,25)
        self.child4.birthDateObject = datetime(2015,9,5)
        self.child5.birthDateObject = datetime(2016,9,6)
        self.assertEqual(US35_list_multiple_births(self.families), [])

if __name__ == "__main__":
    unittest.main()
