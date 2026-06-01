def solution(id_list, report, k):
    answer = []
    set_report = list(set(report))
    report_list = []

    for i in range(len(set_report)) :
        report_list.append(set_report[i].split(' ')[1])

    set_list = set(report_list)

    num = [0] * len(set_list)
    dict_report = dict(zip(set_list, num))
    for i in range(len(report_list)):
        dict_report[report_list[i]] += 1

    for i in list(dict_report.keys()):

        if dict_report[i] < k:
            del dict_report[i]

    check_list = []
    for i in range(len(set_report)):
        if set_report[i].split(' ')[1] in dict_report.keys():
            check_list.append(set_report[i].split(' ')[0])
    for i in range(len(id_list)):
        answer.append(check_list.count(id_list[i]))
    return answer



print(solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2)   )