class Solution:
    """
    check if given string reads the same even if reversed
    plan:
    1. have two pointer, left and right
    2. at each pointer, check if char if alphanum
    3. if not move pointer,
    4. if it is, make sure its in lowercase, check if the chars are equal
    5. if they aren't equal, return False
    6. otherwise, return continue 
    7. do this whil left is less than right pointer
    """
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1

        while l <= r:
            if not s[l].isalnum():
                l += 1
                continue
            if not s[r].isalnum():
                r -= 1
                continue

            if s[l].lower() != s[r].lower():
                return False

            l += 1
            r-= 1

        return True
            
