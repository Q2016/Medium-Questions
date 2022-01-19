Complexity
Time O(N) for one pass
Space O(2) for two options


    def movesToMakeZigzag(self, A):
        A = [float('inf')] + A + [float('inf')]
        res = [0, 0]
        for i in xrange(1, len(A) - 1):
            res[i % 2] += max(0, A[i] - min(A[i - 1], A[i + 1]) + 1)
        return min(res)
