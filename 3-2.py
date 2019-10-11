import sys

n=int(sys.argv[1])
f = range(2)
z = 0

if n > 0:
    while z <= n - 1:
        f2 = f[-1] + f[-1-1]
        f.append(f2)
        z = z + 1
    print f[-1-1]
elif n == 0:
    print f[-1-1]
