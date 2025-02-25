num1 = int(input("Enter num: "))
num2 = int(input("Enter second num: "))
temp = 0
while (num2 > 0) {
    temp = num1 % num2;
    num1 = num2;
    num2 = temp;
}
print("The GCD is: " + str(temp))