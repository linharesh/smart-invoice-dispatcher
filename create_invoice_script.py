import time
import random
import requests

def create_random_invoices():
    num_invoices = random.randint(1, 3)
    
    url = "http://localhost:443/create-invoices"
    
    payload = {"amount": num_invoices}
    
    try:
        response = requests.post(url, json=payload)
        
        if response.status_code == 200:
            print(f"Successfully created {num_invoices} invoices: {response.json()}")
        else:
            print(f"Failed to create invoices. Status code: {response.status_code}, Response: {response.text}")
    except Exception as e:
        print(f"Error making POST request: {e}")

def run_invoice_creator_for_24_hours():
    for _ in range(24):
        create_random_invoices()
        time.sleep(3600)

if __name__ == "__main__":
    print("Starting invoice creation process...")
    run_invoice_creator_for_24_hours()
    print("Invoice creation process completed after 24 hours.")