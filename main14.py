"""
45. Jump Game II
"""


class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        size = len(nums)
        jumps = 0
        i = 0
        while i < size-1:
            print(i)
            jumps += 1
            n = nums[i]
            window = nums[i+1:i+n+1]
            sum = 0
            maxj = 0
            aux = i
            print(window)
            if n + i < size - 1:
                for j, n2 in enumerate(window):
                    curr = n + n2 + j
                    i = aux
                    if curr > sum:
                        sum = curr
                        maxj = j + 1
                i += maxj
            else:
                break

        return jumps


if __name__ == '__main__':
    sol = Solution().jump([1,2,1,1,1])
    print(sol)
