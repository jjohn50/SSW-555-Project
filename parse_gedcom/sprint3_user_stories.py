# US21 - Jenn


# US22 - Jenn

        
# US23 - Matt


# US24 - Matt


# US25 - Justin

         


# US26 - Justin
# No more than one family with the same spouses by name and the same marriage date should appear in a GEDCOM file 
def US26_Unique_fam(id_list):
  duplicates = {} 
  for obj in id_list:
    if obj.husbandObject.name + obj.wifeObject.name + str(obj.marriageDateObject) not in str(duplicates.items()):  
        duplicates.update({obj.husbandObject.name + obj.wifeObject.name + str(obj.marriageDateObject):[obj]})
    else: 
        duplicates[obj.husbandObject.name + obj.wifeObject.name + str(obj.marriageDateObject)].append(obj)
  for key, value in duplicates.items():
      if len(value) > 1:
          errorMsg = "There are " + str(len(value)) + " families with the same spouse and same marriage date"  
          for obj in value:
              obj.errors.append(errorMsg)               

            
# US27 - Angie


# US28 - Angie


# US29 - Liv
### THIS ALREADY EXISTS

# US30 - Liv
