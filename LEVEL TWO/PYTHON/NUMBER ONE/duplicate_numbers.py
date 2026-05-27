def duplicates(array):
    result = []

    for number in array:
        if array.count(number) > 1 and number not in result:
            result.append(number)

    return result




print(duplicates([1, 2, 3, 2, 4, 3]))
