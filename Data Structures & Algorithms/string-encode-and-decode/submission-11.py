class Solution:
    """
    understanding:
    input - list of strings
    ouput -  list that 
    time and space complexity 
    plan:

    """

    def encode(self, strs: List[str]) -> str:
        res = []
        for word in strs:
            res.append(str(len(word)) + "*" + word)

        return "".join(res)

    #"4*love3*you"
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            num = ""
            while s[i] != "*":
                num += s[i]
                i += 1
            num = int(num)
            word = ""
            for j in range(i+1,i+1+num):
                word += s[j]

            res.append(word)
            i = i + 1 + num
        
        return res














