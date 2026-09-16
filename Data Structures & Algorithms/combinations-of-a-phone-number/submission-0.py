class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        res = []
        digit2lst = {
            "2":"abc",
            "3": "def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }

        def dfs(i, sub):
          
            if len(sub) == len(digits):
                res.append(sub)
                return 
            for letter in digit2lst[digits[i]]:
                dfs(i+1, sub + letter)

        dfs(0,"")
        return res
            

        