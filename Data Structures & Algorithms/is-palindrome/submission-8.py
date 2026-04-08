class Solution:
    """
    understand:
        input - string, upper cases, special characters, numbers 
        output - boolean
        empty list? No
        time o(n) and space o(1) complexity?
    match:
        iteration
        two pointer
    plan:
        1. have two pointers at the start and end
        2. compare elements from both sides,
        3. in not alpha numeric, skip
        4. if elements not same, return False
        5. other return True
    """
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1
        while l <= r:
            if not self.isAlphanum(s[l]):
                l+=1
                continue

            if not self.isAlphanum(s[r]):
                r-=1
                continue

            if s[l].lower() != s[r].lower():
                return False

            l+=1
            r-=1
        return True

    def isAlphanum(self,char):
        return (ord('A') <= ord(char) <= ord('Z') or
                ord('a') <= ord(char) <= ord('z') or
                ord('0') <= ord(char) <= ord('9'))










        