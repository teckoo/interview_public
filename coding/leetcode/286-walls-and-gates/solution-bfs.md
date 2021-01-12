import collections


class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        if not rooms or not rooms[0]: return None
        m, n = len(rooms), len(rooms[0])
        max_step = m * n
        q = collections.deque([(i, j) for i, row in enumerate(rooms) \
                                        for j, r in enumerate(row) if not r])
        while q:
            i, j = q.popleft()
            for x, y in (i+1, j), (i-1, j), (i, j+1), (i, j-1):
                if 0 <= x < m and 0 <= y < n and rooms[x][y] > max_step:
                    rooms[x][y] = rooms[i][j] + 1
                    q.append((x, y))
