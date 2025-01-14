import random
import logging
import starkbank
from src.name_generator import NameGenerator
from src.tax_id_generator import TaxIdGenerator
from src.starkbank_auth import StarkBankAuth

logger = logging.getLogger(__name__)

class InvoiceCreator:

    def generate_random_amount(self):
        amount = random.randint(1, 10000000)
        logger.info(f"Generated random amount: {amount}")
        return amount

    def create_invoices(self, num_invoices=3):
        logger.info(f"Starting to create {num_invoices} invoices...")
        invoices = []
        tax_id_generator = TaxIdGenerator()

        for i in range(num_invoices):
            logger.info(f"Creating invoice {i + 1}/{num_invoices}")
            name = NameGenerator.generate_random_name()
            tax_id = tax_id_generator.generate_random_tax_id()
            amount = self.generate_random_amount()

            logger.debug(f"Invoice details - Name: {name}, Tax ID: {tax_id}, Amount: {amount}")

            auth = StarkBankAuth()
            user = auth.get_user()
            starkbank.user = user
            
            invoice = starkbank.Invoice(
                amount=amount,
                name=name,
                tax_id=tax_id,
            )
            invoices.append(invoice)

        logger.info(f"Created {len(invoices)} invoices. Sending to StarkBank API...")
        try:
            result = starkbank.invoice.create(invoices)
            logger.info(f"Invoices successfully sent to StarkBank API: {result}")
            return result
        except Exception as e:
            logger.error(f"Failed to create invoices: {e}")
            raise