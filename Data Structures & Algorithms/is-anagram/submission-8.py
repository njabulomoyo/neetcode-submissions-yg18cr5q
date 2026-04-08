class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        s = sorted(s)
        t = sorted(t)
        

        return s == t


        """
        if len(s) != len(t):
            return False

        dict_s = {}
        dict_t = {}
        for j in range(len(s)):
            dict_s[s[j]] = 1 + dict_s.get(s[j],0)

        for i in range(len(t)):
            dict_t[t[i]] = 1 + dict_t.get(t[i],0)
        
        return dict_s == dict_t
        """