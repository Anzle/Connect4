# connect4.py

class Connect4:
    def __init__(self):
        self.EMPTY = ' '
        self.board = []
        self.player = 'R'
        self.state = 'Unfinished'

        self._cols = 7
        self._rows = 6

        for x in range(self._cols):
            column = [self.EMPTY for i in range(self._rows)]
            self.board.append(column)

    def make_move(self, column: int) -> bool:
        """Returns True if able to place piece in current player's column"""
        column -= 1 # drecement for code
        if (
            self.state != 'Unfinished'
            or not column in range(0,7) 
            or self.board[column][5] != self.EMPTY):
            return False
        
        # get lowest height in column
        lowest_row = self.board[column].index(self.EMPTY)
        self.board[column][lowest_row] = self.player

        self.player = 'R' if self.player == 'Y' else 'Y'

        return True


    def __str__(self) -> str:
        """Return's the board as a String"""
        board_str = 'Current Player: '+self.player + '\n  1   2   3   4   5   6   7  \n'
        for y in range(self._rows-1, -1, -1):
            for x in range(self._cols):
                board_str += '| ' + self.board[x][y] + ' '
            board_str += '|\n'
        board_str += '-'*29
        board_str += '\nGame State: '+ self.state
        return board_str + '\n'

    def __repr__(self) -> str:
        """Return the Connect4 game state as a String"""
        return self.__str__()