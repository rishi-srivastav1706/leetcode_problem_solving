class Solution(object):
    def minimumPushes(self, word):
        n = len(word)
        res =0
        for num in range(n):
            res +=(num/8+1) 
        return res
        