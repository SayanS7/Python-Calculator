from tkinter import *
from tkinter.messagebox import *
import math as m
from audio_helper import PlayAudio
import threading

# some useful variables
font = ('Verdana', 22, 'bold')
ob=PlayAudio()

# important functions
def clear():
    ex = textField.get()
    ex = ex[0:len(ex) - 1]
    textField.delete(0, END)
    textField.insert(0, ex)


def all_clear():
    textField.delete(0, END)


def click_btn_function(event):
    print("btn clicked")
    b = event.widget
    text = b['text']
    print(text)
    t=threading.Thread(target=ob.speak, args=(text))
    t.start()

    if text == 'x':
        textField.insert(END, "*")
        return

    if text == '=':
        try:
            ex = textField.get()
            answer = eval(ex)
            textField.delete(0, END)
            textField.insert(0, answer)

        except Exception as e:
            print("Error...", e)
            showerror("Error", e)
        return

    textField.insert(END, text)


# creating a window
window = Tk()
window.title('My Calculator')
window.configure(bg='light grey')
window.geometry('465x600+550+85')
# picture label
pic = PhotoImage(file='img/cal3.png')
headingLabel = Label(window, image=pic, bg='light grey')
headingLabel.pack(side=TOP, pady=10)

# heading label
heading = Label(window, text='My Calculator', font=font, bg='light grey')
heading.pack(side=TOP)

# textfield
textField = Entry(window, font=font, justify=CENTER)
textField.pack(side=TOP, pady=10, fill=X, padx=10)

"##############################REGULAR MODE###############################################"

# buttons
buttonFrame = Frame(window)
buttonFrame.configure(bg='light grey')
buttonFrame.pack(side=TOP, padx=10)

# adding button
temp = 1
for i in range(0, 3):
    for j in range(0, 3):
        btn = Button(buttonFrame, text=str(temp), font=font, width=5, relief="ridge", activebackground='DarkOrange1',
                     activeforeground='white')
        btn.grid(row=i, column=j)
        temp = temp + 1
        btn.bind('<Button-1>', click_btn_function)

zeroBtn = Button(buttonFrame, text='0', font=font, width=5, relief="ridge", activebackground='DarkOrange1',
                 activeforeground='white')
zeroBtn.grid(row=3, column=0)

dotBtn = Button(buttonFrame, text='.', font=font, width=5, relief="ridge", activebackground='DarkOrange1',
                activeforeground='white')
dotBtn.grid(row=3, column=1)

equalBtn = Button(buttonFrame, text='=', font=font, width=5, relief="ridge", activebackground='DarkOrange1',
                  activeforeground='white')
equalBtn.grid(row=3, column=2)

plusBtn = Button(buttonFrame, text='+', font=font, width=5, relief="ridge", activebackground='DarkOrange1',
                 activeforeground='white')
plusBtn.grid(row=0, column=3)

minusBtn = Button(buttonFrame, text='-', font=font, width=5, relief="ridge", activebackground='DarkOrange1',
                  activeforeground='white')
minusBtn.grid(row=1, column=3)

multBtn = Button(buttonFrame, text='x', font=font, width=5, relief="ridge", activebackground='DarkOrange1',
                 activeforeground='white')
multBtn.grid(row=2, column=3)

divideBtn = Button(buttonFrame, text='/', font=font, width=5, relief="ridge", activebackground='DarkOrange1',
                   activeforeground='white')
divideBtn.grid(row=3, column=3)

clearBtn = Button(buttonFrame, text='C', font=font, width=11, relief="ridge", activebackground='DarkOrange1',
                  activeforeground='white', command=clear)
clearBtn.grid(row=4, column=0, columnspan=2)

allClearBtn = Button(buttonFrame, text='AC', font=font, width=11, relief="ridge", activebackground='DarkOrange1',
                     activeforeground='white', command=all_clear)
allClearBtn.grid(row=4, column=2, columnspan=2)

# binding all btns
plusBtn.bind('<Button-1>', click_btn_function)
minusBtn.bind('<Button-1>', click_btn_function)
multBtn.bind('<Button-1>', click_btn_function)
divideBtn.bind('<Button-1>', click_btn_function)
zeroBtn.bind('<Button-1>', click_btn_function)
dotBtn.bind('<Button-1>', click_btn_function)
equalBtn.bind('<Button-1>', click_btn_function)


def enterClick(event):
    e = Event()
    e.widget = equalBtn
    click_btn_function(e)


textField.bind('<Return>', enterClick)

"#############################SCIENTIFIC MODE#############################################"
# Scientific clac frame
scFrame = Frame(window)

sqrtBtn = Button(scFrame, text='√', font=font, width=5, relief="ridge", activebackground='DarkOrange1',
                 activeforeground='white')
sqrtBtn.grid(row=0, column=0)

powBtn = Button(scFrame, text='^', font=font, width=5, relief="ridge", activebackground='DarkOrange1',
                activeforeground='white')
powBtn.grid(row=0, column=1)

factBtn = Button(scFrame, text='x!', font=font, width=5, relief="ridge", activebackground='DarkOrange1',
                 activeforeground='white')
factBtn.grid(row=0, column=2)

radBtn = Button(scFrame, text='toRad', font=font, width=5, relief="ridge", activebackground='DarkOrange1',
                activeforeground='white')
radBtn.grid(row=0, column=3)

degBtn = Button(scFrame, text='toDeg', font=font, width=5, relief="ridge", activebackground='DarkOrange1',
                activeforeground='white')
degBtn.grid(row=1, column=0)

sinBtn = Button(scFrame, text='sinθ', font=font, width=5, relief='ridge', activebackground='DarkOrange1',
                activeforeground='white')
sinBtn.grid(row=1, column=1)

cosBtn = Button(scFrame, text='cosθ', font=font, width=5, relief='ridge', activebackground='DarkOrange1',
                activeforeground='white')
cosBtn.grid(row=1, column=2)

tanBtn = Button(scFrame, text='tanθ', font=font, width=5, relief='ridge', activebackground='DarkOrange1',
                activeforeground='white')
tanBtn.grid(row=1, column=3)

normalclac = True


# Functions related Scientific Mode
def calculate_sc(event):
    btn = event.widget
    text = btn['text']
    print(text)
    ex = textField.get()
    answer = ''

    if text == 'toDeg':
        print("cal degree")
        answer = str(m.degrees(float(ex)))

    elif text == 'toRad':
        print('radian')
        answer = str(m.radians(float(ex)))

    elif text == 'x!':
        print("cal factorial")
        answer = str(m.factorial(int(ex)))

    elif text == 'sinθ':
        answer = str(m.sin(m.radians(int(ex))))

    elif text == 'cosθ':
        answer = str(m.cos(m.radians(int(ex))))

    elif text == 'tanθ':
        answer = str(m.tan(m.radians(int(ex))))

    elif text == '√':
        print('sqrt')
        answer = m.sqrt(int(ex))

    elif text == '^':
        # Input should be base,power
        print('pow')
        base, pow = ex.split(',')
        print(base)
        print(pow)
        answer = m.pow(int(base), int(pow))

    textField.delete(0, END)
    textField.insert(0, answer)


def sc_click():
    global normalclac
    if normalclac:
        # sc...
        buttonFrame.pack_forget()
        # add sc frame
        scFrame.pack(side=TOP, pady=20)
        buttonFrame.pack(side=TOP)
        window.geometry('480x750+550+20')
        print("show sc")
        normalclac = False
    else:
        print("show normal")
        scFrame.pack_forget()
        window.geometry('465x600')
        normalclac = True


# end functions

# binding sc buttons
sqrtBtn.bind("<Button-1>", calculate_sc)
powBtn.bind("<Button-1>", calculate_sc)
factBtn.bind("<Button-1>", calculate_sc)
radBtn.bind("<Button-1>", calculate_sc)
degBtn.bind("<Button-1>", calculate_sc)
sinBtn.bind("<Button-1>", calculate_sc)
cosBtn.bind("<Button-1>", calculate_sc)
tanBtn.bind("<Button-1>", calculate_sc)

fontMenu = ('', 15)
menubar = Menu(window, font=fontMenu)

mode = Menu(menubar, font=fontMenu, tearoff=0)
mode.add_checkbutton(label="Scientific Calculator", command=sc_click)

menubar.add_cascade(label="Mode", menu=mode)

window.config(menu=menubar)

window.mainloop()
