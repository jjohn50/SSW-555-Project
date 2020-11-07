# US21 - Jenn


# US22 - Jenn

        
# US23 - Matt


# US24 - Matt


# US25 - Justin
# No more than one individual with the same name and birth date should appear in a GEDCOM file 
def US25_unique_birthday_and_name(indiv):
    for i in range(0,len(indiv.individualObject)-1):
        name = indiv.individualObject[i].name
        birthday = indiv.individualObject[i].birthDateObject
        for j in range(i+1, len(indiv.individualObject)-1):
            name2 = indiv.individualObject[j].name
            birthday2 = indiv.individualObject[j].birthDateObject
            if(name == name2 and birthday == birthday2):
                indiv.anomalies.append("Same Name and Birthday are present")   

# US26 - Justin


# US27 - Angie


# US28 - Angie


# US29 - Liv
### THIS ALREADY EXISTS

# US30 - Liv
