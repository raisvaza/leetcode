class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        s = s.split(' ')

        if len(s) != len(pattern):
            return False

        alphabet_last_occurrence_idx = [-1] * 256
        word_code_last_occurrence_idx = [-1] * 256

        word_to_word_code = {}

        for i in range(len(s)):
            if s[i] not in word_to_word_code:
                word_to_word_code[s[i]] = i
            else:
                pass

        for i in range(len(s)):
            if alphabet_last_occurrence_idx[ord(pattern[i])] != word_code_last_occurrence_idx[word_to_word_code[s[i]]]:
                return False
            alphabet_last_occurrence_idx[ord(pattern[i])] = i
            word_code_last_occurrence_idx[word_to_word_code[s[i]]] = i
        return True
