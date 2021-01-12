class Solution:
    def shortestSubarray(self, A: List[int], K: int) -> int:
        N = len(A) + 1
        P = [0] * N
        for i in range(N-1):
            P[i+1] = P[i] + A[i]

        #Want smallest y-x with Py - Px >= K
        ans = N # length + 1 is impossible
        monoq = collections.deque() #opt(y) candidates, represented as indices of P
        for y, Py in enumerate(P):
            #Want opt(y) = largest x with Px <= Py - K
            while monoq and Py <= P[monoq[-1]]:
                monoq.pop()

            while monoq and Py - P[monoq[0]] >= K:
                ans = min(ans, y - monoq.popleft())

            monoq.append(y)

        return ans if ans < N else -1
