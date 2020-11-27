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

# US38 - Liv
def US38_list_upcoming_birthdays(individuals):
    upcoming_bdays = []
    for individual in individuals:
        birthday_this_year = datetime(datetime.now().year, individual.birthDateObject.month, individual.birthDateObject.day)
        birthday_next_year = datetime(datetime.now().year+1, individual.birthDateObject.month, individual.birthDateObject.day)
        if individual.alive == True and (((birthday_this_year - datetime.now()).days <= 30 and (birthday_this_year - datetime.now()).days > 0) or ((birthday_next_year - datetime.now()).days <= 30 and (birthday_next_year - datetime.now()).days > 0)):
            upcoming_bdays.append(individual)
    return upcoming_bdays

def US38_print_upcoming_birthdays(individuals):
    print("List of those with upcoming birthdays:")
    print("--------------------------------------")
    upcoming_bdays = US38_list_upcoming_birthdays(individuals)
    for individual in upcoming_bdays:
        print(individual.Id +": " + individual.name + ", " + individual.birthDateString)

# US39 - Liv

# US40 - Angie