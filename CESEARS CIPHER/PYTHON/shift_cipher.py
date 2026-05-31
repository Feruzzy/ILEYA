def encrypt_caesar(message, shift):
    lower_alphabet = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
    upper_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"
    encrypted_text = ""
   
    for letter in message:
        if letter in lower_alphabet:
           
            position = 0
            for alpha_letter in lower_alphabet:
                if alpha_letter == letter:
                    break  
                position = position + 1
               
            new_position = position + shift
            encrypted_text = encrypted_text + lower_alphabet[new_position]
           
        elif letter in upper_alphabet:
            
            position = 0
            for alpha_letter in upper_alphabet:
                if alpha_letter == letter:
                    break
                position = position + 1
               
            new_position = position + shift
            encrypted_text = encrypted_text + upper_alphabet[new_position]
           
        else:
            encrypted_text = encrypted_text + letter
           
    return encrypted_text


print(encrypt_caesar("i want to marry a software engineer like myself", 10)) 
print(encrypt_caesar("HOW ARE YOU DOING TODAY!", 20))
print(encrypt_caesar("hello can you dash me one million naira", 6))
