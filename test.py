

numbers = []
for x in range (1000, 3001):
    split = [int(d) for d in str(x)]
    odd = False
    for y in range (0, len(split)):
        if split[y] % 2 != 0:
            odd = True
    if (odd == False):
        numbers.append(x)
print(numbers)