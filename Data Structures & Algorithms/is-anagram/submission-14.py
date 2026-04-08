class Solution:
    def isAnagram(self, s: str, t: str) -> bool:        
        if len(s) != len(t):
            return False
        lst_ = [0]*26
        

        for i in range(len(s)):
            lst_[ord(t[i])-ord("z")] += 1
            lst_[ord(s[i])-ord("z")] -= 1

        return all(val==0 for val in lst_)
        


        