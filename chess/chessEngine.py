"""
stores all current state info as well as legal move calculations and move logs
"""


class GameSate():
    def __init__(self):
        self.board = [
            # board displayed as arrays
            ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
            ["bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP"],
            ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]]
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

        # UNFINISHED

        moves = []
        for r in range(len(self.board)):
            for c in range(len(self.board[r])):
                turn = self.board[r][c][0]
                if (turn == "w" and self.whiteToMove) and (turn == "b" and not self.whiteToMove):
                    piece = self.board[r][c][1]
                    if piece == "B":
                        self.getBishopMoves(r, c, moves)
                    elif piece == "K":
                        self.getKingMoves(r, c, moves)
                    elif piece == "N":
                        self.getKnightMoves(r, c, moves)
                    elif piece == "P":
                        self.getPawnMoves(r, c, moves)
                    elif piece == "Q":
                        self.getQueenMoves(r, c, moves)
                    elif piece == "R":
                        self.getRookMoves(r, c, moves)

    def getBishopMoves(self, r, c, moves):
        pass

    def getKingMoves(self, r, c, moves):
        pass

    def getKnightMoves(self, r, c, moves):
        pass

    def getPawnMoves(self, r, c, moves):
        pass

    def getQueenMoves(self, r, c, moves):
        pass

    def getRookMoves(self, r, c, moves):
        pass


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
