class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs= []
        stack = []
        for i in range(len(position)):
            pairs.append([position[i],speed[i]])

        print(sorted(pairs)[::-1])

        for pair in sorted(pairs)[::-1]:            
            curr = (target - pair[0])/pair[1]
            if not stack:
                stack.append(curr)
                continue
            if stack and curr > stack[-1]:
                stack.append(curr)

        return len(stack)



        
