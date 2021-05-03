'''
평소 호기심이 많은 남호는 정보고 사이트에 있는 달팽이 배열 문제를 다르게 만들고 싶었다.

입력 예시와 출력 예시를 참고 하여 n을 입력 받아 출력하는 프로그램을 작성하시오.

입력
배열의 크기 n이 입력된다. (n은 15보다 작은 홀수)

출력
역 달팽이 배열을 출력한다.

입력 예시   
5

출력 예시
1 16 15 14 13 
2 17 24 23 12 
3 18 25 22 11 
4 19 20 21 10 
5 6 7 8 9 
'''
n = int(input())
m = [[0]*n for i in range(n)]
cnt = 0
offset = 0
row = n #행
col = n #열

while row > 0 and col > 0:
    for i in range(offset, offset+col): #열 하나씩 늘리기 가로
        cnt += 1
        m[i][offset] = cnt

    for i in range(offset+1, offset+row): # 세로
        cnt += 1
        m[offset+col-1][i] = cnt
        
    for i in range(offset+col-2, offset-1, -1): #가로
        cnt += 1
        m[i][offset+row-1] = cnt

    for i in range(offset+row-2, offset, -1): #반대세로
        cnt += 1
        m[offset][i] = cnt

    offset += 1
    row -= 2
    col -= 2

for i in range(0, n):
    for j in range(0, n):
        print(m[i][j], end=' ')
    print()