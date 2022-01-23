from tkinter import *
import tkinter.font
import math
root = Tk()
# color variables
number_colors = "black"  # buttons
text_color = "white"  # text inside entry
gray_layout = "#151414"  # layout of the interface
gray_layout1 = "#383737"
disp_backgroundcolors = "#3B3A3A"
# var that holds font displayed
font_disp = tkinter.font.Font(family="Segoe UI", size=25)
font_but = tkinter.font.Font(family="Segoe UI ", size=15)
# title of program
root.title("Calculator")

root.config(bg=gray_layout)
root.geometry("300x350")

e = Entry(root, width=0,  fg="white", bg=gray_layout,
          font=font_disp)
e.config(borderwidth=0)
e.grid(row=0, column=0, columnspan=4, sticky="NSEW")
Entry.rowconfigure(root, ALL, weight=1)
Entry.columnconfigure(root, ALL, weight=1)
Grid.rowconfigure(root, ALL, weight=1)
Grid.columnconfigure(root, ALL, weight=1)


def clicked_numbers(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))


def button_clear():
    e.delete(0, END)


def button_add():
    first_number = e.get()
    global f_num
    global math1
    math1 = '+'
    f_num = (first_number)
    e.delete(0, END)


def button_equal():
    second_number = e.get()
    if math1 != "":
        e.delete(0, END)
        if math1 == '+':

            e.insert(0, float(f_num) + float(second_number))
        if math1 == '/':
            e.insert(0, float(f_num) / float(second_number))
        if math1 == '*':
            e.insert(0, float(f_num) * float(second_number))
        if math1 == '-':
            e.insert(0, float(f_num) - float(second_number))


def button_subtract():

    first_number = e.get()
    global f_num
    global math1
    math1 = '-'
    f_num = (first_number)
    e.delete(0, END)


def button_multiply():
    first_number = e.get()
    global f_num
    global math1
    math1 = '*'
    f_num = (first_number)
    e.delete(0, END)


def button_division():
    first_number = e.get()
    global f_num
    global math1
    math1 = '/'
    f_num = (first_number)
    e.delete(0, END)


def button_sqr():
    first_number = e.get()
    global f_num
    global math1
    f_num = (first_number)
    e.delete(0, END)
    sqrt123 = math.sqrt(int(f_num))
    e.insert(0, sqrt123)

# define buttons 1 , 9 to


size_numberbuttons = 9
size_numberbuttonsy = 38
button_height = 1
button_width = 1
different_buttonsh = 1
different_buttonsw = 1
button_tickness = 0
button_1 = Button(root, text="1", padx=size_numberbuttonsy,
                  pady=size_numberbuttons, command=lambda: clicked_numbers('1'), highlightthickness=button_tickness, highlightbackground="gray", borderwidth=button_tickness, bg=number_colors, fg=text_color, height=button_height, width=button_width)
button_2 = Button(root, text="2", padx=size_numberbuttonsy,
                  pady=size_numberbuttons, command=lambda: clicked_numbers('2'), bg=number_colors, fg=text_color, highlightthickness=button_tickness, borderwidth=button_tickness, height=button_height, width=button_width)
button_3 = Button(root, text="3", padx=size_numberbuttonsy,
                  pady=size_numberbuttons, command=lambda: clicked_numbers('3'), bg=number_colors, fg=text_color, height=button_height, highlightthickness=button_tickness, borderwidth=button_tickness, width=button_width)
button_4 = Button(root, text="4", padx=size_numberbuttonsy,
                  pady=size_numberbuttons, command=lambda: clicked_numbers('4'), bg=number_colors, fg=text_color, height=button_height, highlightthickness=button_tickness, borderwidth=button_tickness, width=button_width)
button_5 = Button(root, text="5", padx=size_numberbuttonsy,
                  pady=size_numberbuttons, command=lambda: clicked_numbers('5'), bg=number_colors, fg=text_color, height=button_height, highlightthickness=button_tickness, borderwidth=button_tickness, width=button_width)
button_6 = Button(root, text="6", padx=size_numberbuttonsy,
                  pady=size_numberbuttons, command=lambda: clicked_numbers('6'), bg=number_colors, fg=text_color, height=button_height, highlightthickness=button_tickness, borderwidth=button_tickness, width=button_width)
button_7 = Button(root, text="7", padx=size_numberbuttonsy,
                  pady=size_numberbuttons, command=lambda: clicked_numbers('7'), bg=number_colors, fg=text_color, height=button_height, highlightthickness=button_tickness, borderwidth=button_tickness, width=button_width)
button_8 = Button(root, text="8", padx=size_numberbuttonsy,
                  pady=size_numberbuttons, command=lambda: clicked_numbers('8'), bg=number_colors, fg=text_color, height=button_height, highlightthickness=button_tickness, borderwidth=button_tickness, width=button_width)
button_9 = Button(root, text="9", padx=size_numberbuttonsy,
                  pady=size_numberbuttons, command=lambda: clicked_numbers('9'), bg=number_colors, fg=text_color, height=button_height, highlightthickness=button_tickness, borderwidth=button_tickness, width=button_width)
button_0 = Button(root, text="0", padx=size_numberbuttonsy,
                  pady=size_numberbuttons, command=lambda: clicked_numbers('0'), bg=number_colors, fg=text_color, height=button_height, highlightthickness=button_tickness, borderwidth=button_tickness, width=button_width)
button_add1 = Button(root, text="+", padx=size_numberbuttons,
                     pady=size_numberbuttons, command=button_add, bg=gray_layout1, fg="white", borderwidth=button_tickness, width=button_width, height=button_height)
button_equal1 = Button(root, text="=", height=different_buttonsh, width=different_buttonsw,
                       command=button_equal, bg=gray_layout1, fg="white", borderwidth=button_tickness)
button_clear1 = Button(root, text="C",
                       command=button_clear, bg=gray_layout1, fg="white", height=different_buttonsh, width=different_buttonsw, borderwidth=button_tickness)
button_dot = Button(root, text=".",  command=lambda: clicked_numbers('.'), padx=size_numberbuttonsy,
                    pady=size_numberbuttons, bg=number_colors, fg=text_color, height=button_height, highlightthickness=button_tickness, borderwidth=button_tickness, width=button_width)
button_subtract = Button(root, text="-", command=button_subtract, padx=size_numberbuttonsy,
                         pady=size_numberbuttons, bg=number_colors, fg=text_color, height=button_height, highlightthickness=button_tickness, borderwidth=button_tickness, width=button_width)
button_divide = Button(root, text="÷", command=button_division, padx=size_numberbuttonsy,
                       pady=size_numberbuttons, bg=number_colors, fg=text_color, height=button_height, highlightthickness=button_tickness, borderwidth=button_tickness, width=button_width)
button_multiply = Button(root, text="x", command=button_multiply, padx=size_numberbuttonsy,
                         pady=size_numberbuttons, bg=number_colors, fg=text_color, height=button_height, highlightthickness=button_tickness, borderwidth=button_tickness, width=button_width)
button_sqr = Button(root, text="√", command=button_sqr, padx=size_numberbuttonsy,
                    pady=size_numberbuttons, bg=number_colors, fg=text_color, height=button_height, highlightthickness=button_tickness, borderwidth=button_tickness, width=button_width)
# put buttons on screen''''''''''''''''''''''''''''''''''''''''''''''
separatenum = 1
serparatenum1 = 1
button_1.grid(row=5, column=0, sticky="NSEW",
              padx=separatenum, pady=serparatenum1)
button_2.grid(row=5, column=1, sticky="NSEW",
              padx=separatenum, pady=serparatenum1)
button_3.grid(row=5, column=2, sticky="NSEW",
              padx=separatenum, pady=serparatenum1)
button_4.grid(row=4, column=0, sticky="NSEW",
              padx=separatenum, pady=serparatenum1)
button_5.grid(row=4, column=1, sticky="NSEW",
              padx=separatenum, pady=serparatenum1)
button_6.grid(row=4, column=2, sticky="NSEW",
              padx=separatenum, pady=serparatenum1)
button_7.grid(row=3, column=0, sticky="NSEW",
              padx=separatenum, pady=serparatenum1)
button_8.grid(row=3, column=1, sticky="NSEW",
              padx=separatenum, pady=serparatenum1)
button_9.grid(row=3, column=2, sticky="NSEW",
              padx=separatenum, pady=serparatenum1)
button_0.grid(row=6, column=1, sticky="NSEW",
              padx=separatenum, pady=serparatenum1)
button_clear1.grid(row=6, column=0,  sticky="NSEW",
                   padx=separatenum, pady=serparatenum1)
button_add1.grid(row=6, column=3, sticky="NSEW",
                 padx=separatenum, pady=serparatenum1)
button_equal1.grid(row=6, column=3, sticky="NSEW",
                   padx=separatenum, pady=serparatenum1)
button_dot.grid(row=6, column=2, sticky="NSEW",
                padx=separatenum, pady=serparatenum1)
button_subtract.grid(row=4, column=3, sticky="NSEW",
                     padx=separatenum, pady=serparatenum1)
button_divide.grid(row=2, column=3, sticky="NSEW",
                   padx=separatenum, pady=serparatenum1)
button_multiply.grid(row=3, column=3,
                     padx=separatenum, pady=serparatenum1, sticky="NSEW")
button_add1.grid(row=5, column=3,
                 padx=separatenum, pady=serparatenum1, sticky="NSEW")
button_sqr.grid(row=2, column=2, sticky="NSEW",
                padx=separatenum, pady=serparatenum1)
button_1['font'] = font_but
button_2['font'] = font_but
button_3['font'] = font_but
button_4['font'] = font_but
button_5['font'] = font_but
button_6['font'] = font_but
button_7['font'] = font_but
button_8['font'] = font_but
button_9['font'] = font_but
button_0['font'] = font_but
button_equal1['font'] = font_but
button_dot['font'] = font_but
button_subtract['font'] = font_but
button_add1['font'] = font_but
button_divide['font'] = font_but
button_multiply['font'] = font_but
root.mainloop()
