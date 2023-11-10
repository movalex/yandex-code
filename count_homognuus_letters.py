"""Given a string s, return the number of homogenous substrings of s. Since the answer may be too large, return it modulo 109 + 7.
A string is homogenous if all the characters of the string are the same.
A substring is a contiguous sequence of characters within a string."""


def countHomogenous(s: str) -> int:
    """
    first attempt
    """
    count = 1
    letters = 0
    result = {}
    s_set = set(s)
    while count < len(s):
        for element in s_set:
            substring = element * count
            print(substring)
            for string in s:
                if substring == string:
                    letters += 1
                    result[substring] = letters

        count += 1
    return result


class Solution:
    def countHomogenous(self, s: str) -> int:
        MOD = 10**9 + 7
        res = {}
        total = 0
        for letter, groups in groupby(s):
            repeating_count = len(list(groups))
            # print(repeating_count)
            total += repeating_count * (repeating_count + 1) // 2
            total %= MOD
        return total


s = Solution()
s.countHomogenous("aaabbccaaaa")


from math import comb


class Solution:
    def countHomogenous(self, s: str) -> int:
        MOD = 10**9 + 7
        prev = s[0]
        counter = 0
        result = 0
        for c in s:
            if c == prev:
                counter += 1
            else:
                result += comb(counter + 1, 2)
                counter = 1
            prev = c
        result += comb(counter + 1, 2)
        return result


s = Solution()
s.countHomogenous("dfdjdjjjjjjsssss")


class Solution:
    def countHomogenous(self, s: str) -> int:
        ans = 0
        curr_streak = 0
        MOD = 10**9 + 7

        for i, string in enumerate(s):
            if i == 0 or string == s[i - 1]:
                curr_streak += 1
            else:
                curr_streak = 1

            ans += curr_streak

        return ans % MOD


s = Solution()
s.countHomogenous("dfdjdjjjjjjsssss")
