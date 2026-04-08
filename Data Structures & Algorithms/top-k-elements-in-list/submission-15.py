class Solution:
    """
    understanding:
    input - list
    output - [] of kth most frequent elements

    plan:
    1. store frequency of the elements
    2. create list of list with indices corresponding to freq of elements
    3. put elements on their respective lists 
    4. then iterate from the end to get the elements with highest freq
    """
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for i in nums:
            d[i] = 1 + d.get(i,0)

        freq = [[] for _ in range(len(nums)+1)]
        for key, val in d.items():
            freq[val].append(key)

        #[[],[1],[2],[3],[],[],[]]
        print(freq)
        res = []
        for i in range(len(freq)-1,-1,-1):
            while freq[i]:
                res.append(freq[i].pop())
                if len(res) == k:
                    return res



        
        
        
        
        
        