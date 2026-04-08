class Solution:
    """
    input - strings
    output - boolean
    case sensetive? will it be only letters?
    empty? True
    len not equal? False

    Plan:

    """
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sd = {}
        td = {}
        for i in range(len(s)):
            sd[s[i]] = 1 + sd.get(s[i],0)
            td[t[i]] = 1 + td.get(t[i],0)

        return sd == td





