class Solution:
    def sortPeople(self, names, heights):
       
        paired = zip(heights, names)
        sorted_paired = sorted(paired, reverse=True)
        
       
        sorted_names = [name for height, name in sorted_paired]
        
       
        for name in sorted_names:
            print(name)
            
        return sorted_names
