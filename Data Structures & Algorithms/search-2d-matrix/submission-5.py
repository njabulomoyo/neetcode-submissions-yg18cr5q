class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left, right = 0, len(matrix)-1
        while left <= right:
            mid = (left + right)//2
            if matrix[mid][0] > target:
                right = mid - 1 
            elif matrix[mid][0] < target:
                left = mid + 1
            else:
                return True
        print(matrix[right])

        l,r = 0, len(matrix[right])-1
        while l<=r:
            m = (l+r)//2
            if matrix[right][m] == target:
                return True
            elif matrix[right][m] < target:
                l += 1
            else:
                r -= 1

        return False

