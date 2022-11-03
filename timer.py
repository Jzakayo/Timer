#Author: Justine Moturi
# PURPOSE: Driver file
# Date: 10/15/2022

from counter import Counter
#timer with hours and minutes
class Timer:

    def __init__(self, hours, minutes, seconds):
        self.hours = Counter(24, hours,2)
        self.minutes = Counter(60, minutes,2)
        self.seconds= Counter(60, seconds,2)

#returns the strings of the counter value with hours minutes and seconds


    def is_zero(self):
         self.hours.get_value() and self.minutes.get_value() and self.seconds.get_value()
         return "Time"
        # else:
        #     return False
#decrements the seconds then minutes then hours by calling tick once each of the limits are reached
    def tick(self):
        if self.seconds.tick():
            if self.minutes.tick():
                self.hours.tick()

    def __str__(self):
        return str(self.hours) +":" +str(self.minutes) +":" +str(self.seconds)
