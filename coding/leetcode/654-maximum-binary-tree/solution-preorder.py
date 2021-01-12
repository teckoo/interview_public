# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        def build(nums, lo, hi):
            # find the max value and its index
            if lo > hi: return None
            mi, mv = hi, nums[hi]
            for i in range(lo, hi):
                if nums[i] > mv:
                    mi, mv = i,nums[i]
            #print(f"mi={mi}, mv={mv}, left:[{lo}, {mi-1}], right=[{mi+1}, {hi}]")
            root = TreeNode(mv)
            root.left = build(nums, lo, mi - 1)
            root.right = build(nums, mi + 1, hi)
            return root

        if not nums: return None
        return build(nums, 0, len(nums) - 1)
