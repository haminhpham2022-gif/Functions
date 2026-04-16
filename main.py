def display():
    name="penguin"
    print(f"my name is {name}")

display()

def display1():
    name="penguin"
    return f"my name is {name}"

print(display1())

def display2(name):
    return f"my name is {name}"

name=input("enter your name: ")
print(display2(name))