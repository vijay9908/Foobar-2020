from collections import defaultdict , deque
from math import gcd
from sys import stdin, stdout
input = stdin.readline
listin = lambda : list(map(int, input().split()))
mapin = lambda : map(int, input().split())


def removeAll(listin,ele):
    for i in range(len(listin)):
        listin.remove(ele)

def solution(data, n): 
    ans = defaultdict(int)
    for ele in data:
        ans[ele]+=1
    for ele in ans:
        if ans[ele] > n:
            for i in range(ans[ele]):
                data.remove(ele)
    return data

