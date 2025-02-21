import random
import time

MIN = 00000000
MAX = 99999999

# 랜덤으로 8자리 숫자 비밀번호 생성 (문자열로 변환)
password = str(random.randint(MIN, MAX)).zfill(8)

# 실제 비밀번호를 확인하려면 이 줄을 유지합니다. (디버그용)
print(f"비밀번호는 {password}입니다.")  
print('찾는 중...')

# 시작 시간 기록
start_time = time.time()

# 비밀번호를 찾기 위해 00000000부터 99999999까지 확인
for guess in range(MIN, MAX + 1):
    # guess 값을 8자리 문자열로 변환
    guess_str = str(guess).zfill(8)
    
    # 비밀번호를 맞추면 시간 측정을 종료하고, 결과 출력
    if guess_str == password:
        # 종료 시간 기록
        end_time = time.time()
        # 걸린 시간 계산
        elapsed_time = end_time - start_time
        print(f"비밀번호를 찾았습니다! 비밀번호는 {guess_str}입니다.")
        print(f"걸린 시간: {elapsed_time:.6f} 초")
        break
