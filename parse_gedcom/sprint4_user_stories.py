from datetime import timedelta

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

# US39 - Liv

# US40 - Angie