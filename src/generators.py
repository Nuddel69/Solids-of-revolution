import numpy as np
from math import radians, cos, sin

from core import Shape


class Generators:
    __all__ = [
        'cube',
        'sphere',
        'function',
    ]


    @staticmethod
    def cube(radius: int = 1, iterations: int = 1) -> Shape:
        vertices = []
        edges = []

        for i in range(2):
            dist = radius if i else -radius
            for j in range(4):
                point = [dist for _ in range(3)]
                if j:
                    point[j-1] = -dist
                
                vertices.append(np.array(point))
        
        for i in range(3):
            edges.append([0, i+1])
            edges.append([4, i+5])
        
        for i in range(2):
            edges.append([1, 6+i])
            edges.append([2, 5+(i*2)])
            edges.append([3, 5+i])

        return vertices, edges
        

    @staticmethod
    def sphere(radius: int = 2, rings: int = 30) -> Shape:
        vertices = []
        edges = []

        for vertical in range(rings):
            v_angle = radians((360 / rings) * vertical)
            for horizontal in range(rings):
                h_angle = radians((360 / rings) * horizontal)

                x = radius * cos(v_angle) * cos(h_angle)
                y = radius * cos(v_angle) * sin(h_angle)
                z = radius * sin(v_angle)

                vertices.append(np.array((x, y, z)))

        return vertices, edges

    @staticmethod
    def function(func, a: int = 0, b: int = 50) -> Shape:
        vertices = [];
        edges = [];

        for vertical in range(a, b):

            for horizontal in range((b-a)):
                h_angle = radians((360 / (b * 100 - a * 100)) * horizontal * 100)

                # x = func(vertical) * cos(v_angle) * cos(h_angle)
                # y = func(vertical) * cos(v_angle) * sin(h_angle)
                # z = horizontal

                x = (-func(vertical) * sin(h_angle)) / 2
                y = (func(vertical) * cos(h_angle)) / 2
                z = vertical / 2

                vertices.append(np.array((x, y, z)))

        return vertices, edges
