def iterate(f, x, a):
  """
    Params:
      f.....function to apply
      x.....return when a is empty
      a.....input sequence
  """
  print('iterate: calling %s x=%s a=%s' % (f.__name__, x, a))
  if len(a) == 0:
    return x
  else:
    return iterate(f, f(x, a[0]), a[1:])

def plus(x, y):
  return x + y

iterate(plus, 0, [2, 5, 1, 6])

def flatten(sequences):
  return iterate(plus, [], sequences)

flatten([[1,2,3], [4], [5,6]])