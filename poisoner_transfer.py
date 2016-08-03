import sys
while True:
	tmp = sys.stdin.readline().strip()
	if tmp == "":
		break
	n,t,c = map(int,tmp.split())
	nums = map(int,sys.stdin.readline().strip().split())[0:n]

	s = sum(nums[:c])
	index = c
	count = 0
	while index < n:
		if s <= t:
			count += 1
		s = s + nums[index] - nums[index-c]
		index += 1

	if s <= t:
		count += 1
	print count