user_input = input(str())

lower_input = user_input.lower()

if lower_input == "hello":
    print("hello")
elif lower_input == "50":
    print("50")
elif lower_input == "this is cs50":
    print("this is cs50")
else:
    print("Invalid input from User")