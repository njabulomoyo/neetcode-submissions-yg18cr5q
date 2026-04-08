class Solution:
    """
    - iterate thru list, negeting elements
    - sort using the heap method
    - pop list until it has k elements
    - return the element on top

    """
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minHeap = [num for num in nums]
        heapq.heapify(minHeap)

        while len(minHeap) > k:
            print(minHeap[0])
            heapq.heappop(minHeap)

        return minHeap[0]



