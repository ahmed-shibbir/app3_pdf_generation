from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

df = pd.read_csv("topics.csv")


for index, row in df.iterrows():
    pdf.add_page()
    # Set the header
    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1)
    # pdf.line(10, 21, 200, 21)
    # y = 21
    # for i in range(27):
    #     pdf.line(10, y, 200, y)
    #     y = y + 10

    # Set the lines in main page
    for y in range(21, 288, 10):
        pdf.line(10, y, 200, y)

    # Set the footer
    pdf.ln(265)
    pdf.set_font(family="Times", style="I", size=8)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=10, txt=row["Topic"], align="R")

    # Add additional pages under each topic
    for i in range(row["Pages"] - 1):
        pdf.add_page()

        # Set the footer
        pdf.ln(275)
        pdf.set_font(family="Times", style="I", size=8)
        pdf.set_text_color(100, 100, 100)
        pdf.cell(w=0, h=10, txt=row["Topic"], align="R")

        # Set the lines in additional pages
        for y in range(21, 288, 10):
            pdf.line(10, y, 200, y)

pdf.output("output.pdf")