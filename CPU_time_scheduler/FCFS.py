# First Come First Serve

from outports import outport

# defining function
def first_come_first_serve(data_sets):
    # outputting message to recognize currently used algorithm
    print("Now using First Come First Serve")
    print("-" * 40)

    # variable test is used to recognize different scheduling_tests output
    tests = 1

    # iterating through different test
    for curr in data_sets:


        # defining elapsed time
        elapsed_time = 0

        # iterating through different processes
        for i in curr:

            # if arrival time is yet to pass, we're adding to elapsed time
            if elapsed_time < int(i['arrival_time']):
                elapsed_time += (int(i["arrival_time"]) - elapsed_time)

            # calculating waiting time for each task
            i["waiting_time"] = elapsed_time - int(i["arrival_time"])

            # adding burst time of task to elapsed time
            elapsed_time += int(i["burst_time"])

            # calculating turn around time for each task
            i["turn_around_time"] = elapsed_time - int(i["arrival_time"])
            i["whole_time"] = elapsed_time

        # outputing test number, average turn around time and average waiting time
        print(f"Test number: {tests}")
        print(f"AVG waiting time: {sum(i['waiting_time'] for i in curr) / len(curr)}")
        print(f"AVG turnaround time: {sum(i['turn_around_time'] for i in curr) / len(curr)}")
        print(f"AVG whole time: {sum(i['whole_time'] for i in curr) / len(curr)}")
        outport("FCFS",tests, curr)
        tests += 1
