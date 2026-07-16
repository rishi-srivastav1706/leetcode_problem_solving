class Solution(object):
    def gcd(self, a, b):
        while b != 0:
            a, b = b, a % b
        return a

    def gcdSum(self, nums):
        n = len(nums)
        prefixGcd = []

        mx = nums[0]

        # Construct prefixGcd
        for i in range(n):
            if nums[i] > mx:
                mx = nums[i]
            prefixGcd.append(self.gcd(nums[i], mx))

        # Sort the array
        prefixGcd.sort()

        # Form pairs and compute sum
        left = 0
        right = n - 1
        ans = 0

        while left < right:
            ans += self.gcd(prefixGcd[left], prefixGcd[right])
            left += 1
            right -= 1

        return ans
        