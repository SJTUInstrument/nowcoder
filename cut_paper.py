import sys
while True:
	tmp = sys.stdin.readline().strip()
	if tmp == "":
		break
	n = int(tmp)
	xmin = 1e10
	xmax = -1e10
	ymin = 1e10
	ymax = -1e10

	for i in range(n):
		x,y = map(int,sys.stdin.readline().strip().split())
		if x > xmax:
			xmax = x
		if x < xmin:
			xmin = x
		if y > ymax:
			ymax = y
		if y < ymin:
			ymin = y
	print max(xmax-xmin,ymax-ymin) ** 2