import unittest


def one_away(s1, s2):
    if len(s1) > len(s2):
        s1, s2 = s2, s1
    s1_length = len(s1)
    s2_length = len(s2)
    if s2_length - s1_length > 1:
        return False
    s1_pointer = s2_pointer = 0
    difference_count = 0

    while s1_pointer < s1_length:
        if s1[s1_pointer] != s2[s2_pointer]:
            difference_count += 1
            if s2_pointer + 1 < s2_length and s2[s2_pointer + 1] == s1[s1_pointer]:
                s2_pointer += 1
            else:
                s1_pointer += 1
                s2_pointer += 1
        else:
            s1_pointer += 1
            s2_pointer += 1
    difference_count += s2_length - s2_pointer
    return difference_count <= 1


class Test(unittest.TestCase):
    true_tests = [("pale", "ple"), ("pale", "bale"), ("pales", "pale")]
    false_tests = [("pales", "ple"), ("pales", "bale"), ("paless", "plae")]

    def test_one_away_true(self):
        for s1, s2 in self.true_tests:
            assert one_away(s1, s2) == True

    def test_one_away_false(self):
        for s1, s2 in self.false_tests:
            assert one_away(s1, s2) == False


if __name__ == "__main__":
    unittest.main()
