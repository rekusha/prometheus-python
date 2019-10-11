def make_sudoku(size):
	a=size
        b=size
	size=size**2
	import random
	l=[]
        y=0
        etal = range(1, size + 1)
        random.shuffle(etal)
	while len(l) < size:
		while len(l) < a: #<---
			l.append(etal)
			etal=etal[b:] + etal[:b]
		etal=etal[1:] + etal[:1]
		a += b
	return l

print make_sudoku(3)

def check_sudoku(l):
	import math
	n = len(l)
	if n == 1 and l == [[1]]:
	    return True
	for i in xrange(n):
	    for j in xrange(n):
	        v = l[i][j]
	        for t in xrange(j + 1, n):
	            if l[i][t] == v:
	                return False
	        for t in xrange(i + 1, n):
	            if l[t][j] == v:
	                return False
	nn = int(math.sqrt(n))
	for i in xrange(nn):
	   for j in xrange(nn):
	    t = j * nn
	    lt = []
	    for x in xrange(nn):
	        lt += l[i * nn + x][t : t + nn]
	    for i1 in xrange(n):
	        for j1 in xrange(i1 + 1, n):
	            if lt[i1] == lt[j1]:
	                return False
	return True