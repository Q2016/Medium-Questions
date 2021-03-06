Question:
Given an m x n matrix, return all elements of the matrix in spiral order.

Example 1:
Input: matrix = [[1->2->3],
                        | 
                 [4->5->6],
                  |     |
                 [7<-8<-9]]
Output: [1,2,3,6,9,8,7,4,5]  
  
  
  
  
  
  
  
  
  
Solution:  
  
  https://www.youtube.com/watch?v=BJnMZNwUk1M
  
class Solution:
  def spiralOrder(self, matrix):
    res=[]
    left, right=0, len(matrix[0])
    top, bottom=0, len(matrix)
    
    while left<right and top<bottom:
      # get every i in the top row
      for i in range(left, right):
        res.append(matrix[top][i])
      top +=1
      
      # get every i in the right col
      for i in range(top, bottom):
        res.append(matrix[i][right-1])
      right -=1
      
      if not (left< right and top<bottom):
        break
        
      # get every i in the bottom row
      for i in range(right-1, left-1,-1):
        res.append(matrix[bottom-1][i])
        
      bottom -=1
      
      # get every i in the left col
      for i in range(bottom-1, top-1,-1):
        res.append(matrix[i][left])
      left+=1
      
    return res  
   
       
  
  
  
  
  
  
  
This is a very simple and easy to understand solution. I traverse right and increment rowBegin, then traverse 
down and decrement colEnd, then I traverse left and decrement rowEnd, and finally I traverse up and increment colBegin.
The only tricky part is that when I traverse left or up I have to check whether the row or col still exists to prevent duplicates. 

  def spiralOrder(self, matrix):
        if not matrix: return []
        
        row_start = 0
        row_end = len(matrix) - 1
        
        col_start = 0
        col_end = len(matrix[0]) - 1
        
        res = []
        while row_start <= row_end and col_start <= col_end:
            
            # right
            for j in range(col_start, col_end+1):
                res.append(matrix[row_start][j])
            row_start += 1
            
            # down
            for i in range(row_start, row_end+1):
                res.append(matrix[i][col_end])
            col_end -= 1
            
            # left
            if row_start <= row_end:
                for j in range(col_end, col_start-1, -1):
                    res.append(matrix[row_end][j])

                row_end -= 1

            # up
            if col_start <= col_end:
                for i in range(row_end, row_start-1, -1):
                    res.append(matrix[i][col_start])
                col_start += 1
         
        return res
