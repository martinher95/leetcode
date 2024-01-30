"""
4. Median of Two Sorted Arrays
"""
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums = sorted(sorted(nums1) + sorted(nums2))
        if len(nums) % 2 == 0:
            n1 = nums[int((len(nums) - 1) / 2)]
            n2 = nums[int((len(nums)) / 2)]
            return (n1+n2)/2
        else:
            return nums[int((len(nums) - 1) / 2)]


if __name__ == '__main__':
    nums1 = [1, 2]
    nums2 = [3, 4]
    sol = Solution().findMedianSortedArrays(nums1, nums2)
    print(sol)
