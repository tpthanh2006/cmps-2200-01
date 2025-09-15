## Generic divide and conquer algorithm.

def my_divide_n_conquer_alg(mylist):    
    if len(mylist) == 0:
        return LEFT_IDENTITY# <identity>
    elif len(mylist) == 1:
        return BASECASE(mylist[0]) # basecase for 1
    else:
        return COMBINE_FUNCTION(
            my_divide_n_conquer_alg(mylist[:len(mylist)//2]),
            my_divide_n_conquer_alg(mylist[len(mylist)//2:])
        )

def COMBINE_FUNCTION(solution1, solution2):
    """ return the combination of two recursive solutions"""
    pass

def BASECASE(value):
    """ return the basecase value for a single input"""
    pass