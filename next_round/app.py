n, k = map(int, input().split())
scores = list(map(int, input().split()))

num = scores[k-1]
count = 0

for x in scores:
    if x >= num and x > 0:
        count += 1

print(count)