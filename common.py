l1 = [0, 3, 6, 9, 10, 2, 5]
l2 = [2, 6, 4, 7, 8, 1, 15]

# An empty list
common = []
for i in l1:
    for j in l2:
        if i==j:
            common.append(i)
            print(common)

coms = list(common.sort())

# Print the result
print(coms)