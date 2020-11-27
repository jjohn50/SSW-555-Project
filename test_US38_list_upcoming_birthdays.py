from datetime import datetime
import unittest
from parse_gedcom.parser import Individual
from parse_gedcom.sprint4_user_stories import US38_list_upcoming_birthdays

class Test(unittest.TestCase):

    def setUp(self):
        self.person1 = Individual("I1")
        self.individuals = [self.person1]
    
    def test_upcoming_bday_alive(self):
        person1 = self.person1
        person1.alive = True
        person1.birthDateObject = datetime(1999, 12, 25)
        person1.age = 20
        self.assertEqual(US38_list_upcoming_birthdays(self.individuals), [person1])

    def test_upcoming_bday_dead(self):
        person1 = self.person1
        person1.alive = False
        person1.birthDateObject = datetime(1999, 12, 25)
        person1.age = 20
        self.assertEqual(US38_list_upcoming_birthdays(self.individuals), [])
    
    def test_not_upcoming_bday_alive(self):
        person1 = self.person1
        person1.alive = True
        person1.birthDateObject = datetime(1999, 8, 30)
        person1.age = 21
        self.assertEqual(US38_list_upcoming_birthdays(self.individuals), [])

if __name__ == "__main__":
    unittest.main()
    print(datetime.now())
