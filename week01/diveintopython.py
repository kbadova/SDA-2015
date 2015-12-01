from firstDay import to_digits
from firstDay import to_character
from firstDay import palindrome
import copy


def is_number_balanced(n):
    list_of_n = to_digits(n)
    print(list_of_n)
    sum1 = sum([int(str(n)[i]) for i in range(0, int((len(str(n))) / 2))])
    sum2 = sum([int(str(n)[i])
                for i in range(int((len(str(n))) / 2), len(str(n)))])
    sum3 = sum([int(str(n)[i])
                for i in range(int((len(str(n))) / 2) + 1, len(str(n)))])
    if len(list_of_n) % 2 == 0:
        return sum1 == sum2
        return False
    else:
        return sum1 == sum3
        return False

# print(is_number_balanced(1238033))


def is_increasing(seq):
    count_steps = 1
    i = 0
    a = seq[i]
    while count_steps < len(seq):
        a = seq[i]
        b = seq[i + 1]
        if a >= b:
            return False
        else:
            a, b = b, b
            i += 1
            count_steps += 1
    return True

# print(is_increasing([1,2,3,6,8]))


def is_decreasing(seq):
    count_steps = 1
    i = 0
    a = seq[i]
    while count_steps < len(seq):
        a = seq[i]
        b = seq[i + 1]
        if a <= b:
            return False
        else:
            a, b = b, b
            i += 1
            count_steps += 1
    return True

# print(is_decreasing([100, 100, 100, 100, 100]))


def get_largest_palindrom(n):
    n -= 1
    while n >= 0:
        if palindrome(n):
            break
        n -= 1
    return n

# print(get_largest_palindrom(754649))


def is_anagram(a, b):
    if len(a) != len(b):
        return False
    for i in to_character(a):
        if not i in to_character(b):
            return False
    return True

# print(is_anagram("TOP_CODER", "COTO_PROD"))


def birthday_ranges(birthdays, ranges):
    list_of_count = []
    for i in ranges:
        count = 0
        for j in birthdays:
            if j >= i[0] and j <= i[1]:
                count += 1
        list_of_count.append(count)
    return list_of_count

# print(birthday_ranges([1, 2, 3, 4, 5],
# [(1, 2), (1, 3), (1, 4), (1, 5), (4, 6)]))


def prime_numbers(n):
    setAll = set(x for x in range(2, n + 1))

    for i in range(2, n + 1):
        list1 = set(x for x in range(i * 2, n + 1, i))
        setAll = setAll - list1

    return sorted(list(setAll))

# print(prime_numbers(30))


def sum_matrix(m):
    suma = 0
    for i in m:
        suma += sum(i)
    return suma

# print(sum_matrix([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]))

##########################################################################################################33


def check_values(matrix_length, i, j):
    if i < 0:
        return False
    if j < 0:
        return False
    if i >= matrix_length:
        return False
    if j >= matrix_length:
        return False
    return True


def check_neighbours(matrix, i, j):
    list_of_neighbours = []
    matrix_length = len(matrix)
    if check_values(matrix_length, i, j+1):
        list_of_neighbours.append((i, j+1))
    if check_values(matrix_length, i, j-1):
        list_of_neighbours.append((i, j-1))
    if check_values(matrix_length, i+1, j):
        list_of_neighbours.append((i+1, j))
    if check_values(matrix_length, i - 1, j):
        list_of_neighbours.append((i - 1, j))
    if check_values(matrix_length, i+1, j+1):
        list_of_neighbours.append((i + 1, j + 1))
    if check_values(matrix_length, i-1, j-1):
        list_of_neighbours.append((i - 1, j - 1))
    if check_values(matrix_length, i+1, j-1):
        list_of_neighbours.append((i+1, j - 1))
    if check_values(matrix_length, i-1, j+1):
        list_of_neighbours.append((i-1, j+1))
    return list_of_neighbours


def refactor_matrix(matrix, bomb_coodinates):
    di = bomb_coodinates[0]
    dj = bomb_coodinates[1]
    list_of_neighbours = check_neighbours(matrix, di, dj)
    for elem in list_of_neighbours:
        matrix[elem[0]][elem[1]] = matrix[elem[0]][elem[1]] - matrix[di][dj]
        if matrix[elem[0]][elem[1]] < 0:
            matrix[elem[0]][elem[1]] = 0
    return matrix


def matrix_bombing(matrix):
    matrix_copy = copy.deepcopy(matrix)
    bomb_counter = 0
    bomb_coordinates=[(0, 0), (0, 1), (0, 2), (1, 0), (1, 1),(1, 2), (2, 0), (2, 1), (2, 2)]
    result = {}
    while bomb_counter < len(bomb_coordinates):
        refactored_matrix = refactor_matrix(matrix, bomb_coordinates[bomb_counter])
        suma = sum_matrix(refactored_matrix)
        result[bomb_coordinates[bomb_counter]] = suma
        matrix = copy.deepcopy(matrix_copy)
        bomb_counter += 1
    return result

print(matrix_bombing([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
