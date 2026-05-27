def checking_palindrome(my_numbers):
    
    start = 0
    end = len(my_numbers) - 1
   
    while start < end:
        if my_numbers[start] != my_numbers[end]:
            return False
        start += 1
        end -= 1
       
    return True

