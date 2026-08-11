class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        n = len(nums)
        my_set =set(nums)
        for num in nums:
            my_set.add(num)
        res= nums[0]
        i = 1

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                res += nums[i]
            else:
                break

        while res in my_set:
            res+=1
        return res