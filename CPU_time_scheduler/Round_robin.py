# Round Robin
import outports
from imports import *
from copy import deepcopy


# function used to determine if object with given id is already in array, and if so, returning it
def get_item_by_id(array, id):
    for i in array:
        if i["id"] == id:
            return i


def round_robin(data, fixed_quantum):
    # outputting message to recognize currently used algorithm
    print("Now using Round Robin")
    print("-" * 40)

    tests = 1
    # iterating through different test
    for curr in data:

        # making a deep copy of test for use in future
        arrival_queue = deepcopy(curr)

        # defining two arrays for final processes output
        data_out = []
        stack = []

        # assigning quantum to value given when calling function
        quantum = fixed_quantum

        # defining elapsed time
        elapsed_time = 0

        # making a loop to run for as long as there is data to be loaded or processed
        while arrival_queue or stack:

            # if anything needs to get processed
            if stack:
                # decrease burst time by one
                stack[0]["burst_time"] = int(stack[0]["burst_time"]) - 1

                # if burst time is zero add turn around time and waiting time to process, then add it to array for output data and reset quantum
                if int(stack[0]["burst_time"]) == 0:
                    stack[0]["done_time"] = elapsed_time
                    stack[0]["waiting_time"] = elapsed_time - int(stack[0]["arrival_time"]) - int((get_item_by_id(curr, stack[0]["id"]))["burst_time"])
                    stack[0]["turn_around_time"] = elapsed_time - int(stack[0]["arrival_time"])
                    stack[0]["whole_time"] = elapsed_time
                    data_out.append(stack[0])
                    quantum = fixed_quantum
                    stack.pop(0)

            # if there's anything yet to be loaded, and it's arrival time is now or have passed, load it
            if arrival_queue:
                if int(arrival_queue[0]["arrival_time"]) <= elapsed_time:
                    stack.append(arrival_queue[0])
                    arrival_queue.pop(0)

            # if quantum equals zero, reset it, and replace top task in stack
            if quantum == 0 and stack:
                quantum = fixed_quantum
                stack.append(stack[0])
                stack.pop(0)

            # increase elapsed time, and decrease quantum
            elapsed_time += 1
            quantum -= 1
        print(stack)

        print(data_out)
        # outputting test number, average turn around time and average waiting time
        print(f"Test number: {tests}")
        print(f"AVG turn around time: {sum(i['turn_around_time'] for i in data_out) / len(data_out)}")
        print(f"AVG waiting time: {sum(i['waiting_time'] for i in data_out) / len(data_out)}")
        print(f"AVG whole time: {sum(i['whole_time'] for i in data_out) / len(data_out)}")

        outports.outport("round_robin", tests, data_out)

        tests += 1
