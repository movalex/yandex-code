class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
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
        mc = count.most_common(2)

        for word, num in mc:
            if word not in banned:
                return word
