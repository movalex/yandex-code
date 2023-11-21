class Solution:
    def numberOfSteps(self, num: int) -> int:
        counter = 0
        while num > 0:
            if num % 2 == 0:
                num /= 2
            else:
                num -= 1
            counter += 1
        return counter


class Solution:
    def number_of_steps(self, num: int) -> int:
        counter = 0
        while num > 0:
            if num & 1 == 0:  # check if rightmost bit is 1 (odd) or 0 (even)
                num = num >> 1  # divde by 2 by shifting bitts to the left
            else:
                num -= 1
            counter += 1
        return counter
