class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res= [0]*len(temperatures)
        stack=[]
        for indx, val in enumerate(temperatures):
            while stack and stack[-1][0] < val:
                    res[stack[-1][1]] = indx - stack[-1][1]
                    stack.pop()
            stack.append([val,indx]) 

        return res
