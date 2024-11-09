'''
1. dp[i]数组的定义
dp[i] 怎么定义？ dp[i]数组即为所求
dp[i]：  到达第 i 个下标位置时时所需要的最小花费为dp[i]

2. 递推公式     求dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])
dp[i - 1]：  跳一步到dp[i] + 向上跳的花费cost[i - 1]       # 想要从第 i - 1 个台阶跳一步到第 i 个需要加上该台阶cost[i - 1]花费的代价
dp[i - 2]：  跳两步到dp[i] + 向上跳的花费cost[i - 2]       # 想要从第 i - 2 个台阶跳两步到第 i 个需要加上该台阶cost[i - 2]花费的代价
dp

3. 初始化
dp[2] = dp[0] + dp[1]
dp[3] = dp[1] + dp[2]
每一项至于其前两项有关，所以只需要初始化dp[0] 和 dp[1]即可
dp[0] = 0, dp[1] = 0    因为前两步不耗费代价，所以都为0

4. 遍历顺序
dp[2] 由 dp[0] 和 dp[1] 相加得来，dp[3] 由 dp[1] 和 dp[2] 相加得来，所以遍历顺序就是从前向后

5. 打印dp数组

'''

class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        n = len(cost)
        dp = [0] * (n + 1)
        for i in range(2, n + 1):
            dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])
            print(dp)

        return dp[n]


if __name__ == "__main__":
    s = Solution()
    cost = [100,1,10,2,3,15,1]
    print(s.minCostClimbingStairs(cost))