from mpmath import mp

mp.dps = 100
cets = []

def sin(x):
    rad = mp.radians(x)
    return mp.sin(rad)

def cos(x):
    rad = mp.radians(x)
    return mp.cos(rad)

def tan(x):
    rad = mp.radians(x)
    return mp.tan(rad)

err = mp.mpf(10 ** -90)

for a in range(1, 89):
    for b in range(1, 89):
        for c in range(1, 89):
            if (sin(c) * sin(c + a) - cos(c - b) * sin(a) * sin(c + b)) != 0:
                cet = mp.degrees(mp.atan((sin(a) * sin(c - b) * sin(c + b)) / (sin(c) * sin(c + a) - cos(c - b) * sin(a) * sin(c + b))))

                lefterr = cet - mp.floor(cet)
                righterr = mp.ceil(cet) - cet
                correct_cet = mp.floor(cet) if lefterr < righterr else mp.ceil(cet)

                if min(lefterr, righterr) < err and not(correct_cet in cets) and correct_cet >= 0:
                    print(f'a = {a}, b = {b}, c = {c}, cet = {correct_cet}')
                    cets.append(correct_cet)