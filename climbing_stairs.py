map = { 1: 1, 2: 2, 3: 3 }

# memoization
# def distinct_ways(n: int) -> int:
    # if n not in map:
        # map[n] = distinct_ways(n - 2) + distinct_ways(n - 1)

    # return map[n]

def distinct_ways(n):
    if n == 1:
        return 1

    previous = 1
    current = 2

    for i in range(n - 2):
        new = previous + current
        previous = current
        current = new

    return current

for i in range(45, 0, -1):
    print(i, distinct_ways(i))
