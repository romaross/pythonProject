list_1 = [1, 2, 3]
list_2 = [5, 6, 7]
list_1 = [0,]+list_1+[4,]
print(list_1)
list_2.extend(list_1)
print(list_2)
list_1.append(list_2)
print(list_1)