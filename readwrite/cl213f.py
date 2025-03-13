class ElectricBill:
    def __init__(self, kwh):
        self.kwh = kwh
        self.cost = 0.0

    def calc(self):
        if kwh < 2001:
            self.cost = kwh * 0.07
        elif 2000 < kwh < 10001:
            self.cost = (2000 * 0.07) + ((kwh-2000) * 0.05)
        elif 10000 < kwh:
            self.cost = (2000 * 0.07) + (8000 * 0.05) + ((kwh-10000) * 0.04)


    def __str__(self):
        return f"The cost of {self.kwh} is ${self.cost:.2f}"