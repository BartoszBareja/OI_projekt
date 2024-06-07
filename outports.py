def outport(algorithm, number, processes):
    file = open(f"./scheduling_tests_out/test{number}_{algorithm}.csv", 'w')
    file.write("id, arrival_time, waiting_time, turn_around_time, turn_around_time, whole_time\n")
    for i in processes:
        curr = f"{i['id']}, {i['arrival_time']}, {i['waiting_time']}, {i['turn_around_time']}, {i['whole_time']}\n"
        file.write(curr)
    file.close()