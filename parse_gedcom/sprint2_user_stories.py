from datetime import datetime
import math 


# US11 - Jenn

       
# US12 - Jenn- no more than 9 months after divorce
def US12_check_child_birth_after_divorce_anomaly(fam):
  if fam.divorced == True:
    for child in fam.childrenObjects: 
      if (((child.birthDateObject-fam.divorceDateObject).days)/30) > 9:
        fam.anomalies.append(child.Id + " born over 9 months after parents divorced")  
        
        
# US13 - Justin

# US14 - Justin

# US15 - Matt
def US15_Siblings_Spacing(fam):
    for i in range(0, len(fam.childrenObjects)-1):
        day1 = fam.childrenObjects[i].birthDateObject
        for j in range(i+1, len(fam.childrenObjects)):
            day2 = fam.childrenObjects[j].birthDateObject
            day3 = (abs((day2 - day1).days))
            if day3 > 2 and day3 < 274:
                fam.anomalies.append("Siblings were born too close together")

# US16 - Matt
def US16_Multiple_births(fam):
    for i in range(0,len(fam.childrenObjects)-1):
        birthday = fam.childrenObjects[i].birthDateObject
        counterId=1
        for j in range(i+1, len(fam.childrenObjects)):
            birthday2 = fam.childrenObjects[j].birthDateObject
            if birthday == birthday2:
                counterId = counterId+1 
        if counterId >= 5:
            fam.anomalies.append("Too many births at one time")
            break

# US17 - Liv
def  US17_fewer_than_15_siblings_anomaly(fam):
    if len(fam.childrenObjects) >= 15:
        fam.anomalies.append("There should be fewer than 15 siblings in a family")

# US18 - Liv
def US18_male_last_names_anomaly(fam):
    lastName = fam.husbandObject.name.split('/')[1]
    for child in fam.childrenObjects:
        if child.gender == 'M':
            if lastName != child.name.split('/')[1]:
                fam.anomalies.append("Males of the same family should have the same last name")


# US19 - Angie
def US19_no_marriages_to_descendants_anomaly(fam):
    if (fam.husbandObject.childFamilyObject in fam.wifeObject.spouseFamilyObjects) or (fam.wifeObject.childFamilyObject in fam.husbandObject.spouseFamilyObjects):
        fam.anomalies.append("Parents should not marry their children")

# US20 - Angie
def US20_siblings_should_not_marry_anomaly(fam):
    if fam.husbandObject.childFamilyObject != "" and fam.husbandObject.childFamilyObject == fam.wifeObject.childFamilyObject:
        fam.anomalies.append("Siblings should not marry")