# Author: Justine
# purpose: System class file
# date: 22/10?2022


from body import Body
from math import sqrt

G = 6.67384e-11

class System:
    # creates the instance body_list
    def __init__(self, body_list):
        self.body_list = body_list


    # updates bodies the bodies in the list
    def update(self, timestep):
        for body in self.body_list:
            body.update_position(timestep)

        for body in self.body_list:
            (ax, ay) = self.compute_acceleration(body)
            body.update_velocity(ax, ay, timestep)

    # draws the bodies
    def draw(self, cx, cy, pixel_per_meter):
        for body in self.body_list:
            body.draw(cx, cy, pixel_per_meter)

    def compute_acceleration(self, t_body):
        global G
        total_ax = 0
        total_ay = 0
        body_x = t_body.get_x()
        body_y= t_body.get_y()

        for o_body in self.body_list:
            if o_body is not t_body:
                dx= o_body.get_x() - body_x
                dy= o_body.get_y() - body_y

                distance = sqrt(dx*dx +dy*dy)

                acelleration= G * o_body.get_mass() / (distance * distance)

                ax= acelleration*dx/distance
                total_ax=total_ax + ax
                ay = acelleration * dy / distance
                total_ay= total_ay + ay
                print(acelleration)
        return (total_ax, total_ay)

