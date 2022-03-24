# # Relatively prettier and more reusable
# import tkinter as tk
#
#
# def draw_cir(x1, y1, x2, y2, label):
#     cirl = canvas.create_oval(x1, y1, x2, y2)
#     cir2 = canvas.create_oval(x1 + 1, y1 + 1, x2 - 1, y2 - 1, fill="white")
#     canvas.pack()
#     text = canvas.create_text(x1 / 2, y1 / 2, test=label)
#
#
# def draw_line(x1, y1, x2, y2):
#     line = canvas.create_line(x1, y1, x2, y2, width=2, arrow=tk.LAST)
#
#
# root = tk.Tk()
# canvas = tk.Canvas(root, width=300, height=500, borderwidth=0, highlightthickness=0, bg="white")
# canvas.grid()
#
# draw_line(30, 75, 30, 200)
# # canvas.create_line(30, 75, 30, 200, width=2, arrow=tk.LAST)
# canvas.create_text(50, 145, text='a')
# # coord = 10, 50, 70, 110
#
# # cir = canvas.create_oval(10, 50, 70, 110, fill="red")
# x1 = 10
# y1 = 50
# dia = 40
# draw_cir(x1, y1, x1 + dia, y1 + dia, 'a')
# canvas.create_text(30, 70, text='0')
# y1 = 200
# draw_cir(x1, y1, x1 + dia, y1 + dia, 'b')
# canvas.create_text(30, 220, text='1')
# root.wm_title("Circles, lines, and Arcs")
# root.mainloop()

import tkinter
from tkinter import HORIZONTAL, BOTTOM, VERTICAL, RIGHT, BOTH, LEFT

state_position = {}
loop_occurrences = {}


def draw_arrow(i, j, canvas, counter, transition):
    if i == j:
        canvas.create_oval(10 + 80 * i, 410, 10 + 80 * i + 20 + 5, 440)
        canvas_id = canvas.create_text(10 + 80 * i - 10,
                                       445 + 30 * loop_occurrences[i],
                                       anchor="nw", font=("Default", 9))
        loop_occurrences[i] += 1
        message = str(transition)[1:-2].split(")(")
        canvas.itemconfig(canvas_id, text="%s" %
                          message[0] + ')-⌄\n(' + message[1] + ')')
        canvas.insert(canvas_id, 12, "")
    else:
        canvas.create_line(10 + 80 * i, 400, 10 + 80 * i, i + (-10)
                           * counter * 1.7 + 400, width=1, fill='blue')
        canvas.create_line(10 + 80 * i, i + (-10) * counter * 1.7 + 400,
                           10 + 80 * j + 35, i + (-10) * counter * 1.7 + 400,
                           width=1, fill='blue')
        canvas.create_line(10 + 80 * j + 35, i + (-10) * counter * 1.7 + 400,
                           10 + 80 * j + 35, 400, width=1, fill='blue')
        canvas.create_line(10 + 80 * j + 30, 395, 10 + 80 *
                           j + 35, 400, width=1, fill='blue')
        canvas.create_line(10 + 80 * j + 40, 395, 10 + 80 *
                           j + 35, 400, width=1, fill='blue')

    if i < j:
        canvas_id = canvas.create_text(
            10 + 80 * i, i + (-10) * counter * 1.7 + 384, anchor="nw")
        canvas.itemconfig(canvas_id, text="%s" % transition)
        canvas.insert(canvas_id, 12, "")
    elif i > j:
        canvas_id = canvas.create_text(
            10 + 80 * i - 110, i + (-10) * counter * 1.7 + 384, anchor="nw")
        canvas.itemconfig(canvas_id, text="%s" % transition)
        canvas.insert(canvas_id, 12, "")

    return counter + 1


def draw_automata(states, transitions):

    w = len(states)
    h = len(transitions)

    root = tkinter.Tk()
    frame = tkinter.Frame(root, width=800, height=600)
    frame.grid(row=0, column=0)
    canvas = tkinter.Canvas(frame, bg='#FFFFFF', width=800, height=600,
                            scrollregion=(0, -h * 15, w * 100, h * 15*3))
    hbar = tkinter.Scrollbar(frame, orient=HORIZONTAL)
    hbar.pack(side=BOTTOM, fill=X)
    hbar.config(command=canvas.xview)
    vbar = tkinter.Scrollbar(frame, orient=VERTICAL)
    vbar.pack(side=RIGHT, fill=Y)
    vbar.config(command=canvas.yview)
    canvas.config(width=800, height=600)
    canvas.config(xscrollcommand=hbar.set, yscrollcommand=vbar.set)
    canvas.pack(side=LEFT, expand=True, fill=BOTH)

    for position, state in enumerate(states):
        state_position[state] = position
        loop_occurrences[position] = 0
        canvas_id = canvas.create_text(10 + 80 * position, 400, anchor="nw")
        canvas.itemconfig(canvas_id, text="state-")
        canvas.insert(canvas_id, 12, "%d" % state)

    counter = 1
    for t in transitions:
        counter = draw_arrow(state_position[t.get_start_state()],
                             state_position[t.get_end_state()],
                             canvas, counter, t)

    root.mainloop()
