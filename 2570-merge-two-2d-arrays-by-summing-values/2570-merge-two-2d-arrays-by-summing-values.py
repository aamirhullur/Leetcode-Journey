class Solution:
    def mergeArrays(
        self, nums1: list[list[int]], nums2: list[list[int]]
    ) -> list[list[int]]:
        N1, N2 = len(nums1), len(nums2)
        ptr1, ptr2 = 0, 0

        merged_array = []
        while ptr1 < N1 and ptr2 < N2:
            # If the id is same, add the values and insert to the result.
            # Increment both pointers.
            if nums1[ptr1][0] == nums2[ptr2][0]:
                merged_array.append(
                    [nums1[ptr1][0], nums1[ptr1][1] + nums2[ptr2][1]]
                )
                ptr1 += 1
                ptr2 += 1
            elif nums1[ptr1][0] < nums2[ptr2][0]:
                # If the id in nums1 is smaller, add it to result and increment the pointer
                merged_array.append(nums1[ptr1])
                ptr1 += 1
            else:
                # If the id in nums2 is smaller, add it to result and increment the pointer
                merged_array.append(nums2[ptr2])
                ptr2 += 1

        # If pairs are remaining in the nums1, then add them to the result.
        while ptr1 < N1:
            merged_array.append(nums1[ptr1])
            ptr1 += 1

        # If pairs are remaining in the nums2, then add them to the result.
        while ptr2 < N2:
            merged_array.append(nums2[ptr2])
            ptr2 += 1

        return merged_array