# Runtime: 36 ms, faster than 53.60% of Python3 online submissions for Reorder Data in Log Files.
# Memory Usage: 12.6 MB, less than 100.00% of Python3 online submissions for Reorder Data in Log Files.

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        def f(log):
            id_, rest = log.split(" ", 1)
            return (0, rest, id_) if rest[0].isalpha() else (1,)

        return sorted(logs, key = f)
