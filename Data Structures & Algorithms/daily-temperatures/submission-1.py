class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0]*len(temperatures)
        stack = [] #pairs [temp,indx]

        for indx, elem in enumerate(temperatures):
            while stack and elem > stack[-1][0]:
                resElem, resIndx = stack.pop()
                res[resIndx] = indx - resIndx
            stack.append([elem,indx])

        return res
