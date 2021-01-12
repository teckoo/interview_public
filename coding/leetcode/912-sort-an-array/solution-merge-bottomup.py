class Solution:
    """ merge sort, bottom up approach"""
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) < 2: return nums

        merge_list = [[i] for i in nums]
        tmp_list = []
        while len(merge_list) > 1:
            for idx in range(0, len(merge_list) - 1, 2):  #0, 2
                tmp_list.append(self.merge(merge_list[idx], merge_list[idx+1]))
            if idx + 2 < len(merge_list):  # for odd residue item
                tmp_list.append(merge_list[idx + 2])
            merge_list = tmp_list   ## [[2, 5], [1, 3]] 
            tmp_list = []
        return merge_list[0]

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
