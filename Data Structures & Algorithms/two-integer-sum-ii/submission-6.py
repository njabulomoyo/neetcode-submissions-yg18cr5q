class Solution:
    """
    understand:
    two sum, sorted array
    - input - sorted array
    - output - [1-indexed indices]
    edge cases?
    - empty list?
    - time complexity? o(n)
    - space o(1)

    Match:
     - two pointers

    Plan:
    1. initiate the two pointers, one on the left and one on the right 
    2. check if the numbers on those pointers add to the target?
    3. if they add up to a number greater than the target, move the right pointer to the left
    4. if the sum is less, move the left pointer to the right
    5. if equal to the target, return the pointers pluss one
    6. end  
    """
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers)-1
        while l<r:
            if numbers[l] + numbers[r] == target:
                return [l+1,r+1]
            elif numbers[l] + numbers[r] < target:
                l += 1
            else:
                r -= 1

        