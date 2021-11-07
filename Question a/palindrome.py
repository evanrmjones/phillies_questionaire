def is_palindrone(s):
    """Old function"""
    r=""
    for c in s:
        r = c +r
    for x in range(0, len(s)):
        if s[x] == r[x]:
            x = True
        else:
            return False
    return x

def better_is_palindrome(s):
    """Better function to check if a word is a palinfrome."""
    r = ""
    for c in s: 
        r = c + r 
    if s == r: 
        return True 
    else: 
        return False