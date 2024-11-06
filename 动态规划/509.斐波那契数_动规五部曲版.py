'''
1 1 2 3 5 8
1. 确定dp[i]含义：   第i个斐波那契数的值为dp[i]
2. 递推公式：    dp[i] = dp[i - 1] + dp[i - 2]
3. dp数组如何初始化：   题目中已经告诉了，dp[0] = 1, dp[1] = 1
4. 确定遍历顺序：  从前向后遍历  （有的需要从后向前，两层for循环要指定先后顺序）
5. 打印dp数组


'''


def fib(n):
    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]


# 对动态规划的压缩，缩小数组开销
def fib_zip(n):
    dp = [1, 1]     # 数组初始化为 1
    sum = 0
    for i in range(2, n + 1):
        sum = dp[0] + dp[1]
        dp[0] = dp[1]
        dp[1] = sum

    return sum


if __name__ == '__main__':
    f = fib(5)
    f1 = fib_zip(5)
    print(f)
    print(f1)