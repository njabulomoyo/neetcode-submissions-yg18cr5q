class Solution:
    #[1,2,2,3,3,3]
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for i in nums:
            count[i] = 1 + count.get(i,0)
        
        freq = [[] for i in range(len(nums)+1)]
        for i, j in count.items():
            freq[j].append(i)
        res = []
        for j in range(len(freq)-1,0,-1):
            for i in freq[j]:
                res.append(i)
                if len(res) == k:
                    return res

        

