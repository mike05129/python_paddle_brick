"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 1000 / 120  # 120 frames per second
NUM_LIVES = 3			 # Number of attempts


def main():
    graphics = BreakoutGraphics()

    # Add the animation loop here!
    while 1:
        if graphics.go:
            if graphics.bricks_amount > 0:
                
                graphics.ball.move(graphics.get_dx(), graphics.get_dy()) #Start move the ball 

                if graphics.ball.x < 0 or graphics.ball.x + graphics.ball.width > graphics.window.width:
                    graphics.change_x_direction()

                graphics.detect_hits() #Detect if ball hits brick

                if graphics.ball.y + graphics.ball.height > graphics.window.height:
                    graphics.reset()
                                     
        pause(FRAME_RATE)


if __name__ == '__main__':
    main()
