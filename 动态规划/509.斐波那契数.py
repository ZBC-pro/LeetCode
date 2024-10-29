class Solution:
    # -> int：这是返回类型注解，表明 fib 方法将返回一个整数值。
    def fib(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 1
        result = self.fib(n - 1) + self.fib(n - 2)

        return  result

if __name__ == '__main__':
    s = Solution()
    n = int(input("请输入要求的fib数n:"))
    print(s.fib(n))
