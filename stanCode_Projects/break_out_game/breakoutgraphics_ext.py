"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

This is the coder side of the special version of breakout game, which adds a 'cannon' to the paddle that the user can
use bounce the ball with.

The code will create the following elements of the game:
1. Window
2. Paddle
3. Cannon
4. Ball
5. Bricks
6. Score board
7. HP bar
The code also includes the relevant functions to operate the game.
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
from campy.graphics.gimage import GImage
import random

BRICK_SPACING = 5  # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40  # Height of a brick (in pixels)
BRICK_HEIGHT = 15  # Height of a brick (in pixels)
BRICK_ROWS = 10  # Number of rows of bricks
BRICK_COLS = 10  # Number of columns of bricks
BRICK_OFFSET = 50  # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10  # Radius of the ball (in pixels)
PADDLE_WIDTH = 75  # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15  # Height of the paddle (in pixels)
PADDLE_OFFSET = 50  # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7  # Initial vertical speed for the ball
MAX_X_SPEED = 5  # Maximum initial horizontal speed for the ball


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title=
                 'Breakout plus: I got a cannon!'):
        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle
        self.paddle = GRect(paddle_width, paddle_height)
        self.paddle.filled = True
        self.window.add(self.paddle, x=(self.window.width - self.paddle.width) / 2, y=self.window.height -
                                                                                      paddle_offset - paddle_height)

        # Create cannon
        self.cannon = GRect(paddle_width/6, paddle_height)
        self.cannon.filled = True
        self.window.add(self.cannon, x=(self.window.width - self.cannon.width) / 2, y=self.window.height -
                                                            paddle_offset - paddle_height - self.cannon.height)

        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius * 2, ball_radius * 2)
        self.ball.filled = True
        self.window.add(self.ball, x=(self.window.width - self.ball.width) / 2, y=(self.window.height -
                                                                                   self.ball.height) / 2)

        # Default initial velocity for the ball
        self.__dx = 0
        self.__dy = 0

        # Default initial velocity for the cannon
        self.cannon_dx = 0
        self.cannon_dy = 0

        # Initialize our mouse listeners
        onmouseclicked(self.launch_ball)
        onmousemoved(self.change_position)

        # Draw bricks
        for i in range(1, brick_rows + 1):
            for j in range(brick_cols):
                self.bricks = GRect(brick_width, brick_height)
                self.bricks.filled = True

                if i % 10 == 1 or i % 10 == 2:
                    self.bricks.fill_color = 'red'
                    self.bricks.color = 'red'
                elif i % 10 == 3 or i % 10 == 4:
                    self.bricks.fill_color = 'orange'
                    self.bricks.color = 'orange'
                elif i % 10 == 5 or i % 10 == 6:
                    self.bricks.fill_color = 'yellow'
                    self.bricks.color = 'yellow'
                elif i % 10 == 7 or i % 10 == 8:
                    self.bricks.fill_color = 'green'
                    self.bricks.color = 'green'
                elif i % 10 == 9 or i % 10 == 0:
                    self.bricks.fill_color = 'blue'
                    self.bricks.color = 'blue'

                self.window.add(self.bricks, x=j * self.bricks.width + j * brick_spacing,
                                y=brick_offset + (i - 1) * self.bricks.height + (i - 1) * brick_spacing)

        # Score board
        self.num_bricks = brick_rows * brick_cols
        self.score_board = GLabel(f'Bricks left: {self.num_bricks}')
        self.score_board.font = '-20'
        self.window.add(self.score_board, x=0, y=window_height)

        # HP bar
        for i in range(1, 4):
            self.heart_img = GImage('hearts.jpg')
            self.window.add(self.heart_img, x=self.window.width - self.heart_img.width*i, y=self.window.height -
                                                                                      self.heart_img.height)

    def change_position(self, event):
        """
        Create paddle centering at mouse.x position
        :param event: Mouse moves
        :return: Paddle position
        """
        if event.x + self.paddle.width / 2 > self.window.width:
            pass
        elif event.x - self.paddle.width / 2 < 0:
            pass
        else:
            self.window.add(self.paddle, x=event.x - self.paddle.width / 2, y=self.paddle.y)
            self.window.add(self.cannon, x=event.x - self.cannon.width / 2, y=self.cannon.y)

    def launch_ball(self, event):
        """
        Start the game
        :param event: Mouse click position
        :return: Initial direction and velocity of ball
        """
        if event.x > 0 and self.__dx == 0:
            self.__dy = INITIAL_Y_SPEED
            self.__dx = random.randint(1, MAX_X_SPEED)
            if random.random() > 0.5:
                self.__dx *= -1
        if event.x > 0 and self.cannon_dx == 0:
            self.cannon_dx = 0
            self.cannon_dy = -1

    def re_position_ball(self):
        """
        Reset the ball at initial position to start another round
        """
        self.ball.x = (self.window.width - self.ball.width) / 2
        self.ball.y = (self.window.height - self.ball.height) / 2
        self.__dx = 0
        self.__dy = 0

    def game_over(self, lives, num_bricks):
        """
        Show label when game-end condition being met
        :param lives: Remaining rounds
        :param num_bricks: Remaining bricks
        :return: GLabel 'Game Over!!!' or 'You Win!!!'
        """
        if lives == 0:
            self.window.remove(self.ball)
            self.paddle.filled = False
            self.paddle.color = 'white'
            self.cannon.filled = False
            self.cannon.color = 'white'
            label = GLabel('Game Over!!!')
            label.font = '-40'
            self.window.add(label, x=self.window.width / 4,
                            y=self.window.height / 1.5)
        elif num_bricks == 0:
            self.window.remove(self.ball)
            self.paddle.filled = False
            self.paddle.color = 'white'
            self.cannon.filled = False
            self.cannon.color = 'white'
            label = GLabel('You Win!!!')
            label.font = '-40'
            self.window.add(label, x=self.window.width / 3.5,
                            y=self.window.height / 2)

    # Setter & Getter
    def get_x_speed(self):
        """
        :return: strict private __dx to user
        """
        return self.__dx

    def get_y_speed(self):
        """
        :return: strict private __dy to user
        """
        return self.__dy

    def set_x_speed(self, x):
        """
        :param x: ball x velocity from user side
        :return: update __dx
        """
        self.__dx = x

    def set_y_speed(self, y):
        """
        :param y: ball y velocity from user side
        :return: update __dy
        """
        self.__dy = y

    def check_image(self, image):
        """
        This function decides whether the ball hits the HP bar
        :param image: get.object from user side
        :return: True if object is HP bar
        """
        if image.height == self.heart_img.height:
            return True
