from datetime import datetime

# US11 - Jenn 
def US11_no_bigamy(fam, indiv):
  counterId=0
       # we know they're married and alive
       #check number of partners
  if indiv.spouseFamilyIds == "FAMS":
    counterId= counterId+1
    if counterId > 1:
      if fam.married == True and fam.divorced == False: #married- not divorced
        if fam.husbandObject.alive == True and fam.wifeObject.alive == True: #both spouses are alive
          fams.errors.append("Bigamy")
      if fam.married == True and fam.divorced == True: # married and divorced
          if fam.husbandObject.alive == True and fam.wifeObject.alive == True: #both spouses are alive
              if fam.divorceDateObject > fam.marriageDateObject: #divorced after new marriage
                fams.errors.append("Bigamy")
      if fam.married == True and fam.divorced == False: #married- not divorced
          if fam.husbandObject.alive == False or fam.wifeObject.alive == False: #one or both spouses are alive
              if fam.husbandObject.deathDateObject > fam.marriageDateObject or fam.wifeObject.deathDateObject > fam.marriageDateObject: 
                  fams.errors.append("Bigamy")
      if fam.married == True and fam.divorced == True: #married and divorced
          if fam.husbandObject.alive == False or fam.wifeObject.alive == False: #one or both spouses are dead
              if fam.divorceDateObject > fam.marriageDateObject: #divorced after new marriage
                  fams.errors.append("Bigamy")
              if fam.husbandObject.deathDateObject > fam.marriageDateObject or fam.wifeObject.deathDateObject > fam.marriageDateObject:
                  fams.errors.append("Bigamy")
      

# US12 - Jenn

# US13 - Justin

# US14 - Justin

# US15 - Matt

# US16 - Matt

# US17 - Liv

# US18 - Liv

# US19 - Angie

# US20 - Angie
