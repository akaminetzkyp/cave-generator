import cave_maker


if __name__ == '__main__':
    matrix = cave_maker.generate_matrix(100, 100, 0.5)
    matrix = cave_maker.smoothen_matrix(matrix, iterations=8)
    cave_maker.plot(matrix)
