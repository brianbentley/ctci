def is_unique(s):
    char_map = {}
    for char in s:
        if char in char_map:
            return False
        else:
            char_map[char] = True
    return True


def is_unique2(s):
    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            if s[i] == s[j]:
                return False
    return True


def test_is_unique():
    unique = ["abcdefghi", "123456789"]
    not_unique = ["aaaajlkj", "123456999"]

    for s in unique:
        assert is_unique(s) == True

    for s in not_unique:
        assert is_unique(s) == False


def test_is_unique2():
    unique = ["abcdefghi", "123456789"]
    not_unique = ["aaaajlkj", "123456999"]

    for s in unique:
        assert is_unique2(s) == True

    for s in not_unique:
        assert is_unique2(s) == False
