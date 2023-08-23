'''
this module is to guide the car to the destination
ref: https://math.stackexchange.com/questions/256100/how-can-i-find-the-points-at-which-two-circles-intersect


'''

import math
import numpy as np


class Circle:
    '''
    Literally, circle.
    '''
    def __init__(self, coor: tuple[float, float], radius: float):
        self.radius = radius
        self.center = np.array(coor)

    @staticmethod
    def get_intersection(circle1: 'Circle', circle2: 'Circle', circle3: 'Circle'):
        x1, y1 = circle1.center
        x2, y2 = circle2.center
        x3, y3 = circle3.center
        d = np.sqrt(np.sum(np.square(circle1.center - circle2.center)))

        if d > circle1.radius + circle2.radius:
            return 'too apart'
        elif (d < circle1.radius - circle2.radius) or (d < circle2.radius - circle1.radius):
            return 'too close'
        else:            
            l = (circle1.radius**2 - circle2.radius**2 + d**2) / (2*d)
            h = np.sqrt(circle1.radius**2 - l**2)

            temp_a = l/d*(x2-x1)
            temp_b = h/d*(y2-y1)
            temp_c = l/d*(y2-y1)
            temp_d = h/d*(x2-x1)
            intersect_candidate_1_x = temp_a + temp_b + x1
            intersect_candidate_1_y = temp_c - temp_d + y1
            intersect_candidate_2_x = temp_a - temp_b + x1
            intersect_candidate_2_y = temp_c + temp_d + y1
            
            error1 = np.abs((x3 - intersect_candidate_1_x)**2 + (y3 - intersect_candidate_1_y)**2 - circle3.radius**2)
            error2 = np.abs((x3 - intersect_candidate_2_x)**2 + (y3 - intersect_candidate_2_y)**2 - circle3.radius**2)

            return (intersect_candidate_1_x, intersect_candidate_1_y) if error1 < error2 else (intersect_candidate_2_x, intersect_candidate_2_y)


# aa = Circle((2,0), 4)
# bb = Circle((-3,0), 3)
# cc = Circle((-1,4), 4.1)

# print(Circle.intersection_case(aa, bb, cc))
