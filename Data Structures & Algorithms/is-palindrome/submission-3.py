class Solution:
    """
    understand:
    -it is case insensitive
    - we also count all the alphanumeric characters
    - what is the best time and space complexity? O(n) time and O(1) space
    - can I use built in methods to check the characters
    Match:
    - we will use two pointers, one pointer on one edn and the other pointer on the other end
    we will be checking if the characters on both sides are the same.

    Plan:
    - we will have two pointers
    - check if the elements or the characters are alphanumeric, if not skip, 
    - if the chracter is a space, then skip
    - once you find that the characters are not matching, then return true
    - otherwise, True when the left and right points pass each other

    """
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1

        while l <= r:
            if not s[l].isalnum():
                l += 1
                continue
            if not s[r].isalnum():
                r-=1
                continue
            
            if s[l].lower() != s[r].lower():                
                return False
            l += 1
            r -= 1
        
        return True


        