from datetime import datetime, timedelta

# US31 - Jenn
def US31_list_fam_with_no_errors_or_anomalies(families):
    no_errorOrAnomalies = []
    for fam in families:
        if len(fam.errors) == 0 and len(fam.anomalies) == 0:
            no_errorOrAnomalies.append(fam)
    return no_errorOrAnomalies

def US31_print_fam_with_no_errors_or_anomalies(families):
    print("List of families with no errors or anomalies:")
    print("------------------------------")
    no_errorOrAnomalies = US31_list_fam_with_no_errors_or_anomalies(families)
    for fam in no_errorOrAnomalies:
        print(fam.Id)
    print("\n")
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
# List all multiple births (same day or one day difference)
def US35_list_multiple_births(families):
    multiple_births = []
    for fam in families:
        multiples = {}
        for child in fam.childrenObjects:
            if child.birthDateObject in multiples:
                multiples[child.birthDateObject].append(child.name + " (" + child.Id + ")")
            elif child.birthDateObject + timedelta(days=1) in multiples:
                multiples[child.birthDateObject + timedelta(days=1)].append(child.name + " (" + child.Id + ")")
            elif child.birthDateObject - timedelta(days=1) in multiples:
                multiples[child.birthDateObject - timedelta(days=1)].append(child.name + " (" + child.Id + ")")
            else:
                multiples.update({child.birthDateObject:[fam.Id + ": " + child.name + " (" + child.Id + ")"]})
        for key, value in multiples.items():
            if len(value) > 1:
                output = value[0]
                for child in range(1,len(value)):
                    output += ", " + value[child]
                multiple_births.append(output)
    return multiple_births

def US35_print_multiple_births(families):
    print("List of multiple births:")
    print("------------------------------")
    multiple_births = US35_list_multiple_births(families)
    for output in multiple_births:
        print(output)
    print("\n")

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
    print("\n")

# US39 - Liv
def US39_list_upcoming_anniversaries(families):
    upcoming_anniv = []
    for fam in families:
        anniv_this_year = datetime(datetime.now().year, fam.marriageDateObject.month, fam.marriageDateObject.day)
        anniv_next_year = datetime(datetime.now().year+1, fam.marriageDateObject.month, fam.marriageDateObject.day)
        if fam.divorced == False and (((anniv_this_year - datetime.now()).days <= 30 and (anniv_this_year - datetime.now()).days > 0) or ((anniv_next_year - datetime.now()).days <= 30 and (anniv_next_year - datetime.now()).days > 0)):
            upcoming_anniv.append(fam)
    return upcoming_anniv

def US39_print_upcoming_anniversaries(families):
    print("List of those with upcoming anniversaries:")
    print("--------------------------------------")
    upcoming_anniv = US39_list_upcoming_anniversaries(families)
    for fam in upcoming_anniv:
        print(fam.Id +": " + fam.wifeObject.name + " and " + fam.husbandObject.name + ", " + fam.marriageDateString)
    print("\n")

# US40 - Angie