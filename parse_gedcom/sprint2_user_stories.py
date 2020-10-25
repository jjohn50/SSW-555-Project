# US11 - Jenn

# US12 - Jenn

# US13 - Justin

# US14 - Justin

# US15 - Matt

# US16 - Matt

# US17 - Liv
def  US17_fewer_than_15_siblings_anomaly(fam):
    if len(fam.childrenObjects) >= 15:
        fam.anomalies.append("There should be fewer than 15 siblings in a family")

# US18 - Liv
def US18_male_last_names_anomaly(fam):
    lastName = fam.husbandObject.name.split('/')[1]
    for child in fam.childrenObjects:
        if child.gender == 'M':
            if lastName != child.name.split('/')[1]:
                fam.anomalies.append("Males of the same family should have the same last name")


# US19 - Angie
def US19_no_marriages_to_descendants_anomaly(fam):
    if (fam.husbandObject.childFamilyObject in fam.wifeObject.spouseFamilyObjects) or (fam.wifeObject.childFamilyObject in fam.husbandObject.spouseFamilyObjects):
        fam.anomalies.append("Parents should not marry their children")

# US20 - Angie
def US20_siblings_should_not_marry_anomaly(fam):
    if fam.husbandObject.childFamilyObject != "" and fam.husbandObject.childFamilyObject == fam.wifeObject.childFamilyObject:
        fam.anomalies.append("Siblings should not marry")