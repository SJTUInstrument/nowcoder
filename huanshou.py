import sys
while True:
	line = sys.stdin.readline()
	if len(line) == 0:
		break
	a,b = map(int,line.strip().split())

	upper = a / 0.9
	lower = a / 0.95

	if b < lower:
		print 0
		continue

	if abs(lower - int(lower)) < 1e-6:
		lower = int(lower)
	else:
		lower = int(lower) + 1

	upper = int(upper)

	if b < upper:
		count = b/5 - lower/5
	else:
		count = upper/5 - lower/5
	if lower % 5 == 0:
		count += 1
	print count
