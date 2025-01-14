import time
import schedule
import logging
from flask import Flask, request
import starkbank
from threading import Thread
from src.transfer import TransferCreator
from src.invoice_creator import InvoiceCreator
import os


# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

app = Flask(__name__)

# Read private key from a file
private_key_file = "private_key.pem"
if not os.path.exists(private_key_file):
    logging.error(f"Private key file not found: {private_key_file}")
    exit(1)

with open(private_key_file, "r") as file:
    private_key_content = file.read()

# for project users:
starkbank.Project(
    environment="sandbox",
    id="5415638830940160",
    private_key=private_key_content
)

@app.route('/')
def index():
    return "server is running"

@app.route('/webhook', methods=['POST'])
def webhook():
    content = request.json  
    if content:
        event = content["event"]
        if event["subscription"] == "invoice" and event["log"]["invoice"]["status"] == "paid":
            app.logger.info("Received paid invoice")
            app.logger.info(content)
            amount = event["log"]["invoice"]["amount"]
            TransferCreator(amount=amount)

    else:
        app.logger.info(f"Received raw data: {request.data.decode('utf-8')}")


def job():
    logging.info("Generating invoice as part of scheduled task...")
    invoice_creator = InvoiceCreator()
    invoice_creator.create_invoices()


def run_scheduler_for_24_hours():
    # Schedule the job to run every hour
    schedule.every(1).hour.do(job)

    # Run the scheduler for 24 hours
    for _ in range(24):
        schedule.run_pending()
        time.sleep(3600)  # Sleep for 1 hour (3600 seconds)


def run_scheduler_in_background():
    scheduler_thread = Thread(target=run_scheduler_for_24_hours)
    scheduler_thread.daemon = True  
    scheduler_thread.start()


if __name__ == "__main__":
    run_scheduler_in_background()
    
    cert_file = 'server.crt'
    key_file = 'server.key'
    
    if not os.path.exists(cert_file) or not os.path.exists(key_file):
        logging.error(f"SSL certificate or key file not found: {cert_file}, {key_file}")
        exit(1)

    app.run(host='0.0.0.0', port=5000, ssl_context=('ssl.crt', 'ssl.key'))