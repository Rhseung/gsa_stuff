from sympy import Integer


polynomial_1 = list(map(int, input("피제수 다항식의 근을 입력해주세요. ").split()))
polynomial_2 = list(map(int, input("제수 다항식의 근을 입력해주세요. ").split()))

def plugin(f, x):
    ret = 1
    for i in f:
        ret *= (x - i)
    return ret

print(plugin(polynomial_1, 3))