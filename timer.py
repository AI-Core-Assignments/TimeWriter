import datetime
from datetime import timedelta
import time# %%
class Timer():
    def __init__(self, start_time = None, time_ellapsed = None):
        self.start_time = start_time
        self.time_ellapsed = time_ellapsed   
    def start_timer(self):
        self.start_time = datetime.datetime.now() # getting the start timepoint
        print('Start time: ',  self.start_time)
        return self.start_time    
    def end_timer(self):
        self.time_ellapsed =  datetime.datetime.now() # getting the end timepoint
        print('End time: ',  self.time_ellapsed)
        return self.time_ellapsed    
    def formatting_seconds(self):
        time_difference = timedelta.total_seconds(self.time_ellapsed - self.start_time)
        print("{} seconds".format(time_difference))
        
timer = Timer()
timer.start_timer()
timer.end_timer()
timer.formatting_seconds()