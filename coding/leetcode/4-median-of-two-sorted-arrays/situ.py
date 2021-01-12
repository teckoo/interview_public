class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        len_1 = len(nums1)
        len_2 = len(nums2)
        if len_1 > len_2:
            nums1, nums2, len_1, len_2 = nums2, nums1, len_2, len_1

        is_odd = (len_1+len_2)%2
        # if the number is odd, return the middle one
        # else, return the avg
        left_1, right_1 = 0, len_1
        left_2, right_2 = 0, len_2
        half_len = (len_1 + len_2 + 1) // 2

        while left_1 <= right_1:
            mid_1 = left_1 + (right_1 - left_1) // 2
            mid_2 = half_len - mid_1
            if mid_1 < len_1 and nums2[mid_2-1] > nums1[mid_1]:
                # mid_1 is too small
                left_1 = mid_1 + 1
            elif mid_1 > 0 and nums1[mid_1-1] > nums2[mid_2]:
                # mid_1 is too big
                right_1 = mid_1 - 1
            else:
                # mid_1 is perfect
                if mid_1 == 0:
                    max_left = nums2[mid_2 - 1]
                elif mid_2 == 0:
                    max_left = nums1[mid_1 - 1]
                else:
                    max_left = max(nums1[mid_1 - 1], nums2[mid_2 - 1])

                if is_odd: return max_left

                if mid_1 == len_1:
                    min_right = nums2[mid_2]
                elif mid_2 == len_2:
                    min_right = nums1[mid_1]
                else:
                    min_right = min(nums1[mid_1], nums2[mid_2])

                return (max_left + min_right) / 2
