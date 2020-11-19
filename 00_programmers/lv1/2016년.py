# 2016년 1월 1일은 금요일
# 2016년은 윤년 (2월은 29일까지)
# a월 b일은 몇요일인가?

def solution(a, b):

    day = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    mon = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    ret = b - 1

    for i in range(a):
        ret += mon[i]

    return day[ret % 7]