class Solution:
    """
    output - boolean

    Plan: 
        1. create a stack
        2 iterate thru the sting
        3. if you find an opening paranthesis, add it to the stack
        4. if its a closing paranthesis, pop the stack and compare 
        5. if the parenthesises are of the same type, then continue
        6. otherwise, return False
        7. do this for all the elements

    """
    def isValid(self, s: str) -> bool:
        stack = []

        for i in s:
            if i in "{[(":
                stack.append(i)

            else:
                if stack:
                    open = stack.pop()
                    if (open == "{" and i == "}" or
                        open == "[" and i == "]" or
                        open == "(" and i == ")"):
                        continue
                   
                return False
        if stack:
            return False

        return True

        