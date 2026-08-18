#1 function of add
def add(x,y):
    return x + y

#2 function of sbract
def subtract(x,y):
    return x - y

#3 function of multyi :
def multiply(x,y):
    return x * y

#4 function of we :
def divide(x,y):
    if y == 0 :
        return "Error : cannot divide by zero"
    return x / y
    
#5 function of f :
def modulo(x,y):
    if y == 0 :
            return "Error : cannot divide by zero"
    return x % y

def main():
    First = float(input("chose the first number "))
    Second = float(input("chose the seconde number "))
    Opreator = input("chose on '/', '*', '-', '+', '%' ")

    #chose the opreation :
    if Opreator == '+' :
        print("you chose addtion '+'")
        print(add(First,Second))

    elif Opreator == '-' :
        print("you chose subraction '-'")
        print(subtract(First,Second))

    elif Opreator == '*' :
        print("you chose multiup '*'")
        print(multiply(First,Second))

    elif Opreator == '/' :
        print("you chose we '/'")
        print(divide(First,Second))

    elif Opreator == '%' :
        print("you chose us '%'")
        print(modulo(First,Second))

    else :
        print("invalib opreator")
if __name__ == "__main__":
    main()