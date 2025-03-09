def testPalindrome(f):
    # Testaa, onko funktio f kelvollinen palindromitarkistin
    test_cases = [
        ("racecar", True),       # Palindromi
        ("A man a plan a canal Panama", True),  # Palindromi (väleillä ja isoilla kirjaimilla)
        ("hello", False),        # Ei palindromi
        ("12321", True),         # Numeropalindromi
        ("abc", False),          # Ei palindromi
        ("", True),              # Tyhjä merkkijono on palindromi
        ("a", True),             # Yhden merkin palindromi
        ("!@#!@!", True),        # Erikoismerkit, mutta symmetrinen
        ("not a palindrome", False)  # Ei palindromi
    ]
    
    for s, expected in test_cases:
        result = f(s)
        if result != expected:
            return False
    return True

def ispal(s):
    #Create a test function to test testPalindrome
    pass

if __name__ == '__main__':
    rc = testPalindrome(ispal)
    print(rc)