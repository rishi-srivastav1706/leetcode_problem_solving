class Solution(object):
    def maximumProduct(self, nums):
        # Track the 3 largest numbers (initialized to lowest possible value)
        max1 = max2 = max3 = float('-inf')
        
        # Track the 2 smallest numbers (initialized to highest possible value)
        min1 = min2 = float('inf')
        
        for n in nums:
            # Update the 3 largest values
            if n > max1:
                max1, max2, max3 = n, max1, max2
            elif n > max2:
                max2, max3 = n, max2
            elif n > max3:
                max3 = n
                
            # Update the 2 smallest values
            if n < min1:
                min1, min2 = n, min1
            elif n < min2:
                min2 = n
        
        # The maximum product is either:
        # 1. Three largest positive numbers
        # 2. Two smallest negative numbers multiplied by the largest positive number
        return max(max1 * max2 * max3, min1 * min2 * max1)
