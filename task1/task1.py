import itertools, sys


n = int(sys.argv[1])
m = int(sys.argv[2])
rez = []
new = []
count = 1
for i in itertools.cycle(range(1,n+1)):

    if len(rez) != 0 and rez[-1][-1] == 1:
        for i in rez:
            new.append(i[0])
        break
    elif  i == 1:
        rez.append(list(itertools.islice(itertools.cycle(range(1,n+1)),i-1,i-1+m)))
    else:
        rez.append(list(itertools.islice(itertools.cycle(range(1, n+1)), rez[-1][-1] - 1 , rez[-1][-1] - 1  + m)))

print(*new, sep='')