"""
164. Maximum Gap
"""


class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        maxdiff = 0
        for i in range(0, len(nums)-1):
            curr = nums[i] - nums[i+1]
            print(curr)
            maxdiff = max(abs(curr), maxdiff)
        return maxdiff


if __name__ == '__main__':
    sol = Solution().maximumGap([10])
    print(sol)
