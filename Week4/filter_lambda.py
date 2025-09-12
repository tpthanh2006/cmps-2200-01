def my_filter(f, a):
    return [x for x in a if f(x)]

def is_even(x):
    return x % 2 == 0

print(my_filter(is_even, [4, 16, 25, 36, 49, 64]))
