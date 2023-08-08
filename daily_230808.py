

# 1213. String

# import sys
# sys.stdin = open('input_1213.txt', 'r', encoding='UTF-8')
#
# T = 10
# for tc in range(1, T+1):
#     N = int(input())
#     my_str = list(input())
#     arr = list(input())
#     str_num = 0                                     # 반환할 문자열의 개수
#
#     for j in range(len(arr)):
#         num = 0                                     # num의 초기값
#         while num < len(my_str):                    # 원하는 글자수만큼 비교 될때까지
#             if j + num < len(arr):                  # 인덱스 범위
#                 if my_str[num] == arr[j+num]:       # 같은 녀석을 만나면 num을 올려줌 num이 올라가면 다음 글자가 비교가 된다.
#                     num += 1
#                 else:                               # 무한루프 방지
#                     break
#             else:                                   # 무한루프 방지
#                 break
#         if num == len(my_str):                      # num이 내가 비교하고자하는 글자수만큼 올랐다는건 일치했다는 것
#             str_num += 1
#
#     print(f'#{tc} {str_num}')



# 1215. 회문1

# import sys
# sys.stdin = open('input_1215.txt', 'r')
#
# T = 10
# for tc in range(1, T+1):
#     length = int(input())
#     arr = [list(input()) for _ in range(8)]
#     my_list = []
#     result_num = 0
#
#     for row in range(8):                    # 가로 판별
#         for col in range(8-length+1):
#             my_list = []
#             for col2 in range(length):
#                 if 0 <= col+col2 < 8:
#                     my_list.append(arr[row][col+col2])
#
#             if my_list[::] == my_list[::-1]:
#                 result_num += 1
#
#     for col in range(8):                    # 세로 판별
#         for row in range(8-length+1):
#             my_list = []
#             for row2 in range(length):
#                 if 0 <= row+row2 < 8:
#                     my_list.append(arr[row+row2][col])
#
#             if my_list[::] == my_list[::-1]:
#                 result_num += 1
#
#     print(f'#{tc} {result_num}')



# 3143. 가장 빠른 문자열 타이핑

import sys
sys.stdin = open('input_3143.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    my_str, word = map(list, input().split())
    min_num = 0
    num = 0
    word_num = 0
    str_case = ''
    word_case = ''

    while num != (len(my_str) - (len(word)-1)):
        str_case = ''
        word_case = ''
        for i in range(len(word)):
            str_case += my_str[num + i]
        for i in word:
            word_case += i
        if str_case == word_case:
            min_num += 1
            word_num += 1
        num += 1

    min_num += len(my_str) - (word_num * len(word))

    print(f'#{tc} {min_num}')



# 4865. 글자수

# import sys
# sys.stdin = open('input_4865.txt', 'r')
#
# T = int(input())
# for tc in range(1,T+1):
#     my_str = list(input())
#     arr = list(input())
#     max_v = 0
#
#     for i in my_str:                # str1을 하나씩 뜯고
#         num = 0
#         for j in arr:               # 몇개 있나 확인
#             if i == j:
#                 num += 1
#                 if max_v < num:     # 제일 많은 글자인지 판별
#                     max_v = num
#
#     print(f'#{tc} {max_v}')



# 1859. 백만 장자 프로젝트

# 1. 제일 비싼거를 찾고 그 전 인덱스는 전부다 제일 비쌀때 팔아야함
# 2. 남은 것중 제일 비싼거를 찾고 1번 반복

# import sys
# sys.stdin = open('input_1859.txt', 'r')
#
# T = int(input())
# for tc in range(1, T+1):
#     day = int(input())
#     arr = list(map(int, input().split()))
#     profit = 0                  # 결과 값 - 벌어들인 이득
#     max_idx = -1                # 최대값의 인덱스 초기값 인덱스 범위 때문에 -1로 설정함.
#
#     while max_idx+1 != day:
#         max_v = 0
#         before_max_idx = max_idx            # 전 단계의 최대값 인덱스가 필요해서 저장해놓음
#         for i in range(max_idx+1, day):     # max_idx 다음부터의 최대값을 새로 구하기 위한 범위 설정
#             if max_v <= arr[i]:             # 최대값 구하기
#                 max_v = arr[i]
#                 max_idx = i
#
#         for j in range(max_idx - before_max_idx):           # 새로운 최대값을 구하기 까지의 횟수
#             if 0 <= j+before_max_idx+1 < day:               # 인덱스 범위 밖으로 나가는 오류 방지
#                 profit += max_v - arr[j+before_max_idx+1]
#                 # 새로운 최대값에서부터 전 단계의 최대값 사이까지의 인덱스를 각각 새로운 최대값에서 빼주고 더함
#
#     print(f'#{tc} {profit}')










# 1974. 스도쿠 검증

# import sys
# sys.stdin = open('input_1974.txt', 'r')
#
# T = int(input())
# for tc in range(1, T+1):
#     arr = [list(map(int,input().split())) for _ in range(9)]
#     my_sum = 0
#     check = 0
#     result = 0
#
#     for row in range(9):                     # 가로 체크
#         my_sum = 0
#         for col in range(9):
#             my_sum += arr[row][col]
#             if my_sum == 45:
#                 check += 1
#
#     for col in range(9):                     # 세로 체크
#         my_sum = 0
#         for row in range(9):
#             my_sum += arr[row][col]
#             if my_sum == 45:
#                 check += 1
#
#     for i in range(0, 7, 3):                 # 네모 체크
#         for j in range(0, 7, 3):
#             my_sum = 0
#             for row in range(i, i+3):
#                 for col in range(j, j+3):
#                     my_sum += arr[row][col]
#                     if my_sum == 45:
#                         check += 1
#
#         if check == 27:
#             result = 1
#         else:
#             result = 0
#
#     print(f'#{tc} {result}')
