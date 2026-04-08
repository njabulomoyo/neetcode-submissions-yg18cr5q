class Solution:
    """
    understand
    input - 2d list
    output - bool
    empty list?
    target always exists?
    time o(log(m*n)) and spce o(1)?
    """
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])

        l, r = 0, rows -1
        while l <= r:
            m = (l+r)//2
            if target < matrix[m][0]:
                r = m - 1
            elif target > matrix[m][-1]:
                l = m + 1
            else:
                break
        left, right = 0, cols - 1

        while left <= right:
            mid = (left + right)//2
            if matrix[m][mid] > target:
                right = mid - 1
            elif matrix[m][mid] < target:
                left = mid + 1
            else:
                return True

        return False




