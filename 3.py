def freqOnes(xs):
    rotated = list(reversed(list(zip(*xs))[::-1]))
    lists = list(map(list, rotated))
    intlists = list(map(lambda x: list(map(int, x)), lists))
    ones = list(map(sum, intlists))
    return ones


with open("input_3") as f:
    lines = [[y for y in x] for x in f.read().splitlines()]
ones = freqOnes(lines)
gamma = "".join(list(map(lambda x: '1' if x > len(lines) / 2 else '0', ones)))
epsilon = "".join(list(map(lambda x: '0' if x == '1' else '1', gamma)))

print(int(gamma, 2) * int(epsilon, 2))

# part 2


def magic(l, r, lines):
    o2lines = lines
    i = 0
    while len(o2lines) > 1:
        ones = freqOnes(o2lines)
        want = l if ones[i] < len(o2lines) / 2 else r
        filtered = list(filter(lambda x: x[i] == want, o2lines))
        o2lines = filtered
        i += 1
    return int("".join(o2lines[0]), 2)


o2 = magic('0', '1', lines)
co2 = magic('1', '0', lines)
print(o2 * co2)
