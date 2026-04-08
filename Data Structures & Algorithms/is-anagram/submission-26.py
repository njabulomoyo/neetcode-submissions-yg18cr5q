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

        sd = [0]*26
        td = [0]*26
        for i in range(len(s)):
            sd[ord("z") - ord(s[i])] += 1
            td[ord("z") - ord(t[i])] += 1

    #[0,1,2,0,0,0,1,0,0,0]
        return sd == td

    """     




        if len(s) != len(t):
            return False
        sd = {}
        td = {}
        for i in range(len(s)):
            sd[s[i]] = 1 + sd.get(s[i],0)
            td[t[i]] = 1 + td.get(t[i],0)

        return sd == td

    """





