class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        exp = ["+","-","*","/"]

        for i in tokens:
            if i not in exp:
                stack.append(float(i))
            else:
                a = stack.pop()
                b = stack.pop()
                if i == "+":
                    res = b + a
                elif i == "-":
                    res = b - a
                elif i == "*":
                    res = b * a
                else:
                    res = b / a
                    if res < 0:
                        res = ceil(res)
                    else:
                        res = floor(res)
                stack.append(int(res))

        return int(stack[-1])
        # for i in range(len(tokens)):
        #     print(stack)
        #     if tokens[i] not in exp:
        #         stack.append(str(tokens[i]))
        #     else:
        #         a = stack.pop()
        #         b = stack.pop()
        #         print([a,b,str(tokens[i])])
        #         if 
                
        #         # res = eval(b+str(tokens[i])+a)
        #         # print(eval(str(b+str(tokens[i]+a))))
        #         # print(res)
        #         # if res < 0:
        #         #     res = str(int(ceil(res)))
        #         # else:
        #         #     res = str(int(floor(res)))

        #         # stack.append(res)
                
        # return int(stack[-1])


        

