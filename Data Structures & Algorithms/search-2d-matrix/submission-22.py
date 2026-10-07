class Solution:
    """
    output: bool (target found)
    brainstorm
    edge cases? empty list?, 
    lists are ordered, ascending
    since lists are ordered we can use binary search

    bruteforce would be to iterate, check ou the numbers one by one -> o(n)

    we can travers thru the grid, using two pointers,
    we can find the list that could potentially contain the target
    the we use binary search on the identified list

    identifying the list:
    we can use the range of the lists
    instead, we can use the upper and lower limit of lst on m
    check if upper is greater, or lower is lower
    if greater, move r if lower move l

    do this until you find a list
    then search that list
    return target

    """
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left, right = 0, len(matrix)-1
        
        
        while left <= right:
            mid = (left+right)//2
            if matrix[mid][0] > target:
                right = mid-1
            else:
                left = mid+1
        
        l, r = 0, len(matrix[0])-1

        while l <= r:
            m = (l+r)//2
            if matrix[right][m] == target:
                return True
            elif matrix[right][m] > target:
                r = m - 1
            else:
                l = m + 1

        return False

        

        





















        