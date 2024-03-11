

a = 7
b = 5
p = 11


target = p - 1
for i in range(0, target + 1):
    j = target - i
    cond_a = a * i <= target
    cond_b = b * j <= target
    if cond_a and cond_b:
        print(i, j)