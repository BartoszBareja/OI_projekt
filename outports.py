#defning function to outport data in csv files
def outport(algorithm, number, processes):
    #opening file, which name is created from given parameters
    file = open(f"./scheduling_tests_out/test{number}_{algorithm}.csv", 'w')

    # adding csv headers
    file.write("id, arrival_time, waiting_time, turn_around_time, whole_time\n")

    # writing actual data to file, iterating through each process and getting specific value
    for i in processes:
        curr = f"{i['id']}, {i['arrival_time']}, {i['waiting_time']}, {i['turn_around_time']}, {i['whole_time']}\n"
        file.write(curr)

    # closeing file
    file.close()