class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Purpose: find # ways to go from top-left to bottom-right
        # Formula: res[i][j] += res[all i][j - 1]

        # build
        dp = [0] * n
        dp[0] = 1

        # find
        for i in range(m):
            for j in range(n):
                if j >= 1:
                    dp[j] += dp[j - 1]
                    print(dp)

                    # return
        return dp[-1]


sol = Solution().uniquePaths(100, 3)
print(sol)