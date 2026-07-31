class Solution(object):
    def minimumPushes(self,word):
    
        char_counts = {}
        for char in word:
            if char in char_counts:
                char_counts[char] += 1
            else:
                char_counts[char] = 1
                
        
        frequencies = sorted(char_counts.values(), reverse=True)
        
        total_pushes = 0
        for index, freq in enumerate(frequencies):
            presses_needed = (index // 8) + 1
            total_pushes += freq * presses_needed
            
        return total_pushes

