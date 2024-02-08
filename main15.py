"""
1584. Min Cost to Connect All Points
"""


class Solution(object):
    def minCostConnectPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        cons = []
        costs = []
        for i, p in enumerate(points):
            points2 = points.copy()
            points2.remove(p)
            min = 1000000
            con = []
            for j, p2 in enumerate(points2):
                j2 = j if j < i else j + 1
                curr = abs(p[0]-p2[0]) + abs(p[1]-p2[1])
                if curr < min and sorted([i, j2]) not in cons:
                    min = curr
                    con = sorted([i, j2])

            costs.append(min)
            cons.append(con)


        return cons, costs


if __name__ == '__main__':
    sol = Solution().minCostConnectPoints([[0,0],[2,2],[3,10],[5,2],[7,0]])
    print(sol)
