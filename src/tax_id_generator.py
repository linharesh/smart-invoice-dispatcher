import random
import logging

logger = logging.getLogger(__name__)

class TaxIdGenerator:

    def generate_random_tax_id(self):
        logger.debug("Generating a random tax ID (CPF)...")

        # Generate the first 9 digits of the CPF
        cpf = ''.join([str(random.randint(0, 9)) for _ in range(9)])
        logger.debug(f"Generated partial CPF (first 9 digits): {cpf}")

        # Calculate the first verification digit
        cpf += self.__calcular_digito(cpf)
        logger.debug(f"Added first verification digit: {cpf[-1]}")

        # Calculate the second verification digit
        cpf += self.__calcular_digito(cpf)
        logger.debug(f"Added second verification digit: {cpf[-1]}")

        logger.info(f"Generated random CPF: {cpf}")
        return cpf

    def __calcular_digito(self, cpf_parcial):
        logger.debug(f"Calculating verification digit for partial CPF: {cpf_parcial}")

        # Calculate the sum for the verification digit
        soma = sum((len(cpf_parcial) + 1 - i) * int(v) for i, v in enumerate(cpf_parcial))
        digito = 11 - soma % 11
        digito = str(digito if digito < 10 else 0)

        logger.debug(f"Calculated verification digit: {digito}")
        return digito