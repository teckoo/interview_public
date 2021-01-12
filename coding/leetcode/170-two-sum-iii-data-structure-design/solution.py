class TwoSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nums = {}

    def add(self, number: int) -> None:
        """
        Add the number to an internal data structure..
        """
        self.nums[number] = self.nums.get(number, 0) + 1

    def find(self, value: int) -> bool:
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        """
        for key in self.nums:
            res = value - key
            if key != res and res in self.nums:
                return True
            if key == res and self.nums[key] > 1:
                return True

        return False
