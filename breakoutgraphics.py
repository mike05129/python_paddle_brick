"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

YOUR DESCRIPTION HERE
"""
from turtle import color
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

# Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_SPACING = 5
BRICK_WIDTH = 40       # Height of a brick (in pixels)
BRICK_HEIGHT = 15      # Height of a brick (in pixels)
BRICK_ROWS = 10        # Number of rows of bricks
BRICK_COLS = 10        # Number of columns of bricks
# Vertical offset of the topmost brick from the window top (in pixels)
BRICK_OFFSET = 50
BALL_RADIUS = 10       # Radius of the ball (in pixels)
PADDLE_WIDTH = 75      # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels)
# Vertical offset of the paddle from the window bottom (in pixels)
PADDLE_OFFSET = 50
INITIAL_Y_SPEED = 7    # Initial vertical speed for the ball
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):

        # Create a graphical window, with some extra space
        window_width = brick_cols * \
            (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * \
            (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width,
                              height=window_height, title=title)

        # Create a paddle
        self.paddle = GRect(paddle_width, paddle_height)
        self.paddle.x = (window_width - paddle_width)//2
        self.paddle.y = window_height - paddle_offset - paddle_height
        self.paddle.filled = True
        self.window.add(self.paddle)

        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius * 2, ball_radius*2)
        self.ball_init_x = window_width // 2 - ball_radius
        self.ball_init_y = window_height // 2 - ball_radius
        self.ball.x = self.ball_init_x
        self.ball.y = self.ball_init_y
        self.ball.filled = True
        self.window.add(self.ball)

        # Default initial velocity for the ball
        self.__dx = 0
        self.__dy = 0
        self.go = False
        self.bricks_amount = brick_rows*brick_cols
        

        # Initialize our mouse listeners

        onmousemoved(self.paddle_move)
        onmouseclicked(self.start)

        # Draw bricks
        color = ['red', 'orange', 'yellow', 'green', 'blue']
        for i in range(brick_rows):
            if i < 11:
                brick_color = color[i//2]
            else:
                brick_color = color[0]  # Revised next time
            for j in range(brick_cols):
                brick = GRect(brick_width, brick_height)
                brick.filled = True
                brick.x = j * (brick_width + brick_spacing)
                brick.y = i * (brick_height + brick_spacing)+brick_offset
                brick.fill_color = brick_color
                self.window.add(brick)

    def paddle_move(self, event):
        if self.paddle.width/2 < event.x < self.window.width - self.paddle.width / 2:
            self.paddle.x = event.x - self.paddle.width // 2
        elif event.x < self.paddle.width / 2:
            self.paddle.x = 0
        else:
            self.paddle.x = self.window.width - self.paddle.width
   
    def start(self, event):
        if not self.go:
            self.go = True            
            self.__dx=random.randint(1,MAX_X_SPEED)
            self.__dy = INITIAL_Y_SPEED
            if random.random() > 0.5:
                self.__dx = -self.__dx
                
                
    def detect_hits(self):
        for corner_x in range(self.ball.x, self.ball.x + self.ball.width + 1, self.ball.width):
            for corner_y in range(self.ball.y, self.ball.y + self.ball.height + 1, self.ball.height):
                object_det = self.window.get_object_at(corner_x, corner_y)
                if object_det:
                    if object_det is not self.paddle:
                        self.window.remove(object_det)
                        self.bricks_amount -=1
                        self.__dy *= -1
                        return
                    elif object_det is self.paddle:
                        self.__dy *= -1 
                        return
    
    def reset(self):
        self.ball.x = self.ball_init_x
        self.ball.y = self.ball_init_y
        self.go = False
 
    def get_dx(self):
        return self.__dx
    

    def get_dy(self):
        return self.__dy
       
    def change_x_direction(self):
        self.__dx *= -1
        
    def change_y_direction(self):
        self.__dy *= -1