import tkinter as tk
import math

global first_int
first_int=''
global second_int
second_int=''
global sign
sign=''
global answer
answer=''

root = tk.Tk()

display_text_lower = tk.StringVar()
label1 = tk.Label(root,relief='groove',bg='#D3D3DF',width=30,height=2,textvariable=display_text_lower)
label1.grid(row=1,columnspan=3)

display_text_upper  = tk.StringVar()
label2 = tk.Label(root,relief='groove',bg='#9D9DE6',width=30,height=2,textvariable=display_text_upper)
label2.grid(row=0,columnspan=3)

def add_one():
    global first_int
    if clear == True:
        clear_screen()
    else:
        first_int += '1'
        display_text_lower.set(first_int)

def add_two():
    global first_int
    if clear == True:
        clear_screen()
    else:
        first_int += '2'
        display_text_lower.set(first_int)

def add_three():
    global first_int
    if clear == True:
        clear_screen()
    else:
        first_int += '3'
        display_text_lower.set(first_int)

def add_four():
    global first_int
    if clear == True:
        clear_screen()
    else:
        first_int += '4'
        display_text_lower.set(first_int)

def add_five():
    global first_int
    if clear == True:
        clear_screen()
    else:
        first_int += '5'
        display_text_lower.set(first_int)

def add_six():
    global first_int
    if clear == True:
        clear_screen()
    else:
        first_int += '6'
        display_text_lower.set(first_int)

def add_seven():
    global first_int
    if clear == True:
        clear_screen()
        first_int = ''
    else:
        first_int += '7'
        display_text_lower.set(first_int)

def add_eight():
    global first_int
    if clear == True:
        clear_screen()
    else:
        first_int += '8'
        display_text_lower.set(first_int)

def add_nine():
    global first_int
    if clear == True:
        clear_screen()
    else:
        first_int += '9'
        display_text_lower.set(first_int)

def add_zero():
    global first_int
    if clear == True:
        clear_screen()
    else:
        first_int += '0'
        display_text_lower.set(first_int)


def add_plus():
    if clear == True:
        clear_screen()
    else:
        global second_int
        global sign
        sign = '+'
        if second_int != '' and second_int != ' ':
            operate_numbers()
        global first_int
        display_text_lower.set(first_int + sign)
        move_text()

def add_minus():
    if clear == True:
        clear_screen()
    else:
        global second_int
        global sign
        sign = '-'
        if second_int != '' and second_int != ' ':
            operate_numbers()
        global first_int
        display_text_lower.set(first_int + sign)
        move_text()

def add_star():
    if clear == True:
        clear_screen()
    else:
        global second_int
        global sign
        sign = '*'
        if second_int != '' and second_int != ' ':
            operate_numbers()
        global first_int
        display_text_lower.set(first_int + sign)
        move_text()

def add_slash():
    if clear == True:
        clear_screen()
    else:
        global second_int
        global sign
        sign = '/'
        if second_int != '' and second_int != ' ':
            operate_numbers()
        global first_int
        display_text_lower.set(first_int + sign)
        move_text()

def add_upper_arrow():
    if clear == True:
        clear_screen()
    else:
        global second_int
        global sign
        sign = '^'
        if second_int != '' and second_int != ' ':
            operate_numbers()
        global first_int
        display_text_lower.set(first_int + sign)
        move_text()

####
def add_sqrt():
    if clear == True:
        clear_screen()
    else:
        upper = display_text_upper.get()
        if upper != '' and upper != ' ':
            s = 'Cannot compute'
        else:
            s = display_text_lower.get()
            num_to_root = int(s)
            new = ('sqrt(' + str(s) + ')')
            s = new
            display_text_lower.set(s)
            move_text()
            answer = math.sqrt(num_to_root)
            s = answer
        display_text_lower.set(s)
    
def move_text():
    global first_int
    global second_int
    global sign
##    upper = display_text_upper.get()
    second_int = first_int
    first_int = ''
    display_text_upper.set(second_int + sign)
    display_text_lower.set(first_int)


def operate_numbers():
    global first_int
    global second_int
    global sign
    global answer
    if sign != '' and sign != ' ':
        if sign == '+':
            answer = float(first_int) + float(second_int)
        elif sign == '-':
            answer = float(second_int) - float(first_int)
        elif sign == '*':
            answer = float(first_int) * float(second_int)
        elif sign == '/':
            if int(first_int) == 0:
                answer = 'Cannot divide by zero'
                global clear
                clear = True
            else:
                answer = float(second_int) / float(first_int)
        elif sign == '^':
            answer = float(second_int) ** float(first_int)
        first_int = str(answer)
        second_int = ''
        display_text_lower.set(first_int)
        display_text_upper.set(second_int)
    else:
        print("Error: must contain a function sign\n")


def clear_screen():
    global clear
    clear = False
    global first_int
    first_int = ''
    display_text_lower.set(first_int)
    global second_int
    second_int = ''
    display_text_upper.set(second_int)
    global sign
    sign = ''
    global answer
    answer = ''

def quit_program():
    root.destroy()

one = tk.Button(root,
                 text="1",
                  padx = 5,
                  pady = 5,
                bg='#373740',
                fg='#FFFFFF',
                 command=add_one)
one.grid(row=4,column=0)

two = tk.Button(root,
                 text="2",
                  padx = 5,
                  pady = 5,
                bg='#373740',
                fg='#FFFFFF',
                 command=add_two)
two.grid(row=4,column=1)

three = tk.Button(root,
                 text="3",
                  padx = 5,
                  pady = 5,
                  bg='#373740',
                fg='#FFFFFF',
                 command=add_three)
three.grid(row=4,column=2)

four = tk.Button(root,
                 text="4",
                  padx = 5,
                  pady = 5,
                 bg='#373740',
                fg='#FFFFFF',
                 command=add_four)
four.grid(row=3,column=0)

five = tk.Button(root,
                 text="5",
                  padx = 5,
                  pady = 5,
                 bg='#373740',
                fg='#FFFFFF',
                 command=add_five)
five.grid(row=3,column=1)

six = tk.Button(root,
                 text="6",
                  padx = 5,
                  pady = 5,
                bg='#373740',
                fg='#FFFFFF',
                 command=add_six)
six.grid(row=3,column=2)

seven = tk.Button(root,
                 text="7",
                  padx = 5,
                  pady = 5,
                  bg='#373740',
                fg='#FFFFFF',
                 command=add_seven)
seven.grid(row=2,column=0)

eight = tk.Button(root,
                 text="8",
                  padx = 5,
                  pady = 5,
                  bg='#373740',
                fg='#FFFFFF',
                 command=add_eight)
eight.grid(row=2,column=1)

nine = tk.Button(root,
                 text="9",
                  padx = 5,
                  pady = 5,
                 bg='#373740',
                fg='#FFFFFF',
                 command=add_nine)
nine.grid(row=2,column=2)

zero = tk.Button(root,
                 text="0",
                 padx=5,
                 pady=5,
                 bg='#373740',
                fg='#FFFFFF',
                 command=add_zero)
zero.grid(row=5,columnspan=3)


plus = tk.Button(root,
                text="+",
                padx=5,
                pady=5,
                 bg='#373740',
                fg='#FFFFFF',
                command=add_plus)
plus.grid(row=6,column=0)

minus = tk.Button(root,
                  text="-",
                  padx=5,
                  pady=5,
                  bg='#373740',
                fg='#FFFFFF',
                  command=add_minus)
minus.grid(row=6,column=1)

multiply = tk.Button(root,
                     text="*",
                     padx=5,
                     pady=5,
                     bg='#373740',
                fg='#FFFFFF',
                     command=add_star)
multiply.grid(row=7,column=0)

divide = tk.Button(root,
                   text="/",
                   padx=5,
                   pady=5,
                   bg='#373740',
                fg='#FFFFFF',
                   command=add_slash)
divide.grid(row=7,column=1)

equals = tk.Button(root,
                   text="=",
                   padx=5,
                   pady=5,
                   bg='#373740',
                fg='#FFFFFF',
                   command=operate_numbers)
equals.grid(row=6,column=2)

clear = tk.Button(root,
                  text="Clear Screen",
                  padx=5,
                  pady=5,
                  bg='#373740',
                fg='#FFFFFF',
                  command=clear_screen)
clear.grid(row=8,columnspan=3)

power = tk.Button(root,
                  text="^",
                  padx=5,
                  pady=5,
                  bg='#373740',
                fg='#FFFFFF',
                  command=add_upper_arrow)
power.grid(row=9,column=0)

sqrt = tk.Button(root,
                 text="sqrt()",
                 padx=5,
                 pady=5,
                 bg='#373740',
                 fg='#FFFFFF',
                 command=add_sqrt)
sqrt.grid(row=9,column=1)

quit_calc = tk.Button(root,
                      text="QUIT",
                      padx=5,
                      pady=5,
                      command=quit_program)
quit_calc.grid(row=10,columnspan=3)


root.mainloop()
