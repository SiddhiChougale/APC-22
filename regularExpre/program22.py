import re
text = """
Invoice No: INV-1234
Date: 15-10-2026
Amount: Rs. 2500.50
"""
invoice = re.findall(r'INV-\d+', text)
dates = re.findall(r'\b\d{2}-\d{2}-\d{4}\b', text)
amounts = re.findall(r'Rs\.?\s*[\d,]+(?:\.\d{2})?', text)
print("Invoice:", invoice)
print("Date:", dates)
print("Amount:", amounts)