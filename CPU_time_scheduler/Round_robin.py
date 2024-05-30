# Round Robin

from main import *
from copy import deepcopy


def get_item_from_array_by_id(array, id):
    for i in array:
        if i["id"] == id:
            return i


FIXED_QUANTUM = 5

data = import_data()[0]
arrival_queue = deepcopy(data)
data_out = []

stack = []

quantum = FIXED_QUANTUM

elapsed_time = 0


while arrival_queue or stack:

    removed = False

    if stack:
        stack[0]["burst_time"] = int(stack[0]["burst_time"]) - 1

        if int(stack[0]["burst_time"]) <= 0:
            stack[0]["done_time"] = elapsed_time
            stack[0]["waiting_time"] = elapsed_time - int(stack[0]["arrival_time"]) - int((get_item_from_array_by_id(data, stack[0]["id"]))["burst_time"])
            data_out.append(stack[0])
            print(f"For process: {stack[0]['id']}: {elapsed_time}")
            print(quantum)
            quantum = FIXED_QUANTUM
            stack.pop(0)
            removed = True

    if arrival_queue:
        if int(arrival_queue[0]["arrival_time"]) <= elapsed_time:
            stack.append(arrival_queue[0])
            arrival_queue.pop(0)

    if quantum == 0 and stack:
        # stack[0]["burst_time"] = int(stack[0]["burst_time"]) - 1
        quantum = FIXED_QUANTUM
        if not removed:
            stack.append(stack[0])
            stack.pop(0)

    elapsed_time += 1
    quantum -= 1
    print(stack)
    print(data_out)
    print("_" * 20)

sum = 0
for i in data_out:
    print(i["waiting_time"])
    sum += int(i["waiting_time"])

print(data_out)

print(sum / len(data_out))
