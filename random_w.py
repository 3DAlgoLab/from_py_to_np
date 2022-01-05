import random
import time


class RandomWalker:
    def __init__(self):
        self.position = 0

    def walk(self, n):
        self.position = 0
        for i in range(n):
            yield self.position
            self.position += 2 * random.randint(0, 1) - 1


def random_walker_faster(n=100000):
    from itertools import accumulate
    steps = random.choices([-1, 1], k=n)
    return [0] + list(accumulate(steps))


if __name__ == '__main__':
    start = time.time()
    walker = RandomWalker()
    walk = [position for position in walker.walk(100000)]

    duration = time.time() - start
    print(f"Duration:{duration:.6f} seconds")

    start = time.time()
    random_walker_faster()
    print(f"Duration:{time.time()-start:.6f} seconds")
