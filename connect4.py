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
        """Returns True if able to place a piece in specified column"""
        try:
            # check that the variable is an int
            column = int(column)
        except:
            return False

        column -= 1 # drecement for code
        if (
            self.state != 'Unfinished'
            or not column in range(0,7) 
            or self.board[column][5] != self.EMPTY):
            return False
        
        # get lowest height in column
        lowest_row = self.board[column].index(self.EMPTY)
        self.board[column][lowest_row] = self.player

        # check if player won

        # update the current player
        self.player = 'R' if self.player == 'Y' else 'Y'

        return True

    def __str__(self) -> str:
        """Return the board as a String"""
        board_str = '\n  1   2   3   4   5   6   7  \n'
        for y in range(self._rows-1, -1, -1):
            for x in range(self._cols):
                board_str += '| ' + self.board[x][y] + ' '
            board_str += '|\n'
        board_str += '-'*29
        
        # Change the output based on if game is over or not
        if(self.state == "Unfinished"):
            board_str += '\nPlayer '+self.player + ', it is your turn'
        else:
            board_str += '\nGame State: '+ self.state
        
        return board_str + '\n'

    def __repr__(self) -> str:
        """Return the Connect4 game state as a String"""
        return self.__str__()
    
    def play(self):
        """Play an interactive game of Connect4"""
        print("Welcome to Connect4!")
        print("Each player will take turns dropping their piece in one of the columns.")
        print("Your objective is to get 4 of your pieces in a row on the {col} x {row} sized board".format(col=self._cols, row=self._rows))
        print("\n",self)

        while(self.state == "Unfinished"):
            while(not self.make_move(input("\nPlease select a column: "))):
                print("The column chosen was invalid.")
            print(self)
        
        print("Thank you for playing!")
