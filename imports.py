import os


def import_scheduling_data():
    data_out = []
    files = os.listdir("./scheduling_tests")

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


def import_replacement_data():
    data_out = []
    files = os.listdir("./replacement_tests")

    print(files)

    for file in files:
        curr = open(f"./replacement_tests/{file}", "r")
        lines = curr.readlines()
        print(lines)

    for line in lines:
        data_out.append(line.strip().split(","))

    return data_out
