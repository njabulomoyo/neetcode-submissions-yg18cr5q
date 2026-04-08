class Solution:
    """
    understand:
    what is an anagram?
    input - two strings
    output - boolean
    lowercase letters (a-z)
    edge case? empty? True
    time o(m+n) and space 0(1) comp?
    MATCH:
    -hashmap
    
    Plan:
    1. check size of both strings 
    2. sort each of the strings
    3. check if they are the same or not?

    """
    def isAnagram(self, s: str, t: str) -> bool:
        snew = sorted(s)
        tnew = sorted(t)
        print(snew)
        return snew == tnew
        