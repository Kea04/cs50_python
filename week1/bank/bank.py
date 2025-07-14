greeting = input(str("Greeting: "))

greeting_lower = greeting.lower()
greeting_index = greeting_lower[0]

if greeting_lower == "Hello":
    print("$0")
elif greeting_index == "h" and greeting_lower != "hello":
    print("$20")
else:
    print("$100")