class KthLargest:
    """
    take the list\
    heapify
    and then pop k times to get the kth largest number


    will keep track o the size of the list
    we will then return the top number on the list
    that will be our kth largest element at the time
    """
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.minHeap = nums
        heapq.heapify(self.minHeap)
        while len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)

        return self.minHeap[0]

