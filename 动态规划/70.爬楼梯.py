'''
因为只能走1或者2步，所以最后到达台阶时，只能是1步或者两步，从开始作为例子：
如果有两级台阶，则有两种走法：1 + 1 和 2
如果有三级台阶，则有1 +1 + 1，2 + 1 和 1 + 2 等同于 两级台阶的结果 + 1，因为走两级台阶的方法只有两种，从两级台阶走到三级台阶只需要加一步，所以无论怎样就多一种走法
如果有四级台阶，则有1 + 1 + 1 + 1， 1 + 1 + 2， 1 + 2 + 1， 2 + 1 + 1， 2 + 2 有五种，因为三级台阶有三种，走向四级台阶的方法也就两种，所以直接 3 + 2 = 5

例如n=4时：
我们只需要考虑从 n-1（第 3 级）和 n-2（第 2 级）到达第 n 级（第 4 级）的情况，因为从 n-1 级到 n 级可以爬 1 级，从 n-2 级到 n 级可以爬 2 级。这两种情况就是到达第 n 级的唯一方法。
从第 3 级台阶爬 1 级到达第 4 级的方法有 f(3) 种。
从第 2 级台阶爬 2 级到达第 4 级的方法有 f(2) 种。
所以，到达第 4 级的所有方法就是 f(3) 的所有方法数 + f(2) 的所有方法数。
最终的递推公式为f(n) = f(n-1) + f(n-2)




    代码在每次调用时都会递归地计算 n-1 和 n-2 的结果。由于没有缓存结果，这些递归调用会重复计算相同的子问题。例如：
	计算 climbStairs(5) 需要递归调用 climbStairs(4) 和 climbStairs(3)。
	计算 climbStairs(4) 又会递归调用 climbStairs(3) 和 climbStairs(2)，导致 climbStairs(3) 被重复计算。这样会导致指数级的调用次数，非常低效。
'''
# Time O(n^2), Space O(1)
# class Solution(object):
#     def climbStairs(self, n):
#         if n == 1:
#             return 1
#         if n == 2:
#             return 2
#         m = self.climbStairs(n - 1) + self.climbStairs(n - 2)
#
#         return m

# 动态规划：
# 与深度递归不同的是，直接计算出每一步的值，最后相加，而深度递归是到最后一步后递归的返回每一个子问题
# 例如：climbStairs(5)
# = climbStairs(4) + climbStairs(3)
# = (climbStairs(3) + climbStairs(2)) + (climbStairs(2) + climbStairs(1))
# 当到44时，直接多到爆炸
# 动态规划则是从前向后推导，计算出每一步的前两个值，最后累加即可
# Time O(n), Space O(1)
class Solution(object):
    def climbStairs(self, n):
        if n == 1:
            return 1
        if n == 2:
            return 2
        # 用两个变量保存前两级台阶的方法数
        prev, curr = 1, 2
        for i in range(3, n+1):
            prev, curr = curr, prev + curr  # 更新前两步

        return  curr

if __name__ == "__main__":
    n = int(input("请输入楼梯阶数n："))
    s = Solution()
    result = s.climbStairs(n)
    print(f"到达{n}级台阶的方法数为：{result}")

'''
通过一个具体的例子来演示这个代码的执行过程。假设我们要计算 n = 5 时到达顶层的方法数。根据代码的逻辑，我们使用动态规划方法迭代计算到达第 5 级台阶的所有方法数。

示例：n = 5

我们在一开始定义了 prev 和 curr 来保存前两级台阶的方法数：

	•	prev 表示到达第 n-2 级台阶的方法数
	•	curr 表示到达第 n-1 级台阶的方法数

初始化时：

	•	prev = 1（即 f(1) = 1，到达第 1 级台阶只有一种方法）
	•	curr = 2（即 f(2) = 2，到达第 2 级台阶有两种方法：1 + 1 和 2）

代码的目标是通过迭代更新 prev 和 curr，逐步计算直到第 5 级台阶。

计算过程

	1.	初始状态（n = 1 和 n = 2）：
	•	prev = 1
	•	curr = 2
	2.	第 3 级台阶：
	•	prev, curr = curr, prev + curr
	•	新的 prev = 2（旧的 curr 值）
	•	新的 curr = 1 + 2 = 3（表示到达第 3 级的方法数）
	•	当前结果：f(3) = 3，三种方法：1 + 1 + 1、1 + 2、2 + 1
	3.	第 4 级台阶：
	•	prev, curr = curr, prev + curr
	•	新的 prev = 3（旧的 curr 值）
	•	新的 curr = 2 + 3 = 5（表示到达第 4 级的方法数）
	•	当前结果：f(4) = 5，五种方法：1 + 1 + 1 + 1、1 + 1 + 2、1 + 2 + 1、2 + 1 + 1、2 + 2
	4.	第 5 级台阶：
	•	prev, curr = curr, prev + curr
	•	新的 prev = 5（旧的 curr 值）
	•	新的 curr = 3 + 5 = 8（表示到达第 5 级的方法数）
	•	最终结果：f(5) = 8，八种方法：1 + 1 + 1 + 1 + 1、1 + 1 + 1 + 2、1 + 1 + 2 + 1、1 + 2 + 1 + 1、2 + 1 + 1 + 1、1 + 2 + 2、2 + 1 + 2、2 + 2 + 1

最终结果

当 n = 5 时，到达第 5 级台阶的方法数为 8。

'''