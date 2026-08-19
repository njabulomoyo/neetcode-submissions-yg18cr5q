class Solution:
    """
    output: int - longest substring
    edge cases: empty string? return 0, same chars, return 1

    solution:
    - initiate two pointers, slow and fast 
    - move fast to find unique chars
    - move slow if slow == fast

    edge case, what if the prev char of fast is same as fast? 
    - then we move slow to fast the start counting
    - each time we move the pointers, we check the length
    - return the length of the longest
    """
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        maxSub = 1 
        slow, fast = 0, 1
        while fast < len(s):
            if s[fast] not in s[slow:fast]:
                maxSub = max(maxSub, fast - slow+1)
                fast += 1
            else:
                while s[slow] != s[fast]:
                    slow += 1
                slow += 1
                
            
            while fast < len(s) and s[fast] == s[fast-1]:
                slow = fast
                fast += 1
            

        return maxSub
                










        