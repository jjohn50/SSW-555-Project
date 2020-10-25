from datetime import datetime

# US11 - Jenn
def US11_no_bigamy_anomaly(indiv):  
    if len(indiv.spouseFamilyObjects) > 1:
        for i in range(0,len(indiv.spouseFamilyObjects)-1): #index first fam
            for j in range(i+1,len(indiv.spouseFamilyObjects)): #index for 2nd fam
                fam_i = indiv.spouseFamilyObjects[i]
                fam_j = indiv.spouseFamilyObjects[j]
                i_start = fam_i.marriageDateObject
                j_start = fam_j.marriageDateObject
                if fam_i.divorced == True:
                  i_end = fam_i.divorceDateObject
                elif fam_i.husbandObject != "" and fam_i.husbandObject.alive == False:
                  i_end = fam_i.husbandObject.deathDateObject
                elif fam_i.wifeObject != "" and fam_i.wifeObject.alive == False:
                  i_end = fam_i.wifeObject.deathDateObject
                else:
                  i_end = datetime.now()
                #j loop
                if fam_j.divorced == True:
                  j_end = fam_j.divorceDateObject
                elif fam_i.husbandObject != "" and fam_j.husbandObject.alive == False:
                  j_end = fam_j.husbandObject.deathDateObject
                elif fam_i.wifeObject != "" and fam_i.wifeObject.alive == False:
                  j_end = fam_j.wifeObject.deathDateObject
                else:
                  j_end = datetime.now()
                
                if (i_start < j_start and j_start < i_end) or (j_start < i_start and i_start < j_end):
                  indiv.anomalies.append("Bigamy")

# US12 - Jenn- no more than 9 months after divorce
def US12_check_child_birth_after_divorce_anomaly(fam):
  if fam.divorced == True:
    for child in fam.childrenObjects: 
      if (((child.birthDateObject-fam.divorceDateObject).days)/30) > 9:
        fam.anomalies.append(child.Id + " born over 9 months after parents divorced")  
        
# US13 - Justin
# Child should be born before 9 months after death of father
def US13_fatherdeath_before_child_birth(fam):
  # day1 = fam.husbandObject.DeathDateObject
  # day2 = fam.child.birthDateObject
  # day3 = (((day2 - day1).days))
  if fam.husbandObject.alive == False: 
    for child in fam.childrenObjects:
      day = (child.birthDateObject-fam.husbandObject.deathDateObject).days
      if day > 274: 
        fam.errors.append("Child was born after 9 months after death of father")

# US14 - Justin
# Mother should be less than 60 years older than her children and father should be less than 80 years older than his children 
def US14_Parents_not_too_old(fam):
  for child in fam.childrenObjects:
    day1 = fam.wifeObject.birthDateObject
    day2 = child.birthDateObject
    day3 = (((day2 - day1).days)/365)
    day4 = fam.husbandObject.birthDateObject 
    day5 = child.birthDateObject 
    day6 = (((day5 - day4).days)/365)
    if day3 >= 60:
      fam.anomalies.append("Mother is 60 years older than child/ren")
    if day6 >= 80:
      fam.anomalies.append("Father is 80 years older than child/ren") 

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