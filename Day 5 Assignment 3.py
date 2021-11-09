"""
Day 5
Assignment 3 (calculator)
Make a calculator using function along with if, elif and else statement.

Addition , Subtraction , Multiplication , Division

You enter two numbers and operator you want to do, it will return the answer.
"""
def Add(num1,num2):
    ans = num1 + num2
    return ans

def Sub(num1,num2):
    ans = num1 - num2
    return ans

def Mul(num1,num2):
    ans = num1 * num2
    return ans

def Div(num1,num2):
    ans = num1 / num2
    return ans

opr = input("Please enter your operation: ")
opr = opr.lower()
num1 = float(input("Please enter your first number: "))
num2 = float(input("Please enter your second number: "))
if opr == 'addition':
    ans = Add(num1,num2)
    print("Your answer is",ans)
elif opr == "subtraction":
    ans = Sub(num1,num2)
    print("Your answer is",ans)
elif opr == "multiplication":
    ans = Mul(num1,num2)
    print("Your answer is",ans)
elif opr == "division":
    ans = Div(num1,num2)
    print("Your answer is",ans)
else:
    print("Please enter a correct operation")      
