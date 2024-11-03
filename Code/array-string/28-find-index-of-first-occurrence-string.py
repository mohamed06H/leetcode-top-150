# Easy solution
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        return haystack.find(needle)
# Second solution         
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        for i in range(0, len(haystack)-len(needle)):
            # Compare each substring of length: len(needle) to needle
            if haystack[i:len(needle)] == needle:
                return i
        return -1
