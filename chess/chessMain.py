"""
main driver file - handles user input and displays game objects
"""

import pygame as p
from chess import chessEngine



p.init()
width = height = 400
maxFPS = 15
dimension = 8
squareSize = height // dimension

images = {}
# calls a global dictionary of images




def loadImages():
   pieces = ["bB", "bK", "bN", "bP", "bQ", "bR", "wB", "wK", "wN", "wP", "wQ", "wR"]
   for piece in pieces:
       images[piece] = p.transform.scale(p.image.load("images/" + piece + ".png"), (squareSize, squareSize))


def main():

   p.init()
   screen = p.display.set_mode((width, height))
   clock = p.time.Clock()
   screen.fill(p.Color("white"))
   gs = chessEngine.GameSate()
   print(gs.board)


main()

