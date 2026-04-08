class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_dict = {}
        freq = [[] for i in range(len(nums)+1)]
        for i in nums:
            nums_dict[i] = 1 + nums_dict.get(i,0)

        for i, j in nums_dict.items():
            freq[j].append(i)

        res = []
        for n in range(len(freq)-1,0,-1):
            for num in freq[n]:
                res.append(num)
                if len(res)==k:
                    return res

                

