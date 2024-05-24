#Last Come First Serve

from main import *

data = import_data()

print(data)

for curr in data:
    stack = []
    current_burst_time = 0

    for i in curr:
        print(i)

        if int(i["arrival_time"]) <= current_burst_time:
            stack.append(i)
            current_burst_time -= int(i["arrival_time"])
        else:
            current_burst_time = int(stack[len(stack)-1]["burst_time"])

            while int(i["arrival_time"]) <= current_burst_time:
                stack.pop()
                current_burst_time = int(stack[len(stack)-1]["burst_time"])

            stack.append(i)

    print(stack)
