from CPU_time_scheduler import FCFS
from CPU_time_scheduler import Round_robin
from CPU_time_scheduler import LCFS
from Page_replacement import MFU
from Page_replacement import LRU
from imports import *

data_scheduling = import_scheduling_data()
replacement_data = import_replacement_data()

Round_robin.round_robin(data_scheduling, 4)
#MFU.most_frequently_used(replacement_data, 4)
#FCFS.first_come_first_serve(data_scheduling)
#LCFS.last_come_first_serve(data_scheduling)