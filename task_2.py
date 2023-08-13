from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

def create_payment_receipt(pdf_file, customer_name, amount_paid, payment_date):
    doc = SimpleDocTemplate(pdf_file, pagesize=letter)
    elements = []

    styles = getSampleStyleSheet()

    title = Paragraph("Payment Receipt", styles['Title'])
    elements.append(title)

    receipt_data = [
        ["Customer Name:", customer_name],
        ["Amount Paid:", f"{amount_paid:.2f} INR"],
        ["Payment Date:", payment_date],
    ]

    table = Table(receipt_data, colWidths=[120, 300])
    table.setStyle(TableStyle([
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.blue),
        ('BACKGROUND', (0, 0), (-1, 0), colors.lightgrey),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
    ]))
    elements.append(table)

    doc.build(elements)

if __name__ == "__main__":
    customer_name = "Aniket Roy"
    amount_paid = 1678.0
    payment_date = "2023-08-12"

    pdf_file = "payment_receipt.pdf"
    create_payment_receipt(pdf_file, customer_name, amount_paid, payment_date)
    print("Payment receipt generated successfully.")
