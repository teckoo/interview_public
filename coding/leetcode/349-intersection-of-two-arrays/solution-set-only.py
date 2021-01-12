class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        def intersect(nums1, nums2):
            return [n for n in nums1 if n in nums2]

        nums1 = set(nums1)
        nums2 = set(nums2)
        if len(nums1) < len(nums2):
            return intersect(nums1, nums2)
        else:
            return intersect(nums2, nums1)
