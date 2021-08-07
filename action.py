import turtle
import numpy as np
import math
class Action(object):
    def __init__(self, name):
        self.name = name

    def full_projectile(self, v0x, v0y, x0=-200, y0=-200, g=9.8, step=.1):
        """
        :key Full projectile motion in SI
        :param v0x: initial horizontal velocity
        :param v0y: initial vertical velocity
        :param x0: initial horizontal position (default -200 m)
        :param y0: initial vertical position (default -200 m)
        :param g: acceleration due to gravity (default 9.8 m/s^2)
        :param step: graph time step (default .1s)
        :return: void
        """
        x = x0
        y = y0
        vx = v0x
        vy = v0y

        travel_time = 2 * abs(vy / g)

        projectile = turtle.Turtle(shape='circle')
        projectile.hideturtle()
        projectile.penup()
        projectile.setheading(90)
        projectile.goto(x,y)
        projectile.showturtle()
        projectile.pendown()
        projectile.stamp()

        times = np.arange(1, travel_time, step)

        for t in times:
            x = x0 + vx * t
            y = y0 + vy * t - g / 2 * t ** 2

            projectile.goto(x, y)

        turtle.exitonclick()

    def components(self, v, angle):
        """
        :param v: launch velocity (magnitude)
        :param angle: launch angle from horizontal (radians)
        :return: vx, vy
        """

        vy = float(v * np.sin(angle))
        vx = float(v * np.cos(angle))

        print('vx: ' + str(vx) + ' vy: ' + str(vy))

        return vx, vy


