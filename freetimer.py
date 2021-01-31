# Blasterjacks submission :D
# Adam Taha, Joseph Buskmiller, Cole Newby

from tkinter import *
import datetime
import calendar
import classsss
import threading
import time
import math

def b2():
    global study_timer_going
    print("Button 1 clicked.")
    if (study_timer_going):
        study_timer_going = 0
    else:
        study_timer_going = 1


def b1():
    print("Button 2 clicked.")
    global free_timer_going
    if (free_timer_going):
        free_timer_going = 0
    else:
        free_timer_going = 1


def sel():
    print("set")
    label.config(text=str(var.get()))


def help():
    ctypes.windll.user32.MessageBoxW(0,
                                     "Manage your time with this hackathon submission! Input your schedule in the settings tab, and then use the Freetimer tab to keep track of your study and free time each day.",
                                     "Help", 0)


def about():
    ctypes.windll.user32.MessageBoxW(0,
                                     "This was an entry to Tamuhack 2020 by Adam Taha, Cole Newby, and Joseph Buskmiller, It is simple software to help lazy students manage their time. It uses tkinter. \n\n Thanks for trying it out!",
                                     "What is this?", 0)


# needed widgets: frame, entry, button, tkmessagebox, text, labelframe

# Start Menu
root = Tk()
root.geometry("800x560")
root.minsize(500, 400)
# root.resizable(False,False)
root.title("Freetimer")
root['bg'] = '#dfe0e2'

# setting radio button values to integer
var = StringVar(value="main")

# frame
frametop = Frame(root)
frametop.place(relx=0, rely=0, relwidth=1, relheight=1)

# text boxes for timers
timer1 = Text(root, font=('Courier', 50))
# timer1.insert(INSERT, "12:44")
timer1.tag_configure("center", justify='center')
timer1.tag_add("center", 1.0, "end")

timer2 = Text(root, font=('Courier', 50))
# timer2.insert(INSERT, "12:44")
timer2.tag_configure("center", justify='center')
timer2.tag_add("center", 1.0, "end")

# timer buttons
tbutton1 = Button(root, text="Study Timer", command=b1)

tbutton2 = Button(root, text="Free Timer", command=b2)

timer1.pack()
timer2.pack()
tbutton1.pack()
tbutton2.pack()

timer1.place(relx=0.333 - 0.15, rely=0.5, relwidth=0.3, relheight=0.15)
timer2.place(relx=0.666 - 0.15, rely=0.5, relwidth=0.3, relheight=0.15)
tbutton1.place(relx=0.333 - 0.15, rely=0.7, relwidth=0.3, relheight=0.1)
tbutton2.place(relx=0.666 - 0.15, rely=0.7, relwidth=0.3, relheight=0.1)

M = Text(root, font=("Courier", 44))
M.insert(INSERT, "M", )
M.tag_configure("center", justify='center')
M.tag_add("center", 1.0, "end")
M['state'] = 'disabled'

T = Text(root, font=("Courier", 44))
T.insert(INSERT, "T", )
T.tag_configure("center", justify='center')
T.tag_add("center", 1.0, "end")
T['state'] = 'disabled'

W = Text(root, font=("Courier", 44))
W.insert(INSERT, "W", )
W.tag_configure("center", justify='center')
W.tag_add("center", 1.0, "end")
W['state'] = 'disabled'

Th = Text(root, font=("Courier", 44))
Th.insert(INSERT, "Th", )
Th.tag_configure("center", justify='center')
Th.tag_add("center", 1.0, "end")
Th['state'] = 'disabled'

F = Text(root, font=("Courier", 44))
F.insert(INSERT, "F", )
F.tag_configure("center", justify='center')
F.tag_add("center", 1.0, "end")
F['state'] = 'disabled'

S = Text(root, font=("Courier", 44))
S.insert(INSERT, "S", )
S.tag_configure("center", justify='center')
S.tag_add("center", 1.0, "end")
S['state'] = 'disabled'

Su = Text(root, font=("Courier", 44))
Su.insert(INSERT, "Su", )
Su.tag_configure("center", justify='center')
Su.tag_add("center", 1.0, "end")
Su['state'] = 'disabled'

M.pack()
T.pack()
W.pack()
Th.pack()
F.pack()
S.pack()
Su.pack()

M.place(relx=0.125 - 0.06, rely=0.1, relwidth=0.125, relheight=0.1)
T.place(relx=0.25 - 0.06, rely=0.1, relwidth=0.125, relheight=0.1)
W.place(relx=0.375 - 0.06, rely=0.1, relwidth=0.125, relheight=0.1)
Th.place(relx=0.5 - 0.06, rely=0.1, relwidth=0.125, relheight=0.1)
F.place(relx=0.625 - 0.06, rely=0.1, relwidth=0.125, relheight=0.1)
S.place(relx=0.75 - 0.06, rely=0.1, relwidth=0.125, relheight=0.1)
Su.place(relx=0.875 - 0.06, rely=0.1, relwidth=0.125, relheight=0.1)

L2 = Text(root, font=("Courier", 9))
L2.insert(INSERT, "Study \n Hours")
L2.tag_configure("center", justify='center')
L2.tag_add("center", 1.0, "end")
L2['state'] = 'disabled'

M2 = Text(root, font=("Courier", 22))
M2.insert(INSERT, "4")
M2.tag_configure("center", justify='center')
M2.tag_add("center", 1.0, "end")
M2['state'] = 'disabled'

T2 = Text(root, font=("Courier", 22))
T2.insert(INSERT, "4", )
T2.tag_configure("center", justify='center')
T2.tag_add("center", 1.0, "end")
T2['state'] = 'disabled'

W2 = Text(root, font=("Courier", 22))
W2.insert(INSERT, "4", )
W2.tag_configure("center", justify='center')
W2.tag_add("center", 1.0, "end")
W2['state'] = 'disabled'

Th2 = Text(root, font=("Courier", 22))
Th2.insert(INSERT, "4", )
Th2.tag_configure("center", justify='center')
Th2.tag_add("center", 1.0, "end")
Th2['state'] = 'disabled'

F2 = Text(root, font=("Courier", 22))
F2.insert(INSERT, "4", )
F2.tag_configure("center", justify='center')
F2.tag_add("center", 1.0, "end")
F2['state'] = 'disabled'

S2 = Text(root, font=("Courier", 22))
S2.insert(INSERT, "3", )
S2.tag_configure("center", justify='center')
S2.tag_add("center", 1.0, "end")
S2['state'] = 'disabled'

Su2 = Text(root, font=("Courier", 22))
Su2.insert(INSERT, "3", )
Su2.tag_configure("center", justify='center')
Su2.tag_add("center", 1.0, "end")
Su2['state'] = 'disabled'

L2.pack()
M2.pack()
T2.pack()
W2.pack()
Th2.pack()
F2.pack()
S2.pack()
Su2.pack()

L2.place(relx=0, rely=0.2, relwidth=0.06025, relheight=0.1)
M2.place(relx=0.125 - 0.06, rely=0.2, relwidth=0.125, relheight=0.1)
T2.place(relx=0.25 - 0.06, rely=0.2, relwidth=0.125, relheight=0.1)
W2.place(relx=0.375 - 0.06, rely=0.2, relwidth=0.125, relheight=0.1)
Th2.place(relx=0.5 - 0.06, rely=0.2, relwidth=0.125, relheight=0.1)
F2.place(relx=0.625 - 0.06, rely=0.2, relwidth=0.125, relheight=0.1)
S2.place(relx=0.75 - 0.06, rely=0.2, relwidth=0.125, relheight=0.1)
Su2.place(relx=0.875 - 0.06, rely=0.2, relwidth=0.125, relheight=0.1)

#
#
#

L3 = Text(root, font=("Courier", 9))
L3.insert(INSERT, "Free \n Hours")
L3.tag_configure("center", justify='center')
L3.tag_add("center", 1.0, "end")
L3['state'] = 'disabled'

M3 = Text(root, font=("Courier", 22))
M3.insert(INSERT, "3")
M3.tag_configure("center", justify='center')
M3.tag_add("center", 1.0, "end")
M3['state'] = 'disabled'

T3 = Text(root, font=("Courier", 22))
T3.insert(INSERT, "4", )
T3.tag_configure("center", justify='center')
T3.tag_add("center", 1.0, "end")
T3['state'] = 'disabled'

W3 = Text(root, font=("Courier", 22))
W3.insert(INSERT, "1", )
W3.tag_configure("center", justify='center')
W3.tag_add("center", 1.0, "end")
W3['state'] = 'disabled'

Th3 = Text(root, font=("Courier", 22))
Th3.insert(INSERT, "1", )
Th3.tag_configure("center", justify='center')
Th3.tag_add("center", 1.0, "end")
Th3['state'] = 'disabled'

F3 = Text(root, font=("Courier", 22))
F3.insert(INSERT, "2", )
F3.tag_configure("center", justify='center')
F3.tag_add("center", 1.0, "end")
F3['state'] = 'disabled'

S3 = Text(root, font=("Courier", 22))
S3.insert(INSERT, "6", )
S3.tag_configure("center", justify='center')
S3.tag_add("center", 1.0, "end")
S3['state'] = 'disabled'

Su3 = Text(root, font=("Courier", 22))
Su3.insert(INSERT, "4", )
Su3.tag_configure("center", justify='center')
Su3.tag_add("center", 1.0, "end")
Su3['state'] = 'disabled'

# (self, sleep, study, class_time, gym, transport, work, free)
Monday = classsss.SimpleDay(1, 1, 1, 1, 1, 1, 1)
Tuesday = classsss.SimpleDay(1, 1, 1, 1, 1, 1, 1)
Wednesday = classsss.SimpleDay(1, 1, 1, 1, 1, 1, 1)
Thursday = classsss.SimpleDay(1, 1, 1, 1, 1, 1, 1)
Friday = classsss.SimpleDay(1, 1, 1, 1, 1, 1, 1)
Saturday = classsss.SimpleDay(1, 1, 1, 1, 1, 1, 1)
Sunday = classsss.SimpleDay(1, 1, 1, 1, 1, 1, 1)

Week = [Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday]


def make_editable():
    # print("edit")
    M2['state'] = 'normal'
    T2['state'] = 'normal'
    W2['state'] = 'normal'
    Th2['state'] = 'normal'
    F2['state'] = 'normal'
    S2['state'] = 'normal'
    Su2['state'] = 'normal'
    M3['state'] = 'normal'
    T3['state'] = 'normal'
    W3['state'] = 'normal'
    Th3['state'] = 'normal'
    F3['state'] = 'normal'
    S3['state'] = 'normal'
    Su3['state'] = 'normal'


def make_uneditable():
    # print("no edit")
    M2['state'] = 'disabled'
    M2.tag_add("center", 1.0, "end")
    Monday.set_study(int(M2.get("1.0", "end")))
    T2['state'] = 'disabled'
    T2.tag_add("center", 1.0, "end")
    Tuesday.set_study(int(T2.get("1.0", "end")))
    W2['state'] = 'disabled'
    W2.tag_add("center", 1.0, "end")
    Wednesday.set_study(int(W2.get("1.0", "end")))
    Th2['state'] = 'disabled'
    Th2.tag_add("center", 1.0, "end")
    Thursday.set_study(int(Th2.get("1.0", "end")))
    F2['state'] = 'disabled'
    F2.tag_add("center", 1.0, "end")
    Friday.set_study(int(F2.get("1.0", "end")))
    S2['state'] = 'disabled'
    S2.tag_add("center", 1.0, "end")
    Saturday.set_study(int(S2.get("1.0", "end")))
    Su2['state'] = 'disabled'
    Su2.tag_add("center", 1.0, "end")
    Sunday.set_study(int(Su2.get("1.0", "end")))
    M3['state'] = 'disabled'
    M3.tag_add("center", 1.0, "end")
    Monday.set_free(int(M3.get("1.0", "end")))
    T3['state'] = 'disabled'
    T3.tag_add("center", 1.0, "end")
    Tuesday.set_free(int(T3.get("1.0", "end")))
    W3['state'] = 'disabled'
    W3.tag_add("center", 1.0, "end")
    Wednesday.set_free(int(W3.get("1.0", "end")))
    Th3['state'] = 'disabled'
    Th3.tag_add("center", 1.0, "end")
    Thursday.set_free(int(Th3.get("1.0", "end")))
    F3['state'] = 'disabled'
    F3.tag_add("center", 1.0, "end")
    Friday.set_free(int(F3.get("1.0", "end")))
    S3['state'] = 'disabled'
    S3.tag_add("center", 1.0, "end")
    Saturday.set_free(int(S3.get("1.0", "end")))
    Su3['state'] = 'disabled'
    Su3.tag_add("center", 1.0, "end")
    Sunday.set_free(int(Su3.get("1.0", "end")))
    # print(Monday.get_study())
    # print(Monday.get_free())


make_uneditable()

# top buttons
t1 = Radiobutton(frametop, text="Freetimer", variable=var, value="main", command=make_uneditable, indicatoron=0,
                 font=("Courier", 40))
t2 = Radiobutton(frametop, text="Schedule", variable=var, value="settings", command=make_editable, indicatoron=0,
                 font=("Courier", 40))

t1.pack()
t2.pack()

t1.place(relx=0, rely=0, relheight=0.1, relwidth=0.5)
t2.place(relx=0.5, rely=0, relheight=0.1, relwidth=0.5)

L3.pack()
M3.pack()
T3.pack()
W3.pack()
Th3.pack()
F3.pack()
S3.pack()
Su3.pack()

L3.place(relx=0, rely=0.3, relwidth=0.06025, relheight=0.1)
M3.place(relx=0.125 - 0.06, rely=0.3, relwidth=0.125, relheight=0.1)
T3.place(relx=0.25 - 0.06, rely=0.3, relwidth=0.125, relheight=0.1)
W3.place(relx=0.375 - 0.06, rely=0.3, relwidth=0.125, relheight=0.1)
Th3.place(relx=0.5 - 0.06, rely=0.3, relwidth=0.125, relheight=0.1)
F3.place(relx=0.625 - 0.06, rely=0.3, relwidth=0.125, relheight=0.1)
S3.place(relx=0.75 - 0.06, rely=0.3, relwidth=0.125, relheight=0.1)
Su3.place(relx=0.875 - 0.06, rely=0.3, relwidth=0.125, relheight=0.1)

my_date = datetime.date.today()
# prints the day
print(calendar.day_name[my_date.weekday()])

# variable weekday is 1 for monday-friday and 0 for saturday sunday

max_study_hours = 0
max_free_hours = 0

if (calendar.day_name[my_date.weekday()] != "Monday"):
    max_free_hours = Monday.get_free();
    max_study_hours = Monday.get_study();
elif (calendar.day_name[my_date.weekday()] != "Tuesday"):
    max_free_hours = Tuesday.get_free();
    max_study_hours = Tuesday.get_study();
elif (calendar.day_name[my_date.weekday()] != "Wednesday"):
    max_free_hours = Wednesday.get_free();
    max_study_hours = Wednesday.get_study();
elif (calendar.day_name[my_date.weekday()] != "Thursday"):
    max_free_hours = Thursday.get_free();
    max_study_hours = Thursday.get_study();
elif (calendar.day_name[my_date.weekday()] != "Friday"):
    max_free_hours = Friday.get_free();
    max_study_hours = Friday.get_study();
elif (calendar.day_name[my_date.weekday()] != "Saturday"):
    max_free_hours = Saturday.get_free();
    max_study_hours = Saturday.get_study();
else:
    max_free_hours = Sunday.get_free();
    max_study_hours = Sunday.get_study();


print("MAX FREE HOURS TODAY IS::::")
print(max_free_hours)

# variables for seconds on the timers rn
study_seconds = max_study_hours * 3600
free_seconds = max_free_hours * 3600

# variables for if the timer is paused or not
study_timer_going = 0
free_timer_going = 0

# variables for timer string content
study_string = "35"
free_string = "35"


def second():
    global study_seconds
    global free_seconds
    global study_timer_going
    global free_timer_going

    global study_string
    study_string = str(datetime.timedelta(seconds=study_seconds))
    global free_string
    free_string = str(datetime.timedelta(seconds=free_seconds))
    study_string = study_string[:-3]
    free_string = free_string[:-3]

    threading.Timer(1.0, second).start()
    print(study_seconds)
    print(study_timer_going)
    if (study_timer_going):
        print("blank")
        study_seconds = study_seconds - 1

    if (free_timer_going):
        print("blank")
        free_seconds = free_seconds - 1

    # set text from values of study_ and free_


second()  # start running second once a second


class A:
    def __init__(self, master):
        self.label = Label(master)
        self.label.grid(row=0, column=0)
        self.label.configure(text='nothing')
        self.count = 0
        self.update_label()

    def update_label(self):
        if self.count < 10:
            self.label.configure(text='count: {}'.format(self.count))
            self.label.after(1000, self.update_label)
            self.count += 1
            # print (self.count)
            print("yeah, it works")
            timer1.delete(1.0, END)
            timer1.insert(INSERT, free_string)
            timer2.delete(1.0, END)
            timer2.insert(INSERT, study_string)




A(root)

while True:
    root.update()