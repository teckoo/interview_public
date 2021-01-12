def findNumbers(self, nums: List[int]) -> int:
    return sum(len(str(n)) % 2 == 0 for n in nums)


def findNumbers(self, nums: List[int]) -> int:
    # log10(n) + 1 is the # of digits. e.g. log10(11) = 1.04
    return sum(int(math.log10(n)) % 2 for n in nums)
