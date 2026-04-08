class Solution:
    def isPalindrome(self, s: str) -> bool:
        l,r = 0, len(s)-1
        while l <= r:
            if not self.isalphaNum(s[l]):
                l+= 1
                continue
            if not self.isalphaNum(s[r]):
                r -= 1
                continue
            elif s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True
    
    
    def isalphaNum(self, str):
        return (ord('A') <= ord(str) <= ord('Z') or
                ord('a') <= ord(str) <= ord('z') or
                ord('0') <= ord(str) <= ord('9')
                )     
        