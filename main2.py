def add(a,b):
    return a + b

def subtract(a,b):
    return a - b

def multiply(a,b):
    return a * b

def divide(a,b):
    if b==0:
        print("zero division error")
    else:
        return a / b

print("Welcome to our calculator: \n Choose an option: ")

while True:
    print("1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Exit")
    choice=int(input("Enter your choice: "))
    if choice==5:
        print("Goodbye!!")
        break
    elif choice==1:
        a=float(input("Enter the first number: "))
        b=float(input("Enter the second number: "))
        result=add(a,b)
        print(f"result is: {result}")
    elif choice==2:
        a=float(input("Enter the first number: "))
        b=float(input("Enter the second number: "))
        result=subtract(a,b)
        print(f"result is: {result}")
    elif choice==3:
        a=float(input("Enter the first number: "))
        b=float(input("Enter the second number: "))
        result=multiply(a,b)
        print(f"result is: {result}")
    elif choice==4:
        a=float(input("Enter the first number: "))
        b=float(input("Enter the second number: "))
        result=divide(a,b)
        print(f"result is: {result}")
    else:
        print("Invalid option!!")
        continue
    print("do you want to continue?")
    option=input(":")
    if option.lower().strip()=="yes":
        continue
    else:
        print("goodbye!!")
        break