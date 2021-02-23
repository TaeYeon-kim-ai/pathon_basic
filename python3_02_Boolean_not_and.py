#단항 연산자
#피 연산자를 하나만 갖게됨
#not 연산자

not True  #False
not False #True

#이항연산자
True and True #그리고
or # 또는

#사과 그리고 배 : 사과 + 배 둘 다 들고와
#사과 또는 배 : 사과와 배 중에 아무거나 들고와
#사과 그리고 똥 : 사과 + 똥 -> 명령 거부
#사과 또는 똥 : 명령 OK

사과 and 사과 : OK #True and True = True
사과 and 똥   : X  # True and False = False
똥 and 사과   : X  # False and True = False
똥 and 똥     : XX # False and False = False


age = 20
under_25 = age < 25
under_25
#True

#연예인 티켓구매 시 1인당 1매 + 오후 3시 이후 구매가능
