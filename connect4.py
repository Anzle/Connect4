# connect4.py

class Connect4:
    def __init__(self):
        EMPTY = ' '
        self.board = []
        self.player = 'R'

        self._cols = 7
        self._rows = 6

        for x in range(self._cols):
            column = [EMPTY for i in range(self._rows)]
            self.board.append(column)

    def make_move(self, column: int) -> bool:
        """Returns True if able to place piece in current player's column"""
        
        pass

    def __str__(self) -> str:
        """Return's the board as a String"""
        board_str = 'Current Player: '+self.player+'\n  1   2   3   4   5   6   7  \n'
        for y in range(self._rows-1, -1, -1):
            for x in range(self._cols):
                board_str += '| ' + self.board[x][y] + ' '
            board_str += '|\n'
        board_str += '-'*29
        return board_str

    def __repr__(self) -> str:
        """Return the Connect4 game state as a String"""
        return self.__str__()



def board_test():
    game = Connect4()
    print(game)

board_test()