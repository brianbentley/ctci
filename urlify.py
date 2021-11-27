def urlify(char_list, last_char):
    left = last_char - 1
    right = len(char_list) - 1
    while left < right:
        if char_list[left] == " ":
            char_list[right - 2] = "%"
            char_list[right - 1] = "2"
            char_list[right] = "0"
            right -= 3
            left -= 1
        else:
            char_list[right] = char_list[left]
            right -= 1
            left -= 1


def test_urlify():
    char_list = list("Mr John Smith    ")
    expected = list("Mr%20John%20Smith")
    urlify(char_list, 13)
    assert char_list == expected


if __name__ == "__main__":
    test_urlify()
