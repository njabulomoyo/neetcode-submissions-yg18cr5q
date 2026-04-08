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

        while l < r:
            if s[l] != s[r]:
                skipL, skipR  = s[l + 1:r + 1], s[l:r]                
                return (skipL == skipL[::-1] or
                        skipR == skipR[::-1])

            l, r = l+1, r-1
        return True   

        