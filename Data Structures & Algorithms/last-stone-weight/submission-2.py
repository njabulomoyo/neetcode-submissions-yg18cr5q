class Solution:
    """
    we will use the heapsort method
    reverse, using negetive
    we will pop two times to get the largest stones
    check the difference, if no diff, check next two rocks
    otherwise, insert the different back into the list
    do this while there are atleast two elements on the list
    """
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-elem for elem in stones]
        heapq.heapify(maxHeap)

        while len(maxHeap) > 1:
            x = heapq.heappop(maxHeap)
            y = heapq.heappop(maxHeap)

            if x == y:
                continue
            elif x < y:
                heapq.heappush(maxHeap, x-y)
            else:
                heapq.heappush(maxHeap, y-x)
        if not maxHeap:
            return 0

        return -maxHeap[0]






        