def sum_of_digits(n):
    n = abs(n)
    sum = 0
    for i in range(0, len(str(n))):
        sum += int(str(n)[i])
    return sum

# print(sum_of_digits(1325132435356))


def to_digits(n):
    list_of_digits = []
    for i in str(n):
        list_of_digits.append(int(i))
    return list_of_digits

# print(to_digits(1325132435356))


def to_number(digits):
    string = ""
    for item in digits:
        string += str(item)
    return int(string)

# print(to_number([9,9,9,9,9]))


def fact_digits(n):
    list_of_digits = to_digits(n)
    sum = 0
    for item in list_of_digits:
        sum += factorial(item)
    return sum


def factorial(n):
    fact = 1
    while n != 1:
        fact *= n
        n = n - 1
    return fact

#(fact_digits(999))

def fibonacci(n):
    list_of_first_n_numbers = []
    count_steps = 1
    a, b = 1, 1
    c = a + b
    list_of_first_n_numbers.append(a)
    while count_steps != n:
        a = b
        b = c
        c = a + b
        list_of_first_n_numbers.append(a)
        count_steps = count_steps + 1
    return list_of_first_n_numbers

# print(fibonacci(10))


def fib_number(n):
    return to_number(fibonacci(n))

# print(fib_number(8))

def to_character(string):
    list_of_digits = []
    for item in string:
        list_of_digits.append(item)
    return list_of_digits

# print(to_character("bababasd"))

def palindrome(obj):
    if type(obj) == int:
        list_of_digits = to_digits(obj)
    else:
        list_of_digits = to_character(obj)
    i = 0
    j = len(list_of_digits) - 1
    while i < int(len(list_of_digits) / 2):
        if list_of_digits[i] == list_of_digits[j]:
            i += 1
            j -= 1
        else:
            return False
    return True

# print(palindrome(121))

def count_vowels(str):
    count = 0
    vowels = "aoeyiu"
    for element in str.lower():
        for vowel in vowels:
            if element == vowel:
                count += 1
    return count

#print(count_vowels("Github is the second best thing that happend to programmers, after the keyboard!"))

def count_consonants(str):
    count = 0
    consonants = "bcdfghjklmnpqrstvwxz"
    for element in str.lower():
        if element in consonants:
            count += 1
    return count

#print(count_consonants("Github is the second best thing that happend to programmers, after the keyboard!"))

def char_histogram(string):
    list1 = []
    list2 = []
    for symbol in string:
        list1.append(symbol)
        list2.append(list1.count(symbol))
    dictionary = dict(zip(list1, list2))
    return dictionary

# print(char_histogram("AAAAaab!!!"))
