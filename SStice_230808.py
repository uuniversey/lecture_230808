

# 슬라이싱을 이용한 문자열 탐색

# for _ in range(10):
#     tc = int(input())
#     fs = input()
#     s = input()
#     cnt = 0
#     for i in range(len(fs), len(s)):
#         if s[i-len(fs):i] == fs:
#             cnt += 1
#
#     print(f'#{tc} {cnt}')

# 브루트 포스

# t : target 비교하려는 원래 문자열 (젤 긴거)
# t_idx : target의 인덱스
# p : pattern 비교하려는 문자열 (짧은거)
# p_idx : pattern의 인덱스


# target에서 pattern이 일치하는 t_idx의 시작점을 반환하는 함수

# def my_len(arr):
#     count = 0
#     for i in arr:
#         count += 1
#     return count
#
# def brute_force(target, pattern):
#     # 시작 점 부터 비교
#     t_idx = 0
#     p_idx = 0
#
#     t_len = my_len(target)
#     p_len = my_len(target)
#
#     while (t_idx < t_len) and (p_idx < p_len):
#         # 문자열 비교
#         if target[t_idx] == pattern[p_idx]: # 만약 같다면?
#             #다음번째의 문자를 비교
#             t_idx += 1
#             p_idx += 1
#         else:       #만약 문자가 같지 않다면?
#             t_idx = t_idx - p_idx + 1
#             p_idx = 0

# test
# my_list = ['a','b','c','d','c','b','a']
# if my_list[::] == my_list[::-1]:
#     print(True)



# 보이어-무어 알고리즘 딕셔너리를 통해 만들어보기 - 교수님이 구현해놓은거 올려줄거니까 짜보고 비교해보기


#
