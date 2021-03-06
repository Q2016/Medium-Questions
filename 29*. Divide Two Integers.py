Question:
Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.
The integer division should truncate toward zero, which means losing its fractional part. For example, 8.345 would be 
truncated to 8, and -2.7335 would be truncated to -2. Return the quotient after dividing dividend by divisor.
    
    
    
    
    
    
    
    
    
    
    
    
    
    
The O(n) is trivial but I dont understand the log(n), there's no video and it's time complexity      
    
Solution: Bit 
    
The key observation is that the quotient of a division is just the number of times that we can subtract the divisor from 
the dividend without making it negative. 

first version O(n):
    
    def divide(self, dividend, divisor):
        
        dividend, divisor = abs(dividend), abs(divisor)
        res = 0
        
        while dividend >= divisor:
            dividend-=divisor
            output+= 1
                
        if (dividend<0 and divisor>=0) or (divisor<0 and dividend>=0):
            output = -output
            
        return output

Second improved version log(n):

class Solution:
# @return an integer
def divide(self, dividend, divisor):
    positive = (dividend < 0) is (divisor < 0)
    dividend, divisor = abs(dividend), abs(divisor)
    res = 0
    while dividend >= divisor:
        temp, i = divisor, 1
        while dividend >= temp:
            dividend -= temp
            res += i
            i <<= 1
            temp <<= 1
    if not positive:
        res = -res
    return min(max(-2147483648, res), 2147483647)
