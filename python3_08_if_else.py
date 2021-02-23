'''
if 조건 :
    조건이 참일 떄 실행할 문장

else :
    조건이 거짓일 때 실행할 문장
'''

# if number % 2 == 0 :
#     print("짝수입니다.")

# else : 
#     print("홀수입니다.")



#봄 여름 가을 겨울
import datetime

now = datetime.datetime.now()

if now.hour < 12 :
    print("현재 시간은 {}시 {}분로 오전입니다!".format(now.hour, now.minute)) #현재 시간은 22시 25분로 오후입니다
if now.hour >=12 :
    print("현재 시간은 {}시 {}분로 오후입니다".format(now.hour, now.minute))


# if 3 <= now.month <= 5:
#     print("이번 달은 {}월로 봄입니다".format(now.month))

# else + if 6 <= now.month <= 8:
#     print("이번 달은 {}월로 여름입니다".format(now.month))

# else + if 9 <= now.month <= 11:
#     print("이번 달은 {}월로 가을입니다".format(now.month))

# else + if now.month == 12 or 1 <= now.month <= 2 :
#     print("이번 달은 {}월로 겨울입니다".format(now.month))


if 3 <= now.month <= 5:
    print("이번 달은 {}월로 봄입니다".format(now.month))

elif 6 <= now.month <= 8:
    print("이번 달은 {}월로 여름입니다".format(now.month))

elif 9 <= now.month <= 11:
    print("이번 달은 {}월로 가을입니다".format(now.month))

else :
    print("이번 달은 {}월로 겨울입니다".format(now.month))



#==============================

score = float(input(" > 학점을 입력해 :"))

if score = 4.5 :
    print("당신은 '신'입니다")
elif 4.5 > score  >=4.2 :
    print("당신은 교수님의 사랑을 받고 있습니다.")

elif 4.2 > score  >=3.5 :
    print("당신은 현 체제의 수호자입니다.")

elif 3.5 > score  >= 2.8 :
    print("당신은 일반인 입니다.")

elif 2.8 > score  >= 2.3 :
    print("당신은 일탈을 꿈꾸는 소시민 입니다.")

elif 2.3 > score  >= 1.75 :
    print("당신은 오락문화의 선구자 입니다.")

elif 1.75 > score  >= 1.0 :
    print("당신은 불가촉 천민 입니다.")

elif 1.0 > score  >= 0.5 :
    print("당신은 자벌레 입니다.")

elif 0.5 > score  >= 0.0 :
    print("당신은 플랑크톤 입니다.")

else :
    print("당신은 시대를 앞서가는 혁명의 씨앗 입니다.")


#=================================================
score = float(input(" > 학점을 입력해 :"))

if score == 4.5 :
    print("당신은 '신'입니다")
elif score  >=4.2 :
    print("당신은 교수님의 사랑을 받고 있습니다.")

elif score  >=3.5 :
    print("당신은 현 체제의 수호자입니다.")

elif score  >= 2.8 :
    print("당신은 일반인 입니다.")

elif score  >= 2.3 :
    print("당신은 일탈을 꿈꾸는 소시민 입니다.")

elif score  >= 1.75 :
    print("당신은 오락문화의 선구자 입니다.")

elif score >= 1.0 :
    print("당신은 불가촉 천민 입니다.")

elif score >= 0.5 :
    print("당신은 자벌레 입니다.")

elif score  > 0.0 :
    print("당신은 플랑크톤 입니다.")

else :
    print("당신은 시대를 앞서가는 혁명의 씨앗 입니다.")

        














