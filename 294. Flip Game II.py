Leetcode: Flip Game II 

You are playing the following Flip Game with your friend: Given a string that contains only these two characters: 
+ and -, you and your friend take turns to flip two consecutive "++" into "--". The game ends when a person
can no longer make a move and therefore the other person will be the winner.
Write a function to determine if the starting player can guarantee a win.
For example, given s = "++++", return true. The starting player can guarantee 
a win by flipping the middle "++" to become "+--+".

Follow up:
Derive your algorithm's runtime complexity.
Understand the problem:
At first glance, backtracking seems to be the only feasible solution to this problem. 
We can basically try every possible move for the first player (Let's call him 1P from now on), 
and recursively check if the second player 2P has any chance to win. If 2P is guaranteed to lose, 
then we know the current move 1P takes must be the winning move. The implementation is actually very simple:

 Code (Java):

 
public class Solution {
    public boolean canWin(String s) {
        if (s == null || s.length() == 0) {
            return false;
        }
         
        char[] arr = s.toCharArray();
         
        return canWinHelper(arr);
    }
     
    private boolean canWinHelper(char[] arr) {
        int i = 0;
         
        for (i = 0; i < arr.length - 1; i++) {
            if (arr[i] == '+' && arr[i + 1] == '+') {
                arr[i] = '-';
                arr[i + 1] = '-';
                 
               boolean win = !canWinHelper(arr);
                 
                arr[i] = '+';
                arr[i + 1] = '+';
                 
                if (win) {
                    return true;
                }
            }
        }
         
        return false;
    }
}
 



For most interviews, this is the expected solution. 
Now let's check the time complexity: Suppose originally the board of 
size N contains only '+' signs, then roughly we have:

T(N) = T(N-2) + T(N-3) + [T(2) + T(N-4)] + [T(3) + T(N-5)] + ... 
        [T(N-5) + T(3)] + [T(N-4) + T(2)] + T(N-3) + T(N-2)
     = 2 * sum(T[i])  (i = 3..N-2)

You will find that T(N) = 2^(N-1) satisfies the above equation. 
Therefore, this algorithm is at least exponential.

   
Leetcode: Flip Game 
You are playing the following Flip Game with your friend: 
Given a string that contains only these two characters: + and -, 
you and your friend take turns to flip twoconsecutive "++" into "--". 
The game ends when a person can no longer make a move and therefore the other person will be the winner.
Write a function to compute all possible states of the string after one valid move.
For example, given s = "++++", after one move, it may become one of the following states:
[
  "--++",
  "+--+",
  "++--"
]

If there is no valid move, return an empty list [].
Understand the problem:
The problem only asks for flipping "++" into "--",
NOT -- to ++. So the solution is to move all consecutive "++" into "--".

 
 Code (Java):
public class Solution {
    public List<String> generatePossibleNextMoves(String s) {
        List<String> result = new ArrayList<>();
        if (s == null || s.length() < 2) {
            return result;
        }
         
        for (int i = 0; i < s.length() - 1; i++) {
            if (s.charAt(i) == '+' && s.charAt(i + 1) == '+') {
                String s1 = s.substring(0, i);
                String s2 = "--";
                String s3 = s.substring(i + 2);
                String temp = s1 + s2 + s3;
                result.add(temp);
            }
        }
         
        return result;
    }
}
