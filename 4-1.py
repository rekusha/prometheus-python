import sys

x = str(sys.argv[1]).upper().replace(' ', '')

if x == x[::-1]:
    print 'YES'
else:
    print 'NO'
