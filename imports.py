import os


# function to import scheduling data
def import_scheduling_data():
    # initializing array to store data to import
    data_out = []

    # getting an array of files in given path
    files = os.listdir("./scheduling_tests")

    # iterating through files and adding them to dict, which later is being added to output data
    for file in files:
        curr = open(f"./scheduling_tests/{file}", "r")

        header = curr.readline().strip().split(",")

        lines = curr.readlines()
        tmp = []
        for i in lines:
            i = i.strip().split(",")
            tmp2 = {
                header[0].strip(): i[0],
                header[1].strip(): i[1],
                header[2].strip(): i[2]
            }

            tmp.append(tmp2)

        data_out.append(tmp)

    return data_out


# function to import replacement data
def import_replacement_data():
    # initializing array to store data to import
    data_out = []

    # getting an array of files in given path
    files = os.listdir("./replacement_tests")

    # iterating through files and adding them to array, which later will  be added to output data
    for file in files:
        curr = open(f"./replacement_tests/{file}", "r")
        lines = curr.readlines()

        for line in lines:
            data_out.append(line.strip().split(","))

    return data_out
