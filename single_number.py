from collections import Counter


class Solution:
    def __init__(self, nums: list([int])):
        self.nums = nums

    @property
    def singleNumber(self) -> int:
        """
        return the number that occurs in the list once
        """
        # maths
        # a = 1
        # b = 2
        # c = 3
        # [1,1,1,2,2,3]
        # 2a + 2b + c = 2 (a + b + c) - c
        # c = 2 (a + b + c) - 2a - 2b?
        # 2 (a + b + c) - (a + a + b + b + c) = c
        # return 2 * sum(set(self.nums)) - sum(self.nums)

        check = Counter(self.nums)
        for k, v in check.items():
            if v == 1:
                return k
        return "No single numbers found"


l = [1, 1, 1, 2, 3, 3, 3, 3, 0, 0]


result = Solution(l).singleNumber
print(result)
