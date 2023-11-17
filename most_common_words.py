import unittest
import re
from typing import List
from collections import Counter


class Solution:
    def most_common_word(self, paragraph: str, banned: List[str]) -> str:
        """
        Input: paragraph = "Bob hit a ball, the hit BALL flew far after it was hit.", banned = ["hit"]
        Output: "ball"
        Explanation:
        "hit" occurs 3 times, but it is a banned word.
        "ball" occurs twice (and no other word does), so it is the most frequent non-banned word in the paragraph.
        Note that words in the paragraph are not case sensitive,
        that punctuation is ignored (even if adjacent to words, such as "ball,"),
        and that "hit" isn't the answer even though it occurs more because it is banned.
        """
        paragraph = re.sub("[.,!?;']", " ", paragraph.lower())
        count = Counter(paragraph.split())
        mc = count.most_common()

        for word, num in mc:
            if word not in banned:
                return word


class TestFormatting(unittest.TestCase):
    def setUp(self):
        self.func = Solution()

    def test_formatting1(self):
        paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
        banned = ["hit"]
        actual = self.func.most_common_word(paragraph, banned)
        expected = "ball"
        self.assertEqual(actual, expected)

    def test_formatting2(self):
        paragraph = "Bob bAlL, hIt. ball Int int hit!"
        banned = ["ball", "int"]
        actual = self.func.most_common_word(paragraph, banned)
        expected = "hit"
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
