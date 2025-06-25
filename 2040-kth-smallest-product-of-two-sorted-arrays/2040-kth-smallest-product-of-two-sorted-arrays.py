class Solution:
    def kthSmallestProduct(
        self, nums1: List[int], nums2: List[int], k: int
    ) -> int:

        def f(nums2: List[int], x1: int, v: int) -> int:
            if x1 > 0:
                return bisect_right(nums2, v // x1)
            elif x1 < 0:
                return len(nums2) - bisect_left(nums2, -(-v // x1))
            else:
                return len(nums2) if v >= 0 else 0
        
        left, right = -(10**10), 10**10
        while left <= right:
            mid = (left + right) // 2
            count = sum(f(nums2,nums1[i],mid) for i in range(len(nums1)))
            if count < k:
                left = mid + 1
            else:
                right = mid - 1
        return left