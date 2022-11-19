import numpy as np
from math import radians, cos, sin

from core import Shape
from solid_of_revolution import Revolution_function


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
    def function(accuracy: int = 300) -> Shape:
        _func = Revolution_function();
        func = _func.f_main;
        a: int = _func._a;
        b: int = _func._b;

        vertices = [];
        edges = [];

        for x_val in range(a, b + 1):

            for increment in range(0, accuracy):
                θ = radians((360 / accuracy) * increment)

                x = (-func(x_val) * sin(θ)) / 3
                y = (func(x_val) * cos(θ)) / 3
                z = x_val / 3

                vertices.append(np.array((x, y, z)))

        return vertices, edges
