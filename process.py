class Process:
    """
    To store-
        process ID, 
        arrival times, 
        burst time, 
        completion time, 
        turnaround time, 
        and waiting time. 
    """
    
    def __init__(self, id, at, bt):
        self.id = id
        self.arrival_time = at
        self.burst_time = bt
        self.completion_time = None
        self.turnaround_time = None
        self.waiting_time = None
    
    def get_id(self):
        return self.id
    
    def arrivalTime(self):
        return self.arrival_time

    def burstTime(self):
        return self.burst_time
    
    def completionTime(self):
        return self.completion_time

    def turnaroundTime(self):
        return self.turnaround_time
    
    def waitingTime(self):
        return self.waiting_time