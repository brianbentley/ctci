import unittest


def palindrome_permutation(input_string):
    char_map = {}
    for char in input_string:
        if char.isalpha():
            char_lower = char.lower()
            char_map[char_lower] = char_map.get(char_lower, 0) + 1
    odd = False
    for char_count in char_map.values():
        if odd and char_count % 2:
            return False
        elif char_count % 2:
            odd = True
    return True


class Test(unittest.TestCase):
    palindrome_strings = ["Tact Coa", "tacO Cat"]

    def test_palindrome_permutations(self):
        for palindrome in self.palindrome_strings:
            assert palindrome_permutation(palindrome) == True
        for palindrome in self.palindrome_strings:
            assert palindrome_permutation(palindrome + "b") == False


if __name__ == "__main__":
    unittest.main()
