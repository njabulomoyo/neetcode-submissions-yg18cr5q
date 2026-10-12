class Solution:
    """
    output: int 
    brainstorm:
    - alphabet letters? lowercase uppercase?
    - duplicate? same char? return 1?
    - empty input? return 0
    - range input: 1 - 50000 nlogn, or o(n) time
    - no rearrangement
    - iterate thru string
    - store char in haset/hashmap
    - two pointers?
    - keep track of the longest substring
    - return the recorded substring len


    Solution:
    -iterate thru list
    -each char, check if they in the set of chars passed
    -if true, move slow, removing chars, till no duplicat
    -if char not in set, check the maxlength and record
    -iterate to the end of list
    - return the longest length recorded

    """

    def lengthOfLongestSubstring(self, s: str) -> int:
        slow = 0
        maxLength = 0
        substring = set()

        for fast, char in enumerate(s):
            if char == 0:
                continue
            if char in substring:
                while substring and char in substring:
                    substring.remove(s[slow])
                    slow += 1
            else:
                maxLength = max(maxLength, fast-slow+1)   
            substring.add(char)
        return maxLength









