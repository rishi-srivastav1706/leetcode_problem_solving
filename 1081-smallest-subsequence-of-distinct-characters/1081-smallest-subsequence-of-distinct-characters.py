class Solution(object):
    def smallestSubsequence(self, s):
        # Track the last occurrence index of each character
        last_occurrence = {char: i for i, char in enumerate(s)}
        
        stack = []
        visited = set()
        
        for i, char in enumerate(s):
            # Skip if the character is already in our result stack
            if char in visited:
                continue
                
            # Pop characters from stack if they are larger than current char
            # AND they appear again later in the string
            while stack and stack[-1] > char and last_occurrence[stack[-1]] > i:
                removed_char = stack.pop()
                visited.remove(removed_char)
                
            # Add the current character to stack and visited set
            stack.append(char)
            visited.add(char)
            
        return "".join(stack)
