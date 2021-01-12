import collections


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # use shorter list for hashmap
        if len(nums2) > len(nums1):
            nums1, nums2 = nums2, nums1

        counter = collections.Counter(nums1)
        ans = []
        for n in nums2:
            if n in counter:
                if counter[n] > 0:
                    counter[n] -= 1
                    ans.append(n)
        return ans
