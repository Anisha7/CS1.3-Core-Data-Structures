from sets import Set
import time

# Input: 2 arrays, A & B
# Return: Array with items from A but not B
def redact(A, B):
    ''' Time complexity: O(N), N = len(A) for adding all items in A
    Space complexity: O(N), N = len(A), O(2N) actually because storing
    all items in A in the set and then resulting array and removing 
    none in the worst case.
    '''

    result = Set(len(A), A) # set with items in A
    result.difference_update(B) # remove items in B FROM A
    
    result_array = [] # add all items to an array
    for item in result:
        result_array.append(item)
    return result_array

# Input: 2 arrays, A & B
# Return: Array with items from A but not B
def redact2(A, B):
    ''' Time complexity: O(n*m) because looping over len(A) = n, 
    and checking if each item is in len(B) = m
    Space complexity: O(n) because in the worst case, adding all items from A
    '''
    result = []
    for item in A:
        if item not in B:
            result.append(item)

    return result

# Input: 2 arrays, A & B
# Return: Array with items from A but not B
def redact3(A, B):
    ''' Time complexity: O(n**m**n) because looping over len(A) = n, 
    and checking if each item is in len(B) = m,and then removing that 
    item + shifting items in array.
    Space complexity: O(1) because modifying current list
    ISSUE: Fails on duplicates!!
    '''
    for i in range(len(A)):
        if i >= len(A):
            break
        if A[i] in B:
            A.pop(i)
    return A


# TESTS
def simple_test(r):
    A = [1,2,3,4,5,6,7,8,9,10]
    B = [3,4,5,6]
    A = r(A, B)
    assert A == [1,2,7,8,9,10]
    print(A)
    B = [1,2,11,13,14,4,4,5,6,90,102]
    A = r(A, B)
    assert A == [7,8,9,10]

def duplicate_test(r):
    A = [1,2,3,4,5,6,7,8,9,10,5,6]
    B = [3,4,5,6]
    assert r(A, B) == [1,2,7,8,9,10]

def emptyset_test(r):
    # no items to remove
    A = [1,2,3,4,5]
    B = [6,7]
    assert r(A, B) == [1,2,3,4,5]
    # empty arrays
    A = []
    B = [1,2,3]
    assert r(A,B) == []
    A = [1,2,3]
    B = []
    assert r(A,B) == [1,2,3]

def test(r):
    # simple case
    simple_test(r)
    # with duplicates
    duplicate_test(r)
    # empty sets
    emptyset_test(r)

if __name__ == "__main__":
    
    print("TESTING SET IMPLEMENTATION OF REDACT")
    start = time.time()
    test(redact)
    end = time.time()
    print("PASSED ALL TESTS")
    runtime = end-start
    msg = "Runtime: {time} seconds to complete\n".format(time=runtime)
    print(msg)

    print("TESTING LIST IMPLEMENTATION OF REDACT")
    start = time.time()
    test(redact2)
    end = time.time()
    print("PASSED ALL TESTS")
    runtime = end-start
    msg = "Runtime: {time} seconds to complete\n".format(time=runtime)
    print(msg)