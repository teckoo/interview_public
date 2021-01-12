class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1, p2 = m - 1, n - 1
        pos = p1 + p2 + 1
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]: 
                nums1[pos] = nums1[p1]
                p1 -= 1
            else:
                nums1[pos] = nums2[p2]
                p2 -= 1
            pos -= 1
        if p2 >= 0:
            for i in range(p2 + 1):
                nums1[i] = nums2[i]
