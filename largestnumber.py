num1=float(input("enter first number:"))
num2=float(input("enter second number:"))
num3=float(input("enter third number:"))
if (num1>=num2) and (num1>=num3):
    max=num1
elif(num2>=num1) and (num2>=num3):
    max=num2
else:
    max=num3
print("the largest number is", max)

    

