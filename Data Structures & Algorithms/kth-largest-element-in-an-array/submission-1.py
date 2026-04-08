class Solution:
    """
    - iterate thru list, negeting elements
    - sort using the heap method
    - pop list until it has k elements
    - return the element on top

    """
    def findKthLargest(self, nums: List[int], k: int) -> int:    
        heapq.heapify(nums)
        while len(nums) > k:
            heapq.heappop(nums)

        return nums[0]



