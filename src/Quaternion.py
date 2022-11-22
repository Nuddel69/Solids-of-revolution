import numpy as np
from math import sin, cos, radians

from typing import Union, Tuple, Sequence

Numeric = Union[int, float]

Rotation = Tuple[Numeric, Numeric, Numeric]
Edges = Sequence[Tuple[int, int]]
Vertices = Sequence[np.ndarray]

Shape = Tuple[Vertices, Edges]

class Quaternion:
    def __init__(self) -> None:
        self._w = 0;
        self._x = 0;
        self._y = 0;
        self._z = 0;
        self._val = (self._w, self._x, self._y, self._z);

    def get_conjugate(self):
        w, x, y, z = self._val;
        result = Quaternion.from_value(np.array((w, -x, -y, -z)));
        return result;

    def updateLocal(self):
        self._w = self._val[0];
        self._x = self._val[1];
        self._y = self._val[2];
        self._z = self._val[3];

    def __mul__(self, b):

        if isinstance(b, Quaternion):
            return self._multiply_with_quaternion(b);
        elif isinstance(b, (list, tuple, np.ndarray)):
            if len(b) != 3:
                raise Exception(f"Input vector has invalid length {len(b)}");
            return self._multiply_with_vector(b);
        else:
            raise Exception(f"Multiplication with unknown type {type(b)}");

    def __add__(self, b: Quaternion):
        if isinstance(b, Quaternion):
            self.updateLocal();
            b.updateLocal();
            self.add_quaternion(self, b);
        else:
            raise Exception(f"Addition with unknown type {type(b)}")
        pass

    def add_quaternion(a: Quaternion, b: Quaternion):
        pass

    def q_from_axisangle(self, v, theta):
        v = normalise(v);
        x, y, z = v;
        theta /= 2.;

        w = cos(theta);
        x = x * sin(theta);
        y = y * sin(theta);
        z = z * sin(theta);

        self._val = np.array((w, x, y, z));
        self.updateLocal();

    def q_to_axisangle(q):
        w, v = q._w, q._val[1:]
        theta = acos(w) * 2.0
        return normalise(v), theta

    def from_value(value):
        new_quaternion = Quaternion()
        new_quaternion._val = value
        return new_quaternion

    def _multiply_with_quaternion(self, q2):
        w1, x1, y1, z1 = self._val
        w2, x2, y2, z2 = q2._val
        w = w1 * w2 - x1 * x2 - y1 * y2 - z1 * z2
        x = w1 * x2 + x1 * w2 + y1 * z2 - z1 * y2
        y = w1 * y2 + y1 * w2 + z1 * x2 - x1 * z2
        z = w1 * z2 + z1 * w2 + x1 * y2 - y1 * x2

        result = Quaternion.from_value(np.array((w, x, y, z)))
        return result

    def _multiply_with_vector(self, v):
        q2 = Quaternion.from_value(np.append((0.0), v))
        return (self * q2 * self.get_conjugate())._val[1:]

    def __repr__(self):
        theta, v = self.get_axisangle()
        return f"((%.6f; %.6f, %.6f, %.6f))"%(theta, v[0], v[1], v[2])

    def get_axisangle(self):
        w, v = self._val[0], self._val[1:]
        theta = acos(w) * 2.0

        return theta, normalise(v)

    def tolist(self):
        return self._val.tolist()

    def vector_norm(self):
        w, v = self.get_axisangle()
        return np.linalg.norm(v)

    def euler_to_quaternion(self, rotation):
        radRotation = [];
        radRotation.append(radians(rotation[0]));
        radRotation.append(radians(rotation[1]));
        radRotation.append(radians(rotation[2]));
        
        r = normalise(radRotation);
        phi = r[0];
        theta = r[1];
        psi = r[2];

        qw = cos(phi/2) * cos(theta/2) * cos(psi/2) + sin(phi/2) * sin(theta/2) * sin(psi/2);
        qx = sin(phi/2) * cos(theta/2) * cos(psi/2) - cos(phi/2) * sin(theta/2) * sin(psi/2);
        qy = cos(phi/2) * sin(theta/2) * cos(psi/2) + sin(phi/2) * cos(theta/2) * sin(psi/2);
        qz = cos(phi/2) * cos(theta/2) * sin(psi/2) - sin(phi/2) * sin(theta/2) * cos(psi/2);
        
        q = Quaternion()
        q._val = [qw, qx, qy, qz];

        return q;

def normalise(v, tolerance=0.00001):
    mag2 = sum(n * n for n in v)
    if abs(mag2 - 1.0) > tolerance:
        mag = sqrt(mag2)
        v = tuple(n / mag for n in v)
    return np.array(v)

'''
class Quaternion:

    def from_axisangle(theta, v):
        theta = theta
        v = normalise(v)

        new_quaternion = Quaternion()
        new_quaternion._axisangle_to_q(theta, v)
        return new_quaternion

    def from_value(value):
        new_quaternion = Quaternion()
        new_quaternion._val = value
        return new_quaternion

    def _axisangle_to_q(self, theta, v):
        x = v[0]
        y = v[1]
        z = v[2]

        w = cos(theta/2.)
        x = x * sin(theta/2.)
        y = y * sin(theta/2.)
        z = z * sin(theta/2.)

        self._val = np.array([w, x, y, z])

    def __mul__(self, b):

        if isinstance(b, Quaternion):
            return self._multiply_with_quaternion(b)
        elif isinstance(b, (list, tuple, np.ndarray)):
            if len(b) != 3:
                raise Exception(f"Input vector has invalid length {len(b)}")
            return self._multiply_with_vector(b)
        else:
            raise Exception(f"Multiplication with unknown type {type(b)}")

    def _multiply_with_quaternion(self, q2):
        w1, x1, y1, z1 = self._val
        w2, x2, y2, z2 = q2._val
        w = w1 * w2 - x1 * x2 - y1 * y2 - z1 * z2
        x = w1 * x2 + x1 * w2 + y1 * z2 - z1 * y2
        y = w1 * y2 + y1 * w2 + z1 * x2 - x1 * z2
        z = w1 * z2 + z1 * w2 + x1 * y2 - y1 * x2

        result = Quaternion.from_value(np.array((w, x, y, z)))
        return result

    def _multiply_with_vector(self, v):
        q2 = Quaternion.from_value(np.append((0.0), v))
        return (self * q2 * self.get_conjugate())._val[1:]

    def get_conjugate(self):
        w, x, y, z = self._val
        result = Quaternion.from_value(np.array((w, -x, -y, -z)))
        return result

    def __repr__(self):
        theta, v = self.get_axisangle()
        return f"((%.6f; %.6f, %.6f, %.6f))"%(theta, v[0], v[1], v[2])

    def get_axisangle(self):
        w, v = self._val[0], self._val[1:]
        theta = acos(w) * 2.0

        return theta, normalise(v)

    def tolist(self):
        return self._val.tolist()

    def vector_norm(self):
        w, v = self.get_axisangle()
        return np.linalg.norm(v)
'''

