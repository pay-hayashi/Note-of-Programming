# 部分和問題のBit全探索。

n=int(input())
a=list(map(int,input().split()))
k=int(input())

for i in range(2**n):
    s=0
    for b in range(n):
        if (i>>b)&1:
            s+=a[b]
    if s==k:
        print('Yes')
        exit()
print('No')
