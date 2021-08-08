import turtle
import numpy as np
import math
import stats


class Projectile(object):
    def __init__(self, v0x, v0y, x0=-200, y0=-200, g=9.8, step=.1, zoom = 100):
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
        self.stats = stats.Stats() #card generation, file management

        self.x_vals = []
        self.y_vals = []
        self.x = x0
        self.y = y0
        self.vx = v0x
        self.vy = v0y

        self.travel_time = 2 * abs(self.vy / g)



        self.times = np.arange(1, self.travel_time, step)

        for t in self.times:
            self.x_vals.append(self.x)
            self.y_vals.append(self.y)
            self.x = x0 + self.vx * t
            self.y = y0 + self.vy * t - g / 2 * t ** 2



        #print(self.times)
        #print(self.x_vals)
        #print(self.y_vals)





    def run(self):
        projectile = turtle.Turtle(shape='circle')
        projectile.hideturtle()
        projectile.penup()
        projectile.setheading(90)
        projectile.goto(self.x_vals[0], self.y_vals[0])
        projectile.showturtle()
        projectile.pendown()
        projectile.stamp()

        for i in range(len(self.x_vals)):
            projectile.goto(self.x_vals[i], self.y_vals[i])

        turtle.exitonclick()

    def generate(self, writeToFile=False):
        range = self.x_vals[-1] - self.x_vals[0]

        maxh = max(self.y_vals)

        return self.stats.getcard([['Range', range],
                            ['Maximum Height', maxh]])


    def full_data(self):
        pass


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
        x_vals = []
        y_vals = []
        x = x0
        y = y0
        vx = v0x
        vy = v0y

        travel_time = 2 * abs(vy / g)

        projectile = turtle.Turtle(shape='circle')
        projectile.hideturtle()
        projectile.penup()
        projectile.setheading(90)
        projectile.goto(x, y)
        projectile.showturtle()
        projectile.pendown()
        projectile.stamp()

        times = np.arange(1, travel_time, step)

        for t in self.times:
            x_vals.append(x)
            y_vals.append(y)
            x = x0 + vx * t
            y = y0 + vy * t - g / 2 * t ** 2

            projectile.goto(x, y)

        #print(times)
        #print(x_vals)
        #print(y_vals)



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

#TEST
a = Projectile(20,88)
#a.run()
print(a.generate())
#a.full_projectile(20, 88)
