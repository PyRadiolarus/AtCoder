from sys import stdin
stdin = open("../stdin.txt")

P = int(stdin.readline())
coin = [3628800,362880,40320,5040,720,120,24,6,2,1]
coin = [i for i in coin if i <= P]
res = 0 
for i in range(len(coin)):
    sale = coin[i]
    count = P // sale
    res += count
    P -= sale * count
print(res)