# 部分和問題の深さ優先探索。

n=int(input())
a=list(map(int,input().split()))
k=int(input())

# メモ化のためのツール
# なし：n=37程度まで
# あり：n=2**31-1まで（maxsizeの上限がint32bitのため）
from functools import lru_cache
@lru_cache(maxsize=2**n)
def dfs(i,s):
    if i==n:
        return s==k
    if dfs(i+1,s) or dfs(i+1,s+a[i]):
        return True
    else:
        return False

print('Yes' if dfs(0, 0) else 'No')
