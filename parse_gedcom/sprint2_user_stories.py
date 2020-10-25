# US11 - Jenn

# US12 - Jenn

# US13 - Justin

# US14 - Justin

# US15 - Matt

# US16 - Matt

# US17 - Liv

# US18 - Liv

# US19 - Angie
def US19_no_marriages_to_descendants_anomaly(fam):
    if (fam.husbandObject.childFamilyObject in fam.wifeObject.spouseFamilyObjects) or (fam.wifeObject.childFamilyObject in fam.husbandObject.spouseFamilyObjects):
        fam.anomalies.append("Parents should not marry their children")

# US20 - Angie
def US20_siblings_should_not_marry_anomaly(fam):
    if fam.husbandObject.childFamilyObject != "" and fam.husbandObject.childFamilyObject == fam.wifeObject.childFamilyObject:
        fam.anomalies.append("Siblings should not marry")