"""
CMPS 2200  Assignment 2.
See assignment-02.md for details.
"""
from collections import defaultdict
import math

#### Helper functions

def iterate(f, x, a):
    """
    Sequentially applies function f to each element in a, starting with x.
    
    Params:
      f...a function that takes in two arguments
      x...the initial value
      a...a list of values
      
    Returns:
      the result of applying f to each element in a, starting with x
      
    e.g., iterate(lambda acc, v: acc + v, 0, [1, 2, 3]) == 6
    """
    result = x
    for item in a:
        result = f(result, item)
    return result

def reduce(f, id_, a):
    """
    Applies function f to combine all elements in list a, starting with identity id_.
    
    Params:
      f...a function that takes in two arguments  
      id_...the identity/initial value
      a...a list of values
      
    Returns:
      the result of applying f to combine all elements
    """
    result = id_
    for item in a:
        result = f(result, item)
    return result

def plus(x, y):
    """
    Returns the sum of x and y.
    """
    return x + y

#### Iterative solution
def parens_match_iterative(mylist):
    """
    Implement the iterative solution to the parens matching problem.
    This function should call `iterate` using the `parens_update` function.
    
    Params:
      mylist...a list of strings
    Returns
      True if the parenthesis are matched, False otherwise
      
    e.g.,
    >>>parens_match_iterative(['(', 'a', ')'])
    True
    >>>parens_match_iterative(['('])
    False
    """
    ### TODO
    return iterate(parens_update, 0, mylist) == 0
    ###


def parens_update(current_output, next_input):
    """
    This function will be passed to the `iterate` function to 
    solve the balanced parenthesis problem.
    
    Like all functions used by iterate, it takes in:
    current_output....the cumulative output thus far (e.g., the running sum when doing addition)
    next_input........the next value in the input
    
    Returns:
      the updated value of `current_output`
    """
    ###TODO
    if current_output == -math.inf:  # in an invalid state; carry it forward
        return current_output
    if next_input == '(':            # new open parens 
        return current_output + 1
    elif next_input == ')':          # new close parens
        if current_output <= 0:      # close before an open -> invalid
            return -math.inf
        else:                        # valid
            return current_output - 1
    else:                            # ignore non-parens input
        return current_output
    ###





#### Scan solution

def parens_match_scan(mylist):
    """
    Implement a solution to the parens matching problem using `scan`.
    This function should make one call each to `scan`, `map`, and `reduce`
    
    Params:
      mylist...a list of strings
    Returns
      True if the parenthesis are matched, False otherwise
      
    e.g.,
    >>>parens_match_scan(['(', 'a', ')'])
    True
    >>>parens_match_scan(['('])
    False
    
    """
    ###TODO
    history, last = scan(plus, 0, list(map(paren_map, mylist)))
    return last == 0 and reduce(min_f, 0, history) >= 0
    ###

def scan(f, id_, a):
    """
    This is a horribly inefficient implementation of scan
    only to understand what it does.
    We saw a more efficient version in class. You can assume
    the more efficient version is used for analyzing work/span.
    """
    return (
            [reduce(f, id_, a[:i+1]) for i in range(len(a))],
             reduce(f, id_, a)
           )

def paren_map(x):
    """
    Returns 1 if input is '(', -1 if ')', 0 otherwise.
    This will be used by your `parens_match_scan` function.
    
    Params:
       x....an element of the input to the parens match problem (e.g., '(' or 'a')
       
    >>>paren_map('(')
    1
    >>>paren_map(')')
    -1
    >>>paren_map('a')
    0
    """
    if x == '(':
        return 1
    elif x == ')':
        return -1
    else:
        return 0

def min_f(x,y):
    """
    Returns the min of x and y. Useful for `parens_match_scan`.
    """
    if x < y:
        return x
    return y



#### Divide and conquer solution

def parens_match_dc(mylist):
    """
    Calls parens_match_dc_helper. If the result is (0,0),
    that means there are no unmatched parentheses, so the input is valid.
    
    Returns:
      True if parens_match_dc_helper returns (0,0); otherwise False
    """
    # done.
    n_unmatched_left, n_unmatched_right = parens_match_dc_helper(mylist)
    return n_unmatched_left==0 and n_unmatched_right==0

def parens_match_dc_helper(mylist):
    """
    Recursive, divide and conquer solution to the parens match problem.
    
    Returns:
      tuple (R, L), where R is the number of unmatched right parentheses, and
      L is the number of unmatched left parentheses. This output is used by 
      parens_match_dc to return the final True or False value
    """
    ###TODO
    # Base cases
    if len(mylist) == 0:
        return (0,0)
    elif len(mylist) == 1:
        if mylist[0] == '(':
            return (0, 1) # one unmatched (
        elif mylist[0] == ')':
            return (1, 0) # one unmatched )    
        else:
            return (0, 0)
    i,j = parens_match_dc_helper(mylist[:len(mylist)//2])
    k,l = parens_match_dc_helper(mylist[len(mylist)//2:])
    # Combination:
    # Return the tuple (R,L) using some combination of the values i,j,k,l defined above.
    # This should be done in constant time.
    if j > k:
        return (i, l + j - k)
    else:
        return (i + k - j, l)
    ###
    

