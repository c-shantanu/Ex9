from curses.ascii import islower, isupper

user_input = input("Please enter your string: ")
if user_input.isupper():
    print(user_input.capitalize(),"!")
elif user_input.islower():
    print(user_input.capitalize())

    

