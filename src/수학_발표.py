import random

testcase = int(input())
sum_each = 0
count = [0] * testcase

for i in range(testcase):
    sum_each = 0

    while sum_each < 1:
        sum_each += random.random()
        count[i] += 1
    print(f'{i+1:4}번째 시도\n  1을 넘긴 최초의 누적값: {sum_each:.16f}\n   1을 넘기 위해 더해진 횟수: {count[i]}')

for i in range(testcase):
    if count.count(i) == 0: continue
    print(f'{i}회 -> {count.count(i)}번')
print(f'평균 {sum(count) / len(count)}번')