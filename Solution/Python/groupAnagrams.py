class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        groups = dict()
        for str in strs:
            group = ''.join(sorted(str))
            if group in groups.keys():
                groups[group].append(str)
            else:
                groups[group] = list()
                groups[group].append(str)

        return list(groups.values())
