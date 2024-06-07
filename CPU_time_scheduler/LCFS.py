# Last Come First Serve
import outports
from outports import outport


def last_come_first_serve(data):
    # outputting message to recognize currently used algorithm
    print("Now using Last Come First Serve")
    print("-" * 40)
    tests = 1

    for curr in data:
        # initializing all variables and arrays that will be used
        stack = []
        stack_out = []
        curr_burst_time = 0
        curr_process = False
        elapsed_time = 0

        # if anything is yet to be loaded or if anything is in stack
        while curr or stack:

            # if there is something to be loaded
            if curr:
                # if the thing to be loaded should be loaded
                if int(curr[0]["arrival_time"]) <= elapsed_time:
                    stack.append(curr[0])
                    curr.pop(0)

            # if current process ended and there is something in queue
            if curr_burst_time == 0 and stack:
                # if the next process in stack has already arrived
                if int(stack[len(stack)-1]["arrival_time"]) <= elapsed_time:
                    # to avoid using firstly implemented dummy data
                    if curr_process:
                        curr_process["waiting_time"] = elapsed_time - int(curr_process["burst_time"]) - int(curr_process["arrival_time"])
                        curr_process["turn_around_time"] = elapsed_time - int(curr_process["arrival_time"])
                        curr_process["whole_time"] = elapsed_time
                        stack_out.append(curr_process)
                    # setting new current process and its time
                    curr_process = stack[len(stack)-1]
                    curr_burst_time = int(stack[len(stack)-1]["burst_time"])
                    # pushing new "current process" out of stack
                    stack.pop(len(stack)-1)

            # checking if current burst time is 0 to avoid setting it below 0
            if curr_burst_time != 0:
                curr_burst_time -= 1

            # updating elapsed time
            elapsed_time += 1

        # at the end, adding final tick and final process to stack_out
        elapsed_time += 1
        curr_process["waiting_time"] = elapsed_time - int(curr_process["burst_time"]) - int(curr_process["arrival_time"])
        curr_process["turn_around_time"] = elapsed_time - int(curr_process["arrival_time"])
        curr_process["whole_time"] = elapsed_time
        stack_out.append(curr_process)

        # outputting data for tests
        print(f"test: {tests}")
        print(f"AVG waiting time: {sum(i['waiting_time'] for i in stack_out) / len(stack_out)}")
        print(f"AVG turnover time: {sum(i['turn_around_time'] for i in stack_out) / len(stack_out)}")
        print(f"AVG whole time: {sum(i['whole_time'] for i in stack_out) / len(stack_out)}")
        outports.outport("LCFS", tests, stack_out)
        tests+=1
