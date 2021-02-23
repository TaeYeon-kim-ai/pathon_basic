import datetime

now = datetime.datetime.now()

if now.hour < 12 :
    print("현재 시간은 {}시 {}분로 오전입니다!".format(now.hour, now.minute)) #현재 시간은 22시 25분로 오후입니다
if now.hour >=12 :
    print("현재 시간은 {}시 {}분로 오후입니다".format(now.hour, now.minute))


if 3 <= now.month <= 5:
    print("이번 달은 {}월로 봄입니다".format(now.month))

if 6 <= now.month <= 8:
    print("이번 달은 {}월로 여름입니다".format(now.month))

if 9 <= now.month <= 11:
    print("이번 달은 {}월로 가을입니다".format(now.month))

if now.month == 12 or 1 <= now.month <= 2 :
    print("이번 달은 {}월로 겨울입니다".format(now.month))

#이번 달은 2월로 겨울입니다

# print(now.year)
# print(now.month)
# print(now.day)
# print(now.hour)
# print(now.minute)
# print(now.second)

# 2021
# 2
# 23
# 22
# 23
# 14

