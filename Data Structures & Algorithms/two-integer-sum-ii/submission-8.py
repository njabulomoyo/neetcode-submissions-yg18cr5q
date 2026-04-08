class Solution:
    """
    output - list (1-indexed)
    we need the indices
    list is sorted
    empty list? no

    Plan:
        1. have two pointers, one at the start and another at the end
        2. check the sum of the numbers at the pointers, if they are equal to target, return indexes
        3. it the sum is greater than target, move right pointer
        4. if sum is less than the target, move the left pointer
        5. check till you find solution
        return 1-indexes
    """
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        while l < r:
            num = numbers[l] + numbers[r]
            if num < target:
               l += 1
            elif num > target:
                r -= 1
            else:
                return [l+1, r+1]



