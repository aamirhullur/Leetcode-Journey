class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        if len(flowerbed) == 1:
            if flowerbed[0] == 1:
                return True if n == 0 else False
            else:
                return True if n < 2 else False 
        for i in range(len(flowerbed)):
            if flowerbed[i] == 1:
                continue
            else:
                if i == 0:
                    # print('a')
                    if flowerbed[i+1] != 1:
                        flowerbed[i] = 1
                        n-=1
                elif i == len(flowerbed) - 1:
                    # print('b')
                    if flowerbed[i-1] != 1:
                        flowerbed[i] = 1
                        n-=1
                else:
                    # print('c')
                    if flowerbed[i-1] != 1 and flowerbed[i+1] != 1:
                        flowerbed[i] = 1
                        n-=1
        
        return True if n < 1 else False 
