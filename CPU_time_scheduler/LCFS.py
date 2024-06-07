# Last Come First Serve

from imports import import_scheduling_data

data = import_scheduling_data()
i = 1

for curr in data:

    print(curr)
    stack = []
    stack_out = []
    obecne_trwanie = 0
    obecny_proces = 0
    czas = 0
    waiting_sum = 0
    turnover_sum = 0

    while curr or stack:


        if curr:
            if int(curr[0]["arrival_time"]) <= czas:
                stack.append(curr[0])
                curr.pop(0)

        if obecne_trwanie == 0 and stack:
            if int(stack[len(stack)-1]["arrival_time"]) <= czas:
                if obecny_proces != 0:
                    waiting_sum += czas - int(obecny_proces["burst_time"]) - int(obecny_proces["arrival_time"])
                    turnover_sum += czas - int(obecny_proces["arrival_time"])
                    stack_out.append(obecny_proces)
                obecny_proces = stack[len(stack)-1]
                obecne_trwanie = int(stack[len(stack)-1]["burst_time"])
                stack.pop(len(stack)-1)


        if obecne_trwanie != 0:
            obecne_trwanie -= 1

        czas += 1

    print(f"test: {i}")
    print(f"AVG waiting time: {waiting_sum/len(stack_out)}")
    print(f"AVG turnover time: {turnover_sum/len(stack_out)}")
    i += 1