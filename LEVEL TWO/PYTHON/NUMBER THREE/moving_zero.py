def move_zeros(array):
    result = []

    for number in array:
        if number != 0:
            result.append(number)

    zero_count = array.count(0)

    for counter in range(zero_count):
        result.append(0)

    return result



print(move_zeros([5, 0, 3, 0, 2, 0]))
