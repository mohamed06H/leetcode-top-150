class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """ 
        # count length of last word
        count = 0
        i = len(s)
        last_word_started = False
        while i >= 0:
            i -= 1
            if s[i] != ' ':
                last_word_started = True
                count +=1
            elif last_word_started:
                break;
                
        return count
        
