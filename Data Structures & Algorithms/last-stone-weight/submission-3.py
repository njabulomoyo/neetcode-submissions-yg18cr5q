class Solution:
    """
    sort the list using the heap sort method
    get 2 heaviest stones and compare them,
    if they equal, we continue
    if not equal, we take the diff
    and push it back to the list
    do this until we are left with one elem/weight on the list

    """
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-elem for elem in stones]
        heapq.heapify(maxHeap)
        
        while maxHeap and len(maxHeap) > 1:
            x = heapq.heappop(maxHeap)
            y = heapq.heappop(maxHeap)
            print("x is", x)
            print("y is", y)
            if x == y:
                continue
            else:
                diff = abs(x-y)
                heapq.heappush(maxHeap,-diff)
       
        if maxHeap:
            return -maxHeap[0]
        else:
            return 0
        