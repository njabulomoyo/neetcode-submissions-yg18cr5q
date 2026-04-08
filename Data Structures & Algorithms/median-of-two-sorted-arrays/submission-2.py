class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) == 0 and len(nums2) == 0:
            return 0
        p1 = p2 = 0
        res = []
        while p1 < len(nums1) and p2 < len(nums2):
            if nums1[p1] < nums2[p2]:
                res.append(nums1[p1])
                p1 += 1
            else:
                res.append(nums2[p2])
                p2 += 1

        if p1 < len(nums1):
            res.extend(nums1[p1:len(nums1)])
            p1 += 1
        if p2 < len(nums2):
            res.extend(nums2[p2:len(nums2)])
            p2 += 1

        print(res)
        m = len(res)
        if m % 2 == 0:
            return (res[m//2] + res[(m-1)//2])/2
        else:
            return res[m//2]

        

        


        