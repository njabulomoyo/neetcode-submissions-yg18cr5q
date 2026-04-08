class Solution:
    def isAnagram(self, s: str, t: str) -> bool:        
        if len(s) != len(t):
            return False
        lst_t = [0]*26
        lst_s = [0]*26

        for i in range(len(s)):
            lst_t[ord("z")-ord(t[i])] += 1
            lst_s[ord("z")-ord(s[i])] += 1

        return lst_t == lst_s
        


        