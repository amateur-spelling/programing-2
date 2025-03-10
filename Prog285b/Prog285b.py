from cl285b import Salesperson


def  main():
    try:
        print("Number\tCode\tSales\tCommission")
        with open("Langdat/prog285b.dat", 'r') as f:
            for line in f:
                data = line.split(" ")
                id = int(data[0])
                code = int(data[1])
                sales = float(data[2])

                person = Salesperson(id, code, sales)
                person.calc_commission()
                print(str(person))
    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    main()