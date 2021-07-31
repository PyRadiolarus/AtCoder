from sys import stdin
stdin = open("../stdin.txt")

X = [int(i) for i in stdin.readline().rstrip()]
count = 0
if len(set(X)) == 1:
    print("Weak")
else:
    for i in range(len(X)-1):
        if X[i+1] == 0 and X[i] == 9:
            count += 1
        elif X[i+1] - X[i] == 1:
            count += 1
        else:
            pass
    if count == 3:
        print("Weak")
    else:
        print("Strong")