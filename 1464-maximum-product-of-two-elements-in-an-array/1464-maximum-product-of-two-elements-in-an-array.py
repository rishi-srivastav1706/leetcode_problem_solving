class Solution(object):
    def maxProduct(self, nums):
        n = len(nums)
        a = 0
        b= 0
        for num in nums:
            oa = a 

            a = max(a,num)
            b = max(b, min(oa,num))
        
        return (a-1)*(b-1)