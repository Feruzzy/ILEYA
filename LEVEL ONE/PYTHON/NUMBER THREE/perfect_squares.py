import math

def get_perfect_squares(numbers):
    perfect_squares = []
    for number in numbers:
        if number >= 0:
            root = math.isqrt(number)
            if root * root == number:
                perfect_squares.append(number)
               
    return perfect_squares


my_numbers = [4, 7, 9, 10, 16, 18]
output = get_perfect_squares(my_numbers)
print(output) 
