Question:
There are two types of soup: type A and type B. Initially, we have n ml of each type of soup. There are four kinds of operations:
Serve 100 ml of soup A and 0 ml of soup B,
Serve 75 ml of soup A and 25 ml of soup B,
Serve 50 ml of soup A and 50 ml of soup B, and
Serve 25 ml of soup A and 75 ml of soup B.
When we serve some soup, we give it to someone, and we no longer have it. Each turn, we will choose from the four operations with an equal 
probability 0.25. If the remaining volume of soup is not enough to complete the operation, we will serve as much as possible. We stop once we 
no longer have some quantity of both types of soup.
Note that we do not have an operation where all 100 ml's of soup B are used first.
Return the probability that soup A will be empty first, plus half the probability that A and B become empty at the same time. Answers within 10-5 
of the actual answer will be accepted.

Example 1:
Input: n = 50
Output: 0.62500
Explanation: If we choose the first two operations, A will become empty first.
For the third operation, A and B will become empty at the same time.
For the fourth operation, B will become empty first.
So the total probability of A becoming empty first plus half the probability that A and B become empty at the same time, is 0.25 * (1 + 1 + 0.5 + 0) = 0.625.



Solution:
First, 25ml is annoying
The decription is very difficult to understand, and all 25ml just make it worse.
When I finally figure it out, I consider only how many servings left in A and B.
1 serving = 25ml.
Well, it works similar to your milk powder or protin powder.
If the left part is less than 25ml, it is still considered as one serving.

Second, DP or recursion with memory
Now it's easy to solve this problem.
f(a,b) means the result probability for a ml of soup A and b ml of soup B.
f(a-4,b) means that we take the first operation: Serve 100 ml of soup A and 0 ml of soup B. f(a-3,b-1), f(a-2,b-2), f(a-1,b-3) are other 3 operations.
The condition a <= 0 and b <= 0 means that we run out of soup A and B at the same time, so we should return a probability of 0.5, which is half of 1.0.
The same idea for other two conditions.
I cached the process as we do for Fibonacci sequence. It calculate every case for only once and it can be reused for every test case. No worries for TLE.

Third, take the hint for big N
"Note that we do not have the operation where all 100 ml's of soup B are used first. "
It's obvious that A is easier to be empty than B. And when N gets bigger, we have less chance to run out of B first.
So as N increases, our result increases and it gets closer to 100 percent = 1.

Answers within 10^-5 of the true value will be accepted as correct.
Now it's obvious that when N is big enough, result is close enough to 1 and we just need to return 1.
When I incresed the value of N, I find that:
When N = 4800, the result = 0.999994994426
When N = 4801, the result = 0.999995382315
So if N>= 4800, just return 1 and it will be enough.

Complexity Analysis
I have to say this conversion process is necessary.

The solution using hashmap may luckly get accepted.
Thanks to leetcode infrastructure,
every test cases will run in seperate instances.
(this can be easily tested).

In this case it's the same for space and time using hashmap.

But are you writing codes running only once?
How about the case running multiple test cases within the same instance?

Without this conversion,
it needs O(200 * 200 * 25) time & space if A == B,
it needs O(5000 * 5000) time & space if A != B, (which sounds like 250mb)

But in our solution above, we use only O(200 * 200) time & space.


class Solution(object):
    memo = {}
    def soupServings(self, N):
        if N > 4800: return 1
        def f(a, b):
            if (a, b) in self.memo: return self.memo[a, b]
            if a <= 0 and b <= 0: return 0.5
            if a <= 0: return 1
            if b <= 0: return 0
            self.memo[(a, b)] = 0.25 * (f(a - 4, b) + f(a - 3, b - 1) + f(a - 2, b - 2) + f(a - 1, b - 3))
            return self.memo[(a, b)]
        N = math.ceil(N / 25.0)
        return f(N, N)
