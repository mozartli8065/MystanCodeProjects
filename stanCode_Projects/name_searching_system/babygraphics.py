"""
File: babygraphics.py
Name: 李汝民
--------------------------------
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950,
         1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index where the current year is in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                            with the current year.
    """
    which_year = 0

    for year in YEARS:
        if year == year_index:
            break
        else:
            which_year += 1

    width_bt_lines = (width - GRAPH_MARGIN_SIZE * 2) / len(YEARS)

    return GRAPH_MARGIN_SIZE + width_bt_lines * which_year


def draw_fixed_lines(canvas):
    """
    Draws the fixed background lines on the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
    """
    canvas.delete('all')  # delete all existing lines from the canvas

    # ----- Write your code below this line ----- #

    # Draw the two (upper and lower) lines
    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, CANVAS_WIDTH - GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE)
    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE, CANVAS_WIDTH - GRAPH_MARGIN_SIZE,
                       CANVAS_HEIGHT - GRAPH_MARGIN_SIZE)

    # Draw the vertical lines
    for year in YEARS:
        canvas.create_line(get_x_coordinate(CANVAS_WIDTH, year), 0,
                           get_x_coordinate(CANVAS_WIDTH, year), CANVAS_HEIGHT)

        text_x = get_x_coordinate(CANVAS_WIDTH, year) + TEXT_DX
        text_y = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE + TEXT_DX

        canvas.create_text(text_x, text_y, text=year, anchor=tkinter.NW)


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)  # draw the fixed background grid

    # ----- Write your code below this line ----- #

    color_index = -1

    for name in lookup_names:
        old_d_name = name_data[name]
        color_index += 1                                # Change line color

        for ele in YEARS:
            if str(ele) not in old_d_name:
                old_d_name[str(ele)] = str(MAX_RANK)    # Assign MAX_RANK to year exceeding #1000 in rank

        d_name = {}

        # Find corresponding ranks for each year
        for ele in YEARS:
            for year, rank in old_d_name.items():
                if str(ele) == year:
                    d_name[str(ele)] = rank

        # Draw lines to connect each year/rank data, put labels aside each data point
        previous_x = 0
        previous_y = 0

        for year, rank in d_name.items():
            year_index = int(year)

            text_x = get_x_coordinate(CANVAS_WIDTH, year_index) + TEXT_DX
            text_y = GRAPH_MARGIN_SIZE + int(int(rank) * ((CANVAS_HEIGHT - GRAPH_MARGIN_SIZE * 2) / MAX_RANK)) - TEXT_DX

            if rank == '1000':
                text_label = name, '*'
            else:
                text_label = name, rank

            canvas.create_text(text_x, text_y, text=text_label, anchor=tkinter.SW, fill=COLORS[color_index])

            current_x = get_x_coordinate(CANVAS_WIDTH, year_index)
            current_y = GRAPH_MARGIN_SIZE + int(int(rank) * ((CANVAS_HEIGHT - GRAPH_MARGIN_SIZE * 2) / MAX_RANK))

            if year_index == 1900:  # Not draw line for first datapoint
                pass
            else:
                canvas.create_line(previous_x, previous_y, current_x, current_y, width=LINE_WIDTH,
                                   fill=COLORS[color_index])

            previous_x = current_x
            previous_y = current_y

        if color_index == 3:        # Reset color rotation
            color_index = -1


# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
