quantity = int(input("Enter Quantity: "))
price = 0.0
total = 0.0

#if copies > 0 and copies <= 99:
if 0 < quantity <= 99:
    price = 5.95
elif 99 < quantity <= 199:
    price = 5.75
elif 199 < quantity <= 299:
    price = 5.40
elif 299 < quantity:
    price = 5.15
else:
    print("The number is invalid!")
    quit
total = quantity * price

print("Cost: $" + str(price))
print("Amount Due: $" + str(total))