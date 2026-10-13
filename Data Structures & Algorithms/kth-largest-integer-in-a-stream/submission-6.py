class KthLargest:
    import heapq
    def __init__(self, k: int, nums: List[int]):
        self.store = nums
        self.limit = k
        heapq.heapify(self.store)

        while len(self.store) > self.limit:
            heapq.heappop(self.store)

        
        

    def add(self, val: int) -> int:
        heapq.heappush(self.store, val)

        while len(self.store) > self.limit:
            heapq.heappop(self.store)

        return self.store[0]
        
