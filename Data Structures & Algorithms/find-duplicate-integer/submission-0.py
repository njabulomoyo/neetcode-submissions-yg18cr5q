class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        setlist = set()
        for i in nums:
            if i in setlist:
                return i
            setlist.add(i)