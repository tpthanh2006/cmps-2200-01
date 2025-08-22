# Asymptotic Analysis

'''
* Big Idea -> ignore machine-dependent constants

* Asymptotic Dominance: Function f(n) dominates function g(n) if there exist constants c and n0 such that:
      c * f(n) >= g(n) for all n >= n0
'''

def new_linear_search(mylist, key): # cost      number of times
  for i in range(len(mylist)):      #  c5             n
    if mylist[i] == key:            #  c6             n
      return i                      #  c3             0 -> worst case: key not found
      
  return -1                         #  c4             1

  # Cost(new-linear-search, n) = c5n + c6n + c4 = f1(n)