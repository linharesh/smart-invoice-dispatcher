import random
import time
import schedule
import logging
from flask import Flask, jsonify
import starkbank
from threading import Thread
from datetime import datetime

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

app = Flask(__name__)


# Flask route to trigger the invoice creation manually
@app.route("/generate_invoice", methods=["GET"])
def generate_invoice():
    logging.info("Generating a new invoice...")
    invoice_creator = InvoiceCreator()
    invoice_creator.create_invoices()
    return jsonify({"message": "Invoice generated successfully!"})


# Scheduler function
def schedule_invoices():
    schedule.every(1).hour.do(job)  # Schedule job every hour

    while True:
        schedule.run_pending()
        time.sleep(1)  # Sleep for 1 second to reduce CPU usage


def job():
    logging.info("Generating invoice as part of scheduled task...")
    invoice_creator = InvoiceCreator()
    invoice_creator.create_invoices()


# Flask thread to run the scheduler in the background
def run_scheduler_in_background():
    scheduler_thread = Thread(target=schedule_invoices)
    scheduler_thread.daemon = True  # Allows program to exit even if scheduler is running
    scheduler_thread.start()


if __name__ == "__main__":
    # Start the scheduler in the background
    run_scheduler_in_background()

    # Run the Flask app
    app.run(debug=True, use_reloader=False)  # Set use_reloader=False to prevent duplicate scheduler threads
