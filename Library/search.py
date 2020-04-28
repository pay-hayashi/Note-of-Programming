# Binary Search - 二分探索

from bisect import bisect_left, bisect_right

# 第1引数の配列に、順序を崩さずに第2引数を挿入するときのインデックスを返す。
# 最左・最右の2つ
# O(log_n)

bisect_left([1, 3, 5, 7, 9, 11, 13, 15], 4)
# -> 2
bisect_left([1, 2, 2, 3, 4, 5, 6], 2)
# -> 1
bisect_right([1, 2, 2, 3, 4, 5, 6], 2)
# -> 3
