def solution(id_list, report, k):
    num1 = len(report)
    ans_list = {}
    id_dic = {}
    splitreport = [report[i].split(' ') for i in range(num1)]

    for i in id_list:
        id_dic[i] = 0

    splitreport = list(set(map(tuple, splitreport)))

    num = len(splitreport)

    for i in range(num):
        try:
            ans_list[splitreport[i][1]] += 1
        except:
            ans_list[splitreport[i][1]] = 1

    for i in range(num):
        for key in ans_list:
            if key == splitreport[i][1] and ans_list[key] >= k:
                id_dic[splitreport[i][0]] += 1

    answer = list(id_dic.values())
    return answer

id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k = 2

ans = solution(id_list, report, k)
print(ans)

