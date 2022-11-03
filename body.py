# Author: Justine
# purpose: planet class file
# date: 22/10?2022
from cs1lib import *


class Body:
    # creating instance varriable for the bodies
    def __init__(self, mass, x, y, v_x, v_y, pixel_radius, r, g, b):
        self.mass = mass
        self.x = x
        self.y = y
        self.v_x = v_x
        self.v_y = v_y

        self.r = r
        self.g = g
        self.b = b
        self.pixel_radius = pixel_radius

    # updates the position of the bodies
    def update_position(self, timestep):
        self.x = self.x + self.v_x * timestep
        self.y = self.y + self.v_y * timestep

    # updates the velocities of the bodies based on the accelaration
    def update_velocity(self, ax, ay, timestep):
        self.v_x = self.v_x + ax * timestep
        self.v_y = self.v_y + ay * timestep

    # draws the position of the bodies
    def draw(self, cx, cy, pixel_per_meter):
        pixel_x = cx + self.x * pixel_per_meter
        pixel_y = cy + self.y * pixel_per_meter
        pixel_r = self.pixel_radius

        set_fill_color(self.r, self.g, self.b)
        draw_circle(pixel_x, pixel_y, pixel_r)

    #gets the x values of the bodies
    def get_x(self):
        return self.x

    #gets the y values of the vodies
    def get_y(self):
        return self.y

    def get_mass(self):
        return self.mass

