from random import choice
class RandomWalk():
    def __init__(self,num_points=5000):
        self.num_points=num_points
        self.xvalue=[0]
        self.yvalue=[0]
    def fill_walk(self):
        while len(self.xvalue)<self.num_points:
            x_direction =choice([1,-1])
            x_distance =choice([0,1,2,3,4])
            x_step=x_distance*x_direction
            y_direction =choice([1,-1])
            y_distance=choice([0,1,2,3,4])
            y_step=y_distance*y_direction

            if x_step==0 and y_step==0:
                continue
            next_x = self.xvalue[-1] + x_step
            next_y = self.yvalue[-1] + y_step

            self.xvalue.append(next_x)
            self.yvalue.append(next_y)


