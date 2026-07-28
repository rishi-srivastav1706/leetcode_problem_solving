class Solution(object):
    def sumOddLengthSubarrays(self, arr):
         
        total_sum = 0
        n = len(arr)
        
        for i in range(n):
             
            left_choices = i + 1
            right_choices = n - i
            total_subarrays = left_choices * right_choices
            
             
            odd_frequency = (total_subarrays + 1) // 2
            
       
            total_sum += odd_frequency * arr[i]
            
        return total_sum
