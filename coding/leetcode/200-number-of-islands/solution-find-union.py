# Runtime: 124 ms, faster than 98.76% of Python3 online submissions for Number of Islands.
# Memory Usage: 13.7 MB, less than 85.47% of Python3 online submissions for Number of Islands.

class Solution:

    def __init__(self):
        self.flags = []
        self.islands = 0
        self.island_set = set()

    def numIslands(self, grid: List[List[str]]) -> int:
        row = len(grid)
        if row == 0:
            return 0
        col = len(grid[0])
        # initialize parent matrix
        [self.flags.append([0]*col) for _ in range(row)]

        for x in range(0, row):
            for y in range(0, col):
                self.lookup(x, y, grid)
        return len(self.island_set)

    def lookup(self, x, y, g):
        if g[x][y] == '0':  # skip 0s
            return 0

        # first cell
        if x == 0 and y == 0 and g[x][y]=='1':
            self.islands += 1
            self.flags[x][y] = self.islands
            self.island_set.add(self.islands)
            return

        # first row
        if x == 0:
            if g[x][y-1] == '1':
                # print("1st row union:", x, y, self.flags[x][y-1])
                self.flags[x][y] = self.flags[x][y-1]
            else:
                # print(x, y, g[x][y])
                self.islands += 1
                self.flags[x][y] = self.islands
                self.island_set.add(self.islands)
            return

        # 2nd row and below
        # 1st column
        if y==0:
            if g[x-1][y] == '1':
                # print("1st col union:", x, y, self.flags[x-1][y])
                self.flags[x][y] = self.flags[x-1][y]
            else:
                # print(x, y, g[x][y])
                self.islands += 1
                self.flags[x][y] = self.islands
                self.island_set.add(self.islands)
        else:  # regular cells
            if g[x][y-1] == '1' and g[x-1][y] == '1':  # union islands
                self.flags[x][y] = self.flags[x][y-1]
                if self.flags[x][y-1] != self.flags[x-1][y]:
                    # print("union:", x, y, self.flags[x][y-1], self.flags[x-1][y])
                    self.union_islands(self.flags[x][y-1], self.flags[x-1][y])

            elif g[x][y-1] == '1':
                self.flags[x][y] = self.flags[x][y-1]
            elif g[x-1][y] == '1':
                self.flags[x][y] = self.flags[x-1][y]
            else:
                # print(x, y, g[x][y])
                self.islands += 1
                self.flags[x][y] = self.islands
                self.island_set.add(self.islands)

    def union_islands(self, m, n):
        small = min(m, n)
        big = max(m, n)

        for x in range(len(self.flags)):
            for y in range(len(self.flags[x])):
                if self.flags[x][y] == big:
                    self.flags[x][y] = small
        self.island_set.remove(big)
