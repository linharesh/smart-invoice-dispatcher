import starkbank
from datetime import datetime



# This is only an example of a private key content. You should use your own key.
private_key_content = """
-----BEGIN EC PRIVATE KEY-----

-----END EC PRIVATE KEY-----
"""

# for project users:
user = starkbank.Project(
    environment="sandbox",
    id="5415638830940160",
    private_key=private_key_content
)

print(user)
starkbank.user = user

webhooks = starkbank.webhook.query()

for webhook in webhooks:
    print(webhook)

from src.invoice_creator import InvoiceCreator

invoice_creator = InvoiceCreator()
invoices = invoice_creator.create_invoices(3)

print(invoices)