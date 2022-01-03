list = [-5, -10, -50, -2, 5, -6]

isPositive = False

for i in list:
    if i > 0:
        isPositive = True
        break

# print(isPositive)

# any() liste de herhangi biri True ise True. Boşsa ve tümü yanlışsa False döndürür.
# all() tüm öğeler True ise veya liste boşsa True döndürür.

list = [-5, -10, -50, -2, 5, -6]
isPositive = any(i > 0 for i in list)
# print(isPositive)


isPositive = not all(i <= 0 for i in list)
print(isPositive)
