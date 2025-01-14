import random
import starkbank
from src.name_generator import NameGenerator
from src.tax_id_generator import TaxIdGenerator

class InvoiceCreator:


    def generate_random_amount(self):
        return random.randint(1, 10000000)

    def create_invoices(self, num_invoices=3):
        invoices = []
        tax_id_generator = TaxIdGenerator()
        for _ in range(num_invoices):
            name = NameGenerator.generate_random_name()
            tax_id = tax_id_generator.generate_random_tax_id()
            amount = self.generate_random_amount()

            invoice = starkbank.Invoice(
                amount=amount,
                name=name,
                tax_id=tax_id,
            )
            invoices.append(invoice)

        return starkbank.invoice.create(invoices)

