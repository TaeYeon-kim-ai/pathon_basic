'''
10*10 크기의 보드판이 있다.

각 말들은 제일 아래쪽에서 위쪽 방향으로 진격한다.

장애물은 0이 아닌 숫자로 나타내며, 0보다 크면 블럭 장애물, 0보다 작으면 구덩이 장애물, 0이면 평지이다.

10*10 보드판의 정보가 입력되고, 각 세로줄 아래에 말이 있으면 1, 없으면 0이 입력될 때 각 말의 생존여부를 구하는 프로그램을 구현하시오.

입력
10*10의 보드판의 정보가 입력된다.

11째줄에 각 말의 위치 여부가 입력된다.(1:있음, 0:없음)

출력
블럭 장애물에 부딪혀서 실패시 "세로줄 번호 crash", 

구덩이에 떨어져서 실패시 "세로줄 번호 fall",

무사히 통과하면 "세로줄 번호 safe"를 출력한다.

(단, 말이 없는 줄은 아무결과도 출력하지 않는다.)

입력 예시   
0 0 0 0 0 0 0 0 0 0 
0 2 0 0 0 0 0 0 0 0 
0 0 -1 0 0 0 0 0 2 0 
0 0 0 0 0 0 0 6 0 0 
0 0 0 0 0 0 0 0 0 0 
0 0 0 0 0 -4 2 0 0 0 
0 0 2 0 0 0 0 0 0 0 
0 0 0 0 3 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 0 
1 1 0 0 1 1 0 1 0 1 

출력 예시
1 safe
2 crash
5 crash
6 fall
8 crash
10 safe
'''

m = []
isProblem = False

for i in range(10) : 
    board = list(map(int, input().split()))

horse = list(map(int, input().split()))

for i in range(0, 10) :
    if horse[i] == 0 :
        continue
    isProblem = False
    for j in range(9, -1, -1) :
        if m[j][i] != 0:
            if m[j][i] > 0 :
                print(i+1, 'crash')
                isProblem = True
                break
            else:
                print(i+1, 'fall')
                isProblem = True
                break
        if not isProblem : 
            print(i+1, 'safe')



m = []
isProblem = False
​
for i in range(10):
    board = list(map(int, input().split()))
    m.append(board)
​
horse = list(map(int, input().split()))
​
for i in range(0, 10):
    if horse[i] == 0:
        continue
    isProblem = False
    for j in range(9, -1, -1): #9부터 끝까지 -1(reverse)
        if m[j][i] != 0:
            if m[j][i] > 0:
                print(i+1, 'crash')
                isProblem = True
                break
            else:
                print(i+1, 'fall')
                isProblem = True
                break
    if not isProblem:
        print(i+1, 'safe')

'''
matrix = []
isProblem = False
​
for i in range(10):
    board = list(map(int, input().split()))
    matrix.append(board)
​
horse = list(map(int, input().split()))
​
for i in range(0, 10):
    if horse[i] == 0:
        continue
    isProblem = False
    for j in range(9, -1, -1):
        if matrix[j][i] != 0:
            if matrix[j][i] > 0:
                print(i+1, 'crash')
                isProblem = True
                break
            else:
                print(i+1, 'fall')
                isProblem = True
                break
    if not isProblem:
        print(i+1, 'safe')
'''
