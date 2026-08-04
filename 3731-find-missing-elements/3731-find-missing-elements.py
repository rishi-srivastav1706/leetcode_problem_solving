class Solution(object):
    def findMissingElements(self, nums):
        nums.sort()
        n= len(nums)
        min_val = min(nums)
        max_val = max(nums)
        missing = []
        for num in range(min_val, max_val+1):
            
            if num not in nums:
                missing.append(num)
        return missing
        