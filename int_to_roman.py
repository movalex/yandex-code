class Solution:
    def intToRoman(self, num: int) -> str:
        roman = {}
        symbols = {
            1: "I",
            4: "IV",
            5: "V",
            9: "IX",
            10: "X",
            40: "XL",
            50: "L",
            90: "XC",
            100: "C",
            400: "CD",
            500: "D",
            900: "CM",
            1000: "M",
        }

        result = ""
        for digit in sorted(symbols.keys(), reverse=True):
            # print(digit)
            if num // digit == 0:
                continue
            result = result + (symbols[digit] * (num // digit))
            # roman[digit] = num // digit
            num %= digit

        return result


s = Solution()

result = s.intToRoman(1214)
print(result)
