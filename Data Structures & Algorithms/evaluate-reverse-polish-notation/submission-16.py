class Solution:
    """
    give the calculation/ evealuation from the given string.

    Plan:
        1. create a stack
        2. if you see a number, add it to the stack
        3. if you find a symbol, pop() twice and use those numbers and the operater 
        4. add what you get when you using the operator and the numbers
        5. do this till the end of the string
    """
    def evalRPN(self, tokens: List[str]) -> int:
        stck = []
        summ = 0
        for i in tokens:
            if i not in "+-*/":
                stck.append(int(i))
            else:
                nums1 = stck.pop()
                nums2 = stck.pop()
                if i == "+":
                    summ = nums1 + nums2
                elif i == "*":
                    summ = nums1 * nums2
                elif i == "/":
                    summ = nums2 / nums1
                elif i == "-" :
                    summ = nums2 - nums1

                stck.append(int(summ))
        
        return stck.pop()






