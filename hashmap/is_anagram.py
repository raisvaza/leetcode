class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        occurrence_s = [0] * 200
        occurrence_t = [0] * 200

        for i in range(len(s)):
            occurrence_s[ord(s[i])] += 1
            occurrence_t[ord(t[i])] += 1
        
        return occurrence_s == occurrence_t