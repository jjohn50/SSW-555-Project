# US21 - Jenn
# wife - get mom famc and dad family id
#husband mom famc and dad famc and compare moms and 
def US21_first_cousins_should_not_marry_anomaly(fam):
    wifeMom = wifeDad = husbandMom = husbandDad = ""
    try:
        wifeMom = fam.wifeObject.childFamilyObject.wifeObject.childFamilyObject
    except AttributeError:
        pass
    try:
        wifeDad = fam.wifeObject.childFamilyObject.husbandObject.childFamilyObject
    except AttributeError:
        pass
    try:
        husbandMom = fam.husbandObject.childFamilyObject.wifeObject.childFamilyObject
    except AttributeError:
        pass
    try:
        husbandDad = fam.husbandObject.childFamilyObject.husbandObject.childFamilyObject
    except AttributeError:
        pass
    if wifeMom != "":
        if (husbandMom != "" and wifeMom == husbandMom) or (husbandDad != "" and wifeMom == husbandDad):
            fam.anomalies.append("First cousins should not marry")
    if wifeDad != "":
        if (husbandMom  != "" and wifeDad == husbandMom) or (husbandDad != "" and wifeDad == husbandDad):
            fam.anomalies.append("First cousins should not marry")        

# US22 - Jenn
   
# US23 - Matt


# US24 - Matt


# US25 - Justin


# US26 - Justin


# US27 - Angie


# US28 - Angie


# US29 - Liv
### THIS ALREADY EXISTS

# US30 - Liv
