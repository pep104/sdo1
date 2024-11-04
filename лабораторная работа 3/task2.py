participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"


# TODO Провеьте работу функции с разделителем отличным от запятой

def find_common_participants(first_group, second_group, separator = ','):
    first_group_arr = first_group.split(separator)
    second_group_arr = second_group.split(separator)
    ans = []
    for i in first_group_arr:
        if i in second_group_arr:
            ans.append(i)
    return ans


ans2 = find_common_participants(participants_first_group, participants_second_group, '|')
print(*ans2)
