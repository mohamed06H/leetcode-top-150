class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Define the symbol value mapping in a dict
        symbol_value_dict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        # Get each literal's corrsponding integer value in a list
        mapped_s = []
        for i in range(len(s)):
            mapped_s.append(symbol_value_dict[s[i]])

            
        # Count the final integer doing sum or substraction 
        count = 0
        i = 0
        while i < len(mapped_s)-1:
            if mapped_s[i] >= mapped_s[i+1]:
                count += mapped_s[i]
            else:
                count -= mapped_s[i]
            i += 1
        count += mapped_s[i]
        return count
        
