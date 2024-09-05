# 2개의 문자열을 포인터 변수 s와 k에,
# 양의 정수를 정수형 변수 n에 각가 전달 받아 s 문자열의 뒤 부분의 n개 문자를 k문자열 앞에 끼워 넣는 코드 작성

def insert_substring(s: str, k: str, n: int) -> str:
    # s의 뒤에서 n개의 문자 추출
    substring = s[-n:]

    # k 문자열 앞에 추출한 부분 문자열을 붙임
    result = substring + k

    return result


# 예시
s = "seoul"
k = "korea"
n = 2

result = insert_substring(s, k, n)
print(f"Result: {result}")
