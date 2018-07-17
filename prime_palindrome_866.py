class Solution(object):
    def primePalindrome(self, N):
        """
        :type N: int
        :rtype: int
        """
        def is_palindrome(n):
            return str(n) == str(n)[::-1]
        
        def is_prime(n):
            import math
            tmp = int(math.sqrt(n)) + 1
            for i in range(2, tmp):
                if n % i == 0:
                    return False
            return True
        
        def next_palindrome(N):
            length = len(str(N))
            half_length = length / 2
            if length % 2 == 0:
                left = int(str(N)[:half_length])
                if left == 10**half_length - 1:
                    return 10**length + 1
                first_digit_of_left = int(str(left)[0])
                if first_digit_of_left in (2,4,6,8):
                    left = 10**(half_length-1) * (first_digit_of_left + 1)
                while int(str(left) + str(left)[::-1]) <= N:
                    left += 1
                return int(str(left) + str(left)[::-1])
            else:
                left_middle = int(str(N)[:half_length+1])
                if left_middle == 10**(half_length+1) - 1:
                    return 10**length + 1
                first_digit_of_left = int(str(left_middle)[0])
                if first_digit_of_left in (2,4,6,8):
                    left = 10**(half_length) * (first_digit_of_left + 1)
                while int(str(left_middle) + str(left_middle)[:half_length][::-1]) <= N:
                    left_middle += 1
                return int(str(left_middle) + str(left_middle)[:half_length][::-1])
                
        small_n_map = {
            1: 2,
            2: 2, 
            3: 3,
            4: 5,
            5: 5,
            6: 7,
            7: 7,
            8: 11,
            9: 11,
            10: 11,
            11: 11
        }
        if N < 1:
            return 0
        if 1 <= N <= 11:
            return small_n_map[N]
        if N % 2 == 0:
            return self.primePalindrome(N + 1)
        if is_prime(N) and is_palindrome(N):
            return N
        N = next_palindrome(N)
        while not is_prime(N):
            N = next_palindrome(N)
        return N

if __name__ == "__main__":
    s = Solution()
    print s.primePalindrome(13)
    print s.primePalindrome(9989900)
    print s.primePalindrome(31880255)

