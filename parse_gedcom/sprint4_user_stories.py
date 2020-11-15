# US31 - Jenn

# US32 - Jenn
def US32_list_deceased(individuals):
    deceased = []
    for indiv in individuals:
        if indiv.alive == False: 
            deceased.append(indiv)
    return deceased

def US32_print_deceased(individuals):
    print("List of deceased people:")
    print("------------------------------")
    deceased = US32_list_deceased(individuals)
    for indiv in deceased:
        print(indiv.Id + ": " + indiv.name)
    print("\n")
# US33 - Matt
# List all living married people in a GEDCOM file
def US33_list_living_married(families):
    living_married = []
    for fam in families:
        if fam.divorced == False and fam.wifeObject.alive == True and fam.husbandObject.alive == True:
            living_married.append(fam)
    return living_married

def US33_print_living_married(families):
    print("List of living married people:")
    print("------------------------------")
    living_married = US33_list_living_married(families)
    for fam in living_married:
        print(fam.Id + ": " + fam.husbandObject.name + " and " + fam.wifeObject.name)
    print("\n")

# US34 - Matt

# US35 - Angie

# US36 - Justin

# US37 - Justin

# US38 - Liv

# US39 - Liv

# US40 - Angie