def book_suggestion_system():
    while True:
        print("\n---Welcome to the Book Suggestion System---")
        print("1. Get Suggestions")
        print("2. Add Book") 
        print("3. Remove Book") 
        print("4. Update book") 
        print("5. Show all books")
        print("0. Back")

        choice = input("Enter operation: ")

        if choice == "1":
            book_suggestion_system_get_suggestions()
        elif choice == "2":
            add_book()
        elif choice == "3":
            remove_book()
        elif choice == "4":
            update_book()
        elif choice == "5":
            show_books()
        elif choice == "0":
            break
        else:
            print("Get Suggestions selected:", choice)



def book_suggestion_system_get_suggestions():
    while True:
        print("\n--- Book for the Day: ---")
        print("1. Book Title: ")
        print("2. WOuld you like to get another suggestion?(yes/no):")
        print("0. Back")
        
        choice = input("select option: ")
        if choice == "0":
            break
        elif choice == "1":
            book_title_for_the_day()
        elif choice == "2":
            another_suggestion()
        else:
            print("Option selected:", choice)

def another_suggestion():
    while True:
        print("1. yes")
        print("2. no")
        print("0. Back")
        
        choice = input("select option: ")
        if choice == "0":
            break
        elif choice == "1":
            book_title_for_another_suggestion()
        elif choice == "2":
            break
        else:
            print("Option selected:", choice)


def book_title_for_another_suggestion():
    while True:
        print("The Mystery")
        print("Page: 12")
        print("0. Back")

        choice = input("select option: ")
        if choice == "0":
            break
        else:
            print("Option selected:", choice)
    

     


def book_title_for_the_day():
    while True:
        print("The Hobbit")
        print("Page: 47")
        print("0. Back")

        choice = input("select option: ")
        if choice == "0":
            break
        else:
            print("Option selected:", choice)


def add_book():
    while True:
        print("1. Enter the book title: ")
        print("0. Back")
            
        choice = input("Enter Operation: ")

        if choice == "1":
            book_title()
        elif choice == "0":
            break
        else:
            print("Option selected:", choice)

def book_title():
    while True:
        print("Animal Farm")
        print("Book added successfully!")
        print("0. Back")

        choice = input("select option: ")
        if choice == "0":
            break
        else:
            print("Option selected:", choice)



def remove_book():
    while True:
        print("1. Enter the book title to remove: ")
        print("0. Back")
            
        choice = input("Enter Operation: ")

        if choice == "1":
            book_title_to_remove()
        elif choice == "0":
            break
        else:
            print("Option selected:", choice)

def book_title_to_remove():
    while True:
        print("The mystry")
        print("Book removed successfully!")
        print("0. Back")

        choice = input("select option: ")
        if choice == "0":
            break
        else:
            print("Option selected:", choice)


def update_book():
    while True:
        print("1. Enter the old title: ")
        print("0. Back")

        choice = input("Enter Operation: ")
        
        if choice == "1":
            update_old_book()
        elif choice == "0":
            break
        else:
            print("Option selected:", choice)

def update_old_book():
    while True:
        print("Brave Kind")
        print("1. Enter the new title: ")
        print("0. Back")
        
        choice = input("Enter Operation: ")

        if choice == "1":
            update_new_book()
        elif choice == "0":
            break
        else:
            print("Option selected:", choice)


def update_new_book():
    while True:
        print("Brave Kingdom")
        print("Book updated successfully!")
        print("0. Back")

        choice = input("select option: ")
        if choice == "0":
            break
        else:
            print("Option selected:", choice)



def show_books():
    while True:
        print("\n--- All Books---")
        print("1. The Hobbit")
        print("2. The Mystery")
        print("3. Animal Farm")
        print("4. Brave Kingdom")
        print("5. ............")
        print("0. Back")
        
        choice = input("select option: ")
        if choice == "0":
            break
        else:
            print("Showing books...")




book_suggestion_system()



      
        







    
     
