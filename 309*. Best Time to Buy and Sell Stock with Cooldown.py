Question:
You are given an array prices where prices[i] is the price of a given stock on the ith day. Find the maximum profit you 
can achieve. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times) 
with the following restrictions: After you sell your stock, you cannot buy stock on the next day (i.e., cooldown one day).
Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

Example 1:
Input: prices = [1,2,3,0,2]
Output: 3
Explanation: transactions = [buy, sell, cooldown, buy, sell]    
    






    
Solution:  DP 
picture bellow: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/discuss/75928/Share-my-DP-solution-(By-State-Machine-Thinking)
                                                                                                     rest
There are three states, according to the action that you can take.                      rest    s0 <--------- s2
                                                                                                  \          />
                                                                                           buy     \        /  sell
                                                                                                    \>     /
                                                                                                       s1
Hence, from there, you can now the profit at a state at time i as:                                    rest
s0[i] = max(s0[i - 1], s2[i - 1])              Stay at s0, or rest from s2
s1[i] = max(s1[i - 1], s0[i - 1] - prices[i])  Stay at s1, or buy from s0
s2[i] = s1[i - 1] + prices[i]                  Only one way from s1
Then, you just find the maximum of s0[n] and s2[n], since they will be the maximum profit we need 

Define base case:
s0[0] = 0; // At the start, you don't have any stock if you just rest
s1[0] = -prices[0]; // After buy, you should have -prices[0] profit. Be positive!
s2[0] = INT_MIN; // Lower base case

    def maxProfit([list]-> prices):
	n=len(prices)
	if (len(prices) <= 1): 
	    return 0;
	s0=[0]*n
	s1=[0]*n
	s2=[0]*n
	
	s1[0] = -prices[0]
	s0[0] = 0
	s2[0] = INT_MIN

	for i in range(1, len(prices): 
	    s0[i] = max(s0[i - 1], s2[i - 1])
	    s1[i] = max(s1[i - 1], s0[i - 1] - prices[i])
	    s2[i] = s1[i - 1] + prices[i]
		
	return max(s0[len(prices) - 1], s2[len(prices) - 1])
