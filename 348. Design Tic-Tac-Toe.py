Question:
Design a Tic-tac-toe game that is played between two players on a nxn grid. You may assume the following rules: 
A move is guaranteed to be valid and is placed on an empty block. Once a winning condition is reached, no more moves is allowed.
A player who succeeds in placing n of their marks in a horizontal, vertical, or diagonal row wins the game.

Example:
Given n = 3, assume that player 1 is "X" and player 2 is "O" in the board.
TicTacToe toe = new TicTacToe(3);
toe.move(0, 0, 1); -> Returns 0 (no one wins)
|X| | |
| | | |    // Player 1 makes a move at (0, 0).
| | | |
toe.move(0, 2, 2); -> Returns 0 (no one wins)
|X| |O|
| | | |    // Player 2 makes a move at (0, 2).
| | | |
toe.move(2, 2, 1); -> Returns 0 (no one wins)
|X| |O|
| | | |    // Player 1 makes a move at (2, 2).
| | |X|
toe.move(1, 1, 2); -> Returns 0 (no one wins)
|X| |O|
| |O| |    // Player 2 makes a move at (1, 1).
| | |X|
toe.move(2, 0, 1); -> Returns 0 (no one wins)
|X| |O|
| |O| |    // Player 1 makes a move at (2, 0).
|X| |X|
toe.move(1, 0, 2); -> Returns 0 (no one wins)
|X| |O|
|O|O| |    // Player 2 makes a move at (1, 0).
|X| |X|
toe.move(2, 1, 1); -> Returns 1 (player 1 wins)
|X| |O|
|O|O| |    // Player 1 makes a move at (2, 1).
|X|X|X|
Follow up:
Could you do better than O(n^2) permove() operation? Could you get O(1) per move() operation?


Solution:
class TicTacToe(object):

    def __init__(self, n):
        self.__size = n
        self.__rows = [[0, 0] for _ in xrange(n)]
        self.__cols = [[0, 0] for _ in xrange(n)]
        self.__diagonal = [0, 0]
        self.__anti_diagonal = [0, 0]
        
    def move(self, row, col, player):
        """
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        """
        i = player - 1
        self.__rows[row][i] += 1
        self.__cols[col][i] += 1
        if row == col:
            self.__diagonal[i] += 1
        if col == len(self.__rows) - row - 1:
            self.__anti_diagonal[i] += 1
        if any([self.__rows[row][i] == self.__size), 
                self.__cols[col][i] == self.__size, 
                self.__diagonal[i] == self.__size, 
                self.__anti_diagonal[i] == self.__size]):
            return player
        return 0

    
# Time:  O(1), per move.
# Space: O(n^2)    
