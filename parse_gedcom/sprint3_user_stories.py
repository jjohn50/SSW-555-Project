# US21 - Jenn


# US22 - Jenn

        
# US23 - Matt

# US24 - Matt
def US24_Unique_IDs(id_list, identifier):
    duplicates = {}
    for obj in id_list:
        if obj.Id not in str(duplicates.items()):
            duplicates.update({obj.Id:[obj]})
        else:
            duplicates[obj.Id].append(obj)
    for key, value in duplicates.items():
        if len(value) > 1:
            errorMsg = "There are " + str(len(value)) + " " + identifier + " with id " + key
            for obj in value:
                obj.errors.append(errorMsg)

# US25 - Justin


# US26 - Justin


# US27 - Angie


# US28 - Angie


# US29 - Liv
### THIS ALREADY EXISTS

# US30 - Liv
