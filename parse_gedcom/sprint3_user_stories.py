# US21 - Jenn


# US22 - Jenn 
def US22_aunt_uncle_should_not_marry_anomaly(fam):
    uncle = aunt = wifeMom = wifeDad = husbandMom = husbandDad = ""
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
    try:
        uncle = fam.husbandObject.childFamilyObject
    except AttributeError:
        pass
    try:
        aunt = fam.wifeObject.childFamilyObject
    except AttributeError:
        pass
    if aunt != "":
        if (husbandMom != "" and aunt == husbandMom) or (husbandDad != "" and aunt == husbandDad):
            fam.anomalies.append("Aunts should not marry nephews")
    if uncle != "":
        if (wifeMom  != "" and uncle == wifeMom) or (wifeDad != "" and uncle == wifeDad):
            fam.anomalies.append("Uncles should not marry neices")        

        
# US23 - Matt


# US24 - Matt


# US25 - Justin


# US26 - Justin


# US27 - Angie


# US28 - Angie


# US29 - Liv
### THIS ALREADY EXISTS

# US30 - Liv
