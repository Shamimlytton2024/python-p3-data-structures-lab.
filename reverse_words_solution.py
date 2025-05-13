def reverse_words(s):
    """
    Reverse the order of words in the input string s.
    Words are separated by exactly one space with no leading or trailing spaces.
    """
    words = s.split(' ')
    reversed_words = words[::-1]
    return ' '.join(reversed_words)
