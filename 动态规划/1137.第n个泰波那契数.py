'''
泰波那契序列 Tn 定义如下：

T0 = 0, T1 = 1, T2 = 1, 且在 n >= 0 的条件下 Tn+3 = Tn + Tn+1 + Tn+2

给你整数 n，请返回第 n 个泰波那契数 Tn 的值。

'''


class Solution:
    def tribonacci(self, n: int) -> int:
        dp = [0, 1, 1] + [0] * (n - 2)
        if n >= 3:
            for i in range(2, n + 1):
                dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]

        return dp[n]



if __name__ == "__main__":
    s = Solution()
    n = int(input("请输入要求的泰波那契数："))
    print(s.tribonacci(n))
