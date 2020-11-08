# US21 - Jenn


# US22 - Jenn

        
# US23 - Matt


# US24 - Matt


# US25 - Justin


# US26 - Justin


# US27 - Angie


# US28 - Angie


# US29 - Liv
### THIS ALREADY EXISTS

# US30 - Liv
def US30_large_age_gaps_between_couples_anomalies(fam):
    if(fam.wifeObject.age > (fam.husbandObject.age * 2)):
        fam.anomalies.append("Wife is more than twice the age of the Husband")
    if(fam.husbandObject.age > (fam.wifeObject.age * 2)):
        fam.anomalies.append("Husband is more than twice the age of the Wife")
