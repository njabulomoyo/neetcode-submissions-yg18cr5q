class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s)==sorted(t)
        """
        if len(s) != len(t):
            return False
        dict_t = {}
        dict_s = {}

        for i in range(len(s)):
            dict_t[t[i]] = 1 + dict_t.get(t[i],0)
            dict_s[s[i]] = 1 + dict_t.get(s[i],0)

        return dict_t == dict_s
        """


        