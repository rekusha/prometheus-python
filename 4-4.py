import sys, math

a1, a2 = int(sys.argv[1]), int(sys.argv[2])
l1=[]
l2=[]

while a1 < a2 + 1:
    l1.insert(-1, str(a1))
    a1 += 1

for i in l1:
    if len(i) < 6:
        while len(i) < 6:
            i = '0' + i;
    l2.insert(-1, i);
del l1[0:]

for i in l2:
    if (int(i[0])+int(i[1])+int(i[2])) == (int(i[3])+int(i[4])+int(i[5])):
        l1.append(i)

print len(l1)
