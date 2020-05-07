def removeAll(listin,ele):
    for i in range(len(listin))


def solution(data, n): 
    from collections import defaultdict
    ans = defaultdict(int)
    for ele in data:
        ans[ele]+=1
    for ele in ans:
        if ans[ele] > n:
            for i in range(ans[ele]):
                data.remove(ele)
    return data

