# US21 - Jenn


# US22 - Jenn

        
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


# US29 - Liv
### THIS ALREADY EXISTS

# US30 - Liv
def US30_large_age_gaps_between_couples_anomalies(fam):
    if(fam.wifeObject.age > (fam.husbandObject.age * 2)):
        fam.anomalies.append("Wife is more than twice the age of the Husband")
    if(fam.husbandObject.age > (fam.wifeObject.age * 2)):
        fam.anomalies.append("Husband is more than twice the age of the Wife")
