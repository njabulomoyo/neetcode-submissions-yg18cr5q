class Solution:
    """
    find the houses that will give the most money

    Brainstorm:
    output: int
    - going thru the list, checking the numbers, adding them to some total variable
    - problem solution can be represented as a tree, for the decisions that will be made
    - you start with index 0 or one, then you skip over one and then check the next one
    -question? is it always that we skip one house, can it be more than one? like skip two houses?
    - we can start of at index 0 or 1

    Solution:
    - start with index 1 or 2,
    - start adding the numbers, skipping houses by one, until end of list
    - return the maximum
    """
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        robbers = [0]*n
        
        #[rob1, rob2, n, n+1,....]
        def dfs(i):
            if i>=n:
                return 0

            if robbers[i] != 0:
                return robbers[i]

            robbers[i] = max(dfs(i+1), nums[i]+ dfs(i+2))

            return robbers[i]

        

        return dfs(0)
        

        