input_question =  input("What is the answer to the Great Question of Life, the Universe, and Everything? ").strip().lower()

if input_question == "42" or input_question == "forty-two" or input_question == "forty two":
    print("Yes")
else:
    print("No")