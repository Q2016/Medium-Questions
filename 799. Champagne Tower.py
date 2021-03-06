Question:
We stack glasses in a pyramid, where the first row has 1 glass, the second row has 2 glasses, and so on until the 100th row.  Each glass holds 
one cup of champagne. Then, some champagne is poured into the first glass at the top.  When the topmost glass is full, any excess liquid poured 
will fall equally to the glass immediately to the left and right of it.  When those glasses become full, any excess champagne will fall equally 
to the left and right of those glasses, and so on. 
Now after pouring some non-negative integer cups of champagne, return how full the jth glass in the ith row is?

Example 1:
Input: poured = 2, query_row = 1, query_glass = 1
Output: 0.50000
Explanation: We poured 2 cups of champange to the top glass of the tower (which is indexed as (0, 0)). There is one cup of excess liquid. 
The glass indexed as (1, 0) and the glass indexed as (1, 1) will share the excess liquid equally, and each will get half cup of champange.    







Solution: Simulation [Accepted]
Instead of keeping track of how much champagne should end up in a glass, keep 
track of the total amount of champagne that flows through a glass. For example, 
if poured = 10 cups are poured at the top, then the total flow-through of the top 
glass is 10; the total flow-through of each glass in the second row is 4.5, and so on.

In general, if a glass has flow-through X, then Q = (X - 1.0) / 2.0 quantity of champagne 
will equally flow left and right. We can simulate the entire pour for 100 rows of glasses. 
A glass at (r, c) will have excess champagne flow towards (r+1, c) and (r+1, c+1).


class Solution(object):
    def champagneTower(self, poured, query_row, query_glass):
        A = [[0] * k for k in xrange(1, 102)]
        A[0][0] = poured
        for r in xrange(query_row + 1):
            for c in xrange(r+1):
                q = (A[r][c] - 1.0) / 2.0
                if q > 0:
                    A[r+1][c] += q
                    A[r+1][c+1] += q

        return min(1, A[query_row][query_glass])
