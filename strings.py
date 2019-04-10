#!python

def contains(text, pattern):
    """Return a boolean indicating whether pattern occurs in text."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # Implement contains here (iteratively and/or recursively)
    i = 0
    for letter in text:
        # check if we found the pattern
        if i == len(pattern):
            return True
        # check for equality
        elif letter == pattern[i]:
            i += 1
        else:
            i = 0
            # check if first pattern letter is equal to the curr letter
            if letter == pattern[i]:
                i += 1
    
    # check if we found pattern
    if i == len(pattern):
        return True
    # we didn't find it -->
    return False


def find_index(text, pattern):
    """Return the starting index of the first occurrence of pattern in text,
    or None if not found."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # Implement find_index here (iteratively and/or recursively)
    # make sure pattern exists
    if (contains(text, pattern) == False):
        return None
    
    i = 0
    start = 0
    for letter_index in range(len(text)):
        letter = text[letter_index]
        # check if we found the pattern
        if i == len(pattern):
            return start
        # check for equality
        elif letter == pattern[i]:
            if i == 0: 
                start = letter_index
            i += 1
        else:
            i = 0
            start = 0
            # check if first pattern letter is equal to the curr letter
            if letter == pattern[i]:
                i += 1
                start = letter_index
    
    # check if we found pattern
    if i == len(pattern):
        return start
    # we didn't find it -->
    return None

def find_all_indexes_helper(text, pattern, result, left):
    # print(left)
    if (pattern == ''):
        return list(range(len(text)))
    # make sure pattern exists
    if (contains(text[left:], pattern) == False):
        return result

    if (len(text[left:]) <= 0 or left >= len(text)):
        return result
    # gets the first index for pattern in text
    found_index = find_index(text[left:], pattern) + left
    # print("ADDING: %d"% found_index)
    result.append(found_index)
    # we didn't find it -->
    left = found_index + len(pattern)
    
    return find_all_indexes_helper(text, pattern, result, left)


def find_all_indexes(text, pattern):
    """Return a list of starting indexes of all occurrences of pattern in text,
    or an empty list if not found."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # TODO: Implement find_all_indexes here (iteratively and/or recursively)
    result = []
    return find_all_indexes_helper(text, pattern, result, 0)


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


if __name__ == '__main__':
    # 'ababc', 'abc'
    main()
