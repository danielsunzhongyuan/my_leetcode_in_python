class Solution(object):
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 1:
            return 0
        digits = self.getAllDigits(n)
        result = 0
        if digits[0] == 1:
            result += self.convertToNumber(digits[1::]) + 1
        else:
            result += 10 ** (len(digits) - 1)
        for i, digit in enumerate(digits):
            if i == 0:
                continue
            if digit > 1:
                result += self.convertToNumber(digits[0:i] + [9] * len(digits[i+1::])) + 1
            elif digit == 1:
                result += self.convertToNumber(digits[0:i] + digits[i+1::]) + 1
            else:
                result += self.convertToNumber(self.getAllDigits(self.convertToNumber(digits[0:i]) - 1) + [9] * len(digits[i+1::])) + 1
        return result

    def convertToNumber(self, digits):
        length = len(digits)
        result = 0
        for i, n in enumerate(digits):
            result += n * (10 ** (length - 1 -i))
        return result

    def getAllDigits(self, n):
        result = []
        while n:
            result.insert(0, n % 10)
            n /= 10
        return result


def main():
    a = Solution()

    print a.countDigitOne(392)
    print a.countDigitOne(1392)
    print a.countDigitOne(111)
    print a.countDigitOne(102)
    print a.countDigitOne(8192)

if __name__ == "__main__":
    main()
