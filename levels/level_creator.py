import pickle

level0 = [[0, 0],
          [0, 0]]
level1 = [[0, 0],
          [0, 0],
          [0, 0]]


def create_level(level, name):
    with open(name, 'bw') as f:
        pickle.dump(level, f)


def load_level(filename):
    with open(filename, 'br') as f:
        level = pickle.load(f)
    return level

if __name__ == '__main__':
    create_level(level0, 'level0')

    level_picked = load_level('level0')
    print(level_picked)
