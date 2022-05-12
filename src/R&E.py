from kiwipiepy import Kiwi
kiwi = Kiwi()
kiwi.prepare()

for result, score in kiwi.analyze("형태소 분석 결과입니다.", top_n=5):
    print(result, sep='\t')