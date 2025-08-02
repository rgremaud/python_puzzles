# Conway’s Game of Life is a cellular automata simulation that
# follows simple rules to create interesting patterns. It was
# invented by mathematician John Conway in 1970 and popularized
# by Martin Gardner’s “Mathematical Games” column in Scientific American.
# Today, it’s a favorite among programmers and computer scientists,
# though it’s more an interesting visualization than a true “game.”

# The living or dead state of the cells in the next step of the simulation
# depends entirely on their current state. The cells don’t “remember” any older
# states. There is a large body of research regarding the patterns that these
# simple rules produce. Tragically, Professor Conway passed away of complications
# from COVID-19 in April 2020. More information about Conway’s Game of Life can
# be found at https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life, and more
# information about Martin Gardner at https://en.wikipedia.org/wiki/Martin_Gardner.

# The two-dimensional board has a grid of “cells,” each of which follows three simple rules:
# Living cells with two or three neighbors stay alive in the next step of the simulation.
# Dead cells with exactly three neighbors become alive in the next step of the simulation.
# Any other cell dies or stays dead in the next step of the simulation.

import random

# The cells and nextCells are dictionaries for the state of the game.
# Their keys are (x, y) tuples and their values are one of the ALIVE
# or DEAD values.


class GameOfLife:
    """A class to plot out Conway's game of life"""

    def __init__(self, width, height):
        """Initialize the width and length for game"""
        self.width = width
        self.height = height
        self.cells = {}

    def build_dictionary(self):
        """Generate a dictionary with a set of tuples for grid"""
        for x in range(self.width):
            for y in range(self.height):
                if random.randint(0, 1) == 0:
                    # Living cell
                    self.cells[(x, y)] = "O"
                else:
                    # Dead cell
                    self.cells[(x, y)] = " "

    # Build a method to print out the cells as grid
    def print_grid(self):
        """Print grid of current cells"""
        print(self.cells[(0, 0)])
        # Build the grid by printing cells for each row until you hit the width-1
        # add in a space "\n"
        # repeat until count is equal to height-1

    # Build a method to refresh the cells

    # Build a method to check if a cell is alive/dead
    # Accomplish this by checking each neighboring cell
    # top left, top right, top middle
    # middle left, middle, right
    # bottom left, bottom middle, bottom right
    # each alive cell is +=1 to total_neighbors
    # if total_neighbors == 2 or 3 and cell is alive
    #   no change
    # elif total_neighbors == 3 and cell is dead
    #   update value for tuple to alive
    # else
    #   update to dead


game = GameOfLife(width=100, height=30)
game.build_dictionary()
game.print_grid()
