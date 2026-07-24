class Solution(object):
    def addDigits(self, num):
        # Keep looping until num becomes a single digit
        while num > 9:
            total_sum = 0
            while num > 0:
                rem = num % 10
                total_sum += rem
                num = num // 10
            # Update num with the new sum for the next round
            num = total_sum 
            
        return num
