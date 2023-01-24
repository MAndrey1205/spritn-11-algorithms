k = int(input())
items = []
for _ in range(4):
    line = input()
    items.extend(int(x) for x in list(line) if x != '.')

score = 0
for t in range(1, 10):
    count = items.count(t)
    if 0 < count <= k * 2:
        score += 1

print(score)
