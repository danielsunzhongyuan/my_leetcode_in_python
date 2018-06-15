import itertools
import time
import random
import string
#import profile
from line_profiler import LineProfiler

exec_times = 5

# this is slow
# Since the length of S/T is less than 200, it is OK.
def backspaceCompare(S, T):
    return final(S) == final(T)
    
@LineProfiler
def final(x):
    ret = ""
    for i in x:
        if i == "#":
            ret = ret[:-1]
        else:
            ret += i
    return ret

# when the length of S is 800,000 the first method runs about 5 seconds
# however the following method runs only 1 second.
def backspaceCompare2(S, T):
    i, j = len(S) - 1, len(T) - 1
    count = 0
    while i >= 0 or j >= 0:
        count = 0
        while i >= 0 and (S[i] == "#" or count > 0):
            count += 1 if S[i] == "#" else -1
            i -= 1
        count = 0
        while j >= 0 and (T[j] == "#" or count > 0):
            count += 1 if T[j] == "#" else -1
            j -= 1
        if i < 0 or j < 0 or S[i] != T[j]:
            return i == -1 and j == -1
        i -= 1
        j -= 1
    return True


def _timeit_analyze_(func):
    from timeit import Timer
    t1 = Timer("%s()" % func.__name__, "from __main__ import %s" % func.__name__)
    print "{:<20}{:10.6} s".format(func.__name__ + ":", t1.timeit(exec_times))


length = 80
S = ""
s = "abcdefghijklmnopqrstuvwxyz#"
length_s = len(s)
for i in range(length):
    S += s[int(random.random()*length_s)]

def a():
    backspaceCompare(S, S)

def b():
    backspaceCompare2(S, S)

def main():
    _timeit_analyze_(a)
    _timeit_analyze_(b)

    
if __name__ == "__main__":
    #profile.run("main()")
    #profile.run("a()")
    main()

