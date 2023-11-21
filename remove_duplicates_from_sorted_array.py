class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        start from the second value as the first one always valid
        check if the current value is larger than previous
        if so, update the pointer, (a place where the difference is found).
        That would be exactly the length of a new array.
        The values are replaced in-place, the complexity is O(2n) or O(n)
        """
        result = 1
        for last in range(1, len(nums)):
            if nums[last] > nums[last - 1]:
                nums[result] = nums[last]
                result += 1
        return result
