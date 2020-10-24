from datetime import datetime
import math 
# US11 - Jenn

# US12 - Jenn

# US13 - Justin
# def US13_FatherDeath_Before_Child_Birth(fam):      
#     for child in fam.childrenObjects:
#         if(abs(fam.husbandObject.deathDateObject-child.birthDateObject).days) > 274:
#             fam.anomalies.append("Child was born after 9 months after death of father")

#Mother should be less than 60 years older than her children and father should be less than 80 years older than his children 
def US14_Parents_not_too_old(fam):
    for child in fam.childrenObjects:
        day1 = fam.wifeObject.birthDateObject
        day2 = child.birthDateObject
        day3 = (((day2 - day1).days)/365)
        day4 = fam.husbandObject.birthDateObject
        day5 = child.birthDateObject 
        day6 = (((day5 - day4).days)/365) 
        if day3 >= 60 :
            fam.anomalies.append("Mother is 60 years older than child/ren")
        if day6 >= 80:
            fam.anomalies.append("Father is 80 years older than child/ren")

def US15_Siblings_Spacing(fam):
        for child in fam.childrenObjects:
            day1 = child.birthDateObject
            day2 = child.birthDateObject 
            day3 = (abs((day2 - day1).days))
            if day3 > 2 or day3 < 240:
                fam.anomalies.append("Siblings were born too close together")

# US16 - Matt goal Multiple births <= 5 US16_mutiplebirths 
# US17 - Liv

# US18 - Liv

# US19 - Angie

# US20 - Angie
def US20_siblings_should_not_marry_anomaly(fam):
    if fam.husbandObject.childFamilyObject != "" and fam.husbandObject.childFamilyObject == fam.wifeObject.childFamilyObject:
        fam.anomalies.append("Siblings should not marry")