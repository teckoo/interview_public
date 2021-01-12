class Solution:
    """ merge sort, top down approach"""
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) < 2: return nums

        pivot = len(nums) // 2
        sm_lst = self.sortArray(nums[:pivot])
        bg_lst = self.sortArray(nums[pivot:])
        return self.merge(sm_lst, bg_lst)

    def merge(self, list_1, list_2):
        idx_1, idx_2 = 0, 0
        ret = []
        while idx_1 < len(list_1) and idx_2 < len(list_2):
            if list_1[idx_1] < list_2[idx_2]:
                ret.append(list_1[idx_1])
                idx_1 += 1
            else:
                ret.append(list_2[idx_2])
                idx_2 += 1
        ret.extend(list_1[idx_1:])
        ret.extend(list_2[idx_2:])
        return ret
