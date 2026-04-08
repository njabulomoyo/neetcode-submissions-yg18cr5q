class Solution:
    """
    edge cases:
        ~empty list: return ""
        ~
    
    """

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        res = ""
        for string in strs:
            res += str(len(string)) + '#' + string

        return res

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        #'4#neet4#code4love3you'
        i = 0
        res = []
        while i < len(s):
            num = ""
            while s[i] != "#":
                num += s[i]
                i += 1

            num = int(num)
            res.append(s[i+1:i+1+num])

            i = i + 1 + num

        return res





