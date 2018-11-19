"""
0.1 < 1.1 < 1.2 < 13.37
0.1 = 0.01.0.0
"""


class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        if version1.find(".") >= 0:
            subVersions1 = [int(v) for v in version1.split(".")]
        else:
            subVersions1 = [int(version1), 0]

        if version2.find(".") >= 0:
            subVersions2 = [int(v) for v in version2.split(".")]
        else:
            subVersions2 = [int(version2), 0]

        len1, len2 = len(subVersions1), len(subVersions2)
        print subVersions1
        print subVersions2
        i = 0
        while i < len1 and i < len2:
            if subVersions1[i] < subVersions2[i]:
                return -1
            elif subVersions1[i] > subVersions2[i]:
                return 1
            else:
                i += 1
        if i < len1 and sum(subVersions1[i:]) > 0:
            return 1
        elif i < len2 and sum(subVersions2[i:]) > 0:
            return -1
        else:
            return cmp(subVersions1[i - 1], subVersions2[i - 1])
