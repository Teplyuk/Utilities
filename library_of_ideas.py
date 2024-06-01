# library of ideas embodied in code
# creator Teplyuk Valeriy
# @@@


# list with all index options
def list_all_options(n):

    # def adding_variant(list, rank):
    #     for i in range(rank, n):
    #         list_new = change_list(list, i, rank? True)
    #         if not list_new in result:
    #             result.append(list_new)
    #         adding_variant(list_new, rank + 1)

    # result = []
    # list = [i for i in range(n)]
    # adding_variant(list, 0)
    # # result.sort()

    def adding_variant(list, rank):
        for i in range(rank, n):
            if i == rank:
                adding_variant(list, rank + 1)
            else:
                list_new = change_list(list, i, rank, True)
                result.append(list_new)
                adding_variant(list_new, rank + 1)

    result = []
    list = [i for i in range(n)]
    result.append(list)
    adding_variant(list, 0)
    # result.sort()

    return result


# list with moved item
def change_list(list, old_i, new_i, new_list=False):
    if new_list:
        list_new = list.copy()
    else:
        list_new = list
    item = list_new.pop(old_i)
    list_new.insert(new_i, item)
    return list_new


# decimal to binary
def decimal_to_binary_old(decimal):
    binary = [0]
    for i in range(decimal):
        rank = 1
        for j in range(len(binary)):
            if binary[j] + rank == 0:
                binary[j] = 0
                rank = 0
            elif binary[j] + rank == 1:
                binary[j] = 1
                rank = 0
            else:
                binary[j] = 0
                rank = 1
        if rank == 1:
            binary.append(1)
    return "".join(str(binary[i]) for i in range(len(binary) - 1, -1, -1))


# decimal to binary
def decimal_to_binary(decimal):
    list = convert_number_to_reverse_list(decimal)
    rank = 0
    binary = 0
    for i in list:
        rank = 1 if rank == 0 else add_binary_number_times(rank, 10)
        binary = add_two_binary_numbers(binary, add_binary_number_times(rank, i))
    return binary


def add_binary_number_times(number, quantity):
    number_new = 0
    for i in range(quantity):
        number_new = add_two_binary_numbers(number_new, number)
    return number_new


def add_two_binary_numbers(number1, number2):
    list = []
    list1 = convert_number_to_reverse_list(number1)
    list2 = convert_number_to_reverse_list(number2)
    rank = 0
    for i in range(max(len(list1), len(list2))):
        if i < len(list1):
            digit1 = list1[i]
        else:
            digit1 = 0
        if i < len(list2):
            digit2 = list2[i]
        else:
            digit2 = 0
        if digit1 + digit2 + rank == 3:
            rank = 1
            list.append(1)
        elif digit1 + digit2 + rank == 2:
            rank = 1
            list.append(0)
        elif digit1 + digit2 + rank == 1:
            rank = 0
            list.append(1)
        else:
            rank = 0
            list.append(0)
    if rank == 1:
        list.append(1)
    list.reverse()

    return convert_list_to_number(list)


def convert_number_to_reverse_list(number):
    list = []
    while number > 0:
        list.append(number % 10)
        number = number // 10
    return [0] if list == [] else list


def binary_to_decimal(binary):
    binary_list = convert_number_to_reverse_list(binary)
    result = 0
    for i in range(len(binary_list)):
        result = result + binary_list[i] * 2**i
    return result


def convert_list_to_number(list):
    # return int("".join(map(str, list)))
    number = 0
    for digit in list:
        number = number * 10 + digit
    return number
