#!/usr/bin/env python

from tkinter import *
from datetime import datetime
import time

root = Tk()
root.configure(background='#000000')
bRoot = Tk()
bRoot.configure(background='#000000')
bRoot.geometry("410x800")

root.title('Presenter View')
bRoot.title('Buttons')
bRoot.configure(height=400)

e = Entry(bRoot, width=20, bg='gray', highlightcolor='blue')
e2 = Entry(bRoot, width=20, bg='gray', highlightcolor='blue')

m = 0
s = 0

# hours = '%H'
# minutes = '%M'
# seconds = '%S'
# format = '%M:%S'
# timeMinutes = (datetime.now()).strftime(minutes)
# timeSeconds = (datetime.now()).strftime(seconds)

x = 0
off = 0
t = 0
f = 400

def clear():
    global m
    global s
    global ms
    m = 0
    s = 0
    ms -= 0

def play():
    global off
    off = 1

def stop():
    global off
    off = 0

def setMinute():
    global m
    m = e.get()
    if m.isnumeric() == True:
        m = int(m)
    if m.isnumeric() == False:
        m = 0

def setSeconds():
    global s
    s = str(e.get())
    if s.isnumeric() == True:
        s = int(s)
    if s.isnumeric() == False:
        s = 0

def add():
    global m
    c = 1
    m += 1

def sub():
    global m
    c = 0
    m -= 1

def add10():
    global m
    m += 10

def sub10():
    global m
    m -= 10

def addS():
    global s
    s += 1

def subS():
    global s
    s -= 1

def add10S():
    global s
    s += 10

def sub10S():
    global s
    s -= 10

def sendMessage():
    global t
    t = 1

def hideMessage():
    global t
    t = 0

def timerSizeAdd():
    global f
    f += 10

def timerSizeSub():
    global f
    f -= 10

buttonFont = 20

clearButton = Button(bRoot, text='Clear Clock', padx=143, pady=10, font=('calibri', buttonFont, 'bold'), foreground='red', command=clear)
clearButton.pack()
clearButton.place(x=10, y=265)

playButton = Button(bRoot, text='Start', padx=66, pady=10, font=('calibri', buttonFont, 'bold'), foreground='green', command=play)
playButton.pack()
playButton.place(x=10, y=160)

stopButton = Button(bRoot, text='Stop', padx=69, pady=10, font=('calibri', buttonFont, 'bold'), foreground='red', command=stop)
stopButton.pack()
stopButton.place(x=220, y=160)

setMinute = Button(bRoot, text='Set Minute', padx=38, pady=10, font=('calibri', buttonFont, 'bold'), foreground='black', command=setMinute)
setMinute.pack()
setMinute.place(x=10, y=210)

setSeconds = Button(bRoot, text='Set Seconds', padx=33, pady=10, font=('calibri', buttonFont, 'bold'), foreground='black', command=setSeconds)
setSeconds.pack()
setSeconds.place(x=220, y=210)

addTime = Button(bRoot, text='Add +1 Min', padx=37, pady=10, font=('calibri', buttonFont, 'bold'), foreground='blue', command=add)
addTime.pack()
addTime.place(x=10, y=320)

subTime = Button(bRoot, text='Subtract -1 Min', padx=17, pady=10, font=('calibri', buttonFont, 'bold'), foreground='purple', command=sub)
subTime.pack()
subTime.place(x=10, y=380)

addTime10 = Button(bRoot, text='Add +10 Min', padx=30, pady=10, font=('calibri', buttonFont, 'bold'), foreground='blue', command=add10)
addTime10.pack()
addTime10.place(x=10, y=440)

subTime10 = Button(bRoot, text='Subtract -10 Min', padx=10, pady=10, font=('calibri', buttonFont, 'bold'), foreground='purple', command=sub10)
subTime10.pack()
subTime10.place(x=10, y=500)

addTimeS = Button(bRoot, text='Add +1 Sec', padx=37, pady=10, font=('calibri', buttonFont, 'bold'), foreground='blue', command=addS)
addTimeS.pack()
addTimeS.place(x=220, y=320)

subTimeS = Button(bRoot, text='Subtract -1 Sec', padx=17, pady=10, font=('calibri', buttonFont, 'bold'), foreground='purple', command=subS)
subTimeS.pack()
subTimeS.place(x=220, y=380)

addTime10S = Button(bRoot, text='Add +10 Sec', padx=30, pady=10, font=('calibri', buttonFont, 'bold'), foreground='blue', command=add10S)
addTime10S.pack()
addTime10S.place(x=220, y=440)

subTime10S = Button(bRoot, text='Subtract -10 Sec', padx=10, pady=10, font=('calibri', buttonFont, 'bold'), foreground='purple', command=sub10S)
subTime10S.pack()
subTime10S.place(x=220, y=500)

sendMessage = Button(bRoot, text='Show Message', padx=20, pady=10, font=('calibri', buttonFont, 'bold'), foreground='purple', command=sendMessage)
sendMessage.pack()
sendMessage.place(x=10, y=625)

hideMessage = Button(bRoot, text='Hide Message', padx=20, pady=10, font=('calibri', buttonFont, 'bold'), foreground='purple', command=hideMessage)
hideMessage.pack()
hideMessage.place(x=220, y=625)

timerSizeAddButton = Button(bRoot, text='Increase font', padx=29, pady=10, font=('calibri', buttonFont, 'bold'), foreground='black', command=timerSizeAdd)
timerSizeAddButton.pack()
timerSizeAddButton.place(x=10, y=685)

timerSizeSubButton = Button(bRoot, text='Decrease Font', padx=18, pady=10, font=('calibri', buttonFont, 'bold'), foreground='black', command=timerSizeSub)
timerSizeSubButton.pack()
timerSizeSubButton.place(x=220, y=685)

ms = 0

def update_time():
    global string
    global f
    global s
    global m
    global c

    if s < 0:
        s = 59
        m -= 1

    if t == 1:
        string2 = e2.get()

    if t == 0:
        string2 = ''

    if s >= 10:
        timeSet = str(m) + ':' + str(s)
        string = timeSet

    if s < 10:
        timeSet = str(m) + ':0' + str(s)
        string = timeSet

    if m < 10 and s < 10:
        timeSet = '0' + str(m) + ':0' + str(s)
        string = timeSet


    if m < 10 and s >= 10:
        timeSet = '0' + str(m) + ':' + str(s)
        string = timeSet

    if s >= 60:
        s = s - 60
        m += 1

    if off == 1:
        s -= 1
        l.after(1000, update_time)

    if off == 0:
        s += 0
        l.after(10, update_time)

    if s < 0:
        s = 59
        m -= 1

    if m < 0:
        m = 0
        s = 0
        s -= 0

    l.config(text=string, font=('calibri', f, 'bold'))
    l2.config(text=string)
    l3.config(text=string2)
    l4.config(text='Type Message')

white = 'white'
red = 'red'
colors = [white, red]

l = Label(root, background='black', foreground=colors[0])
l.pack(anchor='center')

l2 = Label(bRoot, font=('calibri', 100, 'bold'), background='black', foreground=colors[0])
l2.pack(anchor='center')
l2.place(x=55, y=30)

l3 = Label(root, font=('calibri', 100, 'bold'), background='black', foreground=colors[0])
l3.pack(anchor='center')

l4 = Label(bRoot, font=('calibri', 20, 'bold'), background='black', foreground=colors[0])
l4.pack(anchor='center')
l4.place(x=140, y=555)

e.place(x=110, y=2)
e2.place(x=110,y=590)

update_time()
root.mainloop()