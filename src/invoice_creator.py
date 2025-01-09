import random
import starkbank
from src.name_generator import NameGenerator
from src.tax_id_generator import TaxIdGenerator

class InvoiceCreator:

    def __init__(self, num_invoices):
        self.num_invoices = num_invoices

    def generate_random_amount(self):
        return random.randint(1, 10000000)

    def create_invoices(self):
        invoices = []
        for _ in range(self.num_invoices):
            name = NameGenerator.generate_random_name()
            tax_id = TaxIdGenerator.generate_random_tax_id()
            amount = self.generate_random_amount()

            invoice = starkbank.Invoice(
                amount=amount,
                name=name,
                tax_id=tax_id,
            )
            invoices.append(invoice)

        return starkbank.invoice.create(invoices)


# Example usage
# creator = InvoiceCreator(5)
# created_invoices = creator.create_invoices()
# for invoice in created_invoices:
#     print(invoice)
