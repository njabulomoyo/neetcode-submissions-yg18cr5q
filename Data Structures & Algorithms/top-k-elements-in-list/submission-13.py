class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        freq = [[] for i in range(len(nums)+1)]
        for elem in nums:
            d[elem] = 1 + d.get(elem,0)
       
        for key, value in d.items():
            freq[value].append(key)
        res = []
        for i in range(len(freq)-1,0,-1):
            for j in freq[i]:
                res.append(j)
                if len(res)==k:
                    return res
            



            




