class Solution:
    """
    output: int count the subarrays meeting the requirements
    Edge cases? empty list? 

    Solutions:
    - create two poijters, l and r
    - initiate a variable for keeping count of the number of arrays that meet the reqs
    - iterate thru the list until you get to the end
    - for every iteration, calculate average check against threshold
    - if >= add to count
    - otherwise continue
    """
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        if len(arr) < k:
            return 0
        
        l, r = 0, k-1
        count = 0

        while r < len(arr):
            avg = sum(arr[l:r+1])/k
            if avg >= threshold:
                count += 1

            l += 1
            r += 1

        return count
        