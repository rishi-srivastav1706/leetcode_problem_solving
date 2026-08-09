class Solution:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:
        left, right = 0, len(nums) - 1
        while left < right:
            if nums[left] % 2 > nums[right] % 2:
                # Swap if left is odd and right is even
                nums[left], nums[right] = nums[right], nums[left]
                
            if nums[left] % 2 == 0: left += 1
            if nums[right] % 2 != 0: right -= 1
            
        return nums
