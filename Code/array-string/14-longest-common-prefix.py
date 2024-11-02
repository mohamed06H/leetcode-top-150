class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        # Iterrate till no common letter is found
        position = 0
        is_common_at_position = True
        prefix = ""
        while is_common_at_position is True:
            current_letter = strs[0][position]
            # Verrify the letter at current position is the same for all strings
            for word in strs:
                if word[position] != current_letter:
                    is_common_at_position = False
            if is_common_at_position is True:
                prefix = prefix+current_letter
                position += 1
        return prefix
