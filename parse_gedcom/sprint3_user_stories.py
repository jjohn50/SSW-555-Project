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
def US23_Correct_gender_for_role(fam):
    if fam.husbandObject.gender == 'F':
        fam.errors.append("Husband is a female")
    if fam.wifeObject.gender == 'M':
        fam.errors.append("Wife is a male")
        
# US24 - Matt
def US24_Unique_IDs(id_list, identifier):
    duplicates = {}
    for obj in id_list:
        if obj.Id not in str(duplicates.items()):
            duplicates.update({obj.Id:[obj]})
        else:
            duplicates[obj.Id].append(obj)
    for key, value in duplicates.items():
        if len(value) > 1:
            errorMsg = "There are " + str(len(value)) + " " + identifier + " with id " + key
            for obj in value:
                obj.errors.append(errorMsg)

# US25 - Justin
# No more than one individual with the same name and birth date should appear in a GEDCOM file 
def US25_unique_birthday_and_name(id_list):
    duplicates = {}
    for obj in id_list:
        if obj.name + obj.birthDateString not in str(duplicates.items()):
            duplicates.update({obj.name + obj.birthDateString:[obj]})
        else: 
            duplicates[obj.name + obj.birthDateString].append(obj)
    for key, value in duplicates.items():
        if len(value) > 1:
            errorMsg = "There are " + str(len(value)) + " people with the same name and birthday"  
            for obj in value:
                obj.errors.append(errorMsg)   

# US26 - Justin
# No more than one family with the same spouses by name and the same marriage date should appear in a GEDCOM file 
def US26_Unique_fam(id_list):
  duplicates = {} 
  for obj in id_list:
    if obj.husbandObject.name + obj.wifeObject.name + str(obj.marriageDateObject) not in str(duplicates.items()):  
        duplicates.update({obj.husbandObject.name + obj.wifeObject.name + str(obj.marriageDateObject):[obj]})
    else: 
        duplicates[obj.husbandObject.name + obj.wifeObject.name + str(obj.marriageDateObject)].append(obj)
  for key, value in duplicates.items():
      if len(value) > 1:
          errorMsg = "There are " + str(len(value)) + " families with the same spouse and same marriage date"  
          for obj in value:
              obj.errors.append(errorMsg)
            
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
