Question:
You are given an integer array deck. There is a deck of cards where every card has a unique integer. The integer on the ith card is deck[i].
You can order the deck in any order you want. Initially, all the cards start face down (unrevealed) in one deck.
You will do the following steps repeatedly until all cards are revealed:
Take the top card of the deck, reveal it, and take it out of the deck.
If there are still cards in the deck then put the next top card of the deck at the bottom of the deck.
If there are still unrevealed cards, go back to step 1. Otherwise, stop.
Return an ordering of the deck that would reveal the cards in increasing order.
Note that the first entry in the answer is considered to be the top of the deck.

Example 1:
Input: deck = [17,13,11,2,3,5,7]
Output: [2,13,3,11,5,17,7]
Explanation: 
We get the deck in the order [17,13,11,2,3,5,7] (this order does not matter), and reorder it.
After reordering, the deck starts as [2,13,3,11,5,17,7], where 2 is the top of the deck.
We reveal 2, and move 13 to the bottom.  The deck is now [3,11,5,17,7,13].
We reveal 3, and move 11 to the bottom.  The deck is now [5,17,7,13,11].
We reveal 5, and move 17 to the bottom.  The deck is now [7,13,11,17].
We reveal 7, and move 13 to the bottom.  The deck is now [11,17,13].
We reveal 11, and move 17 to the bottom.  The deck is now [13,17].
We reveal 13, and move 17 to the bottom.  The deck is now [17].
We reveal 17.
Since all the cards revealed are in increasing order, the answer is correct.    



Solution: Simulate the process with a queue.

Sort the deck, it is actually the "final sequence" we want to get according to the question.
Then put it back to the result array, we just need to deal with the index now!
Simulate the process with a queue (initialized with 0,1,2...(n-1)), now how do we pick the card?
We first pick the index at the top: res[q.poll()]=deck[i]
Then we put the next index to the bottom: q.add(q.poll());
Repeat it n times, and you will have the result array!
update
Let's walk through the example:
Input: [17,13,11,2,3,5,7]
Output: [2,13,3,11,5,17,7]

Sort the deck: [2,3,5,7,11,13,17], this is the increasing order we want to generate
Initialize the queue: [0,1,2,3,4,5,6], this is the index of the result array
The first card we pick is res[0], observe the deck, it should be deck[0]==2, so assign res[0]=2
Then we put res[1] to the bottom, so we re-insert 1 to the queue
The second card we pick is res[2], which should be deck[1]==3, so assign res[2]=3
Then we re-insert 3 to the queue
Each time we assign 1 value to the res, so we repeat this n times.
Hope this helps.

class Solution {
public:
    vector<int> deckRevealedIncreasing(vector<int>& deck) {
        int n=deck.size();
        sort(deck.begin(), deck.end());
        queue<int> q;
        for (int i=0; i<n; i++) q.push(i);
        vector<int> res;
        res.resize(n);
        for (int i=0; i<n; i++){
            res[q.front()]=deck[i];
            q.push(q.front());
        }
        return res;
    }
    
};

 c++
    vector<int> deckRevealedIncreasing(vector<int>& deck) {
        sort(deck.rbegin(), deck.rend());
        deque<int> d;
        d.push_back(deck[0]);
        for (int i = 1; i < deck.size(); i++) {
            d.push_front(d.back());
            d.pop_back();
            d.push_front(deck[i]);
        }
        vector<int> res(d.begin(), d.end());
        return res;
    }

Java
class Solution {
    public int[] deckRevealedIncreasing(int[] deck) {
        int n= deck.length;
        Arrays.sort(deck);
        Queue<Integer> q= new LinkedList<>();
        for (int i=0; i<n; i++) q.add(i);
        int[] res= new int[n];
        for (int i=0; i<n; i++){
            res[q.poll()]=deck[i];
            q.add(q.poll());
        }
        return res;
    }
}



From Leetcode solution:
Simulate the revealing process with a deck set to [0, 1, 2, ...]. If for example this deck is revealed in 
the order [0, 2, 4, ...] then we know we need to put the smallest card in index 0, the second smallest card in index 2, 
the third smallest card in index 4, etc.

class Solution(object):
    def deckRevealedIncreasing(self, deck):
        N = len(deck)
        index = collections.deque(range(N))
        ans = [None] * N

        for card in sorted(deck):
            ans[index.popleft()] = card
            if index:
                index.append(index.popleft())

        return ans


