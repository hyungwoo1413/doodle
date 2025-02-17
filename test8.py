sample3 = [[0,20],[1,30],[2,40],[3,50]]
for idx, value in sample3:
    print(f'인덱스{idx} : {value}', end=' ')

# 결과 : 인덱스0 : 20 인덱스1 : 30 인덱스2 : 40 인덱스3 : 50


## 챌린지 2 , 이거 풀면 실력 +1.2
## enumerate 메서드 : 리스트의 요소에 인덱스를 붙혀서 반환해주는 무언가.
sample4 = [20,30,40,50]
for idx, value in enumerate(sample4):
    print(f'인덱스{idx} : {value}', end=' ')