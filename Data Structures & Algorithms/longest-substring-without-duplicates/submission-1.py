class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        #"pwwekew"
        #     l  r
        l = r = 0
        setChar = set()
        res, count = 0, 0
        while r < len(s):
            if s[r] in setChar:
                while s[r] in setChar:
                    setChar.remove(s[l])
                    l+= 1
            setChar.add(s[r])
            res = max(res,len(setChar)) 
            r += 1    

        return res

        