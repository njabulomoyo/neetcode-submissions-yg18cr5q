class Solution:
    """
    what are anagrams?
    input - two strings
    output? boolean
    time o(m+n) and space? o(1) 

    Match:
    - Hashmap
    - 

    """
    def isAnagram(self, s: str, t: str) -> bool:
        s = sorted(s)
        t = sorted(t)

        return "".join(s) == "".join(t)


        