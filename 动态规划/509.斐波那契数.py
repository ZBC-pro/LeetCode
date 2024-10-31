# 古典斐波那契
class Solution:
    # -> int：这是返回类型注解，表明 fib 方法将返回一个整数值。
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 1
        result = self.fib(n - 1) + self.fib(n - 2)

        return  result

# 动态规划思想通过记忆化来优化fib函数的递归运算
# 避免重复计算提高效率
class Solution_pro:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n

        # 初始化前两个斐波那契数
        # 此时不再是通过递归的方式去计算斐波那契额数，而是通过数组的方式去填补

        # 初始化数组大小， 如果是计算fib(5)则是f(4) + f(3)，0，1，2，3，4，5-> 数组长度为6
        # 所以初始化后的数组就为[0, 1, 0, 0, 0, 0]
        dp = [0] * (n + 1)
        dp[1] = 1

        # 从 2 开始遍历，填充数组
        # 直接计算并存入数组避免重复生成子任务
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]

if __name__ == '__main__':
    s = Solution()
    s_p = Solution_pro()
    n = int(input("请输入要求的fib数n:"))
    # print(s.fib(n))
    print(s_p.fib(n))
