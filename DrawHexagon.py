# File: DrawHexagon.py

from pgl import GWindow, GPolygon

# Constants

GWINDOW_WIDTH = 500
GWINDOW_HEIGHT = 200
HEXAGON_SIDE = 50

def draw_hexagon():
    """
    Draws a hexagon at the center of the graphics window.
    """
    gw = GWindow(GWINDOW_WIDTH, GWINDOW_HEIGHT)
    gw.add(create_hexagon(HEXAGON_SIDE), gw.get_width() / 2, gw.get_height() / 2)

def create_hexagon(side):
    """
    Creates a GPolygon representing a regular hexagon with the reference
    point at the center.
    """
    hex = GPolygon()
    hex.add_vertex(-side, 0)
    angle = 60
    for i in range(6):
        hex.add_polar_edge(side, angle)
        angle -= 60
    return hex

if __name__ == "__main__":
    draw_hexagon()
