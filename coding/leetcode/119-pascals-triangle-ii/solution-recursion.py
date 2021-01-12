class Solution:
    def __init__(self):
        self.memo = {}

    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex in (0, 1): return [1] * (rowIndex + 1)
        if rowIndex not in self.memo:
            prev_row = self.getRow(rowIndex - 1)
            row = [1] + [prev_row[i-1] + prev_row[i] for i in range(1, rowIndex)] + [1]
            self.memo[rowIndex] = row
        return self.memo[rowIndex]
