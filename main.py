# This is a test script
import math
from pprint import pprint



def increments_by_x(ls, x):
    return [l + x for l in ls]


l = [1,2,3,4,5]

print(l.reverse())
print(increments_by_x(l, 5))


class Incrementer:
    def __init__(self):
        pass

    def increments_by_x(self, ls, x):
        return [l + x for l in ls]


inc = Incrementer()

print(inc.increments_by_x(l, 4))

if __name__ == "__main__":
    print(math.pi)
    print("Running script...")
    a = 10
    b = 5
    res = 10 / 5
    print(res)
    u_duct = {
        "one": 1,
        "two": 2,
        "three": 3,
    }
    pprint(u_duct)
