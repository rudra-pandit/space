num1 = input("Enter number between 1-12 N1= ")
num2 = input("Enter number between 1-12 N2= ")

if int(num1) <= 12 and int(num2) <= 12:
    print(int(num1), "+" , int(num2), "=", int(num1)+int(num2))
    print(int(num1), "x" , int(num2), "=", int(num1)*int(num2))
else:
    print("Please, enter values between 1-12")
