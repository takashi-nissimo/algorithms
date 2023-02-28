if __name__ == '__main__':
    from sys import argv
    from pathlib import Path
    from random import choice

    with open(Path(argv[1])) as f:
        words = [w.strip() for l in f.readlines() for w in l.split(' ')]
    print(choice(words))
