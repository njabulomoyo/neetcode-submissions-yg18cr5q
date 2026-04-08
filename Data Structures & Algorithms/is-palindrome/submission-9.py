class Solution:
    """
    Output - boolean...
    empty string?
    strings are alphanum? upper, lower, numbers
    skip special keys

    plan:
         two pointer
         check characters on bioth ends
         if elem is not alphanum, move pointer, 
         if you find elements that are not equal, return False 
         
    """
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1

        while l < r:
            if not s[l].isalnum():
                l += 1
                continue
            if  not s[r].isalnum():
                r -= 1
                continue

            if s[l].lower() != s[r].lower():
                print("s[l]=",s[l], "s[r]=", s[r])
                return False
            l += 1
            r -= 1

        return True
        