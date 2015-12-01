from firstDay import to_character
import re

def count_words(arr):
    dictionary = dict()
    for i in arr:
        dictionary[i] = arr.count(str(i))
    return dictionary

# print(count_words(["apple", "banana", "apple", "pie"]))


def nan_expand(times):
    list_of_a = []
    for i in range(0, times):
        list_of_a.append("Not a")
    list_of_a.append("NaN")
    return " ".join(str(x) for x in list_of_a)
# print(nan_expand(3))


def iterations_of_nan_expand(expanded):
    "".join(to_character(expanded))
    return expanded.replace(" ", "").count("Nota")
# print(iterations_of_nan_expand("Not a Not a NaN"))


def append_list(list_of_nums):
    index = 1
    firs_elem = list_of_nums[0]
    result = [firs_elem]
    while index < len(list_of_nums) and firs_elem == list_of_nums[index]:
        result.append(list_of_nums[index])
        index += 1
    return result


def group(list_of_group):
    result = []
    while len(list_of_group) != 0:
        current_group = append_list(list_of_group)
        result.append(current_group)
        list_of_group = list_of_group[len(current_group):]
    return result

#print(group([1, 2, 1, 2, 3, 3]))


def max_consecutive(items):
    list1_of_len = []
    for i in group(items):
            list1_of_len.append(len(i))
    return max(list1_of_len)

# print(max_consecutive([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 5]))


def sum_of_numbers(str):
    suma = 0
    for i in re.findall('\d+', str):
        suma += int(i)
    return suma

# print(sum_of_numbers("ab"))


def check_first_station(stations, result, tank_size):
    for i in range(0, len(stations)):
        if stations[i] > tank_size:
            result.append(stations[i-1])
            break
    return result


def gas_stations(distance, tank_size, stations):
    stations.append(distance)
    result, list_of_max_distance = [], []
    check_first_station(stations, result, tank_size)

    for i in range(0, len(stations)):
        for j in range(1, len(stations) - 1):
            if stations[j] - stations[i] < tank_size:
                list_of_max_distance.append(stations[j])
            maxi = max(list_of_max_distance)
        if maxi not in result:
            result.append(maxi)
    return result

print(gas_stations(320, 90, [50, 80, 140, 180, 220, 290]))
