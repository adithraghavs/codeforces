t = int(input())
x = 0

for i in range(t):
    command = input()
    if '++' in command:
        x += 1
    else:
        x -= 1

print(x)