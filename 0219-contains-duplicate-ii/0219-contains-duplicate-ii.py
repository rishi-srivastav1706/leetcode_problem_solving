class Solution(object):
    def containsNearbyDuplicate(self,nums, k):
        window = set()
        
        for i, num in enumerate(nums):
            # 1. If duplicate is found in the current window
            if num in window:
                return True
                
            # 2. Add current number to window
            window.add(num)
            
            # 3. Shrink window from the left if it exceeds size k
            if len(window) > k:
                window.remove(nums[i - k])
                
        return False
