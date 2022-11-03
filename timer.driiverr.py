#Author : Justine Moturi
#Purpose: To wwrite a timer
# Date: 10/16/2022


from timer import Timer

timer = Timer(1,60,0)
timer.tick()

for time in range(5400):
    print(timer.is_zero())
    print(timer)
    timer.tick()


