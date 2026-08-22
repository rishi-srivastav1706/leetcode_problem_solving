class Solution:
    def checkDivisibility(self, n: int) -> bool:
        original = n
        digit_sum = 0
        digit_product = 1
        
        # Extract digits one by one
        while n > 0:
            digit = n % 10
            digit_sum += digit
            digit_product *= digit
            n //= 10
            
     
        combined_sum = digit_sum + digit_product
        
      
        return original % combined_sum == 0
