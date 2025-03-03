class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        tmp = True
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                tmp = False

        if tmp:
            return nums
        l, r = 0, len(nums)-1 
        cnt = 0
        while l <= r:
            # print([nums,l,r])
            if nums[l] < pivot:
                l+=1
            else:
                n = nums.pop(l)
                if n != pivot:
                    nums.append(n)
                else:
                    nums.insert(r,n)
                r-=1

        return nums
                