'''
progrommers.가장 큰 수의 Docstring
문제 설명
0 또는 양의 정수가 주어졌을 때, 정수를 이어 붙여 만들 수 있는 가장 큰 수를 알아내 주세요.

예를 들어, 주어진 정수가 [6, 10, 2]라면 [6102, 6210, 1062, 1026, 2610, 2106]를 만들 수 있고, 이중 가장 큰 수는 6210입니다.

0 또는 양의 정수가 담긴 배열 numbers가 매개변수로 주어질 때, 순서를 재배치하여 만들 수 있는 가장 큰 수를 문자열로 바꾸어 return 하도록 solution 함수를 작성해주세요.

제한 사항
numbers의 길이는 1 이상 100,000 이하입니다.
numbers의 원소는 0 이상 1,000 이하입니다.
정답이 너무 클 수 있으니 문자열로 바꾸어 return 합니다.

[3, 30, 34, 5, 9]
9 5 34 3 30 -> 
3 < 30
33 3030
30 300
3030 > 300300
33 332 
3333 332332
3 332

'''
def main():
    numbers = [3, 30, 300, 5, 9]
    str_numbers = [str(number) for number in numbers]
    # print(str_numbers)
    str_numbers.sort(key=lambda x:x*3,reverse=True)
    # print(str_numbers)
    answer = "".join(str_numbers)
    print(answer)
    return answer

if __name__=="__main__":
    main()
