from datetime import datetime

# US11 - Jenn
def US11_no_bigamy_anomaly(indiv):  
    if len(indiv.spouseFamilyObjects) > 1:
        for i in range(0,len(indiv.spouseFamilyObjects)-1): #index first fam
            for j in range(i+1,len(indiv.spouseFamilyObjects)): #index for 2nd fam
                fam_i = indiv.spouseFamilyObjects[i]
                fam_j = indiv.spouseFamilyObjects[j]
                i_start = fam_i.marriageDateObject
                j_start = fam_j.marriageDateObject
                if fam_i.divorced == True:
                  i_end = fam_i.divorceDateObject
                elif fam_i.husbandObject != "" and fam_i.husbandObject.alive == False:
                  i_end = fam_i.husbandObject.deathDateObject
                elif fam_i.wifeObject != "" and fam_i.wifeObject.alive == False:
                  i_end = fam_i.wifeObject.deathDateObject
                else:
                  i_end = datetime.now()
                #j loop
                if fam_j.divorced == True:
                  j_end = fam_j.divorceDateObject
                elif fam_i.husbandObject != "" and fam_j.husbandObject.alive == False:
                  j_end = fam_j.husbandObject.deathDateObject
                elif fam_i.wifeObject != "" and fam_i.wifeObject.alive == False:
                  j_end = fam_j.wifeObject.deathDateObject
                else:
                  j_end = datetime.now()
                
                if (i_start < j_start and j_start < i_end) or (j_start < i_start and i_start < j_end):
                  indiv.anomalies.append("Bigamy")
                
# US12 - Jenn

# US13 - Justin

# US14 - Justin

# US15 - Matt

# US16 - Matt

# US17 - Liv

# US18 - Liv

# US19 - Angie

# US20 - Angie
