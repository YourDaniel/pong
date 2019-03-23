from tkinter import *
from random import randint
root = Tk()
canvas_w = 1024
canvas_h = 768
c = Canvas(root, bg='black', width=canvas_w, height=canvas_h)
#border = c.create_rectangle(20, 20, canvas_w-17, canvas_h-17, fill='black', width=5, outline='white')

'''PAD PARAMETERS'''
pad_h = 70
pad_w = 20
pad_start = (80, 40)
pad_1 = c.create_rectangle(pad_start, pad_start[0]+pad_w, pad_start[1] + pad_h, fill='white')

'''BALL PARAMETERS'''
ball_start = (400, 500)
ball_size = 16
ball = c.create_rectangle(ball_start, ball_start[0] + ball_size, ball_start[1] + ball_size, fill='white')
game_speed = 40
delta_x, delta_y = -10, -10


def move_pad_1(event):
    if event.y - 60 > 0 and event.y + 30 < canvas_h:
        c.coords(pad_1, pad_start[0], event.y - pad_h/2, pad_start[0]+pad_w, event.y + pad_h/2)


def mouse_position(event):
    root.title('Pong {}x{}'.format(event.x, event.y))


def show_data():
    bc = c.coords(ball)[1]+ball_size/2
    pc = c.coords(pad_1)[1]+pad_h/2
    root.title('Ball Center {} - Pad Center {}'.format(bc, pc))
    root.after(game_speed, show_data)


def move_ball():
    global delta_x, delta_y

    # Walls collision
    if c.coords(ball)[2] > canvas_w or c.coords(ball)[0] < 0:
        #delta_x = -delta_x
        delta_x = -randint(0, 10)
        c.itemconfig(ball, fill="red")
    if c.coords(ball)[3] > canvas_h or c.coords(ball)[1] < 0:
        delta_y = -delta_y
        c.itemconfig(ball, fill="green")
    # Pad collision
    if (c.coords(ball)[0] < c.coords(pad_1)[2]) and (abs((c.coords(ball)[1]+8) - (c.coords(pad_1)[1]+30)) < (pad_h/2)+7):
        delta_x = -delta_x
        c.itemconfig(ball, fill="blue")
        #print('Hit')

    c.move(ball, delta_x, delta_y)
    root.after(game_speed, move_ball)



#root.bind('<Motion>', mouse_position)
c.bind('<Motion>', move_pad_1)
#canvas.bind('<Right>', move_b)

show_data()
move_ball()
c.pack()
root.mainloop()
