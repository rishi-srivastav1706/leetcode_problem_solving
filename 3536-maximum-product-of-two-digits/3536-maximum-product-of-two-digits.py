class Solution(object):
    def maxProduct(self, n):
        prod = 1
        first = 0
        second = 0
        while n>0:
            x = n%10
            if x>first:
                second = first 
                first = x
            elif x >second:
                second = x
            n//=10
        return first*second


        