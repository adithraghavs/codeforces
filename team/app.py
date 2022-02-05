count = 0

for i in range(int(input())):
    statement = input()
    l = statement.split(' ')
    total = 0
    for j in l:
        total += int(j)
    if total >= 2:
        count += 1
        
print(count)