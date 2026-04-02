#문법 공부

#10억의 지수 표현
print(1e9)

#거듭제곱
print(2 ** 5)

#리스트[] list()

#크기가 N이고, 모든 값이 0인 1차원 리스트 초기화
n = 10
a = [0] * n
print(a)

# 0부터 19까지의 수 중에서 홀수만 포함하는 리스트
array = [i for i in range(20) if i % 2 == 1]
print(array)

#딕셔너리 dict() / 키-값 쌍
data = dict()
data['사과'] = 'Apple'
data['바나나'] = 'Banana'
data['코코넛'] = 'Coconut'

#키 데이터만 담은 리스트
key_list = data.keys()
#값 데이터만 담은 리스트
value_list = data.values()
print(key_list)
print(value_list)

#각 키에 따른 값을 하나씩 출력
for key in key_list:
    print(data[key])

#집합자료형 {} set /중복허용x , 순서없음
data = set([1, 1, 2, 3, 4, 4, 5])
data = {1, 1, 2, 3, 4, 4, 5}

""" 조건문
if 조건문 1: 
    조건문 1이 True일 때 실행되는 코드
elif 조건문 2:
    조건문 1에 해당 x, 조건문 2가 True일 때 
else:
    위의 모든 조건문이 모두 True 값이 아닐 때
"""

# while문 
i = 1
result = 0

#i가 9보다 작거나 같을 때 아래 코드를 반복적으로 수행
while i <= 9:
    result += i
    i += 1

print(result)

#for 문
"""for 변수 in 리스트:
    실행할 소스코드"""
scores = [90, 85, 77, 65, 97]
cheating_list = [2, 4]

for i in range(5):
    if i + 1 in cheating_list:
        continue
    if scores[i+1] >= 80:
        print(i + 1, "번 학생은 합격입니다.")

#함수
"""
def 함수명(매개변수):
    실행할 소스코드
    return 반환 값
"""

#입츨력

#데이터의 개수 입력
n = int(input())
#각 데이터를 공백으로 구분하여 입력
data = list(map(int, input().split()))

import sys
# 문자열 입력받기
data = sys.stdin.readline().rstrip()
print(data)

