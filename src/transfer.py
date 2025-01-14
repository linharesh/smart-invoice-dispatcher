import starkbank


class TransferCreator:

    def create(self, amount, name="Stark Bank S.A.", tax_id="20.018.183/0001-80", bank_code="20018183",
               branch_code="0001", account_number="6341320293482496", account_type="payment"):

        transfer = starkbank.transfer.create(
            [
                starkbank.Transfer(
                    amount=amount,
                    name=name,
                    tax_id=tax_id,
                    bank_code=bank_code,
                    branch_code=branch_code,
                    account_number=account_number,
                    account_type=account_type,
                )
            ]
        )

        print(transfer)
