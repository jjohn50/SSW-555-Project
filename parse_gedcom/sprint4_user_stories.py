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

# US36 - Justin

# US37 - Justin

# US38 - Liv

# US39 - Liv

# US40 - Angie