# Relatively prettier and more reusable
import tkinter as tk


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
    cir2 = canvas.create_oval(x1 + 1, y1 + 1, x2 - 1, y2 - 1, fill="white")
    cir3 = canvas.create_oval(x1 + 5, y1 + 5, x2 - 5, y2 - 5)
    canvas.pack()
    text = canvas.create_text(x1 + radius, y1 + radius, text=label)


def draw_vertical_line(x1, y1, x2, y2, label):
    avg_y = average_pos(y1, y2)
    line = canvas.create_line(x1, y1, x2, y2, width=2, arrow=tk.LAST)
    text = canvas.create_text(x1 + label_offset, avg_y, text=label)


def draw_horizontal_line(x1, y1, x2, y2, label):
    avg_x = average_pos(x1, x2)
    line = canvas.create_line(x1, y1, x2, y2, width=2, arrow=tk.LAST)
    text = canvas.create_text(avg_x, y1 + label_offset, text=label)


def draw_semi_circle(x1, y1, x2, y2, label):
    cirl = canvas.create_oval(x1, y1, x2, y2)
    text = canvas.create_text(x1 + label_offset, y1 + radius, text=label)
    line = canvas.create_line(x1, y1 + radius, x1, y1 - 1, width=2, arrow=tk.LAST)


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

# draw starting line
draw_vertical_line(pos_x + radius, pos_y - offset / 2, pos_x + radius, pos_y, '')

draw_vertical_line(pos_x + radius, pos_y + diameter, pos_x + radius, pos_x + line_length, 'a')  # Left to right
draw_horizontal_line(pos_x + line_length, pos_y + radius, pos_x + diameter, pos_y + radius, 'b')

draw_semi_circle(pos_x - radius, pos_y, pos_x + radius, pos_y + diameter, 'x')

draw_state(pos_x, pos_y, pos_x + diameter, pos_y + diameter, '0')
pos_y = pos_y + line_length
draw_accept_state(pos_x, pos_y, pos_x + diameter, pos_y + diameter, '1')
pos_y = pos_y - line_length
pos_x = pos_x + line_length
draw_state(pos_x, pos_y, pos_x + diameter, pos_y + diameter, '3')

root.wm_title("Circles, lines, and Arcs")
root.mainloop()
