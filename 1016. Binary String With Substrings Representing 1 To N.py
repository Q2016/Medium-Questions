Intuition:
The construction of S is a NP problem,
it's time consuming to construct a short S.
I notice S.length <= 1000, which is too small to make a big N.

This intuition lead me to the following 1-line python solution,
which can be implemented very fast.


Explanation:
Check if S contains binary format of N,
If so, continue to check N - 1.


Time Complexity
Have a look at the number 1001 ~ 2000 and their values in binary.

1001 0b1111101001
1002 0b1111101010
1003 0b1111101011
...
1997 0b11111001101
1998 0b11111001110
1999 0b11111001111
2000 0b11111010000

The number 1001 ~ 2000 have 1000 different continuous 10 digits.
The string of length S has at most S - 9 different continuous 10 digits.
So S <= 1000, the achievable N <= 2000.
So S * 2 is a upper bound for achievable N.
If N > S * 2, we can return false directly in O(1)

Note that it's the same to prove with the numbers 512 ~ 1511, or even smaller range.

N/2 times check, O(S) to check a number in string S.
The overall time complexity has upper bound O(S^2).


Python:

    def queryString(self, S, N):
        return all(bin(i)[2:] in S for i in xrange(N, N / 2, -1))

Solution2
Continue to improve the above solution to O(S)

Python:

    def queryString(self, S, N):
        if N > len(S) * 2: return False
        L = len(bin(N)) - 2
        seen = {S[i:i + L] for i in xrange(len(S))} | {S[i:i + L - 1] for i in xrange(len(S))}
        return all(bin(i)[2:] in seen for i in xrange(N, N / 2, -1))
seen can be calculated by two passes of rolling hash.
