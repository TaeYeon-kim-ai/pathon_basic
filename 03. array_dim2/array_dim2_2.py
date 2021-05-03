'''
n이 입력되면 크기가 n인 다음과 같은 2차원 배열을 출력하시오.

입력 예)

3
출력 예)
1 4 7
2 5 8
3 6 9
입력
2차원 배열의 크기 n이 입력된다. (n<=50)

출력
크기가 n인 배열을 출력한다.(설명 참조)

입력 예시   
2

출력 예시
1 3 
2 4 
'''
n = int(input())

map = [[0]*n for i in range(n)]

cnt = 0

for i in range(0, n) : # 0번쨰부터 n까지 넣기
    for j in range(0, n) : # 0번쨰부터 n까지 넣기
        cnt += 1 # j는 +1해서 계속 출력
        map[j][i] = cnt

for i in range(0, n) :
    for j in range(0, n) :
        print(map[i][j], end = ' ')
    print()


