
r: Zhongyuan Sun
class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        if denominator == 0:
            return "NaN"
        if numerator == 0:
            return "0"
        if numerator < 0 and denominator < 0:
            return self.fractionToDecimal(-numerator, -denominator)
        elif (numerator < 0 and denominator > 0) or (numerator > 0 and denominator < 0):
            return "-" + self.fractionToDecimal(abs(numerator), abs(denominator))
        else:
            res = ""
            res += str(numerator/denominator)
            if numerator % denominator == 0:
                return res
            else:
                res += "."
                tmp = (numerator % denominator) * 10
                divisor, remainder = tmp/denominator, tmp%denominator
                divisor_remainder_pairs = [(divisor, remainder)]
                while remainder != 0:
                    divisor = (remainder*10) / denominator
                    remainder = (remainder*10) % denominator
                    if (divisor, remainder) in divisor_remainder_pairs:
                        break
                    else:
                        divisor_remainder_pairs.append((divisor, remainder))
                if remainder == 0:
                    res += "".join([str(x[0]) for x in divisor_remainder_pairs])
                else:
                    loop_begin = divisor_remainder_pairs.index((divisor, remainder))
                    res += "".join([str(x[0]) for x in divisor_remainder_pairs[:loop_begin]])
                    res += "(" + "".join([str(x[0]) for x in divisor_remainder_pairs[loop_begin:]]) + ")"
                return res
