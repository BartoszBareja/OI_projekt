import numpy
import os
import random
from tkinter import *
from tkinter import filedialog


def choose_path():
    filename = filedialog.askdirectory(initialdir=os.getcwd()+"/tests")
    path_variable.set(filename)


def generate_dataset():
    file = name_variable.get()
    arrival_time = [arrival_min_entry.get(), arrival_max_entry.get()]
    burst_time = [burst_min_entry.get(), burst_max_entry.get()]

    if len(file) > 3 or file[-4:] != ".csv":
        file += ".csv"

    write = open(str(path_variable.get())+"/"+file, "w")
    out = "id, arrival_time, burst_time\n"
    for i in range(1, int(processes_num_entry.get())+1):
        curr = (f'{i},{random.randint(int(arrival_time[0]), int(arrival_time[1]))},'
                f'{random.randint(int(burst_time[0]), int(burst_time[1]))} ')

        out += curr + "\n"

    write.write(out)

    write.close()

    windows.destroy()


windows = Tk()

path_variable = StringVar()
name_variable = StringVar()

path_label = Label(windows, text="Please input path to store your csv file")
path_localisation = Entry(windows, textvariable=path_variable)
path_button = Button(windows, text="Choose path for your csv", command=choose_path)

name_label = Label(windows, text="Please input name for data file")
name_entry = Entry(windows, textvariable=name_variable)

processes_num_label = Label(windows, text="Please input amount of processes in file")
processes_num_entry = Entry(windows, )

arrival_label1 = Label(windows, text="Please input/select min time for your processes")
arrival_min_radio1 = Radiobutton(windows, text="0")
arrival_min_radio2 = Radiobutton(windows, text="25")
arrival_min_entry = Entry(windows, )

arrival_label2 = Label(text="Please input/select max time for your processes")
arrival_max_radio1 = Radiobutton(windows, text="50")
arrival_max_radio2 = Radiobutton(windows, text="100")
arrival_max_entry = Entry(windows, )

burst_label1 = Label(windows, text="Please input/select min burst time for your processes")
burst_min_radio1 = Radiobutton(windows, text="0")
burst_min_radio2 = Radiobutton(windows, text="25")
burst_min_entry = Entry(windows, )

burst_label2 = Label(text="Please input/select max burst time for your processes")
burst_max_radio1 = Radiobutton(windows, text="50")
burst_max_radio2 = Radiobutton(windows, text="100")
burst_max_entry = Entry(windows, )

gen_button = Button(windows, text="Generate data", command=generate_dataset)

for i in windows.children:
    windows.children[i].pack()

windows.mainloop()
