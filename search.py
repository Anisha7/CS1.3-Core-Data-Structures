#!python

def linear_search(array, item):
    """return the first index of item in array or None if item is not found"""
    # implement linear_search_iterative and linear_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    # return linear_search_iterative(array, item)
    return linear_search_recursive(array, item)


def linear_search_iterative(array, item):
    # loop over all array values until item is found
    for index, value in enumerate(array):
        if item == value:
            return index  # found
    return None  # not found


def linear_search_recursive(array, item, index=0):
    # implement linear search recursively here
    # checked the entire array, item not found
    if (index >= len(array)):
        return None
    # found solution
    if (array[index] == item):
        return index
    
    # check next item
    return linear_search_recursive(array, item, index+1)
    # once implemented, change linear_search to call linear_search_recursive
    # to verify that your recursive implementation passes all tests


def binary_search(array, item):
    """return the index of item in sorted array or None if item is not found"""
    # implement binary_search_iterative and binary_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    return binary_search_iterative(array, item)
    # return binary_search_recursive(array, item)

# return true if word1 comes before word2 in alphabetical order
def comesFirst(word1, word2):
    i = 0
    j = 0

    while (i < len(word1) and j < len(word2)):
        if ord(word1[i]) < ord(word2[j]):
            return True
        if ord(word1[i]) > ord(word2[j]):
            return False
        i += 1
        j += 1
    return False

def binary_search_iterative(array, item):
    # implement binary search iteratively here
    left = 0
    right = len(array)
    while (right - left > 0):
        mid = left + (right-left)//2
        # if found
        if array[mid] == item:
            return mid
        
        elif comesFirst(item, array[mid]):
            right = mid
        else:
            left = mid + 1
    
    return None
        
    # once implemented, change binary_search to call binary_search_iterative
    # to verify that your iterative implementation passes all tests


def binary_search_recursive(array, item, left=None, right=None):
    # TODO: implement binary search recursively here
    if (left == None):
        left = 0
    if (right == None):
        right = len(array)
    if (right - left <= 0):
        return None
    # set mid
    mid = (right - left) // 2

    if (array[mid] == item):
        return left + mid

    # item is less than mid, go left
    if (array[mid] > item):
        return binary_search_recursive(array, item, left, mid)

    # item is less than mid, go left
    if (array[mid] < item):
        return binary_search_recursive(array, item, mid, right)
    # once implemented, change binary_search to call binary_search_recursive
    # to verify that your recursive implementation passes all test

if __name__ == '__main__' :
    names = ['Alex', 'Brian', 'Julia', 'Kojin', 'Nabil', 'Nick', 'Winnie']
    # binary search should return the index of each item in the list

    print(comesFirst('Alex', 'Brian'))
    print(comesFirst('Bpex', 'Beple'))
    print(binary_search(names, 'Alex'))
    print(binary_search(names, 'Brian'))
    print(binary_search(names, 'Julia'))
    print(binary_search(names, 'Kojin'))
    print(binary_search(names, 'Nabil'))
    print(binary_search(names, 'Nick'))
    print(binary_search(names, 'Winnie'))