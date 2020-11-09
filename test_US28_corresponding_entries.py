import unittest
from parse_gedcom.parser import Individual, Family
from parse_gedcom.sprint3_user_stories import US28_corresponding_individual_entries_error, US28_corresponding_family_entries_error

class Test(unittest.TestCase):

    def test_indiv_childFam_valid(self):
        indiv = Individual("I1")
        testFam = Family("F1")
        indiv.childFamilyObject = testFam
        testFam.childrenObjects.append(indiv)
        US28_corresponding_individual_entries_error(indiv)
        self.assertEqual(len(indiv.errors), 0)
        self.assertEqual(indiv.errors, [])
    
    def test_indiv_childFam_invalid(self):
        indiv = Individual("I1")
        testFam = Family("F1")
        indiv.childFamilyObject = testFam
        US28_corresponding_individual_entries_error(indiv)
        self.assertEqual(len(indiv.errors), 1)
        self.assertEqual(indiv.errors[0], "Individual not found as child in F1")

    def test_indiv_spouseFam_valid(self):
        indiv = Individual("I1")
        testFam = Family("F1")
        indiv.spouseFamilyObjects.append(testFam)
        testFam.wifeObject = indiv
        US28_corresponding_individual_entries_error(indiv)
        self.assertEqual(len(indiv.errors), 0)
        self.assertEqual(indiv.errors, [])
    
    def test_indiv_spouseFam_invalid(self):
        indiv = Individual("I1")
        testFam = Family("F1")
        indiv.spouseFamilyObjects.append(testFam)
        US28_corresponding_individual_entries_error(indiv)
        self.assertEqual(len(indiv.errors), 1)
        self.assertEqual(indiv.errors[0], "Individual not found as spouse in F1")
    
    def test_indiv_nullChildFam_nullSpouseFam_valid(self):
        indiv = Individual("I1")
        US28_corresponding_individual_entries_error(indiv)
        self.assertEqual(len(indiv.errors), 0)
        self.assertEqual(indiv.errors, [])

    def test_husband_spouseFam_valid(self):
        husband = Individual("I1")
        testFam = Family("F1")
        testFam.husbandObject = husband
        husband.spouseFamilyObjects.append(testFam)
        US28_corresponding_family_entries_error(testFam)
        self.assertEqual(len(testFam.errors), 0)
        self.assertEqual(testFam.errors, [])
    
    def test_husband_spouseFam_invalid(self):
        husband = Individual("I1")
        testFam = Family("F1")
        testFam.husbandObject = husband
        US28_corresponding_family_entries_error(testFam)
        self.assertEqual(len(testFam.errors), 1)
        self.assertEqual(testFam.errors[0], "Corresponding spouse family not listed for husband individual")

    def test_wife_spouseFam_valid(self):
        wife = Individual("I1")
        testFam = Family("F1")
        testFam.wifeObject = wife
        wife.spouseFamilyObjects.append(testFam)
        US28_corresponding_family_entries_error(testFam)
        self.assertEqual(len(testFam.errors), 0)
        self.assertEqual(testFam.errors, [])
    
    def test_wife_spouseFam_invalid(self):
        wife = Individual("I1")
        testFam = Family("F1")
        testFam.wifeObject = wife
        US28_corresponding_family_entries_error(testFam)
        self.assertEqual(len(testFam.errors), 1)
        self.assertEqual(testFam.errors[0], "Corresponding spouse family not listed for wife individual")
    
    def test_wife_spouseFam_valid_husband_spouseFam_invalid(self):
        wife = Individual("I1")
        husband = Individual("I2")
        testFam = Family("F1")
        testFam.wifeObject = wife
        testFam.husbandObject = husband
        wife.spouseFamilyObjects.append(testFam)
        US28_corresponding_family_entries_error(testFam)
        self.assertEqual(len(testFam.errors), 1)
        self.assertEqual(testFam.errors[0], "Corresponding spouse family not listed for husband individual")

    def test_wife_spouseFam_invalid_husband_spouseFam_invalid(self):
        wife = Individual("I1")
        husband = Individual("I2")
        testFam = Family("F1")
        testFam.wifeObject = wife
        testFam.husbandObject = husband
        US28_corresponding_family_entries_error(testFam)
        self.assertEqual(len(testFam.errors), 2)
        self.assertEqual(testFam.errors[0], "Corresponding spouse family not listed for husband individual")
        self.assertEqual(testFam.errors[1], "Corresponding spouse family not listed for wife individual")

    def test_nullHusband_nullWife_valid(self):
        testFam = Family("F1")
        US28_corresponding_family_entries_error(testFam)
        self.assertEqual(len(testFam.errors), 0)
        self.assertEqual(testFam.errors, [])

    def test_childFam_valid(self):
        child1 = Individual("I1")
        child2 = Individual("I2")
        testFam = Family("F1")
        child1.childFamilyObject = testFam
        child2.childFamilyObject = testFam
        testFam.childrenObjects = [child1, child2]
        US28_corresponding_family_entries_error(testFam)
        self.assertEqual(len(testFam.errors), 0)
        self.assertEqual(testFam.errors, [])

    def test_childFam_one_invalid(self):
        child1 = Individual("I1")
        child2 = Individual("I2")
        testFam = Family("F1")
        child1.childFamilyObject = testFam
        testFam.childrenObjects = [child1, child2]
        US28_corresponding_family_entries_error(testFam)
        self.assertEqual(len(testFam.errors), 1)
        self.assertEqual(testFam.errors[0], "Corresponding child family not listed for I2")

    def test_childFam_two_invalid(self):
        child1 = Individual("I1")
        child2 = Individual("I2")
        testFam = Family("F1")
        testFam.childrenObjects = [child1, child2]
        US28_corresponding_family_entries_error(testFam)
        self.assertEqual(len(testFam.errors), 2)
        self.assertEqual(testFam.errors[0], "Corresponding child family not listed for I1")
        self.assertEqual(testFam.errors[1], "Corresponding child family not listed for I2")

if __name__ == "__main__":
    unittest.main()
