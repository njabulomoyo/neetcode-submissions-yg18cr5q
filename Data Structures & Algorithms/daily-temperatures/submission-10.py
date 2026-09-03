class Solution:
    """
    [30,38,30,36,35,40,28]
       
         
    stack = [(30,0)]

    pop()
    tmps[l] = r-l
    append(r)
    l += 1

    """
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0]*(len(temperatures))
        for ind, cur in enumerate(temperatures):
            if not stack:
                stack.append((ind, cur))
            
            if cur > stack[-1][1]:
                while stack and cur > stack[-1][1]:
                    i, val = stack.pop()
                    res[i] = ind - i
                stack.append((ind, cur))
            else:
                stack.append((ind, cur))

        return res

        