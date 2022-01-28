Question:
Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.
The integer division should truncate toward zero, which means losing its fractional part. For example, 8.345 would be 
truncated to 8, and -2.7335 would be truncated to -2. Return the quotient after dividing dividend by divisor.
    
    
Solution: Bit 
    
The key observation is that the quotient of a division is just the number of times that we can subtract the divisor from 
the dividend without making it negative. Suppose dividend = 15 and divisor = 3, 15 - 3 > 0. We now try to subtract more by 
shifting 3 to the left by 1 bit (6). Since 15 - 6 > 0, shift 6 again to 12. Now 15 - 12 > 0, shift 12 again to 24, which is 
larger than 15. So we can at most subtract 12 from 15. Since 12 is obtained by shifting 3 to left twice, it is 1 << 2 = 4 times of 3. 
We add 4 to an answer variable (initialized to be 0). The above process is like 15 = 3 * 4 + 3. We 
now get part of the quotient (4), with a remaining dividend 3.
Then we repeat the above process by subtracting divisor = 3 from the remaining dividend = 3 
and obtain 0. We are done. In this case, no shift happens. We simply add 1 << 0 = 1 to the answer variable.


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
