from itertools import permutations

# 1부터 9까지의 숫자
digits = '123456789'

# 5자리 수와 4자리 수를 만들기 위한 모든 숫자들의 순열
valid_results = []

for perm in permutations(digits, 9):  # 9개의 숫자에 대해 순열을 구함
    # 5자리 수와 4자리 수를 분리
    five_digit_number = int(''.join(perm[:5]))  # 첫 5개 숫자로 5자리 수
    four_digit_number = int(''.join(perm[5:]))  # 나머지 4개 숫자로 4자리 수

    # 조건을 만족하는지 확인
    if five_digit_number - four_digit_number == 33333:
        valid_results.append((five_digit_number, four_digit_number))

# 결과 출력
for five_digit_number, four_digit_number in valid_results:
    print(f"{five_digit_number} - {four_digit_number} = 33333")
