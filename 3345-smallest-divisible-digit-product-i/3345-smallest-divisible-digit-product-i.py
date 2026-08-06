class Solution(object):
    def smallestNumber(self, n, t):
        res = n

        while True:
            pro = 1
            cur = res

            if cur == 0:
                pro = 0
            else:
                while cur > 0:
                    pro *= (cur % 10)
                    cur //= 10

            if pro % t == 0:
                return res

            res += 1