"""
1. Two Sum
"""


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums = list(nums)
        find = []
        for num in nums:
            nums2 = nums.copy()
            nums2.remove(num)
            for num2 in nums2:
                if num + num2 == target:
                    if num in nums2:
                        find.append([nums.index(num), nums2.index(num)+1])
                    else:
                        find.append([nums.index(num), nums.index(num2)])
        return find[0]


if __name__ == '__main__':
    sol = Solution().twoSum([2,7,11,15], 9)
    print(sol)
