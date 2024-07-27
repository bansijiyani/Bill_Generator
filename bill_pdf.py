from reportlab.pdfgen import canvas
from reportlab.lib import pdfencrypt
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
from datetime import date



pdf = canvas.Canvas("Bills.pdf",pagesize=letter)


def generate(shop_name,c_name,id,item,date):

    pdf.setFontSize(20)
    pdf.drawString(3.6 * inch, 10 * inch,shop_name)
    pdf.line(1 * inch, 9.8 * inch, 7.5 * inch, 9.8* inch)
    pdf.line(1 * inch, 9.7 * inch, 7.5 * inch, 9.7* inch)



    pdf.setFontSize(14)
    pdf.drawString(1 * inch, 9.3 * inch,f"Customer Name   :   {c_name}")
    pdf.drawString(1 * inch, 9 * inch,f"Transaction ID   :   {id}")
    pdf.line(1 * inch, 8.7 * inch, 7.5 * inch, 8.7 * inch)


    pdf.drawString(5.5 * inch, 9.3 * inch,f"Date : {date}")

    pdf.drawString(1.3 * inch, 8.5 * inch,"ITEM_NAME")
    pdf.drawString(6.5 * inch, 8.5 * inch,"PRICE")

    pdf.line(1 * inch, 8.4 * inch, 7.5 * inch, 8.4 * inch)


    a = 8
    total = 0
    for i,j in item:
        pdf.drawString(1.2 *inch,a*inch,i)
        pdf.drawString(6.2 * inch,a*inch,f"Rs. {j:.2f}")
        total += j
        a -= 0.35

    pdf.line(1*inch,(a)*inch , 7.5 * inch , (a) * inch)

    pdf.drawString(6 * inch , (a-0.3) * inch ,f"Total : Rs. {total}" )

    pdf.save()


shop_name = input("Enter the shop name :")
name =  input("Enter the  Costomer name :")
c_id = input("Enter the transaction ID : ")
i_no = int(input("How many item you purchase : "))
dt = date.today()

item_list = []

for i in range(0,i_no):
    i_name = input("Enter item name : ")
    price = int(input("Enter price of item :"))
    item_list.append([i_name,price])


generate(shop_name,name,c_id,item_list,dt)

# if __name__ == "__generate__":
#     generate(shop_name,name,c_id,item_list,dt)


