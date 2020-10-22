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

# US19 - Angie

# US20 - Angie
def US20_siblings_should_not_marry_anomaly(fam):
    if fam.husbandObject.childFamilyObject != "" and fam.husbandObject.childFamilyObject == fam.wifeObject.childFamilyObject:
        fam.anomalies.append("Siblings should not marry")