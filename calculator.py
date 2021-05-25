from tkinter import *


def click(event):
    global scvalue
    text = event.widget.cget("text")
    print(text)
    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            try:
                value = eval(screen.get())

            except Exception as e:
                print(e)
                value = "Error"

            scvalue.set(value)
            screen.update()

    elif text == "C":
        scvalue.set("")
        screen.update()

    else:
        scvalue.set(scvalue.get() + text)
        screen.update()


root = Tk()
root.geometry("400x600")
root.title("Simple CALCULATOR - Janit Srivastava")
root.configure(background='darkgrey')
root.wm_iconbitmap("Calculator.ico")

scvalue = StringVar()
scvalue.set("")
screen = Entry(root, textvar=scvalue, font="comicsansms 45 bold", bg='grey', fg='blue', relief=GROOVE)
screen.pack(fill=X, ipadx=10,pady=15, padx=10)


f = Frame(root, bg='silver')
b = Button(f, text='9', font="comicsansms 18 bold", padx=12, pady=10, fg='green')
b.pack(side='left', padx=10, pady=5)
b.bind('<Button-1>', click)

b = Button(f, text='8', font="comicsansms 18 bold", padx=12, pady=10, fg='green')
b.pack(side='left', padx=10, pady=5)
b.bind('<Button-1>', click)

b = Button(f, text='7', font="comicsansms 18 bold", padx=12, pady=10, fg='green')
b.pack(side='left', padx=10, pady=5)
b.bind('<Button-1>', click)

b = Button(f, text='-', font="comicsansms 20 bold", padx=12, pady=10, bg='lightgrey', fg='red')
b.pack(side='left', padx=10, pady=5)
b.bind('<Button-1>', click)

f.pack()


f = Frame(root, bg='silver')
b = Button(f, text='6', font="comicsansms 18 bold", padx=12, pady=10, fg='green')
b.pack(side='left', padx=10, pady=5)
b.bind('<Button-1>', click)

b = Button(f, text='5', font="comicsansms 18 bold", padx=12, pady=10, fg='green')
b.pack(side='left', padx=10, pady=5)
b.bind('<Button-1>', click)

b = Button(f, text='4', font="comicsanms 18 bold", padx=12, pady=10, fg='green')
b.pack(side='left', padx=10, pady=5)
b.bind('<Button-1>', click)

b = Button(f, text='+', font="comicsansms 19 bold", padx=12, pady=10, bg='lightgrey', fg='red')
b.pack(side='left', padx=10, pady=5)
b.bind('<Button-1>', click)

f.pack()


f = Frame(root, bg='silver')
b = Button(f, text='3', font="comicsansms 18 bold", padx=12, pady=10, fg='green')
b.pack(side='left', padx=10, pady=5)
b.bind('<Button-1>', click)

b = Button(f, text='2', font="comicsansms 18 bold", padx=12, pady=10, fg='green')
b.pack(side='left', padx=10, pady=5)
b.bind('<Button-1>', click)

b = Button(f, text='1', font="comicsansms 18 bold", padx=12, pady=10, fg='green')
b.pack(side='left', padx=10, pady=5)
b.bind('<Button-1>', click)

b = Button(f, text='*', font="comicsansms 20 bold", padx=12, pady=10, bg='lightgrey', fg='red')
b.pack(side='left', padx=10, pady=5)
b.bind('<Button-1>', click)

f.pack()


f = Frame(root, bg='silver')
b = Button(f, text='0', font="comicsansms 16 bold", padx=14, pady=10, fg='green')
b.pack(side='left', padx=10, pady=5)
b.bind('<Button-1>', click)

b = Button(f, text='00', font="comicsansms 16 bold", padx=14, pady=10, fg='green')
b.pack(side='left', padx=10, pady=5)
b.bind('<Button-1>', click)

b = Button(f, text='.', font="comicsansms 19 bold", padx=11, pady=10, bg='lightgrey', fg='red')
b.pack(side='left', padx=10, pady=5)
b.bind('<Button-1>', click)

b = Button(f, text='/', font="comicsansms 18 bold", padx=14, pady=10, bg='lightgrey', fg='red')
b.pack(side='left', padx=10, pady=5)
b.bind('<Button-1>', click)

f.pack()


f = Frame(root, bg='silver')
b = Button(f, text='C', font="comicsansms 19 bold", padx=11, pady=10, bg='lightgrey', fg='brown')
b.pack(side='left', padx=10, pady=5)
b.bind('<Button-1>', click)

b = Button(f, text='=', font="comicsansms 20 bold", padx=12, pady=10, bg='lightgrey',  fg='darkorange', relief=RAISED)
b.pack(side='left', padx=10, pady=5)
b.bind('<Button-1>', click)

b = Button(f, text='%', font="comicsansms 18 bold", padx=10, pady=10, bg='lightgrey', fg='red')
b.pack(side='left', padx=10, pady=5)
b.bind('<Button-1>', click)

f.pack()

root.mainloop()