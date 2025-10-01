# CMPS 2200 Assignment 2

**Name:** Phu Thanh Tran

In this assignment we'll work on applying the methods we've learned to analyze recurrences, and also see their behavior in practice. As with previous assignments, some of of your answers will go in `main.py` and `test_main.py`. You should feel free to edit this file with your answers; for handwritten work please scan your work and submit a PDF titled `assignment-02.pdf` and push to your github repository.


## Part 1. Asymptotic Analysis

* Uploaded in assignment-02-answers.pdfUploaded in assignment-02-answers.pdf



## Part 2. Algorithm Comparison

* Uploaded in assignment-02-answers.pdfUploaded in assignment-02-answers.pdf



## Part 3: Parenthesis Matching

A common task of compilers is to ensure that parentheses are matched. That is, each open parenthesis is followed at some point by a closed parenthesis. Furthermore, a closed parenthesis can only appear if there is a corresponding open parenthesis before it. So, the following are valid:

- `( ( a ) b )`
- `a () b ( c ( d ) )`

but these are invalid:

- `( ( a )`
- `(a ) ) b (`

Below, we'll solve this problem three different ways, using iterate, scan, and divide and conquer.

**3a. iterative solution** Implement `parens_match_iterative`, a solution to this problem using the `iterate` function. **Hint**: consider using a single counter variable to keep track of whether there are more open or closed parentheses. How can you update this value while iterating from left to right through the input? What must be true of this value at each step for the parentheses to be matched? To complete this, complete the `parens_update` function and the `parens_match_iterative` function. The `parens_update` function will be called in combination with `iterate` inside `parens_match_iterative`. Test your implementation with `test_parens_match_iterative`.

**3b.** What are the recurrences for the Work and Span of this solution? What are their Big Oh solutions?

**Work**: W(n) = O(n) - The iterate function processes each element exactly once, so the work is linear in the input size.

**Span**: S(n) = O(n) - The iterate function is inherently sequential, processing elements one by one, so the span is also linear.

**Big-O Solutions**: 
- Work: O(n)
- Span: O(n)


**3c. scan solution** Implement `parens_match_scan` a solution to this problem using `scan`. **Hint**: We have given you the function `paren_map` which maps `(` to `1`, `)` to `-1` and everything else to `0`. How can you pass this function to `scan` to solve the problem? You may also find the `min_f` function useful here. Implement `parens_match_scan` and test with `test_parens_match_scan`

**3d.** Assume that any `map`s are done in parallel, and that we use the efficient implementation of `scan` from class. What are the recurrences for the Work and Span of this solution? 

**Work**: 
* `map(paren_map, mylist)`: O(n) work
* `scan(plus, 0, mapped_list)`: O(n) work  
* `reduce(min_f, 0, history)`: O(n) work
* Total work: W(n) = O(n)

**Span**:
* `map(paren_map, mylist)`: O(1) span (parallel map)
* `scan(plus, 0, mapped_list)`: O(log n) span (efficient parallel scan)
* `reduce(min_f, 0, history)`: O(log n) span (parallel reduce)
* Total span: S(n) = O(log n)

**Big-O Solutions**:
* Work: O(n)
* Span: O(log n)


**3e. divide and conquer solution** Implement `parens_match_dc_helper`, a divide and conquer solution to the problem. A key observation is that we *cannot* simply solve each subproblem using the above solutions and combine the results. E.g., consider '((()))', which would be split into '(((' and ')))', neither of which is matched. Yet, the whole input is matched. Instead, we'll have to keep track of two numbers: the number of unmatched right parentheses (R), and the number of unmatched left parentheses (L). `parens_match_dc_helper` returns a tuple (R,L). So, if the input is just '(', then `parens_match_dc_helper` returns (0,1), indicating that there is 1 unmatched left parens and 0 unmatched right parens. Analogously, if the input is just ')', then the result should be (1,0). The main difficulty is deciding how to merge the returned values for the two recursive calls. E.g., if (i,j) is the result for the left half of the list, and (k,l) is the output of the right half of the list, how can we compute the proper return value (R,L) using only i,j,k,l? Try a few example inputs to guide your solution, then test with `test_parens_match_dc_helper`.

**3f.** Assuming any recursive calls are done in parallel, what are the recurrences for the Work and Span of this solution? What are their Big Oh solutions?

**Work**: 
* W(n) = 2W(n/2) + O(1)
* The algorithm divides the problem into two subproblems of size n/2 and does constant work to combine results
* By the Master Theorem: W(n) = O(n)

**Span**:
* S(n) = S(n/2) + O(1) 
* Since recursive calls are done in parallel, we only pay for the depth of one branch plus constant combination work
* By the Master Theorem: S(n) = O(log n)

**Big-O Solutions**:
* Work: O(n)
* Span: O(log n)
