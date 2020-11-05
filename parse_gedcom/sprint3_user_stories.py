# US21 - Jenn


# US22 - Jenn

        
# US23 - Matt


# US24 - Matt


# US25 - Justin


# US26 - Justin


# US27 - Angie


# US28 - Angie
# All family roles (spouse, child) specified in an individual record should have corresponding entries in the corresponding family records. 
# Likewise, all individual roles (spouse, child) specified in family records should have corresponding entries in the corresponding individual's records.
def US28_corresponding_individual_entries_error(indiv):
    if indiv.childFamilyObject != "" and indiv not in indiv.childFamilyObject.childrenObjects:
        indiv.errors.append("Individual not found as child in " + indiv.childFamilyObject.Id)
    for spouseFamily in indiv.spouseFamilyObjects:
        if indiv != spouseFamily.husbandObject and indiv != spouseFamily.wifeObject:
            indiv.errors.append("Individual not found as spouse in " + spouseFamily.Id)

def US28_corresponding_family_entries_error(fam):
    if fam.husbandObject != "" and fam not in fam.husbandObject.spouseFamilyObjects:
        fam.errors.append("Corresponding spouse family not listed for husband individual")
    if fam.wifeObject != "" and fam not in fam.wifeObject.spouseFamilyObjects:
        fam.errors.append("Corresponding spouse family not listed for wife individual")
    for child in fam.childrenObjects:
        if child.childFamilyObject != fam:
            fam.errors.append("Corresponding child family not listed for " + child.Id)

# US29 - Liv
### THIS ALREADY EXISTS

# US30 - Liv
