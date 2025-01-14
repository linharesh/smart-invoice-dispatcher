import time
import schedule
import logging
from flask import Flask, request
import starkbank
from threading import Thread
from src.transfer import TransferCreator
from src.invoice_creator import InvoiceCreator
import ssl
import os


# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

app = Flask(__name__)

private_key_content = """
-----BEGIN EC PRIVATE KEY-----
-----END EC PRIVATE KEY-----
"""

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


def schedule_invoices():
    schedule.every(1).hour.do(job) 
    
    while True:
        schedule.run_pending()
        time.sleep(1) 

def job():
    logging.info("Generating invoice as part of scheduled task...")
    invoice_creator = InvoiceCreator()
    invoice_creator.create_invoices()


def run_scheduler_in_background():
    scheduler_thread = Thread(target=schedule_invoices)
    scheduler_thread.daemon = True  
    scheduler_thread.start()


if __name__ == "__main__":
    run_scheduler_in_background()
    
    cert_file = 'server.crt'
    key_file = 'server.key'
    
    if not os.path.exists(cert_file) or not os.path.exists(key_file):
        logging.error(f"SSL certificate or key file not found: {cert_file}, {key_file}")
        exit(1)
    
    context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
    context.load_cert_chain(cert_file, key_file)

    app.run(ssl_context=(cert_file, key_file), host='0.0.0.0')
