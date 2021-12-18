from pprint import pprint

graph = {}
with open('input_12') as file:
    for line in file.readlines():
        [lhs, rhs] = line.split("-")
        lhs, rhs = lhs.rstrip(), rhs.rstrip()
        if lhs not in graph:
            graph[lhs] = [rhs] 
        else:
            graph[lhs].append(rhs)
        if rhs not in graph:
            graph[rhs] = [lhs]
        else:
            graph[rhs].append(lhs)

ways = []
def getways(node, path):
    if node == 'end':
        ways.append(path)
    for choice in graph[node]:
        if (choice not in path and choice.islower()) or choice.isupper():
            getways(choice, path + [node])

#p1
getways('start', [])
print(len(ways))

ways2 = []
def getways2(node, path, twice):
    if node == 'end':
        ways2.append(path)
        return
    for choice in graph[node]:
        if (choice not in path and choice.islower()) or choice.isupper():
            getways2(choice, path + [node], twice)
        elif twice and choice != 'start' and choice.islower():
            getways2(choice, path + [node], False)

getways2('start', [], True)
print(len(ways2))