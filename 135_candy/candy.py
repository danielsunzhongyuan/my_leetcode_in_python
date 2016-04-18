class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        result = 0
        length = len(ratings)
        candies = [1] * length
        for i in range(1, length):
            if ratings[i] > ratings[i - 1]:
                if candies[i] <= candies[i - 1]:
                    candies[i] = candies[i - 1] + 1
                else:
                    continue
            elif ratings[i] == ratings[i - 1]:
                if candies[i] < candies[i - 1]:
                    candies[i] = candies[i - 1]
            elif ratings[i] < ratings[i - 1]:
                if candies[i] < candies[i - 1]:
                    continue
                else:
                    j = i
                    while j > 0 and ratings[j] <= ratings[j - 1] and candies[j - 1] - candies[j] < 1:
                        candies[j - 1] += 1
                        j -= 1
            print candies
        return sum(candies)


class Solution2(object):
    def candy2(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        result = 0
        length = len(ratings)
        candies = [1] * length
        for i in range(1, length):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1
            #elif ratings[i] == ratings[i - 1]:
            #    candies[i] = max(candies[i], candies[i - 1])
            else:
                continue
        for i in range(length - 1, 0, -1):
            if ratings[i] < ratings[i - 1]:
                candies[i - 1] = max(candies[i - 1], candies[i] + 1)
            #elif ratings[i] == ratings[i - 1]:
            #    candies[i - 1] = max(candies[i - 1], candies[i])
            else:
                continue
        print candies
        return sum(candies)

    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        result = 0
        length = len(ratings)
        candies = [1] * length
        for i in range(length - 1, 0, -1):
            if ratings[i - 1] > ratings[i]:
                candies[i - 1] = candies[i] + 1
            #elif ratings[i] == ratings[i - 1]:
            #    candies[i - 1] = max(candies[i - 1], candies[i])
            else:
                continue
        for i in range(1, length):
            if ratings[i - 1] < ratings[i]:
                candies[i] = max(candies[i - 1] + 1, candies[i])
            #elif ratings[i] == ratings[i - 1]:
            #    candies[i] = max(candies[i], candies[i - 1])
            else:
                continue
        print candies
        return sum(candies)

def main():
    a = Solution2()
    #b1 = range(12000, 0, -1)
    #b2 = range(1, 12001)
    #b3 = [1, 2, 3, 4, 5, 6, 1, 2, 3, 4]
    #b4 = [1, 2, 3, 4, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    #b5 = [1, 2, 2, 1, 5, 5, 4, 3, 2, 1]
    b6 = [1, 1, 1, 2, 2, 3, 4, 10, 10, 10, 9, 8, 7, 6, 5, 4, 3, 3, 2, 1, 1]
    #print a.candy(b1)               # 72006000 = 12000 * 12001 / 2
    #print a.candy(b2)               # 72006000 = 12000 * 12001 / 2
    #print a.candy(b3)               # 31 = 1 + 2 + 3 + 4 + 5 + 6 + 1 + 2 + 3 + 4
    #print a.candy(b4)               # 65 = 1 + 2 + 3 + 4 + 10 + 9 + 8 + 7 + 6 + 5 + 4 + 3 + 2 + 1
    #print a.candy(b5)               # 26 = 1 + 2 + 2 + 1 + 5 + 5 + 4 + 3 + 2 + 1
    print a.candy(b6)





if __name__ == "__main__":
    main()
