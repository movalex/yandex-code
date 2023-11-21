class Solution:
    def canConstruct(self, ransom_note: str, magazine: str) -> bool:
        count = 0
        match_index = None
        for i in ransom_note:
            match_index = magazine.rfind(i)
            if match_index == -1:
                return False
            magazine = magazine[:match_index] + magazine[match_index + 1 :]
        return True


class Solution:
    def canConstruct(self, ransom_note: str, magazine: str) -> bool:
        if len(magazine) < len(ransom_note):
            return False

        counter_dict = {}

        for magazine_letter in magazine:
            current_count = counter_dict.get(magazine_letter, 0)
            counter_dict[magazine_letter] = current_count + 1

        for ransom_letter in ransom_note:
            current_count = counter_dict.get(ransom_letter, 0)
            if current_count == 0:
                return False
            counter_dict[ransom_letter] = current_count - 1

        return True
