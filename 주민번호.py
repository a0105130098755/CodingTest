# 주민등록번호를 입력받아 생년월일, 성별,나이 출력하기

from datetime import datetime


def extract_info(jumin):
    # 주민등록번호에서 생년월일과 성별 코드 추출
    birth_part = jumin[:6]
    gender_code = jumin[7]

    # 생년월일 처리
    year = int(birth_part[:2])
    month = int(birth_part[2:4])
    day = int(birth_part[4:6])

    # 성별 코드에 따른 출생 세기 설정 (1900년대, 2000년대 등)
    if gender_code in ['1', '2']:
        year += 1900
    elif gender_code in ['3', '4']:
        year += 2000

    # 성별 처리
    if gender_code in ['1', '3']:
        gender = '남자'
    elif gender_code in ['2', '4']:
        gender = '여자'

    # 나이 계산
    current_year = datetime.now().year
    age = current_year - year

    # 생년월일 출력 형식 설정
    birth_date = f"{year}년 {month}월 {day}일"

    return birth_date, gender, age


jumin = input("주민등록번호를 입력하세요 (형식: YYMMDD-XXXXXXX): ")
birth_date, gender, age = extract_info(jumin)

print(f"생년월일: {birth_date}")
print(f"성별: {gender}")
print(f"나이: {age}세")
