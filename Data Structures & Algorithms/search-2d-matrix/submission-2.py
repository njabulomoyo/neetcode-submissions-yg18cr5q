class Solution:
    """
    Understand:
    - output should be true or false
    - expected time complexity O(m*n)
    - what if the target not be on the list? what are we returning
    - 
    Match:
    - binary search

    plan:
    - have a left and right pointer for the list, 
    - using the mid point of those pointers chck the first element of each list to see if it is equal, less or greater than target
    - if the mid point is greater, then we move the right ponter to mid + 1
    - if the midpoint is less, then move left to mid plus one
    -do this until you get to the last element( which will be the the only list left)
    - then do a binary search on that list to find the target, have left , right and mid point for the implementation
    - 
    
    """
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix)-1
        while l<=r:
            mid = (l+r)//2
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] > target:
                r = mid - 1
            else:
                l = mid + 1
        
        left, right = 0, len(matrix[0]) - 1
        while left <= right:
            mid = (left+right)//2
            if matrix[r][mid] == target:
                return True
            elif matrix[r][mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return False 