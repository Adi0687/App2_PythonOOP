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

    def pays(self, bill, flatmate2):
        to_pay = bill.amount * (self.days_in_flat / (self.days_in_flat + flatmate2.days_in_flat))
        return to_pay