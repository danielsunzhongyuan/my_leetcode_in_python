# -*- encoding=utf-8 -*-
# !/usr/local/bin/python


class Solution(object):
    a = [1 << i for i in range(30)]
    b = [i % 2 for i in range(30)]

    def kthGrammar(self, N, K):
        """
        :param N: int 
        :param K: int
        :return: int
        """
        import bisect
        if K == 1:
            return 0
        if K in self.a:
            index = self.a.index(K)
            return self.b[index]
        x = bisect.bisect_left(self.a, K)
        return 1 ^ self.kthGrammar(N, K - self.a[x - 1])


def main():
    s = Solution()
    assert s.kthGrammar(1, 1) == 0
    assert s.kthGrammar(2, 1) == 0
    assert s.kthGrammar(2, 2) == 1
    assert s.kthGrammar(4, 5) == 1


if __name__ == "__main__":
    main()
