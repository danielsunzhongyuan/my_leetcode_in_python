# @question: 401. Binary Watch
# @author: Zhongyuan Sun
# Solution One: split num into num_of_hour and num_of_minute like (0, num), (1, num-1), (2, num-2) ...
#               then generate all the possibilities of hour and minute
#               then return the combination of hour and minute
# Solution Two: put hour digit and minute digit together, generate all the permutations
#               then read the number as hour:minute
# Solution Three: based on solution two, instead of using itertools.product(("0","1")...) to generate the permutations,
#               use numbers [0, 2**10) to represent the permutation
# Solution Four: get all possible time and output them if count of digit 1 is "num"
import itertools


class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        # Solution One
        # res = []
        # for i in range(min(4,num+1)):
        #     res += [":".join(x) for x in itertools.product(list(map(lambda x:str(x),filter(lambda x3: x3<12, map(lambda x1:int("".join(x1), 2), filter(lambda x2:x2.count("1") == i,itertools.product(("0","1"),("0","1"),("0","1"),("0","1"))))))),list(map(lambda x:"%02d"%x,filter(lambda x3: x3<60, map(lambda x1:int("".join(x1), 2), filter(lambda x2:x2.count("1") == num-i,itertools.product(("0","1"),("0","1"),("0","1"),("0","1"),("0","1"),("0","1"))))))))]
        # return res
        
        # Solution One: one line version
        # return list(y for x in [[":".join(x) for x in itertools.product(list(map(lambda x:str(x),filter(lambda x3: x3<12, map(lambda x1:int("".join(x1), 2), filter(lambda x2:x2.count("1") == i,itertools.product(("0","1"),("0","1"),("0","1"),("0","1"))))))),list(map(lambda x:"%02d"%x,filter(lambda x3: x3<60, map(lambda x1:int("".join(x1), 2), filter(lambda x2:x2.count("1") == num-i,itertools.product(("0","1"),("0","1"),("0","1"),("0","1"),("0","1"),("0","1"))))))))] for i in range(min(4,num+1))] for y in x)
        
        # Solution One: one line version, improved
        # return list(y for x in [[":".join(x) for x in itertools.product(list(map(lambda x:str(x),filter(lambda x3: x3<12, map(lambda x1:int("".join(x1), 2), filter(lambda x2:x2.count("1") == i,itertools.product(*[('0','1')]*4)))))),list(map(lambda x:"%02d"%x,filter(lambda x3: x3<60, map(lambda x1:int("".join(x1), 2), filter(lambda x2:x2.count("1") == num-i,itertools.product(*[('0','1')]*6)))))))] for i in range(min(4,num+1))] for y in x)
        # Solution One: one line version, improved again with product(...,repeat=X)
        # return list(y for x in [[":".join(x) for x in itertools.product(list(map(lambda x:str(x),filter(lambda x3: x3<12, map(lambda x1:int("".join(x1), 2), filter(lambda x2:x2.count("1") == i,itertools.product("01",repeat=4)))))),list(map(lambda x:"%02d"%x,filter(lambda x3: x3<60, map(lambda x1:int("".join(x1), 2), filter(lambda x2:x2.count("1") == num-i,itertools.product("01", repeat=6)))))))] for i in range(min(4,num+1))] for y in x)
        
        # Solution Two: one line version
        # return ["%d:%02d"%(x[0],x[1]) for x in [(int("".join(x[:4]), 2), int("".join(x[4:]), 2)) for x in filter(lambda x:x.count("1")==num, itertools.product(("0","1"),("0","1"),("0","1"),("0","1"),("0","1"),("0","1"),("0","1"),("0","1"),("0","1"),("0","1")))] if x[0]<12 and x[1]<60]

        # Solution Two: one line version, improved
        # return ["%d:%02d"%(x[0],x[1]) for x in [(int("".join(x[:4]), 2), int("".join(x[4:]), 2)) for x in filter(lambda x:x.count("1")==num, itertools.product(*[('0','1')]*10))] if x[0]<12 and x[1]<60]
        
        # Solution Two: one line version, improved again with product(...,repeat=X)
        # return ["%d:%02d"%(x[0],x[1]) for x in [(int("".join(x[:4]), 2), int("".join(x[4:]), 2)) for x in filter(lambda x:x.count("1")==num, itertools.product("01", repeat=10))] if x[0]<12 and x[1]<60]
        
        # Solution Three
        # return ["%d:%02d"%(x[0],x[1]) for x in [(int("".join(x[:4]), 2), int("".join(x[4:]), 2)) for x in filter(lambda x:x.count("1")==num, ["%010d"%int(bin(x)[2:],10) for x in range(2**10)])] if x[0]<12 and x[1]<60]
        
        # Solution Four
        # return ["%d:%02d" % (h, m) for h in range(12) for m in range(60) if (bin(h) + bin(m)).count("1") == num]
        
        # Solution Five: from Han Lee
        return ["%d:%02d" % divmod(x, 100) for x in map(sum, itertools.combinations((1,2,4,8,16,32,100,200,400,800), num)) if x<1200 and x%100 < 60] if num else ["0:00"]

