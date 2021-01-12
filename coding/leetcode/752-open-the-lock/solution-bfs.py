class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        def next_state(s):
            result = []
            for i in range(len(s)):
                ch = int(s[i])
                for d in (-1, 1):
                    y = (ch + d) % 10
                    yield s[:i] + str(y) + s[i+1:]

        que = collections.deque([("0000", 0)])
        deadends = set(deadends)
        visited = set()
        while que:
            state, num = que.popleft()
            if state == target: return num
            if state in deadends: continue
            for s in next_state(state):
                if s in visited: continue 
                que.append((s, num + 1))
                visited.add(s)

        return -1
