class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        nums1.extend(nums2)  #  extend the list instead of creating new one
        nums1.sort()
        middle = len(nums1) // 2
        if len(nums1) % 2 == 0:
            i, j = nums1[middle - 1], nums1[middle]
            return (i + j) / 2
        else:
            return nums1[middle]


class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        n1 = len(nums1)
        n2 = len(nums2)
        # always apply binary search on smaller size array
        # because it require less Time Complexity
        if n1 > n2:
            return self.findMedianSortedArrays(nums2, nums1)
        n = n1 + n2
        total_left = (n + 1) // 2  # Total elements on left side of partition(symmetry)

        # binary search procedure on small size array
        low = 0  # take 0 elements from small array
        high = n1  # maximum case you can take all elements from small array
        while low <= high:
            # find middle point in 1st array
            mid1 = (low + high) // 2

            # logically, total mid2=total elements on left-elements taken from array 1
            mid2 = total_left - mid1
            l1, l2, r1, r2 = float("-inf"), float("-inf"), float("inf"), float("inf")

            # handling edge cases
            if mid1 < n1:
                r1 = nums1[mid1]
            if mid2 < n2:
                r2 = nums2[mid2]
            if mid1 - 1 >= 0:
                l1 = nums1[mid1 - 1]
            if mid2 - 1 >= 0:
                l2 = nums2[mid2 - 1]

            # possibility of getting correct symmetry
            if l1 <= r2 and l2 <= r1:
                # check for odd number of elements
                if n % 2 == 1:
                    return max(l1, l2)
                # check for even number of elements
                else:
                    return (float(max(l1, l2)) + float(min(r1, r2))) / 2.0
            # reduce end
            if l1 > r2:
                high = mid1 - 1
            else:
                low = mid1 + 1
        return 0
