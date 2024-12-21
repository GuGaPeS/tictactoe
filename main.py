class Tictactoe:
    def __init__(self, size: int):
        self.size = size
        self.BLANKSPACE = "-"
        self.winner = None
        self.board = [[self.BLANKSPACE for _ in range(self.size)] for _ in range(self.size)]

    def turn(self, x: int, y: int, p: str) -> None:
        """Update the current state of the match. Checks if the move resulted in a win."""
        if self.playableMove(x, y):
            self.board[y][x] = p
            self.checkVictory()
            return True
        return False
    
    def playableMove(self, x: int, y: int) -> bool:
        """Return if the selected coordinates have a blank space and are within bounds."""
        if 0 <= x < self.size and 0 <= y < self.size:
            return self.board[y][x] == self.BLANKSPACE
        return False

    def displayBoard(self) -> None:
        """Display the board in a user-friendly format."""
        for row in self.board:
            print(" | ".join(row))
        print("-" * (self.size * 4 - 3))

    def makeLine(self, row: list) -> bool:
        """Return if the row is filled with the same player's symbol."""
        return len(set(row)) == 1 and row[0] != self.BLANKSPACE

    def checkVictory(self) -> bool:
        """Check if there is a winner in the current state of the board and updates the self@Tictactoe.winner."""
        # Check horizontal line
        for row in self.board:
            if self.makeLine(row):
                self.winner = row[0]
                return True
        # Check vertical line
        for i in range(self.size):
            v_row = [self.board[x][i] for x in range(self.size)]
            if self.makeLine(v_row):
                self.winner = v_row[0]
                return True
        # Check diagonal line
        d_row = [self.board[x][x] for x in range(self.size)]
        if self.makeLine(d_row):
            self.winner = d_row[0]
            return True
        # Check reversed diagonal line
        d_row_reversed = [self.board[a][b] for a, b in zip(range(self.size), range(self.size - 1, -1, -1))]
        if self.makeLine(d_row_reversed):
            self.winner = d_row_reversed[0]
            return True
        
        if self.checkTie():
            self.winner = "Tie"
            return True

        return False
    
    def checkTie(self) -> bool:
        """... Really? It checks if there is a... TIE. What did you expect?"""
        return all(self.BLANKSPACE not in row for row in self.board)
