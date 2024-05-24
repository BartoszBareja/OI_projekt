# First Come First Serve

import os
from main import *

data = import_data()

print(data)

for curr in data:
    elapsed_time = 0
    waiting_times = []
    turn_around_times = []

    for i in curr:
        print(i)
        waiting_times.append(elapsed_time - int(i["arrival_time"]))
        if elapsed_time < int(i['arrival_time']):
            elapsed_time += (int(i["arrival_time"]) - elapsed_time)

        elapsed_time += int(i["burst_time"])
        turn_around_times.append(elapsed_time - int(i["arrival_time"]))

        print(elapsed_time)
        print(f"AVG turn around time: {sum(turn_around_times)/len(turn_around_times)}")
        print(f"AVG waiting time: {sum(waiting_times)/len(waiting_times)}")


