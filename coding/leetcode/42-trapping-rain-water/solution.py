" Runtime: 44 ms, faster than 97.88% of Python3 online submissions for Trapping Rain Water.
" Memory Usage: 13.5 MB, less than 67.44% of Python3 online submissions for Trapping Rain Water.
from collections import deque

class Solution(object):
    def trap(self, height: List[int]) -> int:
        if len(height) < 3:
            return 0
        stack = deque()
        left_max = 0
        ans = 0
        for val in height:
            if left_max <= val:  # process stack
                while stack:
                    ans += left_max - stack.pop()
                left_max = val
            else:
                stack.append(val)
        if stack:
            right_max = stack.pop()
        while stack:
            cur = stack.pop()
            if cur < right_max:
                ans += right_max - cur
            else:
                right_max = cur

        return ans
