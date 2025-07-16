import artcalculator
print(artcalculator.logo)
def add(n1, n2):
    return n1 + n2
def subtract(n1,n2):
    return n1-n2
def multiply(n1,n2):
    return n1*n2
def divide(n1,n2):
    return n1/n2

operations={'+':add,'-':subtract,'*':multiply,'/':divide}
is_calc_over=False
same_result=True

while not is_calc_over:
    num1=int(input("Enter the first number:"))
    while same_result:
        operator=input("Enter the mathematical operator +,-,* or / :")
        num2=int(input("Enter the second number:"))

        if operator=='+':
            result=operations["+"](num1,num2)
        elif operator=='-':
            result = operations["-"](num1, num2)
        elif operator=='*':
            result = operations["*"](num1, num2)
        elif operator=='/':
            result = operations["/"](num1, num2)
        else:
            print("Invalid operator!!!")

        print(f"The result is {result}")
        resp=input("do you want to continue with previous result, y or n?")
        if resp=="y":
            num1=result
        else:
            same_result=False
    x=input("do you want to continue with another calculation, y or n?")
    if x=="y":
        result=0
        same_result=True
    else:
        is_calc_over=True
        print("you are exited !")

