'''''
Create a function called shortcut to remove the lowercase vowels (a, e, i, o, u ) in a given string.
Examples

"hello"     -->  "hll"
"codewars"  -->  "cdwrs"
"goodbye"   -->  "gdby"
"HELLO"     -->  "HELLO"

    

Strings
Fundamentals

''''''

Function shortcut(s)
Input:
a string
output:
 a new string with all lowercase vowels removed
pseudcode:
1. define a string of vowels:'[aeiou]'
2. use a loop to iterate over the string
3. if the character is in the string of vowels skip it
4. add the character to the new string
5. return the new string
'''
def shortcut(s: str) -> str:
    """
    Remove all lowercase vowels (a, e, i, o, u) from the input string s.
    
    Args:
        s (str): The input string.
        
    Returns:
        str: A new string with all lowercase vowels removed.
    """
    vowels = 'aeiou'
    result = ''.join(char for char in s if char not in vowels)
    return result


# Example usage and test cases
if __name__ == "__main__":
    test_strings = ["hello", "codewars", "goodbye", "HELLO"]
    for test in test_strings:
        print(f"{test} --> {shortcut(test)}")
