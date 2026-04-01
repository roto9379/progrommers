'''
progrommers.hindex의 Docstring
H-Index는 과학자의 생산성과 영향력을 나타내는 지표입니다. 어느 과학자의 H-Index를 나타내는 값인 h를 구하려고 합니다. 위키백과1에 따르면, H-Index는 다음과 같이 구합니다.

어떤 과학자가 발표한 논문 n편 중, h번 이상 인용된 논문이 h편 이상이고 나머지 논문이 h번 이하 인용되었다면 h의 최댓값이 이 과학자의 H-Index입니다.

어떤 과학자가 발표한 논문의 인용 횟수를 담은 배열 citations가 매개변수로 주어질 때, 이 과학자의 H-Index를 return 하도록 solution 함수를 작성해주세요.

제한사항
과학자가 발표한 논문의 수는 1편 이상 1,000편 이하입니다.
논문별 인용 횟수는 0회 이상 10,000회 이하입니다.

h_index = 0 
논문의 갯수 n까지만 순회-> 왜냐하면 h가 n보다 클수없기때문에
순회하면서 조건 체크
조건 체크 어떻게하냐?
 idx
 h 
 나머지 논문이 h번 이하 인용
 case 1 : idx+1>=h
 case 2:  n-(idx+1)<=h
오름차순일떄
102,101,100
1<=c[0]
2<=c[1]
3<=c[2]
102 , 101 , 100
 1  ,  2 , 3

 1 <= 102:
 1번 이상 인용된 논문이 1편 이상이고
 나머지 논문이 1번 이하 인용되었다면 1

 1 ->102
 2 -> 101
'''
def main():

    citations = [1, 2, 2, 3, 3, 4, 4]
    citations.sort(reverse=True)
    print(citations)
    h_index = 0
    for idx,h in enumerate(citations):
        if idx+1<=h:
            h_index = idx+1
        else:
            break
    # print(h_index)
    return h_index

    


if __name__=="__main__":
    main()
