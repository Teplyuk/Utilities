# library of ideas embodied in code
# creator Teplyuk Valeriy


# list with all index options
def list_all_options(n):

    # def adding_variant(list, rank):
    #     for i in range(rank, n):
    #         list_new = change_list(list, i, rank, True)
    #         if not list_new in result:
    #             result.append(list_new)
    #         adding_variant(list_new, rank + 1)

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
    # 1 variant
    # adding_variant(list, 0)
    # 2 variant
    while True:
        new_list = next_item_list(list)
        if list == new_list:
            break
        else:
            list = new_list
            result.append(list)
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


def next_item_list(list):
    for i in range(len(list) - 2, -1, -1):
        begin = list[:i]
        end = list[i:]
        end.sort()
        for item in end:
            if list[i] < item:
                begin.append(item)
                end.remove(item)
                list = begin + end
                break
        if list == begin + end:
            break
    return list


def hamming(n):

    def add_list(list):
        res = list[3]
        index = len(list_auxiliary)
        for item in reversed(list_auxiliary):
            index -= 1
            if item[3] == res:
                return
            if item[3] < res:
                list_auxiliary.insert(index + 1, list)
                return
        list_auxiliary.append(list)

    list_auxiliary = []
    number_next = [0, 0, 0, 1]
    add_list(number_next)
    for i in range(n - 1):
        number = list_auxiliary[i]

        number_next = number.copy()
        number_next[0] = number_next[0] + 1
        number_next[3] = number_next[3] * 2
        add_list(number_next)

        number_next = number.copy()
        number_next[1] = number_next[1] + 1
        number_next[3] = number_next[3] * 3
        add_list(number_next)

        number_next = number.copy()
        number_next[2] = number_next[2] + 1
        number_next[3] = number_next[3] * 5
        add_list(number_next)

    return list_auxiliary[n - 1][3]


def get_generation(cells: list[list[int]], generations: int) -> list[list[int]]:

    def add_empty_borders(cells):
        for row in cells:
            row.insert(0, 0)
            row.append(0)
        cells.insert(0, [0] * len(row))
        cells.append([0] * len(row))
        return cells

    def remove_empty_borders(cells):
        def empty_top(cells):
            if len(cells) == 0:
                return False
            for item in cells[0]:
                if item == 1:
                    return False
            return True

        def remove_top(cells):
            del cells[0]
            return cells

        while empty_top(cells):
            cells = remove_top(cells)

        def empty_bottom(cells):
            if len(cells) == 0:
                return False
            for item in cells[len(cells) - 1]:
                if item == 1:
                    return False
            return True

        def remove_bottom(cells):
            del cells[len(cells) - 1]
            return cells

        while empty_bottom(cells):
            cells = remove_bottom(cells)

        def empty_left(cells):
            if len(cells) == 0:
                return False
            for item in cells:
                if item[0] == 1:
                    return False
            return True

        def remove_left(cells):
            for item in cells:
                del item[0]
            return cells

        while empty_left(cells):
            cells = remove_left(cells)

        def empty_right(cells):
            if len(cells) == 0:
                return False
            for item in cells:
                if item[len(item) - 1] == 1:
                    return False
            return True

        def remove_right(cells):
            for item in cells:
                del item[len(item) - 1]
            return cells

        while empty_right(cells):
            cells = remove_right(cells)

        return cells

    def get_live_cell(cells, row, column):
        len_row = len(cells[row])
        len_column = len(cells)
        displacement = [-1, 0, 1]
        arround = 0
        for i in displacement:
            for j in displacement:
                if (
                    row + i >= 0
                    and row + i < len_column
                    and column + j >= 0
                    and column + j < len_row
                    and (i != 0 or j != 0)
                ):
                    arround += cells[row + i][column + j]
        if arround == 3:
            return 1
        if arround == 2:
            return cells[row][column]
        return 0

    for _ in range(generations):
        cells = add_empty_borders(cells)
        gen_cells = []
        for i in range(len(cells)):
            row = []
            for j in range(len(cells[i])):
                row.append(get_live_cell(cells, i, j))
            gen_cells.append(row)
        cells = remove_empty_borders(gen_cells)

    return cells


def exp_sum_full(n):

    def add_variant():
        new_result = []
        for list in result:
            for i in range(len(list)):
                if i == 0 or list[i] != list[i - 1] and list[i] != 0:
                    new_list = list.copy()
                    new_list[i] += 1
                if new_list not in new_result:
                    new_result.append(new_list)
        return new_result

    result = []
    for i in range(n):
        result = add_variant()
        result.append([1] * (i + 1) + [0] * (n - i - 1))

    return result


def list_prime_numbers(n):
    """index of list is prime"""
    list = [True] * n
    list[0] = list[1] = False
    for i in range(2, n):
        if list[i]:
            for j in range(i * 2, n, i):
                list[j] = False
    return list


def greatest_common_divisor(a, b):
    # if a > b:
    #     return greatest_common_divisor(a - b, b)
    # elif a < b:
    #     return greatest_common_divisor(a, b - a)
    # else:
    #     return a

    if b == 0:
        return a
    return greatest_common_divisor(b, a % b)


def fast_exponentiation(a: float, n: int):
    if n == 0:
        return 1
    elif n % 2 == 0:
        return fast_exponentiation(a * a, n / 2)
    elif n % 2 == 1:
        return fast_exponentiation(a, n - 1) * a


def generate_list_numbers(calculus, rank):

    def generate_next_numbers(rank, prefix):
        if rank == 0:
            result.append(prefix.copy())
            return
        # prefix = prefix or []
        for digit in range(calculus):
            # prefix.append(digit)
            generate_next_numbers(rank - 1, prefix + [digit])
            # prefix.pop()

    result = []
    generate_next_numbers(rank, [])
    return result


def generate_permutatuon(calculus, rank):

    def generate_next_numbers(rank, prefix):
        if rank == 0:
            result.append(prefix.copy())
            return
        # prefix = prefix or []
        for digit in range(calculus):
            if digit in prefix:
                continue
            # prefix.append(digit)
            generate_next_numbers(rank - 1, prefix + [digit])
            # prefix.pop()

    result = []
    if rank > calculus:
        rank = calculus
    generate_next_numbers(rank, [])
    return result


def different_trajectories(q_point, max_step):
    list = [0] * (max_step - 1) + [1] + [0] * (q_point)
    for i in range(max_step, q_point + max_step):
        for step in range(max_step):
            list[i] += list[i - step - 1]
    return list[q_point + max_step - 1]


def quantity_combinations_numbers(n):
    """quantity of combinations of numbers to obtain the sum of the number n"""
    if n < 0:
        return 0
    partitions = [0] * (n + 1)
    partitions[0] = 1

    for i in range(1, n + 1):
        j = 1
        while True:
            pentagonal1 = i - (3 * j**2 - j) // 2
            pentagonal2 = i - (3 * j**2 + j) // 2
            if pentagonal1 < 0 and pentagonal2 < 0:
                break
            sign = -1 if j % 2 == 0 else 1
            if pentagonal1 >= 0:
                partitions[i] += sign * partitions[pentagonal1]
            if pentagonal2 >= 0:
                partitions[i] += sign * partitions[pentagonal2]
            j += 1

    return partitions[n]


def longest_common_subsequence(A, B):
    F = [[0] * (len(B) + 1) for _ in range(len(A) + 1)]
    for i in range(1, len(A) + 1):
        for j in range(1, len(B) + 1):
            if A[i - 1] == B[j - 1]:
                F[i][j] = F[i - 1][j - 1] + 1
            else:
                F[i][j] = max(F[i - 1][j], F[i][j - 1])
    return F[-1][-1]


def longest_increasing_subsequence(A):
    F = [1] + [0] * (len(A))
    for i in range(1, len(A)):
        for j in range(0, i):
            if A[j] < A[i] and F[i] < F[j]:
                F[i] = F[j]
        F[i] += 1
        if F[len(A)] < F[i]:
            F[len(A)] = F[i]

    return F[len(A)]


def levenshtein_distance(A, B):
    F = [
        [i + j if i * j == 0 else 0 for j in range(len(B) + 1)]
        for i in range(len(A) + 1)
    ]

    for i in range(1, len(A) + 1):
        for j in range(1, len(B) + 1):
            if A[i - 1] == B[j - 1]:
                F[i][j] = F[i - 1][j - 1]
            else:
                F[i][j] = 1 + min(F[i - 1][j], F[i][j - 1], F[i - 1][j - 1])

    return F[len(A)][len(B)]
