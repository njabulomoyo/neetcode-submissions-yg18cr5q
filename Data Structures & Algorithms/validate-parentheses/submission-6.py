class Solution:
    """
    understand:
        - input - string
        - output - boolean
        empty string? 
        expected time o(n) and space o(n/2)?

    plan:
        1. create a stack
        2. iterate thru string
        3. if char is opening parenthesis, append
        4. if not check what kind is it
        5. if it doesnt match the opening on top, return False
        6. otherwise, continue
    """
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i in "{[(":
                stack.append(i)
            else:
                if not stack:
                    return False                    
                open = stack.pop()
                if open == "{" and i ==  "}":
                    continue
                elif open == "[" and i ==  "]":
                    continue
                elif open == "(" and i ==  ")":
                    continue
                else:
                    return False            
        if stack:
            return False
        return True















        