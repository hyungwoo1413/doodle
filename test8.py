import re

p = re.compile('\d')    # \d = decimal , 숫자를 탐색하는 정규식
print(p.match('asdf'))  # 결과값 : None
print(p.match('0099'))  # 결과값 : match='0' , 매치된 결과의 시작이 0번인덱스에 존재한다.

pp = re.compile('\w')   # \w = 공백(화이트스페이스)을 제외한 모든 것을 탐색하는 정규식
print(pp.match('asdf')) # 결과값 : match = '0'
print(pp.match('0099')) # 결과값 : match = '0'