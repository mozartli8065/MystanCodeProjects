"""
File: sierpinski.py
Name: 李汝民
---------------------------
This file recursively prints the Sierpinski triangle on GWindow.
The Sierpinski triangle is a fractal described in 1915 by Waclaw Sierpinski.
It is a self similar structure that occurs at different levels of iterations.
"""

from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GLine
from campy.gui.events.timer import pause

# Constants
ORDER = 6                  # Controls the order of Sierpinski Triangle
LENGTH = 600               # The length of order 1 Sierpinski Triangle
UPPER_LEFT_X = 150		   # The upper left x coordinate of order 1 Sierpinski Triangle
UPPER_LEFT_Y = 100         # The upper left y coordinate of order 1 Sierpinski Triangle
WINDOW_WIDTH = 950         # The width of the GWindow
WINDOW_HEIGHT = 700        # The height of the GWindow

# Global Variable
window = GWindow(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)  # The canvas to draw Sierpinski Triangle


def main():
	"""
	TODO: Draw a sierpinski patter using recursive stops.
	"""
	sierpinski_triangle(ORDER, LENGTH, UPPER_LEFT_X, UPPER_LEFT_Y)


def sierpinski_triangle(order, length, upper_left_x, upper_left_y):
	"""
	Input:
		order (int): levels of recursion before reaching base case.
		length (int): length of one side of the first triangle.
		upper_left_x (int): starting x-coordinate of the first triangle.
		upper_left_y (int): starting y-coordinate of the first triangle.
	"""
	if order == 0:
		pass
	else:
		# The top side of the triangle
		triangle_top = GLine(upper_left_x, upper_left_y, upper_left_x+length, upper_left_y)

		# The left side of the triangle.
		triangle_left = GLine(upper_left_x, upper_left_y, upper_left_x+length*0.5, upper_left_y+length*0.866)

		# The right side of the triangle.
		triangle_right = GLine(upper_left_x+length, upper_left_y, upper_left_x+length*0.5, upper_left_y+length*0.866)

		# Add the lines of the triangle to the window.
		window.add(triangle_top)
		window.add(triangle_left)
		window.add(triangle_right)

		pause(30)

		# Run the top left side smaller triangle recursion.
		sierpinski_triangle(order-1, length*0.5, upper_left_x, upper_left_y)

		# Succeed the last level of recursion from above, draw top right side smaller triangle.
		sierpinski_triangle(order-1, length*0.5, upper_left_x+length*0.5, upper_left_y)

		# Succeed the last level of recursion from above, draw down side smaller triangle.
		sierpinski_triangle(order-1, length*0.5, upper_left_x+length*0.5*0.5, upper_left_y+length*0.5*0.866)


if __name__ == '__main__':
	main()
