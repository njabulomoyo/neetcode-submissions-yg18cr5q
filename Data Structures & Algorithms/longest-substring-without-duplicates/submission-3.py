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
        maxSub = 0 
        subStr = set()
         
        slow, fast = 0, 0
        while fast < len(s):
            if s[fast] not in subStr:
                subStr.add(s[fast])
                maxSub = max(maxSub, len(subStr))
                fast += 1
            else:
                while s[fast] in subStr:
                    subStr.remove(s[slow])
                    slow += 1
                
                
            
  
            

        return maxSub
                










        