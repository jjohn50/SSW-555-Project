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

# US37 - Justin
def US37_recent_death(individuals):
    recent_death = []
    for indiv in individuals:
        if indiv.alive == False: 
            day1 = indiv.deathDateObject
            day2 = datetime.now()
            daysPassed = ((day2-day1).days) 
            if ((daysPassed) <= 30):
             recent_death.append(indiv)
    return recent_death

def US37_print_recent_death(individuals):
    print("List of recent deaths:")
    print("------------------------------")
    recent_death = US37_recent_death(individuals)
    for indiv in recent_death:   
        print(indiv.Id + ": " + indiv.name)
    print("\n")
      
# US38 - Liv

# US39 - Liv

# US40 - Angie