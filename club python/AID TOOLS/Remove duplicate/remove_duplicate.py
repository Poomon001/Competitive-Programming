x = [3,3,4,5,7,6,7, 8 ,8]

y = []

def solution1():
    for i in x:
        dup = True
        for j in y:
            if (i == j):
                dup = False
                break;
        if dup:
            y.append(i)

def solution2():
    x.sort()
    i = 1
    for i in range(0, len(x) -1):
        if x[i] != x[i+1]:
            y.append(x[i])

    if y[len(y)-1] != x[len(x)-1]:
        y.append(x[len(x)-1])

solution2()


