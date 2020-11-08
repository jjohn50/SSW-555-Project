import unittest
from datetime import datetime
from parse_gedcom.parser import Individual, Family
from parse_gedcom.sprint3_user_stories import US27_no_duplicate_children_error

class Test(unittest.TestCase):

    def setUp(self):
        self.testFam = Family("F1")
        self.child1a = Individual("I1a")
        self.child1b = Individual("I1b")
        self.child2 = Individual("I2")
        self.child3a = Individual("I3a")
        self.child3b = Individual("I3b")
        self.child3c = Individual("I3c")
        self.child1a.name = self.child1b.name = "Another Child 1"
        self.child2.name = "Unique Child 2"
        self.child3a.name = self.child3b.name = self.child3c.name = "Another Child 3"
        self.child1a.birthDateObject = self.child1b.birthDateObject = datetime(2019, 5, 3)
        self.child2.birthDateObject = datetime(2019, 5, 3)
        self.child3a.birthDateObject = self.child3c.birthDateObject = datetime(2018, 5, 3)        

    def test_duplicate_children(self):
        testFam = self.testFam
        testFam.childrenObjects = [self.child1a, self.child1b, self.child2, self.child3a, self.child3b, self.child3c]
        US27_no_duplicate_children_error(testFam)
        self.assertEqual(len(testFam.errors), 2)
        self.assertEqual(testFam.errors[0], "Duplicate children: I1a, I1b")
        self.assertEqual(testFam.errors[1], "Duplicate children: I3a, I3c")

    def test_no_duplicate_children(self):
        testFam = self.testFam
        self.child1b.birthDateObject = self.child3a.birthDateObject = datetime(2017, 5, 3)
        testFam.childrenObjects = [self.child1a, self.child1b, self.child2, self.child3a, self.child3b, self.child3c]
        US27_no_duplicate_children_error(testFam)
        self.assertEqual(len(testFam.errors), 0)
        self.assertEqual(testFam.errors, [])

    def test_no_children(self):
        testFam = self.testFam
        US27_no_duplicate_children_error(testFam)
        self.assertEqual(len(testFam.errors), 0)
        self.assertEqual(testFam.errors, [])

if __name__ == "__main__":
    unittest.main()
