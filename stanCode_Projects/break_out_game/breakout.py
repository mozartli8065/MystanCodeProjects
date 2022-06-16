"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

This is the user side of the breakout game.
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 1000 / 120  # 120 frames per second
NUM_LIVES = 3			 # Number of attempts

lives = NUM_LIVES


def main():
    """
    The ball will move according to the while loop,
    which include the following actions:
    1. Detect object in-front-of direction of ball
    2. Bounce at paddle
    3. Remove bricks
    4. If going out-of bottom of window edge, -1 lives
    5. When bricks or lives reach 0, end while loop
    """
    global lives

    graphics = BreakoutGraphics()
    num_bricks = graphics.num_bricks

    # Add the animation loop here!
    while True:
        pause(FRAME_RATE)

        vx = graphics.get_x_speed()
        vy = graphics.get_y_speed()

        graphics.ball.move(vx, vy)

        # Detecting object in-front-of ball direction
        upper_left_obj = graphics.window.get_object_at(graphics.ball.x, graphics.ball.y)
        upper_right_obj = graphics.window.get_object_at(graphics.ball.x + graphics.ball.width, graphics.ball.y)
        lower_left_obj = graphics.window.get_object_at(graphics.ball.x, graphics.ball.y + graphics.ball.height)
        lower_right_obj = graphics.window.get_object_at(graphics.ball.x + graphics.ball.width, graphics.ball.y +
                                                        graphics.ball.height)

        if upper_left_obj is not None:
            if upper_left_obj is not graphics.paddle:   # When detected bricks
                graphics.window.remove(upper_left_obj)  # Remove the brick
                num_bricks -= 1                         # Decrease brick amount
                vy *= -1                                # Bounce back
                graphics.set_y_speed(vy)                # Communicate the new vy to coder side
            else:
                if vy > 0:                              # When ball hits side of paddle,
                    vy *= -1                            # this will prevent ball stuck inside paddle.
                    graphics.set_y_speed(vy)

        elif upper_right_obj is not None:
            if upper_right_obj is not graphics.paddle:
                graphics.window.remove(upper_right_obj)
                num_bricks -= 1
                vy *= -1
                graphics.set_y_speed(vy)
            else:
                if vy > 0:
                    vy *= -1
                    graphics.set_y_speed(vy)

        elif lower_left_obj is not None:
            if lower_left_obj is not graphics.paddle:
                graphics.window.remove(lower_left_obj)
                num_bricks -= 1
                vy *= -1
                graphics.set_y_speed(vy)
            else:
                if vy > 0:
                    vy *= -1
                    graphics.set_y_speed(vy)

        elif lower_right_obj is not None:
            if lower_right_obj is not graphics.paddle:
                graphics.window.remove(lower_right_obj)
                num_bricks -= 1
                vy *= -1
                graphics.set_y_speed(vy)
            else:
                if vy > 0:
                    vy *= -1
                    graphics.set_y_speed(vy)

        if graphics.ball.x <= 0 or graphics.ball.x + graphics.ball.width >= graphics.window.width:
            vx *= -1                        # When ball hits the side walls, bounce back
            graphics.set_x_speed(vx)

        if graphics.ball.y <= 0:            # When ball hits the celling, bounce back
            vy *= -1
            graphics.set_y_speed(vy)

        if graphics.ball.y + graphics.ball.height >= graphics.window.height:    # When ball falls under window bottom
            lives -= 1
            graphics.re_position_ball()     # Reset the ball at initial position to start the next round
            if lives == 0:                  # When used up all lives
                break                       # End while loop

        if num_bricks == 0:                 # When clearing all bricks
            break                           # End while loop
    graphics.game_over(lives, num_bricks)   # Return the different outcomes basing on num of lives and bricks


if __name__ == '__main__':
    main()
