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
        total = 0
        ip = 0
        while ip < len(points) and ip not in cons and len(points) > 1:
            p = points[ip]
            points2 = points.copy()
            points2.pop(ip)
            min = 10000000
            con = 0
            for ip2, p2 in enumerate(points2):
                ip2 = ip2 if ip2 < ip else ip2 + 1
                curr = abs(p[0] - p2[0]) + abs(p[1] - p2[1])
                if curr < min:
                    min = curr
                    con = ip2
            cons.append(ip)
            cons.append(con)
            total += min
            for j in range(len(points)):
                if j not in set(cons):
                    ip = j
                    break
        return total, cons


if __name__ == '__main__':
    sol = Solution().minCostConnectPoints([[2,-3],[-17,-8],[13,8],[-17,-15]])
    print(sol)
