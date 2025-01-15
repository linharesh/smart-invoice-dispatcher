import time
import random
import logging
from src.invoice_creator import InvoiceCreator

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

MINIMUM_INVOICES = 8
MAXIMUM_INVOICES = 12
INTERVAL_HOURS = 3
TOTAL_HOURS = 24

def create_random_invoices():
    try:
        num_invoices = random.randint(MINIMUM_INVOICES, MAXIMUM_INVOICES)
        invoice_creator = InvoiceCreator() 
        invoice_creator.create_invoices(num_invoices)
    except Exception as e:
        logging.error(f"Error making POST request: {e}")

iterations = TOTAL_HOURS // INTERVAL_HOURS
for _ in range(iterations):
    create_random_invoices()
    time.sleep(INTERVAL_HOURS * 3600)