import matplotlib.pyplot as plt
import numpy as np
from time import time
from functools import reduce
from konlpy.tag import Kkma
from konlpy.tag import Komoran
from konlpy.tag import Hannanum
from konlpy.tag import Okt
from eunjeon import Mecab

def analyse(sample_text, analyser=Mecab()):
    start = time()
    analysed = analyser.pos(sample_text)
    end = time()
    runtime = end - start

    return (runtime, analysed)

def all_analyse(sample_text):
    kkma = analyse(sample_text, analyser=Kkma())
    komoran = analyse(sample_text, analyser=Komoran())
    hannanum = analyse(sample_text, analyser=Hannanum())
    okt = analyse(sample_text, analyser=Okt())
    mecab = analyse(sample_text, analyser=Mecab())

    return (
        [kkma[0], komoran[0], hannanum[0], okt[0], mecab[0]],   # runtimes
        [kkma[1], komoran[1], hannanum[1], okt[1], mecab[1]]    # results
    )

sample_texts = [
    '봄의 첫날, 나는 줄곧 가을의 끝을 생각하네.',
    '안녕하세요. 여기는 광주과학고등학교입니다.'
]

runtime1 = all_analyse(sample_texts[0])[0];
runtime2 = all_analyse(sample_texts[1])[0];
name = ['Kkma', 'Komoran', 'Hannanum', 'Okt', 'Mecab']

x = np.arange(5)
plt.bar(x, runtime1)
plt.bar(x, runtime2, bottom=runtime1)

sample_texts.reverse()
plt.legend(sample_texts)
plt.xticks(x, name)

plt.show()