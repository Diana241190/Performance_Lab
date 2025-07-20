import sys

spots = []

with open(sys.argv[1], 'r') as f:
    circle = list(map(int, f.read().split()))

with open(sys.argv[2], 'r') as f:
    for line in f:
        spots.append([int(x) for x in line.split()])

for spot in spots:
    a = (circle[0] - spot[0])**2 +(circle[1] - spot[1])**2
    if a < circle[2]**2:
        print(1)
    elif a == circle[2]**2:
        print(0)
    elif a > circle[2]**2:
        print(2)