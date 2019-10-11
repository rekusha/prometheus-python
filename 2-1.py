import sys
import math

x, m, q = float(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3])

print (1 / (q * (math.sqrt(2 * math.pi)))) * (math.exp(-(math.pow((x-m), 2.0) / (2.0 * math.pow(q, 2.0)))))
