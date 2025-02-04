import starkbank
import logging
from src.starkbank_auth import StarkBankAuth

logger = logging.getLogger(__name__)


class TransferCreator:

    def create(self, amount, name="Stark Bank S.A.", tax_id="20.018.183/0001-80", bank_code="20018183",
               branch_code="0001", account_number="6341320293482496", account_type="payment"):
        logger.info("Creating a new transfer...")
        logger.debug(
            f"Transfer details - Amount: {amount}, Name: {name}, Tax ID: {tax_id}, "
            f"Bank Code: {bank_code}, Branch Code: {branch_code}, "
            f"Account Number: {account_number}, Account Type: {account_type}"
        )

        try:
            user = self._authenticate_user()
            starkbank.user = user
            transfer = self._create_transfer(
                amount, name, tax_id, bank_code, branch_code, account_number, account_type)
            logger.info(f"Transfer created successfully: {transfer}")
            return transfer
        except Exception as e:
            logger.error(f"Failed to create transfer: {e}")
            raise

    def _authenticate_user(self):
        auth = StarkBankAuth()
        return auth.get_user()

    def _create_transfer(self, amount, name, tax_id, bank_code, branch_code, account_number, account_type):
        return starkbank.transfer.create(
            [
                starkbank.Transfer(
                    amount=amount,
                    name=name,
                    tax_id=tax_id,
                    bank_code=bank_code,
                    branch_code=branch_code,
                    account_number=account_number,
                    account_type=account_type
                )
            ]
        )
