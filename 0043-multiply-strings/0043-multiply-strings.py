class Solution(object):
    def multiply(self, num1, num2):       
        # Handle the zero edge case
        if num1 == "0" or num2 == "0":
            return "0"
            
        # Check for negative signs
        is_negative = False
        if num1[0] == '-':
            is_negative = not is_negative
            num1 = num1[1:]
        if num2[0] == '-':
            is_negative = not is_negative
            num2 = num2[1:]

        # Result array can at most have a length of len(num1) + len(num2)
        result = [0] * (len(num1) + len(num2))
        
        # Loop from right to left
        for i in range(len(num1) - 1, -1, -1):
            for j in range(len(num2) - 1, -1, -1):
                # Step 1: Convert characters to integers manually using ASCII
                digit1 = ord(num1[i]) - ord('0')
                digit2 = ord(num2[j]) - ord('0')
                
                # Step 2: Multiply and add to the current position
                product = digit1 * digit2
                p1 = i + j      # Carry position
                p2 = i + j + 1  # Current position
                
                total = product + result[p2]
                
                # Step 3: Update positions with the remainder and carry
                result[p2] = total % 10
                result[p1] += total // 10
                
        # Step 4: Convert the result array back to a string manually
        output_chars = []
        # Skip any leading zeros in the result array
        seen_first_digit = False
        
        for digit in result:
            if digit == 0 and not seen_first_digit:
                continue
            seen_first_digit = True
            # Convert digit to character using ASCII
            output_chars.append(chr(digit + ord('0')))
            
        final_str = "".join(output_chars)
        
        return "-" + final_str if is_negative else final_str
