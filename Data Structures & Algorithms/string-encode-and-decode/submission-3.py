class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for word in strs:
            res += str(len(word)) + "!" + word
        return res
    #"4!neet4!code4!love3!you"
    def decode(self, s: str) -> List[str]:


        res = []
        i = 0
        "4!love3!you"
        while i < len(s):
            num = ""
            word = ""
            while s[i] != "!":
                num += s[i]
                i += 1
            # i=1         i+1=2, i+1+int(num)=6
            for j in range(i+1, i + 1 + int(num)):
                word += s[j]

            res.append(word)
            i = i + int(num) + 1

        return res






