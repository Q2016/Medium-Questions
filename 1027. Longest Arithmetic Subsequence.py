in the comments of
https://leetcode.com/problems/longest-arithmetic-subsequence/discuss/274584/Same-as-LIS-problem-python-solution
  
similar to LIS problem  


    def longestArithSeqLength(self, A):
        d = [collections.defaultdict(int) for _ in A]
        res = 1
        for i in range(0,len(A)):
            for j in range(i):
                v = A[i]-A[j]
                d[i][v]=max(d[j][v]+1,d[i][v])
                res = max(d[i][v],res)
        return res+1