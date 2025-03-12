from cl213f import ElectricBill

def main():
    try:
        with open("Langdat/prog213f.dat", 'r') as f:
            for line in f:
                kwh = int(line)
                if kwh != -999:
                    e_bill = ElectricBill(kwh)
                    bill.append(e_bill)
        for bill in bills:
            bill.calc()
            print(bill)
    except OSError as e:
        print("Error:", e)



if __name__ == "__main__":
    main()