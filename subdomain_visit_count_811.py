class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        dic = {}
        for cp in cpdomains:
            (count, domain) = cp.split(" ")
            subdomains = domain.split(".")
            for i in range(len(subdomains)):
                dic[".".join(subdomains[i:])] = int(count) + dic.get(".".join(subdomains[i:]), 0)
        return [str(v)+" "+str(k) for k, v in dic.items()]


if __name__ == "__main__":
    s = Solution()
    print s.subdomainVisits(["9001 discuss.leetcode.com"])
