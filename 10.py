score = 0
scores = []

def getsum(s):
	done = 0
	for e in reversed(s):
		if e == "(":
			done = done * 5 + 1
		if e == "[":
			done = done * 5 + 2
		if e == "{":
			done = done * 5 + 3
		if e == "<":
			done = done * 5 + 4
	global scores
	scores.append(done)

def f(line):
	global score
	s = []
	for char in line:
		if char == ")":
			if len(s) < 1 or s.pop() != "(":
				score += 3
				return False
		elif char == "]":
			if len(s) < 1 or s.pop() != "[":
				score += 57
				return False
		elif char == "}":
			if len(s) < 1 or s.pop() != "{":
				score += 1197
				return False
		elif char == ">":
			if len(s) < 1 or s.pop() != "<":
				score += 25137
				return False
		else:
			s.append(char)
	getsum(s)
	return True

with open('input_10') as file:
	for line in file.readlines():
		f(line.rstrip())
	print("p1:", score)
	scores.sort()
	print("p2:", scores[len(scores) // 2])
