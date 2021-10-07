class Bill:
    """
    Calculates the total amount that needs to be paid
    """

    def __init__(self, amount, period):
        self.amount = amount
        self.period = period


class Flatmate:
    """
    Stores the names of the Flatmates, Number of days in
    flat and how much each one needs to pay
    """

    def __init__(self, name, days_in_flat):
        self.name = name
        self.days_in_flat = days_in_flat

    def pays(self, bill):
        return bill.amount / 2


class Pdf:
    """
    Generates the Pdf and the details needed!
    """

    def __init__(self, filename):
        self.filename = filename

    def generate_pdf(self, flatmate1, flatmate2, bill):
        pass


the_bill = Bill(amount=120, period="Dec 2021")
aadil = Flatmate(name="Aadil", days_in_flat=25)
shadia = Flatmate(name="Shadia", days_in_flat=30)

print(the_bill.amount)
print(aadil.pays(bill=the_bill))
