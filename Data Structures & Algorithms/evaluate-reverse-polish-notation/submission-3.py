class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1:
            return int(tokens[0])

        ans = []   
        for elem in tokens:          
            if elem == "+":
                num = ans.pop() + ans.pop()
                ans.append(num)
                
            elif elem == "*":
                num = ans.pop() * ans.pop()
                ans.append(num)
                
            elif elem == "-":
                a=ans.pop()
                b=ans.pop()
                ans.append(b-a)
                
            elif elem == "/":
                a=ans.pop()
                b=ans.pop()
                ans.append(int(b/a))

            else:
                ans.append(int(elem))

        return ans[0]

            
        