import webbrowser
import os

from fpdf import FPDF


class Pdf:
    """
    Generates the Pdf and the details needed!
    """

    def __init__(self, filename):
        self.filename = filename

    def generate_pdf(self, flatmate1, flatmate2, bill):
        flatmate1_payment = str(round(flatmate1.pays(bill, flatmate2), 2))
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
        pdf.cell(w=100, h=25, txt=flatmate1_payment, border=0, ln=1)

        # # Flatmate2 Detail
        pdf.cell(w=100, h=40, txt=flatmate2.name, border=0)
        pdf.cell(w=100, h=40, txt=flatmate2_payment, border=0, ln=1)

        pdf.output(f"files/{self.filename}")
        # Change Directory
        os.chdir("files")
        # Automatically open PDF file!
        webbrowser.open(self.filename)