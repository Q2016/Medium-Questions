Question:
Given a matrix of integers A with R rows and C columns, find the maximum score of a 
path starting at [0, 0] and ending at [R-1, C-1].
The score of a path is the minimum value in that path. 
 [5, 4, 5] 5->4->5->6->6 in this path, the minimum value is 4, so the score is 4.
 [1, 2, 6]
 [7, 4, 6]
A path moves some number of times from one visited cell to any neighbouring unvisited cell 
in one of the 4 cardinal directions (north, east, west, south).






Solution: Heap
Backtracking: Time O(4^RC), Space O(RC)
Priority Queue: Time O(RC log RC), Space O(RC)
Two-Direction DP: Time O(RC), Space O(RC)

 
from heapq import heappush, heappop
class Solution:
    def maximumMinimumPath(self, A: List[List[int]]) -> int:
        
        #max(t, -matrix[nx][ny] for storing min on each path
        #heappush to guarantee the heap top is the max of "mins on each path"
        if not A:
            return -1

        visited = [[False] * len(A[0]) for _ in range(len(A))]
        
        heap = [(-A[0][0], 0, 0)] #What are the elements: value of the matrix at index i and j=>[(-A[i,j],i,j)]
        
        visited[0][0] = True
        while heap: # why heap and not a queue?
         
            value, i, j = heappop(heap)
            if i == len(A) - 1 and j == len(A[0]) - 1: # reached the end
                return -value
            
            for new_i, new_j in (i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1): # looking up neighbors
                if 0 <= new_i < len(A) and 0 <= new_j < len(A[0]) and not visited[new_i][new_j]:
                    heappush(heap, (max(value, -A[new_i][new_j]), new_i, new_j))
                    visited[new_i][new_j] = True

        return -1

