# Relatively prettier and more reusable
import tkinter as tk
import fsa

canvas_width = 600
canvas_height = 1000

offset = 50
label_offset = -10

diameter = 40
radius = diameter / 2
line_length = 200 - radius

pos_x = offset
pos_y = offset

root = tk.Tk()
canvas = tk.Canvas(root, width=canvas_width, height=canvas_height, borderwidth=0, highlightthickness=0, bg="white")


def start(start_state, states, transitions):
    global canvas_width
    global canvas_height

    global offset
    global label_offset

    global diameter
    global radius
    global line_length

    global pos_x
    global pos_y

    global root
    global canvas

    # draw starting line
    draw_vertical_line(pos_x + radius, pos_y - offset / 2, pos_x + radius, pos_y, ' ')

    # draw state transitions
    draw_semi_circle_right(pos_x, pos_y, 'x')
    draw_vertical_line(pos_x + radius, pos_y + diameter, pos_x + radius, pos_y + line_length, 'y')
    pos_y = pos_y + line_length
    draw_vertical_line(pos_x + radius, pos_y + diameter, pos_x + radius, pos_y + line_length, 'x')
    pos_y = pos_y + line_length
    draw_semi_circle_right(pos_x, pos_y, 'x')
    draw_vertical_line(pos_x + radius, pos_y + diameter, pos_x + radius, pos_y + line_length, 'y')
    pos_y = pos_y + line_length
    draw_semi_circle_right(pos_x, pos_y, 'x')
    draw_vertical_line(pos_x + radius, pos_y + diameter, pos_x + radius, pos_y + line_length, 'z')
    pos_y = pos_y + line_length
    draw_semi_circle_right(pos_x, pos_y, 'x')

    draw_prev_transition(pos_x, pos_y + radius, 4, 1, 'a')

    # go back to the start
    pos_y = offset

    # draw states
    draw_state(pos_x, pos_y, pos_x + diameter, pos_y + diameter, '0')
    pos_y = pos_y + line_length
    draw_accept_state(pos_x, pos_y, pos_x + diameter, pos_y + diameter, '1')
    pos_y = pos_y + line_length
    draw_state(pos_x, pos_y, pos_x + diameter, pos_y + diameter, '2')
    pos_y = pos_y + line_length
    draw_accept_state(pos_x, pos_y, pos_x + diameter, pos_y + diameter, '3')
    pos_y = pos_y + line_length
    draw_state(pos_x, pos_y, pos_x + diameter, pos_y + diameter, '4')

    root.wm_title("FSA")
    root.mainloop()


def average_pos(p1, p2):
    sum = p1 + p2
    avg = sum / 2
    return avg


def draw_state(x1, y1, x2, y2, label):
    cirl = canvas.create_oval(x1, y1, x2, y2)
    cir2 = canvas.create_oval(x1 + 1, y1 + 1, x2 - 1, y2 - 1, fill="white")
    canvas.pack()
    text = canvas.create_text(x1 + radius, y1 + radius, text=label)


def draw_accept_state(x1, y1, x2, y2, label):
    cirl = canvas.create_oval(x1, y1, x2, y2)
    cir3 = canvas.create_oval(x1 + 5, y1 + 5, x2 - 5, y2 - 5)
    cir2 = canvas.create_oval(x1 + 1, y1 + 1, x2 - 1, y2 - 1, fill="white")
    canvas.pack()
    text = canvas.create_text(x1 + radius, y1 + radius, text=label)


def draw_vertical_line(x1, y1, x2, y2, label):
    avg_y = average_pos(y1, y2)
    line = canvas.create_line(x1, y1, x2, y2, width=2, arrow=tk.LAST)
    text = canvas.create_text(x1 + label_offset, avg_y, text=label)


def draw_semi_circle_right(x1, y1, label):
    x2 = x1 + diameter + radius
    y2 = y1 + diameter
    x1 = x1 + radius

    cirl = canvas.create_oval(x1, y1, x2, y2)
    text = canvas.create_text(x2 - label_offset, y2 - radius, text=label)
    line = canvas.create_line(x2, y2 - radius, x2, y2 - 1, width=2, arrow=tk.LAST)


def draw_prev_transition(x1, y1, state1, state2, label):
    diff = state2 - state1
    y2 = y1 + (line_length * diff)
    x2 = x1
    avg_y = average_pos(y1, y2)
    line1 = canvas.create_line(x1, y1, x1 - 10, y1, width=2)
    line2 = canvas.create_line(x1 - 10, y1, x2 - 10, y2, width=2)
    line3 = canvas.create_line(x2 - 10, y2, x1, y2, width=2, arrow=tk.LAST)
    text = canvas.create_text(x1 - 10 + label_offset, avg_y, text=label)
