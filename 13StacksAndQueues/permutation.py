from randomized_queue import RandomizedQueue


def permutation(n, *items):
    n = int(n)
    randq = RandomizedQueue()
    [randq.enqueue(i) for i in items]
    for i in randq:
        if n == 0:
            return
        print(i)
        n -= 1


if __name__ == '__main__':
    from sys import argv
    argv.pop(0)
    print('* Permutation')
    permutation(*argv)
