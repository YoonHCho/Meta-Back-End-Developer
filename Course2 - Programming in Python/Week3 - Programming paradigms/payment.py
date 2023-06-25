class Payslips:
    def __init__(self, name, payment, amount) -> None:
        self.name = name
        self.payment = payment
        self.amount = amount

    def pay(self):
        self.payment = 'yes'

    def status(self):
        if self.payment == 'yes':
            return f"{self.name} is paid {self.amount}"
        else:
            return f"{self.name} is not paid yet {self.amount}"


nathan = Payslips("Nathan", "no", 1000)
roger = Payslips("Roger", "no", 3000)

print(nathan.status())
print(roger.status())
