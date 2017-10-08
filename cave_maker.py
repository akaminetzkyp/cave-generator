import matplotlib.pyplot as plt
import random


def generate_matrix(size_x, size_y, fill_ratio, borders=True):
    matrix = [[0 if fill_ratio < random.random() else 1 for _ in range(size_x)]
              for _ in range(size_y)]
    if borders:
        for y in range(size_y):
            for x in range(size_x):
                if x in [0, size_x - 1] or y in [0, size_y - 1]:
                    matrix[y][x] = 1

    return matrix


def smoothen_matrix(matrix, threshold=5, iterations=1):
    size_x = len(matrix[0])
    size_y = len(matrix)

    new_matrix = matrix

    for _ in range(iterations):
        old_matrix = new_matrix
        for y in range(1, size_y - 1):
            for x in range(1, size_x - 1):
                walls_region = len([1 for j in range(y - 1, y + 2)
                                   for i in range(x - 1, x + 2)
                                   if old_matrix[j][i] == 1])
                new_matrix[y][x] = 1 if walls_region >= threshold else 0

    return new_matrix


def plot(matrix, cmap='binary'):
    plt.matshow(matrix, cmap=cmap)
    plt.show()
