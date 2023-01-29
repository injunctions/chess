"""
stores all current state info as well as legal move calculations and move logs
"""


class GameSate():
    def __init__(self):
        self.board = [
            # board displayed as arrays
            ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
            ["bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP"],
            ["--", "--", "--", "--", "wP", "--", "--", "--"],
            ["--", "--", "bB", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "wB", "--", "--", "--"],
            ["--", "--", "--", "bP", "--", "--", "--", "--"],
            ["wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP"],
            ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]]

        self.moveFunctions = {'B': self.getBishopMoves, 'K': self.getKingMoves, 'N': self.getKnightMoves,
                              'P': self.getPawnMoves, 'Q': self.getQueenMoves, 'R': self.getRookMoves}
        self.whiteToMove = True
        self.moveLog = []

    # function that takes the players inputted move and relays this change to the board

    def makeMove(self, move):

        # removes the piece moved from the board
        self.board[move.startRow][move.startCol] = "--"

        # places the piece moved onto the new square
        self.board[move.endRow][move.endCol] = move.pieceMoved

        # logs the move made
        self.moveLog.append(move)

        # flips the players turns
        self.whiteToMove = not self.whiteToMove

    # function for undoing the players last move

    def undoMove(self):

        # checks that a move has actually been made
        if len(self.moveLog) != 0:
            # gets the last move from the move log
            move = self.moveLog.pop()

            self.board[move.startRow][move.startCol] = move.pieceMoved
            self.board[move.endRow][move.endCol] = move.pieceCaptured

            # flips players turn
            self.whiteToMove = not self.whiteToMove

    def getValidMovies(self):
        # TODO: get valid moves
        return self.getPossibleMoves()

    def getPossibleMoves(self):
        moves = []
        for r in range(len(self.board)):
            for c in range(len(self.board[r])):
                turn = self.board[r][c][0]
                if (turn == "w" and self.whiteToMove) or (turn == "b" and not self.whiteToMove):
                    piece = self.board[r][c][1]
                    self.moveFunctions[piece](r, c, moves)  # Calls move function for piece type
        return moves

    def getBishopMoves(self, r, c, moves):
        directions = ((-1, -1), (-1, 1), (1, -1),
                      (1, 1))  # Holds directions for diagonal up and left, up and right, down and left, down and right
        enemyColour = "b" if self.whiteToMove else "w"
        for d in directions:  # Checks through each of the directions defined above
            for e in range(1, 8):  # Checks through values one to seven
                endRow = r + d[0] * e
                endCol = c + d[1] * e
                if 0 <= endRow < 8 and 0 <= endCol < 8:  # Checks that piece is still on the board
                    endPiece = self.board[endRow][endCol]
                    if endPiece == "--":  # Checks for a valid empty space for the piece to move into
                        moves.append(move((r, c), (endRow, endCol), self.board))
                    elif endPiece[0] == enemyColour:  # Checks for a valid enemy piece to take
                        moves.append(move((r, c), (endRow, endCol), self.board))
                        break
                    else:  # Friendly piece in the way
                        break
                else:  # Move is off the board
                    break

    def getKingMoves(self, r, c, moves):
        pass

    def getKnightMoves(self, r, c, moves):
        directions = ((-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1),
                      (2, 1))  # Tuple of all possible directions the piece can move
        enemyColour = "b" if self.whiteToMove else "w"  # Checks for enemy colour for takes
        for d in directions:
            endRow = r + d[0]
            endCol = c + d[1]
            if 0 <= endRow < 8 and 0 <= endCol < 8:
                endPiece = self.board[endRow][endCol]
                if endPiece[0] == enemyColour or "--": # Checks for either a piece to take or empty square to move into
                    moves.append(move((r, c), (endRow, endCol), self.board)) # Makes move

    def getPawnMoves(self, r, c, moves):
        if self.whiteToMove:  # Checks if it's a white pawn
            # Check if square in front is empty if so add that as a move then check if piece is on row 6 or 2 and square
            # two in front is empty, if so add that as a move
            if self.board[r - 1][c] == "--":  # One square pawn move
                moves.append(move((r, c), (r - 1, c), self.board))
                if r == 6 and self.board[r - 2][c] == "--":  # Two square pawn move
                    moves.append(move((r, c), (r - 2, c), self.board))
            if c - 1 >= 0:  # Makes sure pieces cannot move off the left side of the board
                if self.board[r - 1][c - 1][0] == 'b':  # Checks for black piece to capture
                    moves.append(move((r, c), (r - 1, c - 1), self.board))
            if c + 1 <= 7:  # Makes sure pieces cannot move off the right side of the board
                if self.board[r - 1][c + 1][0] == 'b':  # Checks for black piece to capture
                    moves.append(move((r, c), (r - 1, c + 1), self.board))


        else:  # Black Pawn moves
            if self.board[r + 1][c] == "--":  # One square pawn move
                moves.append(move((r, c), (r + 1, c), self.board))
                if r == 1 and self.board[r + 2][c] == "--":  # Two square pawn move
                    moves.append(move((r, c), (r + 2, c), self.board))
            if c - 1 >= 0:  # Makes sure pieces cannot move off the left side of the board
                if self.board[r + 1][c - 1][0] == 'w':  # Checks for white piece to capture
                    moves.append(move((r, c), (r + 1, c - 1), self.board))  # Capture to the left
            if c + 1 <= 7:  # Makes sure pieces cannot move off the right side of the board
                if self.board[r + 1][c + 1][0] == 'w':  # Checks for white piece to capture
                    moves.append(move((r, c), (r + 1, c + 1), self.board))  # Capture to the right

    def getQueenMoves(self, r, c, moves):
        pass

    def getRookMoves(self, r, c, moves):
        directions = ((-1, 0), (0, -1), (1, 0), (0, 1))  # Holds directions for up, left, down and right
        enemyColour = "b" if self.whiteToMove else "w"
        for d in directions:  # Checks through each of the directions defined above
            for e in range(1, 8):  # Checks through values one to seven
                endRow = r + d[0] * e
                endCol = c + d[1] * e
                if 0 <= endRow < 8 and 0 <= endCol < 8:  # Checks that piece is still on the board
                    endPiece = self.board[endRow][endCol]
                    if endPiece == "--":  # Checks for a valid empty space for the piece to move into
                        moves.append(move((r, c), (endRow, endCol), self.board))
                    elif endPiece[0] == enemyColour:  # Checks for a valid enemy piece to take
                        moves.append(move((r, c), (endRow, endCol), self.board))
                        break
                    else:  # Friendly piece in the way
                        break
                else:  # Move is off the board
                    break


class move():
    ranksToRows = {"1": 7, "2": 6, "3": 5, "4": 4, "5": 3, "6": 2, "7": 1, "8": 0}
    rowsToRanks = {v: k for k, v in ranksToRows.items()}

    filesToCols = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7}
    colsToFiles = {v: k for k, v in filesToCols.items()}

    def __init__(self, startSquare, endSquare, board):
        """
        Initialize the move object with the start and end square of the move and the current state of the board.
        :param startSquare: Tuple of ints (row, col) representing the starting square of the move
        :param endSquare: Tuple of ints (row, col) representing the ending square of the move
        :param board: List of Lists representing the current state of the chess board

        """
        self.startRow = startSquare[0]
        self.startCol = startSquare[1]
        self.endRow = endSquare[0]
        self.endCol = endSquare[1]
        self.pieceMoved = board[self.startRow][self.startCol]
        self.pieceCaptured = board[self.endRow][self.endCol]
        self.moveID = self.startRow * 1000 + self.startCol * 100 + self.endRow * 10 + self.endCol  # Generates unique move id for each possible move made

    # Overriding the equals method

    def __eq__(self, other):
        if isinstance(other, move):
            return self.moveID == other.moveID
        return False

    def getChessNotation(self):
        # Returns basic chess notation of the move

        return self.getRankFile(self.startRow, self.startCol) + self.getRankFile(self.endRow, self.endCol)

    def getRankFile(self, r, c):
        """
        Function that converts the row and col of a square to its rank and file notation
        :param r: int representing the row of the square
        :param c: int representing the col of the square
        :return: string representing the rank and file of the square (ex: 'e2')
        """
        return self.colsToFiles[c] + self.rowsToRanks[r]
