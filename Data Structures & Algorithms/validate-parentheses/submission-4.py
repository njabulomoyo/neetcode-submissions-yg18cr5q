from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        store = deque()
        for elem in s:
            if elem in "{[(":
                store.append(elem)
            else:
                if not store:
                    return False
                else:                        
                    op = store.pop()
                    if (elem == "}" and op == "{" or
                    elem == "]" and op == "[" or 
                    elem == ")" and op == "("):                
                        continue
                    else:
                        return False
        return not store
        