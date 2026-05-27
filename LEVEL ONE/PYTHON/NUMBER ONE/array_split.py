def split_numbers(numbers):

    even = []

    odd = []

    for number in numbers:
        if number % 2 == 0:
            even.append(number)

    for number in numbers:
        if number % 2 != 0:
            odd.append(number)
    
    
    return even, odd
