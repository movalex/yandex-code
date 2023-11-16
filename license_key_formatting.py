import unittest


class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        result = ""
        s = s.replace("-", "")
        first = len(s) % k
        if first != 0:
            result += s[:first] + "-"
        for i, char in enumerate(s[first:], 1):
            if i % k == 0:
                result += f"{char}-"
            else:
                result += char
        result = result.rstrip("-")
        return result.upper()


class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        result = ""
        s = s.replace("-", "")[::-1]  # reverse the string to get the first element last
        counter = 0

        for char in s:
            if counter == k:
                result += "-"
                counter = 0
            result += char
            counter += 1

        return result.upper()[::-1]  # reverse back


class TestFormatting(unittest.TestCase):
    def setUp(self):
        self.func = Solution()

    def test_formatting1(self):
        actual = self.func.licenseKeyFormatting("5F3Z-2e-9-w", 4)
        expected = "5F3Z-2E9W"
        self.assertEqual(actual, expected)

    def test_formatting2(self):
        actual = self.func.licenseKeyFormatting("2-5g-3-J", 2)
        expected = "2-5G-3J"
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
