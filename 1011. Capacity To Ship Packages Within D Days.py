Question:
A conveyor belt has packages that must be shipped from one port to another within days.
The ith package on the conveyor belt has a weight of weights[i]. Each day, we load the ship with packages on the conveyor belt. 
We may not load more weight than the maximum weight capacity of the ship.
Return the least weight capacity of the ship that will result in all the packages on the conveyor belt being shipped within.

Example 1:
Input: weights = [1,2,3,4,5,6,7,8,9,10], days = 5
Output: 15
Explanation: A ship capacity of 15 is the minimum to ship all the packages in 5 days like this:
1st day: 1, 2, 3, 4, 5
2nd day: 6, 7
3rd day: 8
4th day: 9
5th day: 10
Note that the cargo must be shipped in the order given, so using a ship of capacity 14 and splitting the packages into parts like (2, 3, 4, 5), (1, 6, 7), (8), (9), (10) is not allowed.    








Asking for ordered partition with max sum or maximum sum with n(day) partition

Solution: Binary search---> so basically brute force but optimized, sums are monotonic so BS works

// for binary search look at: 
//[Python/ Clear explanation] Powerful Ultimate Binary Search Template. Solved many problems.

class Solution {
public:
    
    bool feasible(int capacity, vector<int>& weights, int D){
        int days = 1;
        int total = 0;
        for (auto weight: weights){
            total += weight;
            if (total > capacity){  // too heavy, wait for the next day
                total = weight;
                days += 1;
                if (days > D){  // cannot ship within D days
                    return false;
                }
            }
        }
        return true;
    }
    
    
    int shipWithinDays(vector<int>& weights, int D) {
        
        int left=0; 
        for(auto w:weights){// max
            if (w>left) left=w;
        }
        //cout<<left;
        
        int right = std::accumulate(weights.begin(), weights.end(), 0);
        //cout<<right;
        
        while (left < right){
            int mid = left + (right - left) / 2;
            if (feasible(mid, weights, D)){
                right = mid;
            }
            else{
                left = mid + 1;
            }
        }
        return left;
    }
    
};

/*
Explanation
Given the number of bags,
return the minimum capacity of each bag,
so that we can put items one by one into all bags.

We binary search the final result.
The left bound is max(A),
The right bound is sum(A).


More Good Binary Search Problems
Here are some similar binary search problems.
Also find more explanations.
Good luck and have fun.

Minimum Number of Days to Make m Bouquets
Find the Smallest Divisor Given a Threshold
Divide Chocolate
Capacity To Ship Packages In N Days
Koko Eating Bananas
Minimize Max Distance to Gas Station
Split Array Largest Sum
*/
