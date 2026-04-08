class Solution:
    """
    output - lsit showing days before a warmer day comes

    Plan:
        1. create new stack
        2. create new list with len equal to the input
        3. iteate thru the list
        4. append numbers that are less than number on top of the stack
        5. if you find number greater, subtract the index of that number and that of the num at top of the stack
        6. update the index of the pop number on the result lit with the diff
        7. do this until you get to the end

    """
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)

        for ind, val in enumerate(temperatures):
            if not stack:
                stack.append((ind,val))
            elif stack[-1][1] >= val:
                stack.append((ind,val))
            else:
                while stack and stack[-1][1] < val:
                    last = stack.pop()[0]
                    diff = ind - last
                    res[last] = diff
                stack.append((ind,val))

        return res












