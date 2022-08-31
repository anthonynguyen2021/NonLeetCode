# time = O(nlogn) | space = O(n) where n = len(grantsArray)
# solution: sort grantsArray. Draw a picture. 
def find_grants_cap(grantsArray, newBudget):
  '''
  return the optimal cap
  
  parameters:
    grantsArray: List[double]
    newBudget: double
    
  return:
    output: double
  '''
  grantsArray.sort()
  
  prev_grant = 0
  grants_left = len(grantsArray)
  budget_left = newBudget
  
  for grant in grantsArray:
    
    if (grant - prev_grant) * grants_left >= budget_left:
      answer = prev_grant + budget_left / float(grants_left)
      break
    
    budget_left -= (grant - prev_grant) * grants_left
    prev_grant = grant
    grants_left -= 1
    
  return answer