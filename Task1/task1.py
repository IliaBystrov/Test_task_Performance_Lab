import sys

if len(sys.argv) == 3:
    n = int(sys.argv[1])
    m = int(sys.argv[2])
    a = []

    for i in range(n):
        a.append(i+1)

    last = 0
    j = 0

    while a[0] != last:
        f = 1
        print(a[j], end="")
        while f < m:
            if j == len(a)-1:
                j=0
            else:
                j+=1
            f+=1
        last = a[j]
else:
    print("Нужно указать 2 параметра!")