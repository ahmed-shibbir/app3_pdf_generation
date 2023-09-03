from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="A4")

df = pd.read_csv("topics.csv")

# print(type(pdf))

# pdf.add_page()
# pdf.set_font(family="Times", style="B", size=12)
# pdf.cell(w=0, h=12, txt="Hello there", align="L", ln=1, border=1)
# pdf.set_font(family="Times", style="B", size=10)
# pdf.cell(w=0, h=12, txt="H|i there", align="L", ln=1, border=1)
#
# pdf.add_page()
# pdf.set_font(family="Times", style="B", size=12)
# pdf.cell(w=0, h=12, txt="Hello there", align="L", ln=1, border=1)
# pdf.set_font(family="Times", style="B", size=10)
# pdf.cell(w=0, h=12, txt="H|i there", align="L", ln=1, border=1)
#
# pdf.output("output.pdf")

len(df["Pages"])


# for item in df["Topic"]:
#     print(item)
#     print(df["Pages"][0])
#     for pages in len(df["Pages"][0]):
#     pdf.add_page()
#     pdf.set_font(family="Times", style="B", size=12)
#     pdf.cell(w=0, h=12, txt=item, align="L", ln=1, border=1)
#     pdf.set_font(family="Times", style="B", size=10)
#     # pdf.cell(w=0, h=12, txt="H|i there", align="L", ln=1, border=1)

for index, row in df.iterrows():
    print(index)
    print(row)

    pdf.add_page()
    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(0, 0, 254)
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1)
    pdf.line(10, 21, 200, 21)


pdf.output("output.pdf")