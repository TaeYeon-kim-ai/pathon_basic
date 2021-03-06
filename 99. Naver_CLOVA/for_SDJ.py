'''
미술 작품에 가격을 매기는 일은 쉽지 안ㅅ습니다. 작품의 가치를 매길 수 있는 정확한 지펴가 없기 떄문
그렇기 떄문에 사람의 주관이 많이 들어가게됨

이런 문제를 해결하기 위해 여러 전문가들에게 감정을 맡겨보기로 했습니다. 하지만 전문가도 항상 정당한 값
을 매기기는 어렵습니다 또 의도적으로 높게 혹은 낮게 가격을 매길 수 있습니다. 그래서 다음과 같은 4가지
방법으로 판매가를 결정하려고 합니다. 1번 방법부터 적용시키 ㄹ수 있으면 적용 시켜서 판매가를 결정하고, 
적용시킬 수 없다며 다음 방법으로 차례차례 넘어갑니다.

1. 가장 비싸게 책정한 가격과 가장 싸게 책정한 가격의 차가 d원이라 하면, 모두 정당한 가격으로 책정했
다고 판단해 전문가들이 제시한 모든 가격의 평균겂으로 판매가를 결정합니다.

2. 가장 비싸게 책정한 가격 하나와 가장 싸게 책정한 가격 하나를 제외시킵니다.
나머지 가격 중 가장비싸 게 책정한 가격과 가장 싸게 책정한 가격의 차가 d원 이하라면, 
앞서 제외한 두 가격 외에는 모두 정당 한 가격이라고 판단해 두 가격을 제외한 
모든 가격의 평균값으로 판매가를 결정합니다.

3. 전문가들이 매긴 모든 가격에서 임의로 k개의 가격을 골랐을 떄 가장 비싸게 책정한 가격과 가장 싸게 
책정한 가격의 차가 d원 이하라면, 그 k개의 가격이 정당하다고 판단해 그k개의 평균값을 판매가로 결정합
니다. 만약 정당한 가격을 책정한 k개의 가격을 고르는 방법이 여러 개라면, 그 중에서 평균값이 가장 
낮은 것을 판매가로 결정합니다.

4. 중앙값을 판매가로 결정 즉, 전문가들이 매긴 모든 가격을 오름차순으로 정렬했을 떄, 가운데 위
치하는 가격을 판매가로 걀정합니다. 가격의 개수가 짝수라면, 가운데 위치하는 두 가격 중에 크지
 않은 가격을 판매가로 결정합니다.

*평균값 계산 시 소수점이하 버림
전문가가 매긴 가격정수 prices, 정수 d, 정수 k가 주어질 떄 미술작품의 판매가를 return하도록

prices            d     k     result
[4 5 6 7 8]       4     3       6
[4 5 6 7 8]       2     1       6
[4 5 6 7 8]       1     2       4
[8 4 5 7 6]       1     3       6
[1 8 1 8 1 8]     6     4       1
'''

from itertools import combinations
#3번에서 combinations 사용됨 : 한 리스트에서 몇개 묶어서 경우의수 만들 수 있음.

def solution(prices, d, k) :
    prices.sort()#먼저 정렬
    #조건1
    if prices[-1] - prices[0] <= d :  #첫번쨰 조건 성립 시 답
        return sum(prices)//len(prices)
    #조건2
    elif  prices[-2] -prices[1] <= d:
        return sum(prices[1:-1])//(len(prices)-2)
    prices1 = prices[:]
    #조건3
    else :
        possible = list(combinations(prices, k))
        possible = [x for x in possible if abs(x[0]-x[-1])<=d]
        possible = [(x[0]+x[1])//2 for x in possible]
    #조건4
        if possible == [] :
            if len(prices) %2 == 0 :
                return prices[(len(prices)//2)-1]
            else :
                return prices[(len(prices)//2]
        
        else : 
            return min(possible)
                