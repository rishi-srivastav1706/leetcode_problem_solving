class Solution(object):
    def findGCD(self, nums):
        n = len(nums)
        largest_ele = max(nums)
        smallest_ele = min(nums)
        while smallest_ele != 0:
            largest_ele, smallest_ele = smallest_ele, largest_ele % smallest_ele  # Formula swaps values with the remainder
        return largest_ele