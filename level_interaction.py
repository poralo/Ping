import pickle

level0 = [[0, 0],
          [0, 0]]
level1 = [[0, 0],
          [0, 0],
          [0, 0]]
level2 = [[1, 0, 1],
          [0, 0, 0],
          [0, 0, 0]]
level3 = [[0, 0, 0, 1],
          [0, 0, 0, 0],
          [0, 0, 0, 1]]
level4 = [[1, 0, 1, 0],
          [0, 0, 0, 0],
          [0, 0, 1, 0]]
level5 = [[0, 0, 0, 0],
          [0, 0, 1, 0],
          [0, 0, 0, 0],
          [1, 0, 0, 0]]
level6 = [[0, 0, 0, 0],
          [1, 0, 0, 0],
          [0, 0, 0, 0],
          [1, 0, 1, 0]]

level00 = [[1, 1, 1, 1],
           [1, 1, 1, 1],
           [1, 1, 1, 1],
           [1, 1, 1, 1]]


def create_level(level, name):
    with open(name, 'bw') as f:
        pickle.dump(level, f)


def load_level(filename):
    with open(filename, 'br') as f:
        level = pickle.load(f)
    return level

if __name__ == '__main__':
    create_level(level6, 'levels/level6')


