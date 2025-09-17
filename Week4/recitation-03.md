# CMPS 2200  Recitation 03

**Name (Team Member 1):** Phu Thanh Tran


## Analyzing a recursive, parallel algorithm


You were recently hired by Netflix to work on their movie recommendation
algorithm. A key part of the algorithm works by comparing two users'
movie ratings to determine how similar the users are. For example, to
find users similar to Mary, we start by having Mary rank all her movies.
Then, for another user Joe, we look at Joe's rankings and count how
often his pairwise rankings disagree with Mary's:

|      | Beetlejuice | Batman | Jackie Brown | Mr. Mom | Multiplicity |
| ---- | ----------- | ------ | ------------ | ------- | ------------ |
| Mary | 1           | 2      | 3            | 4       | 5            |
| Joe  | 1           | **3**  | **4**        | **2**   | 5            |

Here, Joe (somehow) liked *Mr. Mom* more than *Batman* and *Jackie
Brown*, so the number of disagreements is 2:
(3 <->  2, 4 <-> 2). More formally, a
disagreement occurs for indices (i,j) when (j > i) and
(value[j] < value[i]).

When you arrived at Netflix, you were shocked (shocked!) to see that
they were using this O(n^2) algorithm to solve the problem:



``` python
def num_disagreements_slow(ranks):
    """
    Params:
      ranks...list of ints for a user's move rankings (e.g., Joe in the example above)
    Returns:
      number of pairwise disagreements
    """
    count = 0
    for i, vi in enumerate(ranks):
        for j, vj in enumerate(ranks[i:]):
            if vj < vi:
                count += 1
    return count
```

``` python 
>>> num_disagreements_slow([1,3,4,2,5])
2
```

Armed with your CMPS 2200 knowledge, you quickly threw together this
recursive algorithm that you claim is both more efficient and easier to
run on the giant parallel processing cluster Netflix has.

``` python
def num_disagreements_fast(ranks):
    # base cases
    if len(ranks) <= 1:
        return (0, ranks)
    elif len(ranks) == 2:
        if ranks[1] < ranks[0]:
            return (1, [ranks[1], ranks[0]])  # found a disagreement
        else:
            return (0, ranks)
    # recursion
    else:
        left_disagreements, left_ranks = num_disagreements_fast(ranks[:len(ranks)//2])
        right_disagreements, right_ranks = num_disagreements_fast(ranks[len(ranks)//2:])
        
        combined_disagreements, combined_ranks = combine(left_ranks, right_ranks)

        return (left_disagreements + right_disagreements + combined_disagreements,
                combined_ranks)

def combine(left_ranks, right_ranks):
    i = j = 0
    result = []
    n_disagreements = 0
    while i < len(left_ranks) and j < len(right_ranks):
        if right_ranks[j] < left_ranks[i]: 
            n_disagreements += len(left_ranks[i:])   # found some disagreements
            result.append(right_ranks[j])
            j += 1
        else:
            result.append(left_ranks[i])
            i += 1
    
    result.extend(left_ranks[i:])
    result.extend(right_ranks[j:])
    print('combine: input=(%s, %s) returns=(%s, %s)' % 
          (left_ranks, right_ranks, n_disagreements, result))
    return n_disagreements, result

```

```python
>>> num_disagreements_fast([1,3,4,2,5])
combine: input=([4], [2, 5]) returns=(1, [2, 4, 5])
combine: input=([1, 3], [2, 4, 5]) returns=(1, [1, 2, 3, 4, 5])
(2, [1, 2, 3, 4, 5])
```

As so often happens, your boss demands theoretical proof that this will
be faster than their existing algorithm. To do so, complete the
following:

a) Describe, in your own words, what the `combine` method is doing and
what it returns.

. This method uses 2 pointers - i to track the current element in left part, j to track the current in right part. In the while loop, compare the current elements at those two pointers, add the smaller element to the `result` array
. Also, if found some disagreements where `right_ranks[j] < left_ranks[i]`, add the number of elements after pointer i in the `left_ranks` array as all of them will be larger than the current element in `right_ranks`
.  Add remaining elements in `left_ranks` and `right_ranks` array to our final sorted `result` array
. The `combine` method is returning the number of disagreements when put the 2 splitted parts from the orignal array together again, and return the original array that is sorted

b) Write the work recurrence formula for `num_disagreements_fast`. Please explain how do you have this.

The work recurrence is: W(n) = 2W(n/2) + O(n)

Explanation:
- The algorithm splits the input into two equal parts (n/2)
- Each part is processed recursively: 2W(n/2)
- The combine step requires scanning both halves to merge them: O(n)
- Base case: W(1) = O(1)

c) Solve this recurrence using any method you like. Please explain how do you have this.

Using the Master Theorem:
- a = 2 (number of recursive calls)
- b = 2 (input size division factor)
- f(n) = n (work in combine step)
- log_b(a) = log_2(2) = 1
- Since f(n) = n and log_b(a) = 1, we have c = log_b(a)
- Therefore, W(n) = O(n log n)

The algorithm has the same asymptotic complexity as merge sort because it follows a similar divide-and-conquer pattern with linear-time combine step.

d) Assuming that your recursive calls to `num_disagreements_fast` are done in parallel, write the span recurrence for your algorithm. Please explain how do you have this.

The span recurrence is: S(n) = S(n/2) + O(n)

Explanation:
- Recursive calls can be done in parallel, so we only count one: S(n/2)
- The combine step still needs to process n elements sequentially: O(n)
- Base case: S(1) = O(1)

e) Solve this recurrence using any method you like. Please explain how do you have this.

Using the Master Theorem:
- a = 1 (only count one recursive call for span)
- b = 2 (input size division)
- f(n) = n (combine step)
- log_b(a) = log_2(1) = 0
- Since f(n) = n and log_b(a) = 0, we have c > log_b(a)
- Therefore, S(n) = O(n)

The span is linear because while we can parallelize the recursive calls, the combine step must still process all elements sequentially.

f) If `ranks` is a list of size n, Netflix says it will give you lg(n) processors to run your algorithm in parallel. What is the upper bound on the runtime of this parallel implementation? (Hint: assume a Greedy Scheduler). Please explain how do you have this.

Using Brent's Theorem:
T_p ≤ (W/p + S), where:
- W = O(n log n) (total work)
- p = lg(n) (number of processors)
- S = O(n) (span)

Therefore:
T_p ≤ O(n log n)/lg(n) + O(n) = O(n)

The parallel runtime is dominated by the O(n) term from the span, showing that even with lg(n) processors, we cannot achieve better than linear time due to the sequential nature of the combine step.

