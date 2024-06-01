from CPU_time_scheduler import FCFS
from CPU_time_scheduler import Round_robin
from Page_replacement import MFU
from imports import *

data_scheduling = import_scheduling_data()
replacement_data = import_replacement_data()

#Round_robin.round_robin(data_scheduling, 5)
MFU.most_frequently_used(replacement_data, 5)