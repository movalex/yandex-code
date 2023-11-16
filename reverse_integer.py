class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0
        result = 0
        orig_num = x
        if orig_num < 0:
            x *= -1

        while x:
            last_digit = x % 10
            result = result * 10 + last_digit
            x = x // 10
        
        if orig_num < 0:
            result *= -1
        
        if result > 2**31-1 or result < -2**31:
            return 0
        
        return result
