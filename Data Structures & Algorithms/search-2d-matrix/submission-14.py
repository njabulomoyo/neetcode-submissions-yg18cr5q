class Solution:
    """
    output: bool - if target found

    edge case: if target is not there retur -1

    solution:
    - initiate two pointers
    - find the mid pointer
    - check the first number on the list of list
    - if its less. than target, then move l to the right of mid
    - if its greater, then move pointer to the right of mid
    - do this until there is only one list
    - then do the binary search on that list

    """
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix)-1 
        while l<=r:
            m = (l+r)//2
            if matrix[m][0] > target:
                r = m - 1
            else:
                l = m + 1

        left, right = 0, len(matrix[r])-1
        while left <= right:
            mid = (left + right)//2
            if matrix[r][mid] == target:
                return True

            elif matrix[r][mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return False


        