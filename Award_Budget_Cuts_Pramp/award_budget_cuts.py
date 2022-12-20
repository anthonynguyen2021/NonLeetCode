

# time: O(nlogn) where n = len(grantsArray)
# space: O(n)
"""
Solution: 

sort grantsArray in reverse order. Define surplus = sum(grantsARray) - newBudget.
If surplus is negative, that means we have a lot of budgets, so no cuts. So set cap = grantsArray[0].
Let's assume that newBudget is not < 0. Imagine stacking these budgets as bar graphs.
Then we subtrack the highest high and width. If surplus <= 0, break. The moment we break, the answer
is gransArray[idx] + abs(surplus) / float(idx) - draw a picture.
"""
def find_grants_cap(grantsArray, newBudget):

  grantsArray.sort(reverse=True)
  
  surplus = sum(grantsArray) - newBudget
  
  if surplus <= 0:
    return grantsArray[0]
  
  grantsArray.append(0)
  
  for idx in range(1, len(grantsArray)):
    
    surplus -= (grantsArray[idx - 1] - grantsArray[idx]) * idx
    
    if surplus <= 0:
      break
      
  return grantsArray[idx] + (abs(surplus) / float(idx))
