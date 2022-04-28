def solution(lottos, win_nums):
    count = 7
    zero_count = 0
    for i in range (0,6):
        for j in range (0,6):
            if lottos[i] == win_nums[j]:
                count -= 1
        if lottos[i] == 0:
            zero_count += 1
    max = 0
    min = 0
    if count < 7:
        print('여기는 안돼')
        min = count
        max = min - zero_count
    else:
        min = 6
        if zero_count == 6:
            max = min - zero_count+1
        else:
            max = min - zero_count


    answer = [max, min]
    return answer

lottos = [0, 0, 0, 0, 0, 0]
win_nums = [38, 19, 20, 40, 15, 25]

print(solution(lottos, win_nums))

'''
 result는 [max, min]
 max는 최대 등수 
 min은 최소 등수
 
 0은 알수 없음을 의미함..
 같은 숫자가 생기면,,등수가 올라감
 
 2개 번호 일치하면-> 5등
 그 이후부터 차례 등수
 
 그 외는 6등으로 해야함
 --- min 값을 의미함 ---
 
 --- max 값 ---
 0의 개수 보고 판단, min의 등수를 보고 0의 갯수와 비교해서 max값 판별
 
 
 
'''

