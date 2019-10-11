import sys

x, y, z = float(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3])

if (x + y) > z and (x + z) > y and (y + z) > x:
    print "triangle"
else:
    print "not triangle"