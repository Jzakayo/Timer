#Author : Justine Moturi
#Purpose: To wwrite a timer
# Date: 10/16/2022


#creating class counter
class Counter:
    def __init__(self, limit, initial = 0, min_digits = 1) : #creating adressess for the intance variables for the counter
        self.limit = limit
        self.minute = min_digits

        if 0 <= initial <= self.limit - 1: # setting my initial value to any supplied value between 0 and 60
            self.current = initial

        else:
            self.current = self.limit-1 # resets limit to 59


    def get_value(self):# returns the value of the initial as an integer
        return self.current

    def __str__(self):# returns the counter value as a string and pads it with zeros to make the string 4 digits
        digit = 0
        if self.minute > len(str(self.current)):
            digit = self.minute - len(str(self.current))

        return "0" * digit + str(self.current)



    def tick(self): # decrements the counter value

        if self.current == 0:
            self.current = self.limit - 1
            return True
        else:
            self.current = self.current - 1
            return False









