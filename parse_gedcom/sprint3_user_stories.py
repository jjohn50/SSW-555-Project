# US21 - Jenn


# US22 - Jenn

        
# US23 - Matt


# US24 - Matt


# US25 - Justin

         


# US26 - Justin
# No more than one family with the same spouses by name and the same marriage date should appear in a GEDCOM file 
def Unique_fam(fam):
      for i in range(0,len(fam.individualObject)-1):
        husbandname = fam.husbandObject[i].name
        husbandbirth = fam.husbandObject[i].birthdate
        wifename = fam.wifeObject[i].name
        wifebirth= fam.wifeObject[i].birthdate
        for j in range(i+1, len(indiv.individualObject)-1):
            husbandname2 = fam.husbandObject[i].name
            husbandbirth2 = fam.husbandObject[i].birthdate
            wifename2 = fam.wifeObject[i].name
            wifebirth=2 fam.wifeObject[i].birthdate
            if(husband == husband2 or wife == wife2):  
                indiv.anomalies.append("Same spouse with name and marriage date present")  


# US27 - Angie


# US28 - Angie


# US29 - Liv
### THIS ALREADY EXISTS

# US30 - Liv
