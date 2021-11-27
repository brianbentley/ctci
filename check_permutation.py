def check_permutation(s1, s2):
    s1_map = {}
    for c in s1:
        s1_map[c] = s1_map.get(c, 0) + 1
    for c in s2:
        if c not in s1_map:
            return False
        elif s1_map[c] == 1:
            del s1_map[c]
        else:
            s1_map[c] -= 1
    if s1_map == {}:
        return True
    else:
        return False


def test_check_permutation():
    assert check_permutation("abba", "baab") == True
    assert check_permutation("abc", "def") == False
