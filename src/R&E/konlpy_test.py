import matplotlib.pyplot as plt
import numpy as np
from time import time
from functools import reduce
from konlpy.tag import Kkma
from konlpy.tag import Komoran
from konlpy.tag import Hannanum
from konlpy.tag import Okt
from eunjeon import Mecab

def analyse(sample_text):
    analysers = [Kkma(), Komoran(), Hannanum(), Okt(), Mecab()];
    tokenized = []
    runtime = []

    # 형태소 분석하기
    for analyser in analysers:
        start = time()
        tokenized.append(analyser.pos(sample_text))
        end = time()

        runtime.append(end - start)

    # 런타임, 분석 결과 출력
    for i in range(len(analysers)):
        print(f"{(analysers[i].__class__.__name__):<10} : {runtime[i]:.5f} sec\n{tokenized[i]}")
    
    return runtime

sample_texts = [
    '봄의 첫날, 나는 줄곧 가을의 끝을 생각하네.',
    '안녕하세요. 여기는 광주과학고등학교입니다.'
]
runtimes = [[0] * 6] * len(sample_texts)
averages = []

for text in sample_texts:
    runtimes.append(analyse(text))

for i in range(0, 6):
    sum = 0
    for t in range(len(sample_texts)):
        sum += runtimes[t][i]

    averages.append(sum / len(sample_texts))

print(averages)