import os


def import_data():
    data_out = []
    files = os.listdir("../tests")

    for file in files:
        curr = open(f"../tests/{file}", "r")

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
