Ecount = int(input("Enter Egg Count:"))
cost = 0.00
does = Ecount // 12
Eegg = Ecount % 12
Ecegg = 0.00
if 0 <= does < 4:
    cost = does * 0.50
    Ecegg = Eegg * (0.50 / 12)
    print("Your total is: " + str(cost + Ecegg))
elif 4 <= does < 6:
    cost = does * 0.45
    Ecegg = Eegg * (0.45 / 12)
    print("Your total is: " + str(cost + Ecegg))
elif 6 <= does < 11:
    cost = does * 0.40
    Ecegg = Eegg * (0.40 / 12)
    print("Your total is: " + str(cost + Ecegg))
elif 11 <= does:
    cost = does * 0.35
    Ecegg = Eegg * (0.35 / 12)
    print("Your total is: " + str(cost + Ecegg))