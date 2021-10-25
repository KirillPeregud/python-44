array = [1, 2, 4, 56, 67, 7, 77, 88, 99]
result = []

for i, x in enumerate(array):
    if x % 7 == 0:
        result.append((x, i))
        #print(x, i)

print(result)