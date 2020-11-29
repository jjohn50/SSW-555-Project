from datetime import datetime
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

# US35 - Angie

# US36 - Justin
#List all people in a GEDCOM file who were born in the last 30 days
def US36_recent_births(individuals):
    recent_births = []
    for indiv in individuals:
        day1 = indiv.birthDateObject    
        day2 = datetime.now()
        daysPassed = ((day2-day1).days)
        if ((daysPassed) <= 30):
            recent_births.append(indiv)
    return recent_births

def US36_print_recent_births(individuals):
    print("List of recent births people:")
    print("------------------------------")
    recent_births = US36_recent_births(individuals)
    for indiv in recent_births:
        print(indiv.Id + ": " + indiv.name)
    print("\n")
 
# US37 - Justin

# US38 - Liv

# US39 - Liv

# US40 - Angie