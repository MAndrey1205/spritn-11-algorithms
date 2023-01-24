import math


input()
sequence = input().split(' ')

def find_zero_distances(items):
    distance = math.inf
    distances = []
    for item in items:
        if item == '0':
            distance = 0
        else:
            distance += 1
        distances.append(distance)
    return distances

distances_forward = find_zero_distances(sequence)
distances_backward = list(reversed(find_zero_distances(reversed(sequence))))

result = []
for i in range(len(sequence)):
    min_distance = min(distances_forward[i], distances_backward[i])
    result.append(min_distance)
print(*result)
