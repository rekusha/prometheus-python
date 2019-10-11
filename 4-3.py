import sys

x, y, z = (sys.argv[1]), '', ''

if len(x) % 2 != 0:
    print 'NO'
    exit(0)
elif x[0] == ')' or x[-1] == '(':
    print 'NO'
    exit(0)
for i in x:
    if i == '(':
        y += i
    elif i == ')':
        z += i
if len(y) == len(z):
    print 'YES'
else:
    print 'NO'
