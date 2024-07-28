class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        a_dict = defaultdict(list)

        for i in range(len(strs)):
            a_dict[''.join(sorted(strs[i]))].append(strs[i])
        return a_dict.values()
