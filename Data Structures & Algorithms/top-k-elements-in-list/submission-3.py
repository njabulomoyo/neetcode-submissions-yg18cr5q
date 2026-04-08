class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_dict = {}
        for i in nums:
            nums_dict[i]= 1 + nums_dict.get(i,0)
        freq = []
        for i, j in nums_dict.items():
            freq.append([j,i])

        freq.sort()
        res = []
        while len(res) < k:
            res.append(freq.pop()[1])
        return res

