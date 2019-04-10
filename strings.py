#!python
# NOTE: File old_strings.py contains various versions of below functions, 
# iterative/recursive, individually implemented. This file has refactored code.
# NOTE: Stretch challenges (Permutations and Anagrams) are at the bottom of this file.

# ```````````````       HELPERS     ``````````````` #
def find_pattern_index(text, pattern, i):
    if (pattern == ''):
        return i
    if (i+len(pattern) > len(text)):
        return None
    if (text[i:i+len(pattern)] == pattern):
        return i
    return find_pattern_index(text, pattern, i+1)

def contains(text, pattern): # O(N) complexity
    """Return a boolean indicating whether pattern occurs in text."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # Implement contains here (iteratively and/or recursively) --> below commented implementation works
    i = find_pattern_index(text, pattern, 0)
    if i == None:
        return False
    return True

def find_index(text, pattern): # O(N) complexity
    """Return the starting index of the first occurrence of pattern in text,
    or None if not found."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # Implement find_index here (iteratively and/or recursively)
    return find_pattern_index(text, pattern, 0) # implemented recursively
    # iterative implementation can be found is file old_strings.py

def find_all_indexes(text, pattern): # O(N) complexity
    """Return a list of starting indexes of all occurrences of pattern in text,
    or an empty list if not found."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # Implement find_all_indexes here (iteratively and/or recursively)
    # recursively implemented in old_strings.py
    result = []
    if (pattern == ''):
        return list(range(len(text)))

    i = -1
    while (i < len(text) and i != None):
        i = find_pattern_index(text, pattern, i+1)
        if (i == None):
            break
        result.append(i)
    return result


def test_string_algorithms(text, pattern): 
    found = contains(text, pattern)
    print('contains({!r}, {!r}) => {}'.format(text, pattern, found))
    # TODO: Uncomment these lines after you implement find_index
    index = find_index(text, pattern)
    print('find_index({!r}, {!r}) => {}'.format(text, pattern, index))
    # TODO: Uncomment these lines after you implement find_all_indexes
    indexes = find_all_indexes(text, pattern)
    print('find_all_indexes({!r}, {!r}) => {}'.format(text, pattern, indexes))


def main():
    """Read command-line arguments and test string searching algorithms."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 2:
        text = args[0]
        pattern = args[1]
        test_string_algorithms(text, pattern)
    else:
        script = sys.argv[0]
        print('Usage: {} text pattern'.format(script))
        print('Searches for occurrences of pattern in text')
        print("\nExample: {} 'abra cadabra' 'abra'".format(script))
        print("contains('abra cadabra', 'abra') => True")
        print("find_index('abra cadabra', 'abra') => 0")
        print("find_all_indexes('abra cadabra', 'abra') => [0, 8]")


# '''''''''''''' STRETCH CHALLENGES: Permutations and Anagrams ''''''''''''''''''''''' #
def countOccurances(letter, word):
    count = 0
    for l in word:
        if l == letter:
            count += 1
    return count

def permutation_helper(word, result, curr=-1, temp=''):
    if len(temp) == len(word):
        result.append(temp)
        return

    for i in range(len(word)):
        if curr == i or countOccurances(word[i], temp) == countOccurances(word[i], word):
            continue
        print(temp)
        permutation_helper(word, result, i, temp+word[i])
    return

def permutation(word):
    result = []
    permutation_helper(word, result)
    return result

def isValidWord(word):
    with open('/usr/share/dict/words') as f:
        content = f.read()
    return word in  content
    # return True

def anagram_helper(word, result, curr=-1, temp=''):
    if len(temp) == len(word) and isValidWord(temp):
        result.append(temp)
        return

    for i in range(len(word)):
        if curr == i or countOccurances(word[i], temp) == countOccurances(word[i], word):
            continue
        anagram_helper(word, result, i, temp+word[i])
    return

def anagram(word):
    result = []
    anagram_helper(word, result)
    return result
    

if __name__ == '__main__':
    # 'ababc', 'abc'
    # main()
    print(anagram("pea"))
