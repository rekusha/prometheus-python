import sys

x, y, z = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])

w = 'la-'
text = ' ' + w * (x - 1) + 'la'
kuplet = y * text

if z == 1:
        kon = '!'
else:
        kon = '.'

print 'Everybody sing a song:' + kuplet + kon