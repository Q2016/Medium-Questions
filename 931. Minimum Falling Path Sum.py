Question:
Given an n x n array of integers matrix, return the minimum sum of any falling path through matrix. A falling path starts at any element 
in the first row and chooses the element in the next row that is either directly below or diagonally left/right. Specifically, 
the next element from position (row, col) will be (row + 1, col - 1), (row + 1, col), or (row + 1, col + 1).













Solution: DP
https://leetcode.com/problems/minimum-falling-path-sum/discuss/381898/Python-Not-shortest-but-easiest-to-understand-with-explanation

This problem will use DP, by taking the minimum value from itself plus one of the 3 values right above it



def minFallingPathSum(self, A: List[List[int]]) -> int:
    
    for i in range(1,len(A)):
        for j in range(len(A[0])):	
            #edge cases are first column and last column which only have two paths from above
            if j == 0:
                A[i][j]  = min((A[i][j] + A[i - 1][j]), (A[i][j] + A[i - 1][j + 1]) )		
            elif (j == len(A[0]) - 1):
                A[i][j]  = min((A[i][j] + A[i - 1][j]), (A[i][j] + A[i - 1][j - 1]) )		
            #every other column will have three paths coming from above
            else:
                A[i][j] = min(A[i][j] + A[i - 1][j],A[i][j] + A[i - 1][j + 1], A[i][j] + A[i - 1][j - 1])
	# Now that minimum falling sums for each value at the bottom row have been computer
	# We can just take the min of the bottow row to get the smallest overall path sum 
    return min(A[len(A) - 1])


Time complexity: O(mn)
Space: O(1)	
