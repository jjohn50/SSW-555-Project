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
# No more than one child with the same name and birth date should appear in a family
def US27_no_duplicate_children_error(fam):
    if len(fam.childrenObjects) > 1:
        duplicates = {}
        for i in range(0,len(fam.childrenObjects)-1): #index child A
            if fam.childrenObjects[i].Id not in str(duplicates.items()):
                duplicates.update({fam.childrenObjects[i].Id:[]})
                for j in range(i+1,len(fam.childrenObjects)): #index child B
                    if fam.childrenObjects[i].name == fam.childrenObjects[j].name and fam.childrenObjects[i].birthDateObject == fam.childrenObjects[j].birthDateObject:
                        duplicates[fam.childrenObjects[i].Id].append(fam.childrenObjects[j].Id)
        for key, value in duplicates.items():
            if value != []:
                errorMsg = "Duplicate children: " + key
                for childId in value:
                    errorMsg += ", " + childId
                fam.errors.append(errorMsg)

# US28 - Angie
# All family roles (spouse, child) specified in an individual record should have corresponding entries in the corresponding family records. 
# Likewise, all individual roles (spouse, child) specified in family records should have corresponding entries in the corresponding individual's records.
def US28_corresponding_individual_entries_error(indiv):
    if indiv.childFamilyObject != "" and indiv not in indiv.childFamilyObject.childrenObjects:
        indiv.errors.append("Individual not found as child in " + indiv.childFamilyObject.Id)
    for spouseFamily in indiv.spouseFamilyObjects:
        if indiv != spouseFamily.husbandObject and indiv != spouseFamily.wifeObject:
            indiv.errors.append("Individual not found as spouse in " + spouseFamily.Id)

def US28_corresponding_family_entries_error(fam):
    if fam.husbandObject != "" and fam not in fam.husbandObject.spouseFamilyObjects:
        fam.errors.append("Corresponding spouse family not listed for husband individual")
    if fam.wifeObject != "" and fam not in fam.wifeObject.spouseFamilyObjects:
        fam.errors.append("Corresponding spouse family not listed for wife individual")
    for child in fam.childrenObjects:
        if child.childFamilyObject != fam:
            fam.errors.append("Corresponding child family not listed for " + child.Id)

# US29 - Liv
### THIS ALREADY EXISTS

# US30 - Liv
def US30_large_age_gaps_between_couples_anomalies(fam):
    if(fam.wifeObject.age > (fam.husbandObject.age * 2)):
        fam.anomalies.append("Wife is more than twice the age of the Husband")
    if(fam.husbandObject.age > (fam.wifeObject.age * 2)):
        fam.anomalies.append("Husband is more than twice the age of the Wife")
