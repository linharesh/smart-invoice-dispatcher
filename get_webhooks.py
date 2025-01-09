import starkbank

webhooks = starkbank.webhook.query()

for webhook in webhooks:
    print(webhook)