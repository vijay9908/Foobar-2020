def basen(int_base_10,n):
    k = int(int_base_10)
    a = []
    while k >= n:
        r = k%n
        a.append(str(r))
        k = (k-r)//n
    a.append(str(k))
    return ''.join(a[::-1])
    
def base10(int_base_n,n):
    q = [int_base_n[::-1]]
    y = 0
    for i , a in enumerate(q):
        y += int(a)*(n**i)
    return str(y)

def solution(n, b):
    k , m , id = len(n),n,[]
    while m not in id:
        id.append(m)
        q = sorted(m)
        xd = ''.join(q[::-1])
        yd = ''.join(q)
        if b == 10:
            wera = int(xd)-int(yd)
            m = str(wera)
        else:
            werin10 = int(base10(xd,b))-int(base10(yd,b))
            m = basen(str(werin10),b)
        m = (k-len(m))*'0' + m
        print(id)
        return len(id)-id.index(m)
    