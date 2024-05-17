import numpy
import random

def generate_dataset():
    print("Enter the name for a file containing output data (in csv format)")
    file = input()

    print("How many example processes do you want to have in file")

    try:
        processes_num = int(input())
    except:
        print("Given number is incorrect")
        return

    if len(file) > 3 or file[-4:] != ".csv":
        file += ".csv"

    write = open(file, "w")

    for i in range(processes_num):
        print(i)

    write.close()