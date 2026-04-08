class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0]*len(temperatures)
        for i in range(len(temperatures)-1):
            count = 0
            for j in range(i+1,len(temperatures)):
                count+=1
                if temperatures[i] < temperatures[j]:
                    res[i] = count
                    break
            else:
                res[i] = 0
        res[-1] = 0

        return res
