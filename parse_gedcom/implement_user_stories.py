from parser import individuals, families
from sprint1_user_stories import *
from sprint2_user_stories import *
from sprint3_user_stories import *

# individual errors and anomalies
def check_individuals_for_errors_and_anomalies():
  US24_Unique_IDs(individuals, "individuals")
  for indiv in individuals:
    US01_check_date_before_today_error(indiv,"Birth")
    if indiv.alive == False:
      US01_check_date_before_today_error(indiv,"Death")
    US03_check_birth_before_death_error(indiv)
    US07_check_age_less_than_150_error(indiv)
    US11_no_bigamy_anomaly(indiv)
    
# family errors and anomalies
def check_families_for_errors_and_anomalies():
  US24_Unique_IDs(families,"families")
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