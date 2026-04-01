'''
문제 설명
한자리 숫자가 적힌 종이 조각이 흩어져있습니다. 흩어진 종이 조각을 붙여 소수를 몇 개 만들 수 있는지 알아내려 합니다.

각 종이 조각에 적힌 숫자가 적힌 문자열 numbers가 주어졌을 때, 종이 조각으로 만들 수 있는 소수가 몇 개인지 return 하도록 solution 함수를 완성해주세요.

제한사항
numbers는 길이 1 이상 7 이하인 문자열입니다.
numbers는 0~9까지 숫자만으로 이루어져 있습니다.
"013"은 0, 1, 3 숫자가 적힌 종이 조각이 흩어져있다는 의미입니다.

numbers	return
"17"	3
"011"	2

우선 무슨 조합이 가능한지 다 만들어봐야할듯?
dfs로 만들어보자 중복이 되면 안되니까 set으로 만드는게 좋을듯

그다음에 set 순회하면서 소수인지 판단해서 소수면 count +=1

'''


def main():
    numbers ="172"
    list_numbers = list(numbers)
    print(list_numbers)
    result=set()
    n = len(list_numbers)
    visit = [False]*n

    def dfs(current):
        if current:
            result.add(int(current))
        for i in range(n):
            if visit[i]==False:
                visit[i]=True
                dfs(current+list_numbers[i])
                visit[i]=False
    dfs("")
    is_prime=[True]*((10 ** 7) + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2,int(len(is_prime) ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i,len(is_prime) ,i):
                is_prime[j]=False
    count_prime=0
    print(result)
    for number in result:
        if is_prime[number]:
            count_prime += 1
    return count_prime

if __name__=="__main__":
    main()