"""Simple game"""
import tkinter   # graphic library
import random

# constants
WIDTH = 640
HEIGHT = 480
BG_COLOR = "white"
COLORS = ['green', 'yellow', 'pink']
# class
class Ball:

    def __init__(self, x, y, r, color, dx = 0, dy = 0):
        self.x = x
        self.y = y
        self.r = r
        self.color = color
        self.dx = dx
        self.dy = dy
        self.score = 0

    def draw(self):
        # create simple oval
        canvas.create_oval(self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r, fill = self.color)

    def hide(self):
        # create simple oval
        canvas.create_oval(self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r, fill = BG_COLOR, outline = BG_COLOR)

    def is_colisiun(self, ball):
        a = abs(self.x + self.dx - ball.x)
        b = abs(self.y + self.dy - ball.y)
        return (a*a + b*b)**0.5 <= self.r + ball.r

    def move(self):
        # collidium
        if (self.x + self.r + self.dx >=WIDTH) or (self.x - self.r + self.dx <= 0):
            self.dx= -self.dx
        if (self.y + self.r + self.dy >=HEIGHT) or (self.y - self.r + self.dy <=0):
            self.dy = -self.dy
        # ball colosium
        for ball in balls:
            if self.is_colisiun(ball):
                ball.hide()
                balls.remove(ball)
                self.r += 1
                self.score +=1
                self.dx = -self.dx
                self.dy = -self.dy
        # bad ball colisium
        for b_ball in bad_balls:
            if self.is_colisiun(b_ball):
                self.dx = 0
                self.dy = 0
                fail()
        self.hide()
        self.x += self.dx
        self.y += self.dy
        self.draw()

# mouse click events
def mouse_click(event):
    global main_ball
    if event.num == 1:
        if 'main_ball' not in globals():
            main_ball = Ball(event.x, event.y, 25, "blue", 1, 1)
            main_ball.draw()
        else: #turn left
            if main_ball.dx * main_ball.dy > 0:
                main_ball.dy = -main_ball.dy
            else:
                main_ball.dx = -main_ball.dx
    elif event.num == 3: # turn right
        if main_ball.dx * main_ball.dy > 0:
            main_ball.dx = -main_ball.dx
        else:
            main_ball.dy = -main_ball.dy

def create_ball(n):
    lst = []
    while len(lst) <= n:
        ball = Ball(random.choice(range(15, WIDTH - 15)), random.choice(range(15, HEIGHT - 15)),
                    random.choice(range(10, 15)), random.choice(COLORS))
        lst.append(ball)
        ball.draw()
    return lst

def create_bad_balls(n):
    lst = []
    while len(lst) <= n:
        ball = Ball(random.choice(range(15, WIDTH - 15)), random.choice(range(15, HEIGHT - 15)),
                    random.choice(range(10, 15)), "red")
        lst.append(ball)
        ball.draw()
    return lst

# main game loop
def main():
    if 'main_ball' in globals():
        main_ball.move()
        if len(balls) == 0:
            canvas.create_text(WIDTH/2-1, HEIGHT/2-1,
                                text = "YOU WON!!!\nYOUR SCORE = " + str(main_ball.score),
                                font = "Verdana 20", fill = "blue")
            main_ball.hide()
    root.after(5, main)

def fail():
    for b in balls:
        b.hide()
    for bb in bad_balls:
        bb.hide()
    main_ball.hide()
    canvas.create_text(WIDTH / 2 - 1, HEIGHT / 2 - 1, text="YOU FAIL!!!\nYOUR SCORE = " + str(main_ball.score), font="Verdana 20", fill="blue")

root = tkinter.Tk()
root.title("B0lls")
canvas = tkinter.Canvas(root, width = WIDTH, height = HEIGHT, bg = BG_COLOR)
canvas.pack()
canvas.bind("<Button-1>", mouse_click)
canvas.bind("<Button-3>", mouse_click)
balls = create_ball(random.randint(4, 8))
bad_balls = create_bad_balls(random.randint(1, 4))
main()
root.mainloop()