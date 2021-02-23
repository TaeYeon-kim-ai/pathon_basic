#bool() #True #False

#None
#0 + 0.0 = False

#빈컨테이너 
#("", b"", [], (), {})  = False


print(bool(2164564616))
print(bool("ㅇㅂㅇ"))
# True
# True

print(bool({"a":"a"}))
#True



number = 65464646465
if number != 0: 
    print("처리를 한다")

else:
    print("0이 나왔습니다.")


number = 65464646465
if number : #파이썬은 자동으로 bool로 반환
    print("처리를 한다")

else:
    print("0이 나왔습니다.")


message = ""

if message : #메시지가 있으면 처리한다
    print("처리를 한다")

else : 
    print("메시지를 입력해주세요")



