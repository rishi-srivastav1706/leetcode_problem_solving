class Solution(object):
    def maxActiveSectionsAfterTrade(self, s):
        ones = s.count('1')

        zero_blocks = []
        i = 0
        n = len(s)

        while i < n:
            if s[i] == '0':
                j = i
                while j < n and s[j] == '0':
                    j += 1
                zero_blocks.append(j - i)
                i = j
            else:
                i += 1

        gain = 0
        for i in range(len(zero_blocks) - 1):
            gain = max(gain, zero_blocks[i] + zero_blocks[i + 1])

        return ones + gain