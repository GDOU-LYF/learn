n = int(input())
f1, f2 = 1, 1
for i in range(3, n + 1):
    f1, f2 = f2 % 10007, (f1 + f2) % 10007
print(f2)
