class Solution:
    """
    understand:
     - input = string
     - output - bool
    edge cases?
    - empty string?
    - will the string have other characters other than letters?
    - will the letters be upper, lower case or both?
    -  time complexity? 0(n)
    - space o(1)

    Match:
    - two pointers
    - 
    Plan:
    1. initiate the two pointers, pointer left and pointer right
    2. check if the pointer is pointing to an alphanumeric character?
    3. if not continue
    4. else, check if the characters from the two pointers are the same or not
    5. if they are not return False
    6. check until left is no longer less than right pointer

    """
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1
        while l <= r:
            if not s[l].isalnum():
                l += 1
                continue
            if not s[r].isalnum():
                r-= 1
                continue
            else:
                if s[r].lower() != s[l].lower():
                    return False
            l += 1
            r -= 1
        return True
        