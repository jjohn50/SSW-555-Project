# US21 - Jenn


# US22 - Jenn

        
# US23 - Matt


# US24 - Matt

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

    # for i in range(0,len(indiv.individualObject)-1):
    #     name = indiv.individualObject[i].name
    #     birthday = indiv.individualObject[i].birthDateObject
    #     for j in range(i+1, len(indiv.individualObject)-1):
    #         name2 = indiv.individualObject[j].name
    #         birthday2 = indiv.individualObject[j].birthDateObject
    #         if(name == name2 and birthday == birthday2):
    #             indiv.anomalies.append("Same Name and Birthday are present")   

# US26 - Justin


# US27 - Angie


# US28 - Angie


# US29 - Liv
### THIS ALREADY EXISTS

# US30 - Liv
