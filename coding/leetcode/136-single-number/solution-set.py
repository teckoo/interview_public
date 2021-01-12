class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # one-line math soltution
        # return 2 * sum(set(nums)) - sum(nums)
        #
        # verbal solution using hashset
        items = set()
        for n in nums:
            if n in items:
                items.remove(n)
            else:
                items.add(n)

        return list(items)[0] if len(items) == 1 else None
