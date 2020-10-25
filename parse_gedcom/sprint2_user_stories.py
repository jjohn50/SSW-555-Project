# US11 - Jenn

# US12 - Jenn

# US13 - Justin
#Justin John 
#US 13 Child should be born before 9 months after death of father
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
# #Justin John 
# #Mother should be less than 60 years older than her children and father should be less than 80 years older than his children 
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

# US15 - Mat# t
# 
# US16 - Mat# t
# 
# US17 - Liv 
# def US16__:()famfor child in f
#   am.childrenObjects:
# US18 - Liv
 
# US19 - Angie

# US20 - Angie
def US20_siblings_should_not_marry_anomaly(fam):
    if fam.husbandObject.childFamilyObject != "" and fam.husbandObject.childFamilyObject == fam.wifeObject.childFamilyObject:
        fam.anomalies.append("Siblings should not marry")