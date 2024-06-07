from CPU_time_scheduler import FCFS
from CPU_time_scheduler import Round_robin
from CPU_time_scheduler import LCFS
from Page_replacement import MFU
from Page_replacement import LRU
from imports import *

data_scheduling = import_scheduling_data()
replacement_data = import_replacement_data()

# below are commented implemented algorithms, uncomment and fill additional parameters if needed
# round-robin's second parameter is quantum size
# page replacement algorithms second parameter is buffer size

#Round_robin.round_robin(data_scheduling, 10)
#FCFS.first_come_first_serve(data_scheduling)
#LCFS.last_come_first_serve(data_scheduling)
MFU.most_frequently_used(replacement_data, 2)
LRU.least_recently_used(replacement_data, 2)
