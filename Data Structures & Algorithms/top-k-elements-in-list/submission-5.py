class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for elem in nums:
            d[elem] = 1 + d.get(elem,0)
        
        occur = defaultdict(list)
        for key,value in d.items():
            occur[value].append(key)
        res=[]

        for i in range(len(nums),0,-1):
            if i in occur:
                while occur[i]:
                    res.append(occur[i].pop())
                    if len(res) == k:
                        return res
               


