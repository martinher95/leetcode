"""
11. Container With Most Water
"""


class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max = 0
        for i in range(len(height)):
            h = height[i]
            rest = height[i:]
            for j in range(len(rest)):
                r = rest[j]
                area = min(h, r)*j
                if area > max:
                    # print([[h,r], [j,i]])
                    max = area
        return max


if __name__ == '__main__':
    sol = Solution().maxArea([1,8,6,2,5,4,8,3,7])
    print(sol)