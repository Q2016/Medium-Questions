class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {

        if(amount<1) return 0;
        vector<int> count;
        count.resize(amount);
        return helper(coins, amount, count);
    }

    int helper(vector<int>& coins, int rem, vector<int>& count) { 
      // rem: remaining coins after the last step; count[rem]: minimum number of coins to sum up to rem
        if(rem<0) return -1; // not valid
        if(rem==0) return 0; // completed
        if(count[rem-1] != 0) return count[rem-1]; // already computed, so reuse
        int min = INT_MAX;
        for(int coin : coins) {
            int res = helper(coins, rem-coin, count);
            if(res>=0 && res < min)
                min = 1+res;
        }
        count[rem-1] = (min==INT_MAX) ? -1 : min;
        return count[rem-1];
    }
};


/*
#Recursive Method:#
The idea is very classic dynamic programming: think of the last step we take. 
Suppose we have already found out the best way to sum up to amount a, then for the last step, 
we can choose any coin type which gives us a remainder r where r = a-coins[i] for all i's. 
For every remainder, go through exactly the same process as before until either the 
remainder is 0 or less than 0 (meaning not a valid solution). With this idea, the only 
remaining detail is to store the minimum number of coins needed to sum up to r so that 
we don't need to recompute it over and over again.
*/
