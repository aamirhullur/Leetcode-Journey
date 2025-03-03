class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        cnt = 0
        if n == 0:
            return True
            
        if len(flowerbed) == 1:
            return True if not flowerbed[0] else False

        for i in range(len(flowerbed)):
            if not flowerbed[i]:
                if i == 0 and not flowerbed[i] and not flowerbed[i+1]:
                    cnt+=1
                    flowerbed[i] = 1
                elif i == len(flowerbed)-1 and not flowerbed[i] and not flowerbed[i-1]:
                    cnt+=1
                    flowerbed[i] = 1
                elif not flowerbed[i-1] and not flowerbed[i+1]:
                    cnt +=1 
                    flowerbed[i] = 1

        print(cnt)
        return True if n <= cnt else False
