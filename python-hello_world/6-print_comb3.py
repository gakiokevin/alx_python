combinations = []
for i in range(10):
    for j in range(i + 1, 10):
        combination = "{i}{j}".format(i=i, j=j)
        combinations.append(combination)
result = ', '.join(combinations)
print(result)
   