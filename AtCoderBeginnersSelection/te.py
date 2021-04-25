import copy

a = [1]
b=copy.deepcopy(a)

a[0] = 2
print(b)