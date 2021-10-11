from flat import Bill, Flatmate
from reports import Pdf

amount = float(input("Please enter your bill amount: "))
period = input("Which month and year do you want to calculate the bill for?  ")

name = input("What's your name?  ")
days1 = int((input(f"How many days has {name} stayed in the flat for?  ")))

name2 = input("What's your flatmate's name?  ")
days2 = int((input(f"How many days has {name2} stayed in the flat for?  ")))

the_bill = Bill(amount=amount, period=period)
flatmate1 = Flatmate(name=name, days_in_flat=days1)
flatmate2 = Flatmate(name=name2, days_in_flat=days2)

print(the_bill.amount)
print(name + " Pays: ", flatmate1.pays(bill=the_bill, flatmate2=flatmate2))
print(name2 + " Pays: ", flatmate2.pays(bill=the_bill, flatmate2=flatmate1))

filename = the_bill.period + " Report.pdf"
pdf_report = Pdf(filename=filename)
pdf_report.generate_pdf(flatmate1, flatmate2, bill=the_bill)
