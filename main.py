import os


def import_data():
    data_out = []
    files = os.listdir("../tests")

    for file in files:
        curr = open(f"../tests/{file}", "r")

        lines = curr.readlines()
        tmp = []
        for i in lines:
            tmp.append(i.strip().split(","))

        data_out.append(tmp)

    return data_out
