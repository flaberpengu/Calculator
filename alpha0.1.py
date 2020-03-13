import tkinter as tk

root = tk.Tk()

display_text = tk.StringVar()
label1 = tk.Label(root,textvariable=display_text)
label1.grid(row=0,columnspan=3)

def add_one():
    s = display_text.get()
    s += "1"
    display_text.set(s)

def add_two():
    s = display_text.get()
    s += "2"
    display_text.set(s)

def add_three():
    s = display_text.get()
    s += "3"
    display_text.set(s)

def add_four():
    s = display_text.get()
    s += "4"
    display_text.set(s)

def add_five():
    s = display_text.get()
    s += "5"
    display_text.set(s)

def add_six():
    s = display_text.get()
    s += "6"
    display_text.set(s)

def add_seven():
    s = display_text.get()
    s += "7"
    display_text.set(s)

def add_eight():
    s = display_text.get()
    s += "8"
    display_text.set(s)

def add_nine():
    s = display_text.get()
    s += "9"
    display_text.set(s)

def add_zero():
    s = display_text.get()
    s += "0"
    display_text.set(s)


def add_plus():
    s = display_text.get()
    s += "+"
    display_text.set(s)

def add_minus():
    s = display_text.get()
    s += "-"
    display_text.set(s)

def add_star():
    s = display_text.get()
    s += "*"
    display_text.set(s)

def add_slash():
    s = display_text.get()
    s += "/"
    display_text.set(s)

def get_sign():
    s = display_text.get()
    found = False
    sign = " "
    for a in range(len(s)):
        if s[a] != "0" and s[a] != "1" and s[a] != "2" and s[a] != "3" and s[a] != "4" and s[a] != "5" and s[a] != "6" and s[a] != "7" and s[a] != "8" and s[a] != "9":
            found = True
            sign = s[a]
    return found,sign

def operate_numbers(found,sign):
    s = display_text.get()
    nums = []
    nums = s.split(sign)
    if found == True:
        if sign == '+':
            answer = int(nums[0]) + int(nums[1])
        elif sign == '-':
            answer = int(nums[0]) - int(nums[1])
        elif sign == '*':
            answer = int(nums[0]) * int(nums[1])
        elif sign == '/':
            answer = int(nums[0]) / int(nums[1])
        s = str(answer)
        display_text.set(s)
    else:
        print("Error: must contain a function sign\n")

def do_maths():
    found,sign = get_sign()
    operate_numbers(found,sign)

def clear_screen():
    s = display_text.get()
    s = " "
    display_text.set(s)

one = tk.Button(root,
                 text="1",
                  padx = 5,
                  pady = 5,
                 command=add_one)
one.grid(row=3,column=0)

two = tk.Button(root,
                 text="2",
                  padx = 5,
                  pady = 5,
                 command=add_two)
two.grid(row=3,column=1)

three = tk.Button(root,
                 text="3",
                  padx = 5,
                  pady = 5,
                 command=add_three)
three.grid(row=3,column=2)

four = tk.Button(root,
                 text="4",
                  padx = 5,
                  pady = 5,
                 command=add_four)
four.grid(row=2,column=0)

five = tk.Button(root,
                 text="5",
                  padx = 5,
                  pady = 5,
                 command=add_five)
five.grid(row=2,column=1)

six = tk.Button(root,
                 text="6",
                  padx = 5,
                  pady = 5,
                 command=add_six)
six.grid(row=2,column=2)

seven = tk.Button(root,
                 text="7",
                  padx = 5,
                  pady = 5,
                 command=add_seven)
seven.grid(row=1,column=0)

eight = tk.Button(root,
                 text="8",
                  padx = 5,
                  pady = 5,
                 command=add_eight)
eight.grid(row=1,column=1)

nine = tk.Button(root,
                 text="9",
                  padx = 5,
                  pady = 5,
                 command=add_nine)
nine.grid(row=1,column=2)

zero = tk.Button(root,
                 text="0",
                 padx=5,
                 pady=5,
                 command=add_zero)
zero.grid(row=4,columnspan=3)


plus = tk.Button(root,
                text="+",
                padx=5,
                pady=5,
                command=add_plus)
plus.grid(row=5,column=0)

minus = tk.Button(root,
                  text="-",
                  padx=5,
                  pady=5,
                  command=add_minus)
minus.grid(row=5,column=1)

multiply = tk.Button(root,
                     text="*",
                     padx=5,
                     pady=5,
                     command=add_star)
multiply.grid(row=6,column=0)

divide = tk.Button(root,
                   text="/",
                   padx=5,
                   pady=5,
                   command=add_slash)
divide.grid(row=6,column=1)

equals = tk.Button(root,
                   text="=",
                   padx=5,
                   pady=5,
                   command=do_maths)
equals.grid(row=5,column=2)

clear = tk.Button(root,
                  text="Clear Screen",
                  padx=5,
                  pady=5,
                  command=clear_screen)
clear.grid(row=7,columnspan=3)

root.mainloop()
