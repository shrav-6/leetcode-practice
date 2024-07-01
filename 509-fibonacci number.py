class Solution:
    def fib(self, n: int) -> int:
        a = 0
        b = 1
        temp = 0
        if n == 0:
            return a
        elif n == 1:
            return b
        else:
            i = 1
            while(i != n):
                temp = a + b
                a = b
                b = temp
                i = i + 1
            return temp
