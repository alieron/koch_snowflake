import math
import numpy as np
import matplotlib.pyplot as plt

# theta = np.radians(60)
# c, s = np.cos(theta), np.sin(theta)
# R = np.array(((c, -s), (s, c)))

R = np.array([[1 / 2, -(3 ** 0.5) / 2], [(3 ** 0.5) / 2, 1 / 2]])
# r = np.array([[1 / 2, (3 ** 0.5) / 2], [(1 - 3 / 2), (3 ** 0.5) / 2]])
# r = np.array([[1 , 0], [(1 - 3 / 2), (3 ** 0.5) / 2]])
# r = np.array([[1, 0], [(3 ** 0.5) / 2, 1 / 2]])


def findB(a, e):
    return (2 * a + e) / 3


def findD(a, e):
    # return a + (2 / 3) * e
    return (a + 2 * e) / 3


def findC(b, d):
    return b + np.matmul(R, (d - b))


def new_gen(points):
    temp_points = np.array([points[0]])

    for i in range(len(points) - 1):
        point_a = points[i]
        point_e = points[i + 1]
        point_b = findB(point_a, point_e)
        point_d = findD(point_a, point_e)
        point_c = findC(point_b, point_d)

        temp_points = np.concatenate(
            [temp_points, [point_b, point_c, point_d, point_e]])
        # Order point_a, point_b, point_c, point_d, point_e

    return temp_points


def generate_koch(base, generations):
    points = base

    for _ in range(generations):
        points = new_gen(points)

    return points


# base = np.array([[0, 0], [1, 0]])  # Horizontal Line
# base = np.array([[0, 0], [1, 0], [0.5, -(3 ** 0.5) / 2], [0, 0]])  # Triangle
# base = np.array([[0, 0], [1 / 3, 0], [1 / 2, (3 ** 0.5) / 6], [2 / 3, 0], [1, 0]])

points = generate_koch(base, 5)
print(points)

plt.axis("equal")
plt.plot(*points.transpose())
plt.show()
