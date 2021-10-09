################################################################################
# File: SpellingBee.py
# Collaborators:
# Brief description of any extensions:
#
#
#
################################################################################

"""
This program provides the basic framework for the SpellingBee program
you need to implement for Project #2. Be sure to change this comment
so that it describes your program rather than this starter file.
"""

from english import ENGLISH_WORDS
from pgl import GWindow, GCompound, GPolygon, GLabel

# ConstantsA
GWINDOW_WIDTH = 1000                # These constants specify the width
GWINDOW_HEIGHT = 300                # and height of the graphics window

BEEHIVE_X = 150                     # These constants specify the center
BEEHIVE_Y = 150                     # of the beehive diagram

HEX_SIDE = 40                       # The length of the hexagon side
HEX_SEP = 76                        # The distance between the hexagon centers
HEX_LABEL_DY = 14                   # Offset of the label baseline from center

WORDLIST_X = 300                    # Starting x coordinate of the wordlist
WORDLIST_Y = 20                     # Baseline of the first word listed
WORDLIST_DX = 120                   # Separation between wordlist columns
WORDLIST_DY = 17                    # Separation between wordlist rows
SCORE_BASELINE = 10                 # Distance from bottom to score baseline
SCORE_WORDLIST_SEP = 20             # Spacing between wordlist and scores

LABEL_FONT = "36px bold 'Helvetica Neue', 'Sans-Serif'"
WORDLIST_FONT = "16px 'Helventica Neue', 'Sans-Serif'"
CENTER_HEX_COLOR = "#FFCC33"
OUTER_HEX_COLOR = "#DDDDDD"
PANGRAM_COLOR = "#52B3DC"


# Main Program

def spelling_bee():
    """
    Main program to run Spelling Bee. All code besides above constants
    should either be defined within this function or within a separate
    helper function.
    """
    puzzle = "DVONCYE"
    print("Words appearing in {}:".format(puzzle))
    list_spelling_bee_words_on_console(puzzle)

def list_spelling_bee_words_on_console(puzzle):
    """
    Displays the Spelling Bee words appearing in the puzzle.
    """
    # You fill in this part for Milestone 1


# Startup Code
if __name__ == '__main__':
    spelling_bee()
