# Let's remember count[V], the number of previous prefix sums with value V. If our newest prefix sum has value W, and W-V == K, then we add count[V] to our answer.

# This is because at time t, A[0] + A[1] + ... + A[t-1] = W, and there are count[V] indices j with j < t-1 and A[0] + A[1] + ... + A[j] = V. Thus, there are count[V] subarrays A[j+1] + A[j+2] + ... + A[t-1] = K.

# time: O(N)
import collections
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = collections.Counter()
        count[0] = 1
        ans = sum = 0
        for x in A:
            sum += x
            ans += count[sum-K]
            count[sum] += 1
        return ans
