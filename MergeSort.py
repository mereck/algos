def MergeCombine(A, p, q, r):
    """
    Sorts values of array A within p..q..r range 
    by pushing them into left and right stacks
    and then popping off the smallest values to insert into A

    A - original array to be sorted
    p - leftmost index into A
    q - midpoint into A
    r - rightmost index into A
    """
    left, right = [], []

    #push each value onto left and right stacks
    #we reverse because we will need smallest value to be at end of list
    for i in range(p, r + 1)[::-1]:
        if i > q:
            right.append(A[i])
        else:
            left.append(A[i])
    
    ca = p #LTR index into A
    
    while left and right:
        cr, cl = right[len(right)-1], left[len(left)-1]
        A[ca] = right.pop() if cr < cl else left.pop()
        ca += 1

        if not left and right: #reached end of left unwind right half
            while right:
                A[ca] = right.pop()
                ca += 1
        elif not right and left: #reached end of right unwind left half
            while left:
                A[ca] = left.pop()
                ca += 1


def MergeSort(A, p, r):

    if p < r: #recursively find middle, and split each half into halves
        q = (r + p) // 2
        MergeSort(A, p, q)
        MergeSort(A, q + 1, r)
        MergeCombine(A, p, q, r) # combine the two sorted halves

A = [77, 12, 140, 22, 10, 4, 9, 26]

print "Before: {}".format(A)

MergeSort(A, 0, 7)

print "After: {}".format(A)
