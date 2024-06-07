import numpy
import os
import random
from tkinter import *
from tkinter import filedialog
from operator import itemgetter


# function to ask for directory to save file
def choose_path():
    filename = filedialog.askdirectory(initialdir=os.getcwd() + "/replacement_tests/test1.csv")
    path_variable.set(filename)


#function to generate pages
def generate_dataset():
    #recieving file name
    file = name_variable.get()

    #adding pages min and max to array
    pages_num = [int(pages_num_min_entry.get()), int(pages_num_max_entry.get())]

    #adding .csv at the end of file
    if len(file) > 3 or file[-4:] != ".csv":
        file += ".csv"

    #opening file
    write = open(str(path_variable.get()) + "/" + file, "w")

    #adding first page with coma, so it doesn't brake the others
    out = f"{random.randint(pages_num[0], pages_num[1])}"

    #generating rest of pages
    for i in range(int(pages_num_entry.get())):
        out += f",{random.randint(pages_num[0], pages_num[1])}"

    write.write(out)

    write.close()

    windows.destroy()


#initializing generator's main window
windows = Tk()

#creating variables to store name and path of file
path_variable = StringVar()
name_variable = StringVar()

#asking for file path
path_label = Label(windows, text="Please input path to store your csv file")
path_localisation = Entry(windows, textvariable=path_variable)
path_button = Button(windows, text="Choose path for your csv", command=choose_path)

#asking for file name
name_label = Label(windows, text="Please input name for data file")
name_entry = Entry(windows, textvariable=name_variable)

#asking for quantity of pages
pages_num_label = Label(windows, text="Please input amount of pages in file")
pages_num_entry = Entry(windows, )

#asking for min number of pages
pages_num_label1 = Label(windows, text="Please input/select min num for your pages")
pages_num_min_entry = Entry(windows, )

#asking for max number of pages
pages_num_label2 = Label(text="Please input/select max num for your pages")
pages_num_max_entry = Entry(windows, )

#generating button
gen_button = Button(windows, text="Generate data", command=generate_dataset)

#adding all GUI elements to window
for i in windows.children:
    windows.children[i].pack()

windows.mainloop()
