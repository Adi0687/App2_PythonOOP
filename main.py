from fpdf import FPDF

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
        to_pay = bill.amount * (self.days_in_flat/(self.days_in_flat + flatmate2.days_in_flat))
        return to_pay


class Pdf:
    """
    Generates the Pdf and the details needed!
    """

    def __init__(self, filename):
        self.filename = filename

    def generate_pdf(self, flatmate1, flatmate2, bill):

        flatmate1_payment = str(round(flatmate1.pays(bill, flatmate2),2))
        flatmate2_payment = str(round(flatmate2.pays(bill, flatmate1), 2))

        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()

        # Add Icon
        pdf.image("files/house.png", w=30, h=30)

        # Title
        pdf.set_font(family='Times', size=24, style='B')
        pdf.cell(w=0, h=80, txt="Flatmates Bill", border=0, align='C', ln=1)

        # Heading
        pdf.set_font(family='Times', size=14, style='B')
        pdf.cell(w=100, h=25, txt="Period", border=0)
        pdf.cell(w=150, h=25, txt=bill.period, border=0, ln=1)

        # # Flatmate1 Detail
        pdf.set_font(family='Times', size=12)
        pdf.cell(w=100, h=25, txt=flatmate1.name, border=0)
        pdf.cell(w=100, h=25, txt= flatmate1_payment, border=0, ln=1)

        # # Flatmate2 Detail
        pdf.cell(w=100, h=40, txt=flatmate2.name, border=1)
        pdf.cell(w=100, h=40, txt= flatmate2_payment, border=1, ln=1)

        pdf.output(self.filename)



the_bill = Bill(amount=120, period="Dec 2021")
aadil = Flatmate(name="Aadil", days_in_flat=25)
shadia = Flatmate(name="Shadia", days_in_flat=30)

print(the_bill.amount)
print("Aadil Pays: ", aadil.pays(bill=the_bill, flatmate2=shadia))
print("Shadia Pays: ", shadia.pays(bill=the_bill, flatmate2=aadil))

filename = the_bill.period + " Report.pdf"
pdf_report = Pdf(filename=filename)
pdf_report.generate_pdf(flatmate1=aadil, flatmate2=shadia, bill=the_bill)