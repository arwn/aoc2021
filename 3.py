def freqOnes(xs):
    rotated = reversed(list(zip(*xs))[::-1])
    lists = [list(x) for x in rotated]
    intlists = [map(int, x) for x in lists]
    ones = list(map(sum, intlists))
    return ones


with open("input_3") as f:
    lines = [[y for y in x] for x in f.read().splitlines()]
ones = freqOnes(lines)
gamma = "".join(['1' if x > len(lines) / 2 else '0' for x in ones])
epsilon = "".join(['0' if x == '1' else '1' for x in gamma])

print(int(gamma, 2) * int(epsilon, 2))

# part 2


def magic(l, r, lines):
    o2lines = lines
    i = 0
    while len(o2lines) > 1:
        ones = freqOnes(o2lines)
        want = l if ones[i] < len(o2lines) / 2 else r
        filtered = [x for x in o2lines if x[i] == want]
        o2lines = filtered
        i += 1
    return int("".join(o2lines[0]), 2)


o2 = magic('0', '1', lines)
co2 = magic('1', '0', lines)
print(o2 * co2)
