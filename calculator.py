a="+","addition"
b="-","substract"
c="*","multiply"
d="/","divide"
e="%","percentage"

def add(x,y):
    return x+y
def Sustraction(x,y):
    return x-y
def multiplication(x,y):
    return x*y
def division(x,y):
    if y !=0:
     return x/y
    else :
     return "error occur !"
def percentage (x,y):
    return x/y*100 

def calculator():
    print("Happy to see you here tell me how may i help you:")
    print("select any operation from here:")
    print("Add")
    print("Sustraction")
    print("Multiplication")
    print("Division")
    print("percentage")
   
    while True:
        choice= input("choose operation here(1/2/3/4/5):")
        if choice in ("1","2","3","4","5"):
            num1=float(input("Enter the  first number here:"))
            num2=float(input("Enter the second number here:"))
            if choice=="1":
                print(f"{num1} + {num2} = {add(num1, num2)}")
            elif choice == '2':
                print(f"{num1} - {num2} = {Sustraction(num1, num2)}")
            elif choice == '3':
                print(f"{num1} * {num2} = {multiplication(num1, num2)}")
            elif choice == '4':
                print(f"{num1} / {num2} = {division(num1, num2)}")
            elif choice =='5':
                print(f"{num1} / {num2} * 100 = {percentage(num1,num2)}")
        else:
            print("do you want to continue for more calculations:")
        
        new_calculation = input("Do you want to continue more calculation? (yes/no): ")
        if new_calculation.lower() != 'yes':
            break    
            
calculator()
