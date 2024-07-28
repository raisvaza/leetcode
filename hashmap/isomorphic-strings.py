class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool

        Time complexity: O(n)
        Space complexity: O(1)
        """
        
        length = len(s)
        if length != len(t):
            return False

        indexS = [-1] * 200
        indexT = [-1] * 200

        for i in range(length):
            if indexS[ord(s[i])] != indexT[ord(t[i])]:
                return False

            indexS[ord(s[i])] = i
            indexT[ord(t[i])] = i
        return True