"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

This is the user side of the special version of breakout game, which adds a 'cannon' to the paddle that the user can
use bounce the ball with.
"""

from campy.gui.events.timer import pause
from breakoutgraphics_ext import BreakoutGraphics


FRAME_RATE = 1000 / 120  # 120 frames per second
NUM_LIVES = 3			 # Number of attempts

lives = NUM_LIVES


def main():
    """
    The ball and cannon will move according to the while loop,
    which include the following actions:
    1. Detect object in-front-of direction of ball
    2. Bounce at paddle
    3. Bounce at hitting cannon
    4. Remove bricks
    5. Count bricks removed
    6. Count HP left
    7. If going out-of bottom of window edge, -1 lives
    8. When bricks or lives reach 0, end while loop
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

        # Make cannon move up-and-down
        graphics.cannon.move(graphics.cannon_dx, graphics.cannon_dy)
        if graphics.cannon.y <= graphics.window.height/2.5:
            graphics.cannon_dy *= -1
        elif graphics.cannon.y >= graphics.paddle.y - graphics.cannon.height:
            if graphics.cannon_dy > 0:
                graphics.cannon_dy *= -1

        # Detecting object in-front-of ball direction
        for ball_x in range(int(graphics.ball.x), int(graphics.ball.width)+1, int(graphics.ball.width)):
            check = 0
            for ball_y in range(int(graphics.ball.y), int(graphics.ball.height)+1, int(graphics.ball.height)):
                obj = graphics.window.get_object_at(ball_x, ball_y)
                if obj is not None:
                    if obj is graphics.score_board:
                        pass
                    elif graphics.check_image(obj):  # Prevent HP bar being removed
                        pass
                    elif obj is graphics.cannon:  # Cannon bounces the ball
                        if vy > 0:
                            vy *= -1
                            graphics.set_y_speed(vy)
                    elif obj is not graphics.paddle:  # Remove bricks
                        graphics.window.remove(obj)
                        num_bricks -= 1
                        graphics.num_bricks -= 1
                        graphics.score_board.text = 'Bricks left: ' + str(graphics.num_bricks)
                        vy *= -1
                        graphics.set_y_speed(vy)
                    else:  # Paddle bounces ball
                        if vy > 0:
                            vy *= -1
                            graphics.set_y_speed(vy)
                    check = 1
                    break
            if check == 1:
                break

        upper_left_obj = graphics.window.get_object_at(graphics.ball.x, graphics.ball.y)
        upper_right_obj = graphics.window.get_object_at(graphics.ball.x + graphics.ball.width, graphics.ball.y)
        lower_left_obj = graphics.window.get_object_at(graphics.ball.x, graphics.ball.y + graphics.ball.height)
        lower_right_obj = graphics.window.get_object_at(graphics.ball.x + graphics.ball.width, graphics.ball.y +
                                                        graphics.ball.height)

        if upper_left_obj is not None:
            if upper_left_obj is graphics.score_board:
                pass
            elif graphics.check_image(upper_left_obj):        # Prevent HP bar being removed
                pass
            elif upper_left_obj is graphics.cannon:         # Cannon bounces the ball
                if vy > 0:
                    vy *= -1
                    graphics.set_y_speed(vy)
            elif upper_left_obj is not graphics.paddle:     # Remove bricks
                graphics.window.remove(upper_left_obj)
                num_bricks -= 1
                graphics.num_bricks -= 1
                graphics.score_board.text = 'Bricks left: ' + str(graphics.num_bricks)
                vy *= -1
                graphics.set_y_speed(vy)
            else:                                           # Paddle bounces ball
                if vy > 0:
                    vy *= -1
                    graphics.set_y_speed(vy)

        elif upper_right_obj is not None:
            if upper_right_obj is graphics.score_board:
                pass
            elif graphics.check_image(upper_right_obj):
                pass
            elif upper_right_obj is graphics.cannon:
                if vy > 0:
                    vy *= -1
                    graphics.set_y_speed(vy)
            elif upper_right_obj is not graphics.paddle:
                graphics.window.remove(upper_right_obj)
                num_bricks -= 1
                graphics.num_bricks -= 1
                graphics.score_board.text = 'Bricks left: ' + str(graphics.num_bricks)
                vy *= -1
                graphics.set_y_speed(vy)
            else:
                if vy > 0:
                    vy *= -1
                    graphics.set_y_speed(vy)

        elif lower_left_obj is not None:
            if lower_left_obj is graphics.score_board:
                pass
            elif graphics.check_image(lower_left_obj):
                pass
            elif lower_left_obj is graphics.cannon:
                if vy > 0:
                    vy *= -1
                    graphics.set_y_speed(vy)
            elif lower_left_obj is not graphics.paddle:
                graphics.window.remove(lower_left_obj)
                num_bricks -= 1
                graphics.num_bricks -= 1
                graphics.score_board.text = 'Bricks left: ' + str(graphics.num_bricks)
                vy *= -1
                graphics.set_y_speed(vy)
            else:
                if vy > 0:
                    vy *= -1
                    graphics.set_y_speed(vy)

        elif lower_right_obj is not None:
            if lower_right_obj is graphics.score_board:
                pass
            elif graphics.check_image(lower_right_obj):
                pass
            elif lower_right_obj is graphics.cannon:
                if vy > 0:
                    vy *= -1
                    graphics.set_y_speed(vy)
            elif lower_right_obj is not graphics.paddle:
                graphics.window.remove(lower_right_obj)
                num_bricks -= 1
                graphics.num_bricks -= 1
                graphics.score_board.text = 'Bricks left: ' + str(graphics.num_bricks)
                vy *= -1
                graphics.set_y_speed(vy)
            else:
                if vy > 0:
                    vy *= -1
                    graphics.set_y_speed(vy)

        if graphics.ball.x <= 0 or graphics.ball.x + graphics.ball.width >= graphics.window.width:
            vx *= -1                                # When ball hits the side walls, bounce back
            graphics.set_x_speed(vx)

        if graphics.ball.y <= 0:                    # When ball hits the celling, bounce back
            vy *= -1
            graphics.set_y_speed(vy)

        if graphics.ball.y + graphics.ball.height >= graphics.window.height:
            lives -= 1                              # When ball falls under window bottom
            remove_heart = graphics.window.get_object_at(x=graphics.window.width - graphics.heart_img.width*lives,
                                                         y=graphics.window.height)
            graphics.window.remove(remove_heart)    # Removes one HP
            graphics.re_position_ball()             # Reset the ball at initial position to start the next round
            if lives == 0:
                break

        if num_bricks % 10 == 0 and num_bricks != 100:
            vy *= 1.001                             # Ball goes faster every 10 bricks removed
            graphics.set_y_speed(vy)

        if num_bricks == 0:                         # When clearing all bricks
            break
    graphics.game_over(lives, num_bricks)           # Return the different outcomes basing on num of lives and bricks


if __name__ == '__main__':
    main()
