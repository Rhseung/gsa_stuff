import sys
sys.setrecursionlimit(1001)

t = 0

def hS(n):
    global t
    a = []
    tmp = n
    if tmp >= 100:
        while n >= 10:
            a.append(n % 10)
            n = n // 10
        a.append(n)
        for i in range (1, len(a)-1):
            if a[i+1] - a[i] == a[i] - a[i-1]:
                t += 1
        hS(tmp - 1)
    elif tmp != 0:
        t += 1
        hS(tmp - 1)
    else:
        return
    return t
print(hS(992))