class Solution:
    def trap(self, height: List[int]) -> int:
        # def calc(m,n):
        #     h = min(height[m],height[n])
        #     l = (n-m-1)
        #     block = 0
        #     water = h * l
        #     for x in range(m+1,n):
        #         if height[x] > h:
        #             block += h
        #         else:
        #             block += height[x]
        #     water -= block
        #     print([m,n,height[m],height[n],water])
        #     return water
        # print(len(height))
        # l = 0
        # res = 0
        # f_res = 0
        # while l < len(height):
        #     while l<len(height) and not height[l]:
        #         l+=1
        #     r = l+1

        #     while r < len(height):
        #         res = max(calc(l,r), res)
        #         if height[r] >= height[l]:
        #             l = r-1
        #             f_res += res
        #             res = 0
        #             break
        #         r+=1
        #     print(f'res,f_res:{[l,r,res,f_res]}')
        #     if r == len(height):
        #         f_res += res
        #         return f_res
        #     l+=1
        # return f_res

        n = len(height)

        if n == 0:
            return 0

        left_max = [0] * n
        right_max = [0] * n

        left_max[0] = height[0]
        for i in range(1,n):
            left_max[i] = max(left_max[i-1],height[i-1])
        
        right_max[n-1] = height[n-1]
        for i in range(n-2,-1,-1):
            right_max[i] = max(right_max[i+1],height[i+1])


        res = 0
        for i in range(len(height)):
            water = min(left_max[i],right_max[i]) - height[i]
            if water > 0:
                res+=water

        return res