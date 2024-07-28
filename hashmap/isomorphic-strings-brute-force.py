class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        hash_map = {}

        for i in range(len(s)):
            if s[i] not in hash_map:
                if t[i] not in hash_map.values():
                    hash_map[s[i]] = t[i]
                else:
                    return False
            else:
                if hash_map[s[i]] == t[i]:
                    pass
                else:
                    return False
        return True