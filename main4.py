"""
118. Pascal's Triangle
"""


class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        triangle = [[1]]
        for row in range(1, numRows):  # lines
            line = [1]
            if triangle:
                for n in range(0, row - 1):
                    line.append(triangle[row - 1][n] + triangle[row - 1][n + 1])
                line.append(1)
                triangle.append(line)
        return triangle