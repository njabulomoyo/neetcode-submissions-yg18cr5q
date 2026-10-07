class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        Rows, Cols = len(matrix), len(matrix[0])

        left, right = 0, Rows-1

        while left <= right:
            row = (left+right)//2
            if matrix[row][-1] < target:
                left = row+1
            elif matrix[row][0] > target:
                right = row-1
            else:
                break

        if not (left <= right):
            return False

        l, r = 0, Cols-1
        while l<=r:
            m = (l+r)//2
            if target > matrix[row][m]:
                l = m+1
            elif target < matrix[row][m]:
                r = m-1
            else:
                return True

        return False
