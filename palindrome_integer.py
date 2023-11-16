class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0) :
            return False
        """use string conversion"""
        # check = str(x)
        # if check == check[::-1]:
        #     return True
        # return False
        
        """use maths"""
        # find last half of the number
        # if reversed half == first half, return True
        
        reversed_number = 0
        
        while x > reversed_number:
            print(x)
            last_number = x % 10
            reversed_number = reversed_number * 10 + last_number
            print(reversed_number)
            x = x // 10
        
        return x == reversed_number or x == reversed_number // 10
            
