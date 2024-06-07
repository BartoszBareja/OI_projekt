import numpy
import os
import random
from tkinter import *
from tkinter import filedialog
from operator import itemgetter


def choose_path():
    filename = filedialog.askdirectory(initialdir=os.getcwd() + "/replacement_tests/test1.csv")
    path_variable.set(filename)


def generate_dataset():
    file = name_variable.get()

    pages_num = [int(pages_num_min_entry.get()), int(pages_num_max_entry.get())]

    if len(file) > 3 or file[-4:] != ".csv":
        file += ".csv"

    write = open(str(path_variable.get()) + "/" + file, "w")
    out = f"{random.randint(pages_num[0], pages_num[1])}"

    for i in range(int(pages_num_entry.get())):
        out += f",{random.randint(pages_num[0], pages_num[1])}"

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

pages_num_label = Label(windows, text="Please input amount of pages in file")
pages_num_entry = Entry(windows, )

pages_num_label1 = Label(windows, text="Please input/select min num for your pages")
pages_num_min_entry = Entry(windows, )

pages_num_label2 = Label(text="Please input/select max num for your pages")
pages_num_max_entry = Entry(windows, )

gen_button = Button(windows, text="Generate data", command=generate_dataset)

for i in windows.children:
    windows.children[i].pack()

windows.mainloop()
