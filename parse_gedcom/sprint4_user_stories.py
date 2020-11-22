# US31 - Jenn

# US32 - Jenn

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
def US34_list_singles(individuals):
    #List all living people over 30 who have never been married in a GEDCOM file 
    singles = []
    for indiv in individuals:
        if indiv.spouseFamilyObjects == [] and int(indiv.age) > 30:
            singles.append(indiv)
    return singles

def US34_print_singles(individuals):
    print("List of single people:")
    print("------------------------------")
    singles = US34_list_singles(individuals)   
    for indiv in singles:
        print(indiv.Id + ": " + indiv.name)
    print("\n") 

# US35 - Angie

# US36 - Justin

# US37 - Justin

# US38 - Liv

# US39 - Liv

# US40 - Angie