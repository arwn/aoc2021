import pprint

def intersect(a, b):
	return len(set(a).intersection(set(b)))

def getnums(sk):
	nums = [None for _ in range(10)]
	nums[1]= [e for e in sk if len(e) == 2].pop()
	nums[4] = [e for e in sk if len(e) == 4].pop()
	nums[7] = [e for e in sk if len(e) == 3].pop()
	nums[8] = [e for e in sk if len(e) == 7].pop()

	nums[9] = [e for e in sk if len(e) == 6 and intersect(nums[4], e) == 4].pop()
	nums[3] = [e for e in sk if len(e) == 5 and intersect(nums[7], e) == 3].pop()
	nums[2] = [e for e in sk if len(e) == 5 and intersect(nums[4], e) == 2].pop()
	nums[0] = [e for e in sk if len(e) == 6 and intersect(nums[9], e) == 5 and intersect(nums[2], e) == 4 and intersect(nums[1], e) == 2].pop()
	nums[5] = [e for e in sk if len(e) == 5 and intersect(nums[1], e) == 1 and intersect(nums[4], e) == 3].pop()
	nums[6] = [e for e in sk if len(e) == 6 and intersect(nums[1], e) == 1].pop()
	return nums

def is1478(s, nums):
	return (set(s) == set(nums[1])
		or set(s) == set(nums[4])
		or set(s) == set(nums[7])
		or set(s) == set(nums[8]))

count1478 = 0
count = 0
def f(line):
	global count1478
	global count
	[lhs, rhs] = line.split("|")
	sk = lhs.strip().split()
	sn = rhs.strip().split()
	nums = getnums(sk)
	
	numstr = ""
	for sns in sn:
		for i, n in enumerate(nums):
			if set(sns) == set(n):
				numstr += str(i)
				if is1478(sns, nums):
					count1478 += 1
	count += int(numstr)
		

with open('input_8') as file:
	lines = file.readlines()
	for line in lines:
		f(line)
	print(count1478, count)
