class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        if s == "":
            return True

        for i in s:
            if i in "[{(":
                stack.append(i)
            else:
                if not stack:
                    return False
                else:
                    if i == "}" and stack[-1] == "{":
                        stack.pop()
                    elif i == "]" and stack[-1] == "[":
                        stack.pop()
                    elif i == ")" and stack[-1] == "(":
                        stack.pop()
                    else:
                        return False
        return not stack

        