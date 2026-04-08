class Solution:
    """
    understand:
    input - string
    output - boolean
    Match:
        - iteration
        - two pointers
    PLAN:
        - Initiate pointers
        2. iterate thru list and check if characters are the same
        3. if not check if uccc
    """
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        def isPal(left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        while l < r:
            if s[l] != s[r]:                                
                return (isPal(l+1,r) or
                        isPal(l,r-1))

            l, r = l+1, r-1
        return True   

        