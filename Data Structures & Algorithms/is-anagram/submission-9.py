class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_list = [0]*26
        t_list = [0]*26

        for i in range(len(s)):
            a = ord("z") - ord(s[i])
            s_list[a] += 1

        for j in range(len(t)):
            b = ord("z") - ord(t[j])
            t_list[b] += 1

        return s_list == t_list 
