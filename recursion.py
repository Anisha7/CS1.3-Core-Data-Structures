#!python

def factorial(n):
    """factorial(n) returns the product of the integers 1 through n for n >= 0,
    otherwise raises ValueError for n < 0 or non-integer n"""
    # check if n is negative or not an integer (invalid input)
    if not isinstance(n, int) or n < 0:
        raise ValueError('factorial is undefined for n = {}'.format(n))
    # implement factorial_iterative and factorial_recursive below, then
    # change this to call your implementation to verify it passes all tests
    return factorial_iterative(n)
    # return factorial_recursive(n)


def factorial_iterative(n):
    # TODO: implement the factorial function iteratively here
    result = 1
    while n > 0:
        result *= n
        n -= 1
    return result
    # once implemented, change factorial (above) to call factorial_iterative
    # to verify that your iterative implementation passes all tests


def factorial_recursive(n):
    # check if n is one of the base cases
    if n == 0 or n == 1:
        return 1
    # check if n is an integer larger than the base cases
    elif n > 1:
        # call function recursively
        return n * factorial_recursive(n - 1)

# `````````` STRETCH CHALLENGES `````````` #

# n!/(n-k)!
def permutations(n, k):
    return factorial_recursive(n)/factorial_recursive(n-k)


def permutations_recursive_helper(n, nk):
    print(n, nk)
    if (n == nk):
        return 1

    return n * permutations_recursive_helper(n-1, nk)

def permutations_recursive(n, k):
    return int(permutations_recursive_helper(n, n-k))

# n!/((n-k)!k!)
def combinations(n, k):
    return factorial_recursive(n)/(factorial_recursive(n-k)*factorial_recursive(k))

def combinations_recursive_helper(n, nk, k):
    if (n == nk):
        return 1/factorial_recursive(k)
    
    if (n == k):
        return 1/factorial_recursive(nk)
    
    return n*combinations_recursive_helper(n-1, nk, k)

def combinations_recursive(n, k):
    # return permutations_recursive(n,k)/factorial_recursive(k)
    result = int(combinations_recursive_helper(n, n-k, k))
    print(result)
    return result
    # return int(combinations_recursive_helper(n, n-k, k))



def main():
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 1:
        num = int(args[0])
        result = factorial(num)
        print('factorial({}) => {}'.format(num, result))
    else:
        print('Usage: {} number'.format(sys.argv[0]))


if __name__ == '__main__':
    main()

    # print(permutations_recursive(10, 3)) #720
    print(combinations_recursive(10, 3)) #120
    print(combinations_recursive(12, 6))