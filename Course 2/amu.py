from time import sleep

def func():
    name = input("Hi, What's your name?")
    if name == "Babeasaur":
        print("Hey Babyyyy! You're the best!")
        print("I'm sorry, I'm such an asshole.")
        sleep(1)
    else:
        print("Fuck off! Give me the NAME!")
        func()

