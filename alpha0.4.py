import tkinter as tk

root = tk.Tk()

display_text_lower = tk.StringVar()
label1 = tk.Label(root,relief='groove',bg='#D3D3DF',width=30,height=2,textvariable=display_text_lower)
label1.grid(row=1,columnspan=3)

display_text_upper  = tk.StringVar()
label2 = tk.Label(root,relief='groove',bg='#9D9DE6',width=30,height=2,textvariable=display_text_upper)
label2.grid(row=0,columnspan=3)

def add_one():
    if clear == True:
        clear_screen()
    else:
        s = display_text_lower.get()
        s += "1"
        display_text_lower.set(s)

def add_two():
    if clear == True:
        clear_screen()
    else:
        s = display_text_lower.get()
        s += "2"
        display_text_lower.set(s)

def add_three():
    if clear == True:
        clear_screen()
    else:
        s = display_text_lower.get()
        s += "3"
        display_text_lower.set(s)

def add_four():
    if clear == True:
        clear_screen()
    else:
        s = display_text_lower.get()
        s += "4"
        display_text_lower.set(s)

def add_five():
    if clear == True:
        clear_screen()
    else:
        s = display_text_lower.get()
        s += "5"
        display_text_lower.set(s)

def add_six():
    if clear == True:
        clear_screen()
    else:
        s = display_text_lower.get()
        s += "6"
        display_text_lower.set(s)

def add_seven():
    if clear == True:
        clear_screen()
    else:
        s = display_text_lower.get()
        s += "7"
        display_text_lower.set(s)

def add_eight():
    if clear == True:
        clear_screen()
    else:
        s = display_text_lower.get()
        s += "8"
        display_text_lower.set(s)

def add_nine():
    if clear == True:
        clear_screen()
    else:
        s = display_text_lower.get()
        s += "9"
        display_text_lower.set(s)

def add_zero():
    if clear == True:
        clear_screen()
    else:
        s = display_text_lower.get()
        s += "0"
        display_text_lower.set(s)


def add_plus():
    if clear == True:
        clear_screen()
    else:
        upper = display_text_upper.get()
        if upper != '' and upper != ' ':
            do_maths()
        s = display_text_lower.get()
        s += "+"
        display_text_lower.set(s)
        move_text()

def add_minus():
    if clear == True:
        clear_screen()
    else:
        upper = display_text_upper.get()
        if upper != '' and upper != ' ':
            do_maths()
        s = display_text_lower.get()
        s += "-"
        display_text_lower.set(s)
        move_text()

def add_star():
    if clear == True:
        clear_screen()
    else:
        upper = display_text_upper.get()
        if upper != '' and upper != ' ':
            do_maths()
        s = display_text_lower.get()
        s += "*"
        display_text_lower.set(s)
        move_text()

def add_slash():
    if clear == True:
        clear_screen()
    else:
        upper = display_text_upper.get()
        if upper != '' and upper != ' ':
            do_maths()
        s = display_text_lower.get()
        s += "/"
        display_text_lower.set(s)
        move_text()

def add_upper_arrow():
    if clear == True:
        clear_screen()
    else:
        upper = display_text_upper.get()
        if upper != '' and upper != ' ':
            do_maths()
        s = display_text_lower.get()
        s += "^"
        display_text_lower.set(s)
        move_text()
    
def move_text():
    lower = display_text_lower.get()
##    upper = display_text_upper.get()
    upper = lower
    display_text_upper.set(upper)
    display_text_lower.set('')

##############################################
def get_sign():
    upper = display_text_upper.get()
    if upper == '':
        found = False
        sign = " "
    else:
        found = True
        sign = upper[(len(upper)-1)]
    print(found,sign)
    return found,sign

def operate_numbers(found,sign):
    upper = display_text_upper.get()
    lower = display_text_lower.get()
    nums = []
    nums.append(upper[0:(len(upper)-1):1])
    nums.append(lower)
    if found == True:
        if sign == '+':
            answer = float(nums[0]) + float(nums[1])
        elif sign == '-':
            answer = float(nums[0]) - float(nums[1])
        elif sign == '*':
            answer = float(nums[0]) * float(nums[1])
        elif sign == '/':
            if int(nums[1]) == 0:
                answer = 'Cannot divide by zero'
                global clear
                clear = True
            else:
                answer = float(nums[0]) / float(nums[1])
        elif sign == '^':
            answer = float(nums[0]) ** float(nums[1])
        lower = str(answer)
        display_text_lower.set(lower)
        display_text_upper.set('')
    else:
        print("Error: must contain a function sign\n")

def do_maths():
    found,sign = get_sign()
    operate_numbers(found,sign)

def clear_screen():
    global clear
    clear = False
    lower = ""
    display_text_lower.set(lower)
    upper = ''
    display_text_upper.set(upper)
    signs = 0

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
                   command=do_maths)
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

quit_calc = tk.Button(root,
                      text="QUIT",
                      padx=5,
                      pady=5,
                      command=quit_program)
quit_calc.grid(row=10,columnspan=3)


root.mainloop()
