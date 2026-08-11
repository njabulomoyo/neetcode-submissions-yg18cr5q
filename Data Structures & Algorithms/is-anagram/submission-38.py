class Solution:
    """
    output: boolean

    SOLUTION 1:
    1. sort the letters
    2. check if the strings are the same after being sorted
    3. this is O(n log n) time complexity + o(n) space

    Solution 2:
    1. initiate 2 dictionaries for each string
    2. for each letter, add count/frequency to the value of each key
    3. compare the 2 dictionaries
    4. o(n) time + o(n) space

    solution 3:
    1. use bucket arrays
    2. initiate an array of size 26, for each letter of the lowercase alphabet
    3. string 1: for each letter we iterate thru, we update the respective index by adding one
    4. string 2: for each letter, we update respective indx by subytracting one
    5. then iterate thru bucket
    6. if we find non zero element, we return false
    7. otherwise true


    """
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        bucket = [0] * 26
        print(bucket)
        for i in range(len(s)):
            bucket[ord(s[i]) - ord('z')] += 1
            bucket[ord(t[i]) - ord('z')] -= 1

        for elem in bucket:
            if elem != 0:
                return False

        return True














