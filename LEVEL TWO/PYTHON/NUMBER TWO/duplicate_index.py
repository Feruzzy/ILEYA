def duplicate_indexes(array):
    result = []

    for number in array:
        indexes = []

        for count in range(len(array)):
            if array[count] == number:
                indexes.append(count)

        if len(indexes) > 1:
            item = [number, indexes]

            if item not in result:
                result.append(item)

    return result



print(duplicate_indexes([-11, -9, 3, -9, 2, -11]))
