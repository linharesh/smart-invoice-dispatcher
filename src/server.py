import logging
from flask import Flask, request, jsonify
from src.transfer import TransferCreator
from src.invoice_creator import InvoiceCreator
import os

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

app = Flask(__name__)

@app.route('/')
def index():
    return "server is running"

@app.route('/webhook', methods=['POST'])
def webhook():
    content = request.json

    if not content:
        logging.info(f"Received raw data: {request.data.decode('utf-8')}")
        return jsonify({"message": "received"}), 200

    event = content.get("event")
    if not event:
        logging.warning("No event found in the webhook payload")
        return jsonify({"message": "received"}), 200

    handle_event(event)
    return jsonify({"message": "received"}), 200


def handle_event(event):
    """Handles the event from the webhook payload."""
    invoice_status = event.get("log", {}).get("invoice", {}).get("status")
    logging.info(f"Invoice Status: {invoice_status}")

    if is_paid_invoice_event(event):
        logging.info("Received paid invoice")
        logging.info(event)
        amount = event["log"]["invoice"]["amount"]
        create_transfer(amount)


def is_paid_invoice_event(event):
    """Checks if the event is a paid invoice event."""
    return (
        event.get("subscription") == "invoice"
        and event.get("log", {}).get("invoice", {}).get("status") == "paid"
    )


def create_transfer(amount):
    """Creates a transfer for the given amount."""
    transfer_creator = TransferCreator()
    transfer_creator.create(amount)


@app.route('/create-invoices', methods=['POST'])
def create_invoices():
    data = request.json
    if not data or 'amount' not in data:
        return jsonify({"error": "Missing 'amount' in request body"}), 400

    amount = data['amount']
    if not isinstance(amount, int) or amount <= 0:
        return jsonify({"error": "'amount' must be a positive integer"}), 400

    invoice_creator = InvoiceCreator()
    try:
        invoice_creator.create_invoices(amount)
        return jsonify({"message": f"Successfully created {amount} invoices"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    cert_file = 'server.crt'
    key_file = 'server.key'
    
    if not os.path.exists(cert_file) or not os.path.exists(key_file):
        logging.error(f"SSL certificate or key file not found: {cert_file}, {key_file}")
        exit(1)

    app.run(host='0.0.0.0', port=5000, ssl_context=('ssl.crt', 'ssl.key'))