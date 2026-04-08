class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        d = {}

        for elem in nums:
            d[elem] = 1 + d.get(elem,0)
        res=[]
        length = len(nums)
        for key, val in d.items():
            if (val * 3) > length:
                res.append(key)

        return res