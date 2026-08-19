class Solution:
    """
    output: list of list with combination
    edge cases: duplicates? input cant be empty
    solution:
    - initiate rsult list
    - sort the list
    - have three pointers, i,j, k
    - create a function for checking the 2sum from index j till the end
    - after checking the 2sum for the rest of the list, move the i pointer
    - if the next elem is the same as prev, skip
    - skip til you find a unique element
    - add the result list
    - return list of list

    """
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        for i, val in enumerate(nums):
            if i > 0 and nums[i-1] == val:
                continue

            j,k = i+1, len(nums)-1
            
            
            while j<k:
                summ = val + nums[j] + nums[k]
                #print('this is sum',summ)
                if summ < 0:
                    j += 1
                    
                elif summ> 0:
                    k -= 1
                    
                else:
                    result.append([val, nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j-1]:
                        j += 1
                    
                    while j < k and nums[k] == nums[k+1]:
                        k -= 1


        return result
                    





        