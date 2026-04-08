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
        if len(s) != len(t):
            return False
        sdict = {}
        tdict = {}
        for i in range(len(s)):
            if not s[i] in sdict:
                sdict[s[i]] = 0 
            sdict[s[i]] = sdict[s[i]] + 1

            if not t[i] in tdict:
                tdict[t[i]] = 0 
            tdict[t[i]] +=  1

        return sdict == tdict
"""
        {r:2 ; a:2 ; c:2 ; e: 1}
        
"""


        
        