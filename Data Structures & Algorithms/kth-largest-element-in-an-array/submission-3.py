class Solution:
    """
    - iterate thru list, negeting elements
    - sort using the heap method
    - pop list until it has k elements
    - return the element on top

    """
    def findKthLargest(self, nums: List[int], k: int) -> int:    
        minHeap = [-elem for elem in nums]
        heapq.heapify(minHeap)
        
        for _ in range(k-1):
            heapq.heappop(minHeap)

        return -minHeap[0]




