"""
main driver file - handles user input and displays game objects
"""

import pygame as p
from chess import chessEngine

# Initialize pygame library
p.init()

# Set the width and height of the game screen
width = height = 400

# Set the maximum frames per second (FPS)
maxFPS = 15

# Set the dimension of the chess board (8x8)
dimension = 8

# Calculate the size of each square on the board
squareSize = height // dimension

# Create an empty dictionary to store images of chess pieces
images = {}


# Function to load images of chess pieces into the global dictionary
def loadImages():
    pieces = ["bB", "bK", "bN", "bP", "bQ", "bR", "wB", "wK", "wN", "wP", "wQ", "wR"]
    for piece in pieces:
        images[piece] = p.transform.scale(p.image.load("images/" + piece + ".png"), (squareSize, squareSize))


# Main function that runs the game
def main():
    p.init()  # Initialize pygame library
    screen = p.display.set_mode((width, height))  # Create a screen for the game
    clock = p.time.Clock()  # Create a clock for the game to keep track of time
    screen.fill(p.Color("white"))  # Fill the screen with white color
    gs = chessEngine.GameSate()  # Create a new instance of the chess engine game state
    validMoves = gs.getValidMovies()
    moveMade = False  # Flag for when a move is made
    loadImages()  # Load images of chess pieces into the global dictionary
    running = True  # Set the game to running
    squareSelected = ()  # Create a variable to store the selected square
    playerClicks = []    # Create a list to store player clicks

    # Game loop
    while running:
        for e in p.event.get():
            # Check if the player has closed the game window
            if e.type == p.QUIT:
                running = False
            # Check if the player has clicked on the screen
            elif e.type == p.MOUSEBUTTONDOWN:
                # Get the location of the click
                location = p.mouse.get_pos()
                # Calculate the column and row of the square clicked
                col = location[0] // squareSize
                row = location[1] // squareSize

                # Check if the square clicked is the same as the previous square selected
                if squareSelected == (row, col):
                    # If so, deselect the square
                    squareSelected = ()
                    playerClicks = []
                else:
                    # If not, select the square
                    squareSelected = (row, col)
                    playerClicks.append(squareSelected)

                # Check if the player has made two clicks (one for starting square, one for ending square)
                if len(playerClicks) == 2:
                    # Make a move using the chess engine
                    move = chessEngine.move(playerClicks[0], playerClicks[1], gs.board)

                    # Print the chess notation of the move
                    print(move.getChessNotation())

                    # Checks that the players move is valid
                    if move in validMoves:
                        # Update the game state with the move made
                        gs.makeMove(move)
                        moveMade = True



                    # Deselect the square and clear the player clicks list
                    squareSelected = ()
                    playerClicks = []
                # Check if the player has pressed the 'u' key (to undo a move)

            elif e.type == p.KEYDOWN:
                if e.key == p.K_u:
                    # Call the undoMove function in the chess engine to undo the last move
                    gs.undoMove()
                    moveMade = True
                    print("undone")

        if moveMade:
            validMoves = gs.getValidMovies()
            moveMade = False


        # Draw the game state on the screen
        drawGS(screen, gs)

        # Limit the game's fps
        clock.tick(maxFPS)

        # Update the screen with the new game state
        p.display.flip()


# Function to draw the game state on the screen
def drawGS(screen, gs):
    drawBoardSquares(screen)  # Draw the squares on the board
    drawPieces(screen, gs.board)  # Draw the pieces on the squares


# Function to draw the squares on the board
def drawBoardSquares(screen):
    colours = [p.Color("oldlace"), p.Color("sienna")]
    for r in range(dimension):
        for c in range(dimension):
            colour = colours[((r + c) % 2)]
            p.draw.rect(screen, colour, p.Rect(c * squareSize, r * squareSize, squareSize, squareSize))


# Function to draw the pieces on the squares
def drawPieces(screen, board):
    for r in range(dimension):
        for c in range(dimension):
            piece = board[r][c]
            if piece != "--":
                screen.blit(images[piece], p.Rect(c * squareSize, r * squareSize, squareSize, squareSize))


# Check if the script is being run as the main file
if __name__ == "__main__":
    main()
