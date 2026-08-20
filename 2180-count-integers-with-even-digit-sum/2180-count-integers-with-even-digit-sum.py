class Solution:
    def countEven(self, num: int) -> int:
        count = 0
        
        for i in range(1,num+1):
            sum =0
            temp = i
            while temp>0:
                rem = temp%10
                sum= sum+rem
                temp=temp//10
            if sum%2==0:
                count+=1
                
        return count
                

