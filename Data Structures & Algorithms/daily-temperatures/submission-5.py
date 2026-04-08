class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0]*len(temperatures)
        stack = []
        #[(40,5),(28,6)]
        for ind, val in enumerate(temperatures):
            if not stack:
                stack.append((val,ind))
                continue
            if stack[-1][0] >= val: #(28,6)
                stack.append((val,ind))
            else:
                while stack and stack[-1][0] < val:
                    last = stack.pop()[1]
                    diff = ind - last
                    res[last] = diff
                stack.append((val,ind))
                

        return res

            
            