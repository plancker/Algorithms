file = open("2SUM.txt", "r")
r_data = file.readlines()
data = [int(x) for x in r_data]
# data.sort()

pairs = 0

numbers = {}

for d in data:
    numbers[d] = 1


def check(t):
    for x in numbers.keys():
        s = t - x
        if s != x:
            if s in numbers.keys():
                return True
    return False


for t in range(-10000, 10001):
    if check(t):
        pairs = pairs + 1
    print("t = ", t)
    print("pairs = ", pairs)
