class Solution(object):
    def dfs(self, left , right, p1, p2, turn, nums):
        if left> right:
            return p1>=p2
        if turn:
            return self.dfs(left+1, right, p1+nums[left], p2, False, nums) or  self.dfs(left, right-1, p1+nums[right], p2, False, nums)
        else:
            return self.dfs(left+1, right, p1, p2+nums[left], True, nums) and self.dfs(left, right-1, p1, p2+nums[right], True, nums)
    def predictTheWinner(self, nums):
        return self.dfs(0, len(nums)-1,0,0,True, nums)
        
        