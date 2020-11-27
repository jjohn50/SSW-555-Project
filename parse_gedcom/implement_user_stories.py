from parser import individuals, families
from sprint1_user_stories import *
from sprint2_user_stories import *
from sprint3_user_stories import *
from sprint4_user_stories import *

# individual errors and anomalies
def check_individuals_for_errors_and_anomalies():
  US24_Unique_IDs(individuals,"individuals")
  US25_unique_birthday_and_name(individuals)
  for indiv in individuals:
    US01_check_date_before_today_error(indiv,"Birth")
    if indiv.alive == False:
      US01_check_date_before_today_error(indiv,"Death")
    US03_check_birth_before_death_error(indiv)
    US07_check_age_less_than_150_error(indiv)
    US11_no_bigamy_anomaly(indiv)
    US28_corresponding_individual_entries_error(indiv)
    
    
# family errors and anomalies
def check_families_for_errors_and_anomalies():
  US24_Unique_IDs(families,"families")
  US26_Unique_fam(families)
  for fam in families:
    US01_check_date_before_today_error(fam,"Marriage")
    if fam.divorced == True:
      US01_check_date_before_today_error(fam,"Divorce")
    US02_birth_before_marriage_error(fam)
    US04_check_marriage_before_spouse_death_error(fam)
    US05_check_marriage_before_divorce_error(fam)
    US06_check_divorce_before_spouse_death_error(fam)
    US08_check_child_birth_before_mother_death_error(fam)
    US09_check_child_birth_before_marriage_anomaly(fam)
    US10_check_marriage_after_14_anomaly(fam)
    US12_check_child_birth_after_divorce_anomaly(fam)
    US13_fatherdeath_before_child_birth(fam)
    US14_Parents_not_too_old(fam)
    US15_Siblings_Spacing(fam)
    US16_Multiple_births(fam) 
    US17_fewer_than_15_siblings_anomaly(fam)
    US18_male_last_names_anomaly(fam)
    US19_no_marriages_to_descendants_anomaly(fam)
    US20_siblings_should_not_marry_anomaly(fam)
    US21_first_cousins_should_not_marry_anomaly(fam)
    US22_aunt_uncle_should_not_marry_anomaly(fam)
    US23_Correct_gender_for_role(fam)
    US27_no_duplicate_children_error(fam)
    US28_corresponding_family_entries_error(fam)
    US30_large_age_gaps_between_couples_anomalies(fam)

def print_lists():
  US33_print_living_married(families)
  US38_print_upcoming_birthdays(individuals)
  US39_print_upcoming_anniversaries(families)