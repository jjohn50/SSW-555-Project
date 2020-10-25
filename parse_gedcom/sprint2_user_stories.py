from datetime import datetime
import math 
# US11 - Jenn

# US12 - Jenn

def US15_Siblings_Spacing(fam):
    for i in range(0, len(fam.childrenObjects)-1):
        day1 = fam.childrenObjects[i].birthDateObject
        for j in range(i+1, len(fam.childrenObjects)):
            day2 = fam.childrenObjects[j].birthDateObject
            day3 = (abs((day2 - day1).days))
            if day3 > 2 and day3 < 274:
                fam.anomalies.append("Siblings were born too close together")


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
        
        
# we need to look at all children
# then we need to save the bday of child
# set count id = 0
# then  we need to compare that child with all their siblng
# if have same b day increment count
# then before iterating to next child (outside second for within first) check if count >= 5
# if it is then append the error

# US17 - Liv

# US18 - Liv

# US19 - Angie

# US20 - Angie
def US20_siblings_should_not_marry_anomaly(fam):
    if fam.husbandObject.childFamilyObject != "" and fam.husbandObject.childFamilyObject == fam.wifeObject.childFamilyObject:
        fam.anomalies.append("Siblings should not marry")