
'''
두수의 합
nums = [2,7,11,15]
target = 9
return =[0,1]
* 조건 = 같은 인덱스 사용금지
O(N)
인덱스를 기억해야하므로 hash를 사용하면 편리할듯?

'''
def main():
    nums = [2,7,11,15]
    target = 9
    dic = {}
    for i,num in enumerate(nums):
        need = target-num
        if need in dic:
            return [dic[need],i]
        dic[num]=i
    return -1
if __name__ == "__main__":
    main()