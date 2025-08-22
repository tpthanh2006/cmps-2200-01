'''
* The speedup of a parallel algo P over a sequential algo S is:
  speedup(P, S) = T(S) / T(P)
'''

from multiprocessing.pool import ThreadPool

def in_parallel(f1, arg1, f2, arg2):
  with ThreadPool(2) as pool:
    result1 = pool.apply_async(f1, [arg1]) # launch f1
    result2 = pool.apply_async(f2, [arg2]) # launch f2
    return (result1.get(), result2.get()) # wait for both to finish

def sum_list(mylist):
  return sum(mylist)

def parallel_sum_list(mylist):
  '''
  parallel_sum_list is TWICE as fast as sum_list
  '''
  result1, result2 = in_parallel(
    sum_list, mylist[:len(mylist // 2)],
    sum_list, mylist[len(mylist // 2):],
  )

  # combine results
  return result1 + result2