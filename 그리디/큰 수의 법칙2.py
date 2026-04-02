#N, M, K를 공백으로 구분하여 입력받기
# N: 배열 크기 M: M번 더하여 가장 큰 수  K: 연속 K번 초과 더하기 
n, m, k = map(int, input().split())
# N개의 수를 공백으로 구분하여 입력받기
data = list(map(int, input().split()))

data.sort() # 입력받은 수들 정렬하기
first = data[n - 1] # 가장 큰 수
second = data[n -2] # 두번째로 큰 수

# 가장 큰 수가 더해지는 횟수 계산
count = int(m / (k + 1)) * k
count += m % (k + 1)

result = 0
result += (count) * first # 가장 큰 수 더하기
result += (m - count) * second #두 번째로 큰 수 더하기

print(result)