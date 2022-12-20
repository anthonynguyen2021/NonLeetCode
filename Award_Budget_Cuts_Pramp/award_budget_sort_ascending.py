

# time = O(nlogn) | space = O(n) where n = len(grantsArray)
# solution: sort grantsArray. Draw a picture. 
def find_grants_cap(grantsArray, newBudget):

  grantsArray.sort()

  grants_left = len(grantsArray)
  total_grants_left = newBudget

  for grant in grantsArray:
    
    if grant * grants_left >= total_grants_left:
      return total_grants_left / float(grants_left)
    
    grants_left -= 1
    total_grants_left -= grant

  return total_grants_left
