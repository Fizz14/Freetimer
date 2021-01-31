'''Class day

Use numbers for going through each one
have other '''

class Day:
    # initilizes class
    def __init__(self, sleep, study, class_time, gym, transport, work):
        self.sleep = sleep
        self.study = study
        self.class_time = class_time
        self.gym = gym
        self.transport = transport
        self.work = work
    def free_time(self):
        total_time = 24
        time_used = self.sleep + self.study + self.class_time + self.gym + self.transport + self.work
        free_time_for_day = total_time - time_used
        return free_time_for_day

class SimpleDay:
    # initilizes class
    def __init__(self, sleep, study, class_time, gym, transport, work, free):
        self.study = study
        self.free = free
    def get_study(self):
        return self.study
    def get_free(self):
        return self.free
    def set_study(self, valueToSet):
        self.study = valueToSet
    def set_free(self, valueToSet):
        self.free = valueToSet
