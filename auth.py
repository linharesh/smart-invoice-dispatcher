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


invoices = starkbank.invoice.create([
    starkbank.Invoice(
        amount=400000,
        descriptions=[{'key': 'Arya', 'value': 'Not today'}],
        due=datetime(2025, 1, 12, 15, 23, 26, 689377),
        fine=2.5,
        interest=1.3,
        name="Arya Stark",
        tags=['War supply', 'Invoice #1234'],
        tax_id="012.345.678-90",
    )
])

for invoice in invoices:
    print(invoice)